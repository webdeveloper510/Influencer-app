# Generated by Django 4.1.7 on 2023-03-22 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0007_remove_user_country_campaign_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='Influencerid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapp.influencer'),
        ),
    ]
