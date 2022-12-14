# Generated by Django 4.0.6 on 2022-10-11 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppQatarWC2022', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedsticker',
            name='sticker_template',
        ),
        migrations.CreateModel(
            name='GeneratedPlayerSticker',
            fields=[
                ('generatedsticker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppQatarWC2022.generatedsticker')),
                ('sticker_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppQatarWC2022.playersticker')),
            ],
            bases=('AppQatarWC2022.generatedsticker',),
        ),
        migrations.CreateModel(
            name='GeneratedLogoSticker',
            fields=[
                ('generatedsticker_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AppQatarWC2022.generatedsticker')),
                ('sticker_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppQatarWC2022.logosticker')),
            ],
            bases=('AppQatarWC2022.generatedsticker',),
        ),
    ]
