# Generated by Django 5.0.6 on 2024-07-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0005_alter_student_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Petitioner',
        ),
    ]