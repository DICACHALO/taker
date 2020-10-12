# Generated by Django 2.2.7 on 2020-08-28 21:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_auto_20200828_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(related_name='users', through='proyecto.User_Project', to=settings.AUTH_USER_MODEL),
        ),
    ]
