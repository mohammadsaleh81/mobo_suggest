from django.db import models


class StatusChoices(models.IntegerChoices):
    SENT = 0, 'sent'
    seen = 1, 'seen'
    NOT_SENT = 2, 'not sent'
