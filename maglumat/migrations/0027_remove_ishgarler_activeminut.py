# Generated by Django 4.1.2 on 2022-11-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0026_ishgarler_activeminut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ishgarler',
            name='activeminut',
        ),
    ]
