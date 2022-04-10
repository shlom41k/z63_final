from django.db import models
from django.db.models.signals import post_save
from django.core.validators import EmailValidator
from django.dispatch import receiver
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class Teacher(models.Model):

    # Contact info
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    photo = models.ImageField(verbose_name='Photo', upload_to='school_teachers/')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    # About
    short_description = RichTextUploadingField(verbose_name="Description")
    detail_info = RichTextUploadingField(verbose_name="Detail Info")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super(self.__class__, self).save(*args, **kwargs)
        # super(Teacher, self).save(*args, **kwargs)


class TeacherContactInfo(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='contact_info')
    email = models.EmailField(verbose_name='Email', validators=[EmailValidator], blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone', blank=True)
    telegram = models.CharField(max_length=50, verbose_name='Telegram', blank=True)
    vk = models.CharField(max_length=50, verbose_name='VK', blank=True)
    instagram = models.CharField(max_length=50, verbose_name='Instagram', blank=True)

    def __str__(self):
        return f"{self.teacher} contact info"

    def __repr__(self):
        return self.__str__()


@receiver(post_save, sender=Teacher)
def create_teacher_contact_info(sender, instance, created, **kwargs):
    if created:
        TeacherContactInfo.objects.create(teacher=instance)


@receiver(post_save, sender=Teacher)
def save_teacher_contact_info(sender, instance, **kwargs):
    instance.contact_info.save()


