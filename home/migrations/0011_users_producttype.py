# Generated by Django 4.0.2 on 2022-03-09 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_producttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='ProductType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.producttype'),
        ),
    ]
