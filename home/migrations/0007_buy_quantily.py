# Generated by Django 4.0.2 on 2022-02-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_buy_users_delete_transaction_buy_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='quantily',
            field=models.IntegerField(null=True),
        ),
    ]
