# Generated by Django 4.0.3 on 2022-05-18 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentid',
            field=models.ForeignKey(db_column='commentid', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.comment'),
        ),
    ]
