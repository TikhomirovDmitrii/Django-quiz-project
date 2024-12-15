from django.urls import path
from .views import QuizQuestionAPIView


urlpatterns = [
    path('api/quiz/', QuizQuestionAPIView.as_view(), name='quiz-api'),
]