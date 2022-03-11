from django.views.decorators.csrf import csrf_exempt

from .serializers import QuestionSerializer
from .models import Question
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def question_list(request):

    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionSerializer(
           questions, many=True
        )
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors, status=400)