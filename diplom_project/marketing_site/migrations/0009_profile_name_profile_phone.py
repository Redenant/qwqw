# Generated by Django 4.1.7 on 2023-05-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing_site', '0008_alter_contact_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона'),
        ),
    ]
