# Generated by Django 3.0.5 on 2020-04-07 09:05
import datetime

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20200406_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='valid_to',
            field=models.DateTimeField(default=django.utils.timezone.now() + datetime.timedelta(days=30)),
            preserve_default=False,
        ),
    ]
