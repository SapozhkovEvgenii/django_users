# Generated by Django 4.0.1 on 2022-03-03 08:10

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to=post.models.Post.file_path),
            preserve_default=False,
        ),
    ]