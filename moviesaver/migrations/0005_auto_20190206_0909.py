# Generated by Django 2.1.5 on 2019-02-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesaver', '0004_auto_20190205_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='section',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='viewing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
