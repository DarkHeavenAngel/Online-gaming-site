from rest_framework import serializers
from main.models import Game, Author, Publisher


class GameSerializer(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Game
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'