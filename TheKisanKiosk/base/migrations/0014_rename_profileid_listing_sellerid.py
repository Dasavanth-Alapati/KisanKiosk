# Generated by Django 4.0.3 on 2022-05-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_order_remove_credentials_profileid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='profileid',
            new_name='sellerid',
        ),
    ]
