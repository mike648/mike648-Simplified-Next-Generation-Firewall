from django.urls import path
from .views import PacketListCreate

urlpatterns = [
    path('packets/', PacketListCreate.as_view(), name='packet-list-create'),
]
