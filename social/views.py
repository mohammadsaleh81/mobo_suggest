from rest_framework.generics import CreateAPIView
from .models import Message
from rest_framework.permissions import IsAuthenticated
from .serializers import MessageSerializer
from .choices import StatusChoices


class CreateListMessageView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, status=StatusChoices.SENT)






