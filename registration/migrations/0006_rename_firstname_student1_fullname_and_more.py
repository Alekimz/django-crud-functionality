# Generated by Django 5.0.3 on 2024-04-17 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_student1_firstname_alter_student1_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student1',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='student1',
            name='lastname',
        ),
    ]