# Generated by Django 2.1.5 on 2019-02-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesaver', '0005_auto_20190206_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='section',
            field=models.CharField(max_length=20),
        ),
    ]
