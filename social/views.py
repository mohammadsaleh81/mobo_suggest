from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Message
from rest_framework.permissions import IsAuthenticated
from .serializers import MessageSerializer
from .choices import StatusChoices
from .paginations import MessagePagination
from django.db.models import Q


class CreateMessageView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, status=StatusChoices.SENT)


class ListMessageView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer
    pagination_class = MessagePagination

    def get_queryset(self):
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))




