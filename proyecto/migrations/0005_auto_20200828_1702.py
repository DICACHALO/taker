# Generated by Django 2.2.7 on 2020-08-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_auto_20200828_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_project',
            name='type_user',
            field=models.CharField(default='Gerente', max_length=100),
        ),
    ]
