from django.urls import path
from .views import CreateMessageView, ListMessageView

urlpatterns = [
    path('create/', CreateMessageView.as_view()),
    path('list/', ListMessageView.as_view()),
]
