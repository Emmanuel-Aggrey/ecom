# Generated by Django 2.2.10 on 2020-09-25 00:56

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20200922_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='images/%Y/%m/%d/'),
        ),
    ]
