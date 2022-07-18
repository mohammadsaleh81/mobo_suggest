from django.db import models
from product.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from .choices import StatusChoices
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(BaseModel):
    sender = models.ForeignKey(
        User, verbose_name=_('sender'),
        on_delete=models.CASCADE, related_name='messages_sender'
    )
    receiver = models.ForeignKey(
        User, verbose_name=_('receiver'),
        on_delete=models.CASCADE, related_name='messages_receiver'
    )
    title = models.CharField(verbose_name=_('title'), max_length=128)
    text = models.TextField(verbose_name=_('text'))
    status = models.PositiveSmallIntegerField(verbose_name=_('status'), choices=StatusChoices.choices)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return self.title