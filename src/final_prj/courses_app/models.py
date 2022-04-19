from django.db import models
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField
# from phone_field import PhoneField


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


class SchoolCourseApplication(models.Model):
    """
    Course Application model
    """
    course = models.ForeignKey(SchoolCourse, on_delete=models.CASCADE, related_name='course_applications')
    user_name = models.CharField(max_length=100, verbose_name='Person')
    phone = models.CharField(max_length=100, verbose_name='Person Phone')
    # phone = PhoneField(verbose_name='Person Phone')
    # email = models.EmailField(verbose_name='Person Email', blank=True)
    telegram = models.CharField(max_length=100, verbose_name='Telegram', blank=True)

    OPENED = 'OPENED'
    IN_WORK = 'IN_WORK'
    CLOSED = 'CLOSED'

    STATUS_CHOICES = [
        (OPENED, 'Opened'),
        (IN_WORK, 'In Work'),
        (CLOSED, 'Closed'),
    ]
    status = models.CharField(max_length=10, verbose_name='Status', choices=STATUS_CHOICES, default=OPENED)

    def __str__(self):
        return f"User: {self.user_name}  - course: {self.course}"

