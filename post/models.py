from django.db import models
from django.template.defaultfilters import truncatechars

from account.models import Account

class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def short_body(self):
        verbose_name = 'body'
        return truncatechars(self.body, 10)
