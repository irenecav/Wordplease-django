# Generated by Django 2.2.1 on 2019-05-21 09:54

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('posts', '0003_auto_20190521_0945'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorie',
        ),
    ]
