# Generated by Django 2.1.5 on 2019-02-14 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviesaver', '0011_auto_20190214_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='moviesaver.Section', verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='movie',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='moviesaver.Status', verbose_name='Status'),
        ),
    ]
