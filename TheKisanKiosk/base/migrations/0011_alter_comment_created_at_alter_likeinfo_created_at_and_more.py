# Generated by Django 4.0.3 on 2022-05-06 07:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_comment_created_at_alter_likeinfo_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 7, 39, 9, 972374, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='likeinfo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 7, 39, 9, 973180, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 7, 39, 9, 973567, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 7, 39, 9, 973921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 7, 39, 9, 974288, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 7, 39, 9, 974553, tzinfo=utc)),
        ),
    ]
