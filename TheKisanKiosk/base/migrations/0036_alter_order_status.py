# Generated by Django 4.0.3 on 2022-05-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_remove_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ORDERED', 'ORDERED'), ('DELIVERED', 'DELIVERED'), ('IN_TRANSIT', 'IN_TRANSIT'), ('CANCELLED', 'CANCELLED')], max_length=11),
        ),
    ]
