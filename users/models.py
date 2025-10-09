from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField('Avatar Pictures', null=True, blank=True, upload_to="avatars/")
    email_active_code = models.CharField('Active Code', max_length=120)
    about_user = models.CharField('About User', max_length=120, null=True, blank=True)
    phone_number = models.CharField('Phone Numbers', max_length=15, unique=True, null=True, blank=True)
    address = models.CharField('Address', max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email


class Province(models.Model):
    name = models.CharField('Province', max_length=50, null=True, blank=True)
    is_valid = models.BooleanField('Is Valid', default=True)
    modified_at = models.DateTimeField('Modified At', auto_now=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        db_table = 'provinces'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField('Nickname', max_length=30, null=True, blank=True)
    birth_date = models.DateField('Date of Birth', null=True, blank=True)
    gender = models.CharField('Gender', max_length=30, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        db_table = 'user_profiles'

    def get_first_name(self):
        return self.user.phone_number

    def get_last_name(self):
        return self.user.last_name

    def get_nickname(self):
        return self.nickname if self.nickname else self.user.username

    def __str__(self):
        return self.user.username


class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPES = (
        (WEB, 'Web'),
        (IOS, 'IOS'),
        (ANDROID, 'Android'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    device_uuid = models.UUIDField('Device UUID', unique=True, null=True, blank=True)
    last_login = models.DateTimeField('Last Login', null=True, blank=True)
    device_type = models.PositiveSmallIntegerField('Device Type', choices=DEVICE_TYPES, default=ANDROID)
    device_os = models.CharField('Device OS', max_length=30, null=True, blank=True)
    app_version = models.CharField('App Version', max_length=30, null=True, blank=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        db_table = 'devices'
