from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# My User Profile model
class Profile(models.Model):
    # User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # City
    city = models.CharField(verbose_name="City", max_length=100, blank=True)

    # Messengers
    telegram_link = models.CharField(verbose_name="Telegram", max_length=100, blank=True)
    vk_link = models.CharField(verbose_name="VK", max_length=100, blank=True)
    instagram_link = models.CharField(verbose_name="Instagram", max_length=100, blank=True)

    # Learn progress
    UNKNOWN = "Unknown"
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

    LEVELS = [
        (A1, "A1"), (A2, "A2"),
        (B1, "B1"), (B2, "B2"),
        (C1, "C1"), (C2, "C2"),
        (UNKNOWN, "Unknown")
    ]

    status = models.CharField(max_length=8, verbose_name="Status", choices=LEVELS, default=UNKNOWN)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
