# Generated by Django 3.0.5 on 2020-12-10 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]