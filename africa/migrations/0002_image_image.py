# Generated by Django 3.0.3 on 2020-03-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
