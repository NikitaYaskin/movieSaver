# Generated by Django 2.1.5 on 2019-02-06 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesaver', '0007_auto_20190206_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='section',
        ),
    ]
