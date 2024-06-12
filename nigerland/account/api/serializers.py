from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={"input_type":"password"}, write_only=True)
    password = serializers.CharField(style={"input_type":"password"})
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]
        extra_kwargs ={
            "password":{"write_only": True},
            
        }
        
    def save(self):
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]
            
        if password != confirm_password:
            raise serializers.ValidationError({"error":"password1 and password2 must be the same"})
        if User.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError({"error":"this email has already been used"})
            
        account =User(email=self.validated_data["email"], username=self.validated_data["username"])
        account.set_password(password)
        account.save()
            
        return account


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add additional data to the response
        data.update({
            'user_id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
        })

        return data




