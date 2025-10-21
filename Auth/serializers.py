import logging

from rest_framework import serializers
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password_check')
        extra_kwargs = {'password': {'required': True,'write_only': True, 'allow_blank': False},
                        'first_name': {'required': False, 'allow_blank': True, 'max_length': 30},
                        'last_name': {'required': False, 'allow_blank': True, 'max_length': 30},
                        'username': {'required': True, 'max_length': 20, 'allow_blank': False},
                        'email': {'required': True, 'max_length': 30, 'allow_blank': False},
                        }

    def create(self, validated_data):
        validated_data.pop('password_check')
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        logger.info(f"User created successfully")
        return user

    def validate_email(self, value):
        if '@' not in value or '.' not in value:
            logger.warning(f"Invalid email: {value}")
            raise serializers.ValidationError('Invalid email address')
        return value

    def validate(self, data):
        if len(data['password']) < 6:
            logger.warning(f"Invalid password: too short password")
            raise serializers.ValidationError('Password must be at least 6 characters')
        if data['password'] != data['password_check']:
            logger.warning(f"Invalid password: password does not match")
            raise serializers.ValidationError('Passwords must match')
        return data