from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from decouple import config
from django.core.mail import send_mail
# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')

    photo = CloudinaryField('image')

    profession = models.CharField(max_length=50, null=True)

    about = models.TextField(null=True)

    birthday = models.DateField(null=True)

    twitter = models.URLField(max_length=50, null=True)

    linkedin = models.URLField(max_length=50, null=True)

    facebook = models.URLField(max_length=50, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def email(sender, instance, created, **kwargs):
        if created: (
            'Bienvenido a ABC BLOG',
            str('Hola ' + instance.full_name + ', usted se ha registrado satisfactoriamente en el blog.'
                                               '¡Es un placer que seas parte de nuestra familia!'),
            config('EMAIL_HOST_USER'),
            [instance.email]
        )





