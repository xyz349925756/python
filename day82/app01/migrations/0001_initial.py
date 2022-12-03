# Generated by Django 4.1.3 on 2022-12-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('repeat_password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'woman'), (3, 'other')])),
            ],
        ),
    ]