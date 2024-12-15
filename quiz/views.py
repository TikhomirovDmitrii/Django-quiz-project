import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QuizQuestion
from .serializers import QuizQuestionSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class QuizQuestionAPIView(APIView):
    def post(self, request):
        questions_num = request.data.get('questions_num', 1)

        if not isinstance(questions_num, int) or questions_num <= 0: # Проверяем тип данных
            return Response({"error": "Invalid 'questions_num' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        questions = []
        while len(questions) < questions_num:
            response = requests.get(f'https://the-trivia-api.com/v2/questions?limit={questions_num}')
            if response.status_code != 200:
                return Response({"error": "Failed to fetch data from external API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            data = response.json()
            for item in data:
                if not QuizQuestion.objects.filter(question_id=item['id']).exists(): # Прверяем не повторяется ли вопрос
                    question = QuizQuestion.objects.create(
                        question_id=item['id'],
                        question_text=item['question']['text'],
                        answer_text=item['correctAnswer']
                    )
                    questions.append(question)

        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class QuizView(APIView):
    @swagger_auto_schema(
        operation_description='Создание викторины с указанным количеством вопросов',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['questions_num'],
            properties={'questions_num': openapi.Schema(type=openapi.TYPE_INTEGER, description='Количество вопросов')},
        ),
        responses={
            201: openapi.Response(
                description='Викторина успешно создана',
                examples={
                    "application/json": [
                        {
                            "question_id": "example_id",
                            "question_text": "Пример вопроса",
                            "answer_text": "Пример ответа",
                            "created_at": "2024-12-15T12:00:00Z"
                        }
                    ]
                },
            ),
            400: 'Некорректный запрос',
        },
    )
    def post(self, request):
        return Response(data, status=status.HTTP_201_CREATED)
