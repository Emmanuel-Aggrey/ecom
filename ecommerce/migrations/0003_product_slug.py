# Generated by Django 2.2.10 on 2020-09-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20200920_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]