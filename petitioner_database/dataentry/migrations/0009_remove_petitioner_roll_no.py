# Generated by Django 5.0.6 on 2024-07-27 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0008_alter_petitioner_nationality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petitioner',
            name='roll_no',
        ),
    ]
