# Generated by Django 4.1 on 2022-09-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_remove_authordetail_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='authordetail',
            name='address',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
