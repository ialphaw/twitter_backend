from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.core.mail import send_mail

from celery import shared_task

import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from user_profile.models import Profile
from notification.models import Notif

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def send_email():
    users = Profile.objects.all()
    for user in users:
        user_email = user.user.email
        # user_followers = user.followers
        # user_following = user.followings
        notifs = Notif.objects.filter(user=user.user, is_read=False).count()

        logger.info(notifs)

        data = {
            # 'email': user_email,
            # 'followers': user_followers,
            # 'following': user_following,
            'notifs': 'notifs'
        }

        f_data = json.dumps(data)

        # send_mail(f_data)
        logger.info(f'{f_data} has been sent to {user_email}')

    return 'we did it!'


schedule, created = IntervalSchedule.objects.get_or_create(
    every=10, period=IntervalSchedule.SECONDS)

PeriodicTask.objects.create(
    interval=schedule, name='Send Email', task='send_email.tasks.send_email')
