from rest_framework import serializers
from .models import Message
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'title', 'text', 'receiver', 'sender', 'status')
        extra_kwargs = {"sender": {"required": False}, "status": {"required": False}}

    def validate(self, attrs):
        request = self.context['request']
        if attrs['receiver'] == request.user:
            raise ValidationError(_('You cannot send messages to yourself'))
        return attrs

