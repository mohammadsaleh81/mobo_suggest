from django.urls import path
from .views import CreateListMessageView

urlpatterns = [
    path('create/', CreateListMessageView.as_view()),
]
