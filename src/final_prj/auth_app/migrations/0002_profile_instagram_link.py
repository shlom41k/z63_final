# Generated by Django 4.0.3 on 2022-04-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=100, verbose_name='Instagram'),
        ),
    ]