from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from datetime import date
from PIL import Image

class Profile(models.Model):
    """Additional information about a user"""
    # first name, last name, username, and email address are all contained by
    # the user model provided by Django.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    bio = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Say a little about yourself."
    )

    profile_picture = models.ImageField(null=True, upload_to="image-gallery")

    def __str__(self):
        """Identifies the object"""
        return f"{self.user.username}"

    def get_absolute_url(self):
        """Returns url to user profile page for updating and viewing"""
        return reverse("profile_detail", args = [str(self.id)])

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
