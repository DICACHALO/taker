# Generated by Django 2.2.7 on 2020-09-08 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0006_auto_20200828_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='RnF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('type_r', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('state', models.CharField(default='Propuesta', max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Project')),
            ],
        ),
        migrations.CreateModel(
            name='RF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=100)),
                ('state', models.CharField(default='Propuesta', max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Project')),
            ],
        ),
    ]
