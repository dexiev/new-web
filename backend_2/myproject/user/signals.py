from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    # Check if the user is a superuser or staff (admin)
    if not instance.is_superuser and not instance.is_staff:
        if created:
            # Create a profile for regular users
            Profile.objects.create(user=instance)
        else:
            # Save the profile if it exists
            instance.profile.save()
