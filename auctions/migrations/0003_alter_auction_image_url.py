# Generated by Django 4.1.7 on 2023-02-23 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_auction_current_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image_url',
            field=models.URLField(max_length=2083),
        ),
    ]
