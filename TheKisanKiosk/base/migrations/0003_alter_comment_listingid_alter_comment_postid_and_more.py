# Generated by Django 4.0.3 on 2022-05-03 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_listing_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listingid',
            field=models.ForeignKey(blank=True, db_column='listingid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='postid',
            field=models.ForeignKey(blank=True, db_column='postid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='profileid',
            field=models.ForeignKey(db_column='profileid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='likeinfo',
            name='profileid',
            field=models.ForeignKey(db_column='profileid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='profileid',
            field=models.ForeignKey(db_column='profileid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='profileid',
            field=models.ForeignKey(db_column='profileid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='credentials',
            field=models.ForeignKey(db_column='credentials', on_delete=django.db.models.deletion.CASCADE, to='base.credentials'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='buyerid',
            field=models.ForeignKey(db_column='buyerid', on_delete=django.db.models.deletion.CASCADE, related_name='buyer_id', to='base.profile'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='listingid',
            field=models.ForeignKey(db_column='listingid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.listing'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sellerid',
            field=models.ForeignKey(db_column='sellerid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_id', to='base.profile'),
        ),
    ]