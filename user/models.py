from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(verbose_name=_('first_name'), max_length=128)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=128)
