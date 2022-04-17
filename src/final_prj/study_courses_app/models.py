from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Course")
    description = RichTextUploadingField(verbose_name="Course Description")
    image = models.ImageField(upload_to="courses/", verbose_name="Course Image")
    creator = models.ForeignKey(User, on_delete=models.SET("Unknown"), verbose_name="Creator", related_name="created_courses")
    date_of_creating = models.DateField(verbose_name="Date of creating", default=timezone.now)
    students = models.ManyToManyField(User, verbose_name="Students", related_name="current_courses", blank=True)

    COMPLETED = "Completed"
    IN_PROCESS = "In Process"

    COURSE_STATUS_CHOICES = [
        (COMPLETED, "COMPLETED"),
        (IN_PROCESS, "IN_PROCESS"),
    ]

    course_status = models.CharField(max_length=20, choices=COURSE_STATUS_CHOICES, default=IN_PROCESS, verbose_name="Course Status")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", related_name="modules")
    name = models.CharField(max_length=100, verbose_name="Module")
    order = models.PositiveIntegerField(verbose_name="Module Order", blank=True)
    description = models.TextField(verbose_name="Module Description", blank=True)
    image = models.ImageField(upload_to=f"courses/modules/", verbose_name="Module Image", blank=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.course.modules.count() + 1
        super(self.__class__, self).save(*args, **kwargs)


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Module", related_name="lessons")
    name = models.CharField(max_length=100, verbose_name="Lesson")
    order = models.PositiveIntegerField(verbose_name="Lesson Order", blank=True)
    description = models.TextField(verbose_name="Lesson Description", blank=True)
    image = models.ImageField(upload_to=f"courses/modules/lessons/", verbose_name="Module Image", blank=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.module.lessons.count() + 1
        super(self.__class__, self).save(*args, **kwargs)


class Theme(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Lesson", related_name="themes")
    name = models.CharField(max_length=100, verbose_name="Name", blank=True)
    order = models.PositiveIntegerField(verbose_name="Theme Order", blank=True)
    description = models.TextField(verbose_name="Theme Description", blank=True)
    content = RichTextUploadingField(verbose_name="Theme Content")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.lesson.themes.count() + 1
        if not self.name:
            self.name = f"Theme_{self.order}"
        super(self.__class__, self).save(*args, **kwargs)
