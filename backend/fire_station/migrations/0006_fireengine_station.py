# Generated by Django 5.1.3 on 2024-11-21 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire_station', '0005_rename_date_equipment_issue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fireengine',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fire_station.station'),
            preserve_default=False,
        ),
    ]
