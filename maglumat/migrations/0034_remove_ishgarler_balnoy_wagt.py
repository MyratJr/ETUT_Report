# Generated by Django 4.1.2 on 2022-11-07 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0033_ishgarler_balnoy_wagt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ishgarler',
            name='balnoy_wagt',
        ),
    ]