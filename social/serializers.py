from rest_framework import serializers
from .models import Message
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from user.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'title', 'text', 'receiver', 'sender', 'status')
        extra_kwargs = {"sender": {"required": False}, "status": {"required": False}, "receiver": {"required": False}}

    def create(self, validated_data):
        request = self.context['request']
        username = request.data.get('username', None)
        user = User.objects.filter(username=username).first()

        if user:
            if user == request.user:
                raise ValidationError(_('You cannot send messages to yourself.'))

            message = Message.objects.create(receiver=user, **validated_data)
            return message
        else:
            raise ValidationError(_('User nit found.'))




