from django.contrib.auth.models import User, Group
from rest_framework import serializers
from client.quickstartt.models import Reserva
from django.utils import timezone


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ReservaSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    date_posted = serializers.DateTimeField(default=timezone.now)
    content = serializers.CharField(max_length=200)   
    title = serializers.CharField(max_length=100)

