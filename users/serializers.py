from cProfile import label
from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label = "username",
        write_only = True
    )
    password = serializers.CharField(
        label = "password",
        trim_whitespace = False,
        write_only = True
    )
    def validate(self, attrs):
        username = attrs.get('user')
        password = attrs.get('password')

        if username and password: 
            user = authenticate(request=self.context.get('request'), username= username, password=password)
            if not user:
                msg = "wrong user or password"
                raise serializers.ValidationError(msg,code="authorization")
        else:
            msg = "Both user and password required"
            raise serializers.ValidationError(msg,code="authorization")
        attrs['user']= user
        return attrs
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser', 'username', 'password']