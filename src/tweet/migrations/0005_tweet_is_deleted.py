# Generated by Django 2.2.7 on 2019-11-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_auto_20191109_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
