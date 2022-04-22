from django.db import models
from django.db.models.signals import post_save
from django.core.validators import EmailValidator
from django.dispatch import receiver

from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from django.utils.text import slugify


class Teacher(models.Model):
    """
    Model for teachers
    """

    # Main info
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    photo = models.ImageField(verbose_name='Photo', upload_to='school_teachers/')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')

    # About teacher
    short_description = RichTextUploadingField(verbose_name="Description")
    detail_info = RichTextUploadingField(verbose_name="Detail Info")
    slogan = models.TextField(max_length=300, verbose_name="Slogan")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return self.__str__()

    # Create slug for teacher when creating new teacher
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super(self.__class__, self).save(*args, **kwargs)


class TeacherContactInfo(models.Model):
    """
    Teacher contact info
    """
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


# Create TeacherContactInfo instance after Teacher instance is created
@receiver(post_save, sender=Teacher)
def create_teacher_contact_info(sender, instance, created, **kwargs):
    if created:
        TeacherContactInfo.objects.create(teacher=instance)


@receiver(post_save, sender=Teacher)
def save_teacher_contact_info(sender, instance, **kwargs):
    instance.contact_info.save()


class IndividualLessonApplication(models.Model):
    """
    Model for individual lesson applications
    """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='individual_lessons_applications')
    user_name = models.CharField(max_length=100, verbose_name='Person')
    phone = models.CharField(max_length=100, verbose_name='Person Phone')
    telegram = models.CharField(max_length=100, verbose_name='Telegram', blank=True)

    # Application status
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
        return f"User: {self.user_name}, {self.phone}. Teacher: {self.teacher}"

