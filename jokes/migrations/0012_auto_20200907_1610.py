# Generated by Django 3.1 on 2020-09-07 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0011_auto_20200907_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jokevote',
            old_name='update',
            new_name='updated',
        ),
    ]