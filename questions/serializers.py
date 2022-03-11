from rest_framework import serializers
from .models import Question
from core.serializers import UserSerializer


class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Question
        fields = '__all__'
