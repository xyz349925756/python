# Generated by Django 4.1.3 on 2022-11-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_student_age_alter_student_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(error_messages={'required': 'age 不能为空'}, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(error_messages={'max_length': '最大值不能超过16位', 'min_lenght': '最小不能低于3位', 'required': 'name 不能为空'}, max_length=32, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(choices=[(4, 'D'), (5, 'E'), (2, 'B'), (1, 'A'), (3, 'C')], error_messages={'required': 'score 不能为空'}),
        ),
    ]
