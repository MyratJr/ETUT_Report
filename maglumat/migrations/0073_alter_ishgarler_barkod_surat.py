# Generated by Django 4.1.2 on 2023-02-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0072_alter_ishgarler_barkod_surat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='barkod_surat',
            field=models.ImageField(upload_to='barcode_img/'),
        ),
    ]