from django.urls import include , path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    path('', include(router.urls), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/5/vote/
    path('addQues/', views.addQuesView , name='addQues'),
]