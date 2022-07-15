from django.db import models


class PanelChoices(models.IntegerChoices):
    IPS = 0, 'ips'
    AMOLED = 1, 'amoled'
    SUPER_AMOLED = 2, 'super_amoled'


class StorageChoices(models.IntegerChoices):
    GB_64 = 0, '63 GB'
    GB_128 = 1, '128 GB'
    GB_256 = 2, '256 GB'
    GB_512 = 3, '512 GB'


class RamChoices(models.IntegerChoices):
    GB_4 = 0, '4 GB'
    GB_6 = 1, '6 GB'
    GB_8 = 2, '8 GB'
    GB_12 = 3, '12 GB'
    GB_16 = 4, '16 GB'


class OSChoices(models.IntegerChoices):
    Android = 0, 'android'
    IOS = 1, 'IOS'

