# Generated by Django 5.0.3 on 2024-04-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_student1_delete_student2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student1',
            name='firstname',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student1',
            name='lastname',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student1',
            name='password',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
