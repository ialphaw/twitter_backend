from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from account.models import Account
from post.models import Post
from user_profile.models import Relation

class Notif(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    is_like = models.BooleanField(default=False)
    liker = models.ForeignKey(Account, on_delete=models.CASCADE,
                              related_name='liker_notif', blank=True, null=True)
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, blank=True, null=True)

    is_follow = models.BooleanField(default=False)
    follower = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='follower_notif', blank=True, null=True)
    following = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='following_notif', blank=True, null=True)

    is_read = models.BooleanField(default=False)
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-when',)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Relation)
def save_profile(sender, instance, **kwargs):
    if kwargs['created']:
        user = instance.to_user
        follower = instance.from_user
        following = instance.to_user
        n1 = Notif(user=user, is_follow=True, follower=follower, following=following)
        n1.save()
