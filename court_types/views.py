from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import Court_type
from .serializers import Court_typeSerializer
from .permissions import IsAdminOrReadOnly

import ipdb

class Court_typeView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Court_type.objects.all()
    serializer_class = Court_typeSerializer


class Court_typeViewDetail(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Court_type.objects.all()
    serializer_class = Court_typeSerializer

    lookup_url_kwarg = "court_type_id"
