# Generated by Django 3.1.4 on 2020-12-15 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0007_auto_20201215_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='retweeted_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retweeted_from', to=settings.AUTH_USER_MODEL),
        ),
    ]
