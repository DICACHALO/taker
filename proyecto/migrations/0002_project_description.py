# Generated by Django 2.2.7 on 2020-08-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
