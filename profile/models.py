from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=15, null=True, blank=True)
    default_street_adress = models.CharField(max_length=60, null=True, blank=True)
    default_city = models.CharField(max_length=30, null=True, blank=True)
    default_postal_code = models.CharField(max_length=15, null=True, blank=True)
    default_co = models.CharField(max_length=30, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
# post_save.connect(create_profile, sender=User)


# def update_profile(sender, instance, created, **kwargs):
#     if created is False:
#         instance.profile.save()


# post_save.connect(update_profile, sender=User)

