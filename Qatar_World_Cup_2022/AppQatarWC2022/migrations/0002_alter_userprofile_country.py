# Generated by Django 4.0.6 on 2022-09-26 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatarWC2022', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppQatarWC2022.country'),
        ),
    ]