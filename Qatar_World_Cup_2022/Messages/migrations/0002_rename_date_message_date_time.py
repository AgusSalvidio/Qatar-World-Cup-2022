# Generated by Django 4.0.6 on 2022-10-11 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='date',
            new_name='date_time',
        ),
    ]
