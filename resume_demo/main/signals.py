from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile

# we going import post save the built-in user model, this signal is it's a receiver, when a object is created when a user object is created,
# it fires a signal to this signals.py file, there's a receiver that picks up that signal, and then this function is called right so it's create profile
# that is what's going to be used to create the user profile, so when we create a super user in a few moments, that user will be created the signal will
# be fired
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)