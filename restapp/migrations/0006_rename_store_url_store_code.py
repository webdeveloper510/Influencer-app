# Generated by Django 4.1.7 on 2023-03-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0005_campaign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='store_url',
            new_name='code',
        ),
    ]
