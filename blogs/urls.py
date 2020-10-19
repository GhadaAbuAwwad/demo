from django.urls import include , path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

app_name='blogs'
urlpatterns = [
    # ex: /blogs/
    path('', include(router.urls) , name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
   ]