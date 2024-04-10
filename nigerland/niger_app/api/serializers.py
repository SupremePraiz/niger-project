from rest_framework import serializers

from niger_app.models import Surveyor, Documents
    

class DocumentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    surveyor = serializers.CharField(source='surveyor.name')
    
    class Meta:
        model = Documents
        fields = "__all__"
    
class SurveyorSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Surveyor
        fields = "__all__"



