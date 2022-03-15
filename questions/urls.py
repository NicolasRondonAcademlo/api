from django.urls import path
from .views import question_list, QuestionListAPIView

urlpatterns = [
    path("questions/", question_list),
    path("questions_api_view/", QuestionListAPIView.as_view())

]