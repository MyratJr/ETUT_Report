# Generated by Django 4.1.2 on 2022-11-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0020_alter_ishgarler_end_alter_ishgarler_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='end',
            field=models.TimeField(verbose_name=['%H:%M:%S']),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='start',
            field=models.TimeField(verbose_name=['%H:%M:%S']),
        ),
    ]