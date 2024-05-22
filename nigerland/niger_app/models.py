from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Surveyor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Surveyor"
    
    def __str__(self):
        return self.name

    
class Documents(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50)
    surveyor = models.ForeignKey(Surveyor,on_delete=models.CASCADE,related_name="documents")
    file = models.FileField(upload_to='excel_files/')
    created = models.DateTimeField(auto_now_add=True)
    location =models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Documents"
    
    # def create(self, validated_data):
    #     surveyor_data = validated_data.pop('document')
    #     document_instance = Documents.objects.create(**validated_data)
    #     Surveyor.objects.create(document=document_instance, **surveyor_data)
    #     return document_instance
        
    def __str__(self):
        return self.location
   