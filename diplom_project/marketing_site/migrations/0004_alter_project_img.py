# Generated by Django 4.1.7 on 2023-04-06 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing_site', '0003_project_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(upload_to='marketing_site/images/'),
        ),
    ]
