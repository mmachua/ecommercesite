# Generated by Django 2.0.7 on 2018-11-14 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181031_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='phone_no',
        ),
    ]
