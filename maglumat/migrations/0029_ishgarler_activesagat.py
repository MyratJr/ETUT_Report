# Generated by Django 4.1.2 on 2022-11-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0028_ishgarler_activeminut'),
    ]

    operations = [
        migrations.AddField(
            model_name='ishgarler',
            name='activesagat',
            field=models.IntegerField(default=0),
        ),
    ]
