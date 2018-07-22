from django.db import models

from django.dispatch import receiver

from .models import ProfileImage


@receiver(models.signals.post_delete, sender=ProfileImage)
def delete_image_images(sender, instance, **kwargs):
    instance.image.delete_all_created_images()
    instance.image.delete(save=False)
