# Generated by Django 3.2 on 2021-04-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
