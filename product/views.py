from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Mobile
from .serializers import MobileSerializer


class SuggestMobileView(ListAPIView):
    serializer_class = MobileSerializer

    def get_queryset(self):
        min_price = self.request.GET.get('min_price', None)
        max_price = self.request.GET.get('max_price', None)
        min_date = self.request.GET.get('min_date', None)
        max_date = self.request.GET.get('max_date', None)
        queryset = Mobile.objects.all()

        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_date:
            queryset = queryset.filter(production_date__lte=max_date)
        if min_date:
            queryset = queryset.filter(production_date__gte=min_date)

        return queryset
