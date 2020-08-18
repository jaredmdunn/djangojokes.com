# Generated by Django 3.1 on 2020-08-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_joke_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='slug',
            field=models.SlugField(default='foo', editable=False, unique=True),
            preserve_default=False,
        ),
    ]
