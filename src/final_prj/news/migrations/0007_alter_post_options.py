# Generated by Django 4.0.3 on 2022-04-20 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_of_creating']},
        ),
    ]
