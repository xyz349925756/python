# Generated by Django 4.1 on 2022-08-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
