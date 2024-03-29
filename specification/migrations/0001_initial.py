# Generated by Django 3.1 on 2020-10-11 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requeriments', '0003_rnf_specific'),
        ('proyecto', '0007_auto_20200921_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='SRnFFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='specification')),
                ('rnf', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='requeriments.rnf')),
            ],
        ),
        migrations.CreateModel(
            name='SRnF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('type_r', models.CharField(max_length=100)),
                ('sub_type', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('state', models.CharField(default='Propuesta', max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.project')),
                ('rnf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requeriments.rnf')),
            ],
        ),
        migrations.CreateModel(
            name='SRFFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='specification')),
                ('rf', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='requeriments.rf')),
            ],
        ),
        migrations.CreateModel(
            name='SRF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=100)),
                ('state', models.CharField(default='Propuesta', max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=100)),
                ('input', models.CharField(max_length=200)),
                ('output', models.CharField(max_length=200)),
                ('destiny', models.CharField(max_length=200)),
                ('process', models.CharField(max_length=200)),
                ('restriction', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('collateral_damage', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.project')),
                ('rf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requeriments.rf')),
            ],
        ),
    ]
