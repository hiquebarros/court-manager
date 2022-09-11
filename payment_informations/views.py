from rest_framework import generics

from .models import Payment_information
from .serializers import PaymentInformationSerializer
from .permissions import IsAuthenticated, IsOwner




class PaymentInformationView(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):
        permission_classes = [IsAuthenticated, IsOwner] 
        queryset= Payment_information.objects.all()
        serializer_class = PaymentInformationSerializer
        
        def perform_create(self, serializer):
                serializer.save(user=self.request.user)
                
                