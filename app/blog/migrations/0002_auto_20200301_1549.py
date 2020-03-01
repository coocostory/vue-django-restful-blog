# Generated by Django 2.1.4 on 2020-03-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='base_blog',
        ),
        migrations.AddField(
            model_name='comment',
            name='base_blog',
            field=models.ManyToManyField(to='blog.Blog'),
        ),
    ]