# Generated by Django 4.1.5 on 2023-01-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(default=30, verbose_name='나이'),
            preserve_default=False,
        ),
    ]
