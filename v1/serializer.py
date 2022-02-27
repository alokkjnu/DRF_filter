from rest_framework import serializers
from .models import ScoreCard

class ScoreCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreCard
        fields = "__all__"

