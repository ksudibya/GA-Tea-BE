# Generated by Django 4.2.1 on 2023-05-15 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GA_Tea', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='author',
        ),
    ]
