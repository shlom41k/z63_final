from django.db import models
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class SchoolCourse(models.Model):
    """
    Course model
    """
    name = models.CharField(max_length=100, verbose_name='Course Name')
    price = models.CharField(max_length=100, verbose_name='Course Price', blank=True)
    number_of_lessons = models.CharField(max_length=100, verbose_name='Number of Lessons', blank=True)
    course_image = models.ImageField(upload_to='courses_description/', verbose_name='Course Image', blank=True)
    slug = models.SlugField(max_length=100, verbose_name='Slug', unique=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(self.__class__, self).save(*args, **kwargs)


class SchoolCourseDescriptionField(models.Model):
    """
    Course Description model
    """
    course = models.ForeignKey(SchoolCourse, on_delete=models.CASCADE, related_name='course_descriptions')
    title = models.CharField(max_length=100, verbose_name="Title")
    content = RichTextUploadingField(verbose_name="Content")
    course_description_image = models.ImageField(upload_to='courses_description/', blank=True)

    def __str__(self):
        return f"{self.title}"

