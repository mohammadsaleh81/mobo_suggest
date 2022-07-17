from django.urls import path
from .views import SuggestMobileView

urlpatterns = [
    path('suggest/', SuggestMobileView.as_view()),
]
