from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



from .serializers import RegistrationSerializer

# @api_view(['POST'])
# def logout_view(request):
    
#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)



# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
    
    
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    
