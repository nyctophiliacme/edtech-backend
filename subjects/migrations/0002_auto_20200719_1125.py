# Generated by Django 3.0.6 on 2020-07-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='background_end_color',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='background_start_color',
            field=models.TextField(blank=True, null=True),
        ),
    ]
