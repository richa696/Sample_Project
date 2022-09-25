# Generated by Django 3.2.7 on 2022-09-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocurrencymodel',
            old_name='name',
            new_name='Name',
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='Price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='_1h',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='_24h',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='_7d',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='circulating_supply',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='market_cap',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocurrencymodel',
            name='volume',
            field=models.CharField(max_length=100),
        ),
    ]
