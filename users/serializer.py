from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "parol 8 ta sondan iborat bolishi kere."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        return user
