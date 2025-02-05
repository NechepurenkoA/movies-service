from rest_framework import serializers

from directors.models import Director


class DirectorSerializer(serializers.ModelSerializer):
    """Serializer for Director model"""

    class Meta:
        model = Director
        fields = "__all__"
