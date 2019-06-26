from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Plane

@receiver(pre_save, sender = Plane)
def wrapper_around_handle_built_and_updated(sender, instance, **kwargs):
    instance.handle_built_and_updated()