# Generated by Django 2.2.1 on 2019-05-22 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('posts', '0005_auto_20190521_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
