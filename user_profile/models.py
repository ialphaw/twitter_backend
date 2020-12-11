from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.models import Account

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Account)
def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()
