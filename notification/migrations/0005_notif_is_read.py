# Generated by Django 3.1.4 on 2020-12-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20201216_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='notif',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
