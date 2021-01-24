from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
<<<<<<< HEAD
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
=======
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
>>>>>>> 5d854c0 (npm init, etc.)
