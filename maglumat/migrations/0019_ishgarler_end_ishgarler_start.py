# Generated by Django 4.1.2 on 2022-11-02 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0018_remove_ishgarler_end_remove_ishgarler_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='ishgarler',
            name='end',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='ishgarler',
            name='start',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
