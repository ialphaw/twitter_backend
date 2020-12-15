from django.db import models
from django.template.defaultfilters import truncatechars

from account.models import Account

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='author')
    body = models.TextField(max_length=500)
    is_retweeted = models.BooleanField(default=False)
    retweeted_from = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='retweeted_from')
    retweeted_by = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='retweet_by')
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
