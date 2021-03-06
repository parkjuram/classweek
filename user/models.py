# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from datetime import datetime
# from user.models import UserProfile

# 이름, 생년월인, 성별, 폰번
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    name = models.TextField( null=True )
    birthday = models.DateField( null=True )
    phonenumber = models.TextField( null=True )
    gender = models.CharField( max_length=1, null=True)
    # ...


def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)

signals.post_save.connect(create_user_profile, sender=User)


class UserInquire(models.Model):
    user = models.ForeignKey(User, related_name='get_inquires')
    inquire_content = models.TextField( null=True )
    created = models.DateTimeField(auto_now_add=True, default=datetime.now)