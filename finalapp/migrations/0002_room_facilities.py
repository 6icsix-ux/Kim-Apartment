# Generated by Django 5.2 on 2025-04-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
