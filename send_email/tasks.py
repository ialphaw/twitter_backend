from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.core.mail import send_mail

from celery import shared_task

import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from user_profile.models import Profile
from notification.models import Notif


@shared_task
def send_email():
    users = Profile.objects.all()
    for user in users:
        user_email = user.email
        user_followers = user.followers
        user_following = user.followings
        notifs = Notif.objects.filter(user=user, is_read=False).count()

        data = {
            'followers': user_followers,
            'following': user_following,
            'notifs': notifs
        }

        f_data = json.dumps(data)

        send_mail(f_data)
        print(f'emai has been sent to {user_email}')

    return 'we did it'


schedule, created = IntervalSchedule.objects.get_or_create(
    every=1, period=IntervalSchedule.DAYS)

PeriodicTask.objects.create(
    interval=schedule, name='Send Email', task='twitter_backend.send_email.tasks.send_email')
