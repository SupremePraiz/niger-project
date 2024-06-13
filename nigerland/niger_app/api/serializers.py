from rest_framework import serializers

from niger_app.models import Surveyor, Documents
    

class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documents
        fields = "__all__"
    
class SurveyorSerializer(serializers.ModelSerializer):
    # documents = DocumentSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Surveyor
        fields = "__all__"




