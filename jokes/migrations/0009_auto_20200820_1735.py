# Generated by Django 3.1 on 2020-08-20 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0008_auto_20200820_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag']},
        ),
    ]