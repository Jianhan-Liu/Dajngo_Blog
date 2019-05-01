"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/30
  Time: 1:36
  自动添加profile图片
 """
__author__ = 'liujianhan'

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
