# Generated by Django 5.1 on 2024-09-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='album_cover_pages/'),
        ),
    ]
