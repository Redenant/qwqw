# Generated by Django 4.1.7 on 2023-04-07 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing_site', '0005_contact_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='textarea',
            new_name='task',
        ),
    ]
