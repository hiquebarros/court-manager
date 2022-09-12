from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .models import Payment_information
from .serializers import PaymentInformationSerializer
from .permissions import IsAuthenticated, IsOwner





class PaymentInformationView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner] 
    queryset= Payment_information.objects.all()
    serializer_class = PaymentInformationSerializer
    
    import ipdb
    ipdb.set_trace()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
     


class PaymentInformationIDView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    queryset= Payment_information.objects.all()
    serializer_class = PaymentInformationSerializer              
                
                
