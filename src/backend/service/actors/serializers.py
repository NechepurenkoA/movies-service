from rest_framework import serializers

from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    class Meta:
        model = Actor
        fields = "__all__"
