# Generated by Django 3.1.4 on 2020-12-16 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_notif_is_read2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notif',
            options={'ordering': ('-when',)},
        ),
    ]
