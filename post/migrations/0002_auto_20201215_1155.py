# Generated by Django 3.1.4 on 2020-12-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='post',
        ),
        migrations.AddField(
            model_name='hashtag',
            name='post',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]
