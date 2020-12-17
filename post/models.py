from django.db import models
from django.template.defaultfilters import truncatechars
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from account.models import Account

class Post(models.Model):
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='author')
    body = models.TextField(max_length=500)
    is_retweeted = models.BooleanField(default=False)
    retweeted_from = models.ForeignKey(
        Account, on_delete=models.CASCADE, blank=True, null=True, related_name='retweeted_from')
    retweeted_by = models.ForeignKey(
        Account, on_delete=models.CASCADE, blank=True, null=True, related_name='retweet_by')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_time',)

    @property
    def short_body(self):
        verbose_name = 'body'
        return truncatechars(self.body, 10)

    def __str__(self):
        return self.short_body


class Hashtag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

    def get_posts(self):
        return "\n".join([p.short_body for p in self.post.all()])


class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



from notification.models import Notif
@receiver(post_save, sender=Like)
def save_profile(sender, instance, **kwargs):
    if kwargs['created']:
        user = instance.post.author
        liker = instance.user
        post = instance.post
        n1 = Notif(user=user, is_like=True, liker=liker, post=post)
        n1.save()
