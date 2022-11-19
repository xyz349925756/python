# Generated by Django 4.1.3 on 2022-11-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(choices=[(4, 'D'), (5, 'E'), (1, 'A'), (3, 'C'), (2, 'B')]),
        ),
    ]
