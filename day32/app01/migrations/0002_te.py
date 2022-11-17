# Generated by Django 4.1 on 2022-09-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Te',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('phone', models.BigIntegerField(null=True, unique=True, verbose_name='手机号码')),
                ('job', models.IntegerField(blank=True, default='IT', null=True, verbose_name='职业')),
                ('date', models.DateField(blank=True, help_text='yyyy-mm-dd', null=True, verbose_name='date')),
            ],
        ),
    ]