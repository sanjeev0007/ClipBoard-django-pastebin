# Generated by Django 2.0.9 on 2019-01-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20190102_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2000-12-04 06:12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='Unknown', max_length=40),
        ),
    ]
