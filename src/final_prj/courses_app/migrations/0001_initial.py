# Generated by Django 4.0.3 on 2022-04-10 10:11

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Course Name')),
                ('price', models.CharField(blank=True, max_length=100, verbose_name='Course Price')),
                ('number_of_lessons', models.CharField(blank=True, max_length=100, verbose_name='Number of Lessons')),
                ('course_image', models.ImageField(blank=True, upload_to='courses_description/', verbose_name='Course Image')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDescriptionField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('course_description_image', models.ImageField(blank=True, upload_to='courses_description/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_descriptions', to='courses_app.course')),
            ],
        ),
    ]
