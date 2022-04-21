# Generated by Django 4.0.3 on 2022-04-21 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Review', 'Review'), ('Published', 'Published'), ('Rejected', 'Rejected')], default='Created', max_length=10, verbose_name='Status'),
        ),
    ]
