from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts import constants
from common import mixins as common_mixins
from common import models as common_models


class UserProfile(common_mixins.TimestampMixin, common_models.BaseModel):
    user = models.ForeignKey(User, unique=True)
    permission = models.CharField(
        'UserPermission', max_length=40, blank=True, null=True,
        choices=constants.PERMISSION_CHOICES)

    def __unicode__(self):
        if self.user.first_name:
            if self.user.last_name:
                return "{0} {1}'s Profile".format(
                    self.user.first_name, self.user.last_name)
            else:
                return "{0}'s Profile".format(self.user.first_name)
        else:
            return "{0}'s Profile".format(self.user.username)

    @property
    def is_active(self):
        return self.user.is_active

    @property
    def is_staff(self):
        return self.user.is_staff

    def is_permitted(self, permissions):
        return self.user.is_superuser or\
            (self.permission is not None and self.permission in permissions)


def _get_profile(self):
    profile, is_created = UserProfile.objects.get_or_create(user=self)
    return profile

User.profile = property(_get_profile)


@receiver(post_save, sender=UserProfile)
def set_django_permissions(sender, instance, **kwargs):
    user = instance.user
    user.is_staff = (instance.permission in
                     constants.PERMISSIONS_STAFF_AND_ABOVE)
    user.save()
