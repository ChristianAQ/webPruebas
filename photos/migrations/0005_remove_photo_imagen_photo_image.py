# Generated by Django 4.0.3 on 2022-05-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='imagen',
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
