# Generated by Django 3.1.14 on 2023-01-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xodim', '0002_auto_20230102_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='fullname',
        ),
    ]