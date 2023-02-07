from django.contrib.auth import get_user_model
from .models import *
from django.dispatch import receiver
from django.db.models.signals import post_save


user = get_user_model()


@receiver( post_save,sender = user)
def create_user(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance)



