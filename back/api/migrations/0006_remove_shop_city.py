# Generated by Django 2.2 on 2022-04-23 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220423_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='city',
        ),
    ]