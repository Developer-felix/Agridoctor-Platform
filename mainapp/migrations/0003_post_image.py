# Generated by Django 3.1.1 on 2020-09-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200926_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blog_images'),
            preserve_default=False,
        ),
    ]