from rest_framework import generics
from .models import Packet
from .serializers import PacketSerializer

class PacketListCreate(generics.ListCreateAPIView):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer

