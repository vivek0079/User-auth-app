# Generated by Django 2.0 on 2018-03-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180316_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=' ', max_length=120),
        ),
    ]
