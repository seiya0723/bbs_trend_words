# Generated by Django 3.1.2 on 2021-09-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20210913_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='trend',
            name='count',
            field=models.IntegerField(default=0, verbose_name='出現回数'),
        ),
    ]
