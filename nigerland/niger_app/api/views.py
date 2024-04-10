from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from niger_app.models import Surveyor, Documents
from .serializers import SurveyorSerializer, DocumentSerializer
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .pagination import DocumentListPagination, DocumentListPaginationLO, DocumentListPaginationCu


class SurveyorDocument(generics.ListAPIView):
    queryset = Documents.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentSerializer
    pagination_class = DocumentListPaginationCu
       


class SurveyorList(generics.ListCreateAPIView):
    queryset = Surveyor.objects.all()
    serializer_class = SurveyorSerializer
    permission_classes =[IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
    
    
class SurveyorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Surveyor.objects.all()
    serializer_class = SurveyorSerializer
    permission_classes =[IsOwnerOrReadOnly]
    
    
    
class DocumentList(generics.ListAPIView):
    # queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    # permission_classes =[IsOwnerOrReadOnly]
    
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username', 'location']
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['user__username', 'email']
    pagination_class = DocumentListPaginationLO
    
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Documents.objects.filter(user=pk)
    
class DocumentCreate(generics.CreateAPIView):
   
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    
     
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        serializer.save(user=user)
    
    
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    