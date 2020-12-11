# Generated by Django 3.0.5 on 2020-12-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vol', '0004_auto_20201210_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='certificates/'),
        ),
    ]
