# Generated by Django 3.0.3 on 2020-03-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africa', '0002_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]