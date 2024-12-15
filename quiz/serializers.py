from rest_framework import serializers
from .models import QuizQuestion


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['question_id', 'question_text', 'answer_text', 'created_at']