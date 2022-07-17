from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Mobile
from .serializers import MobileSerializer
from django.db.models import Q


class SuggestMobileView(ListAPIView):
    serializer_class = MobileSerializer

    def get_queryset(self):
        min_price = self.request.GET.get('min_price', None)
        max_price = self.request.GET.get('max_price', None)
        queryset = Mobile.objects.all()

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        return queryset
