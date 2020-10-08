from django.urls import path
from django.views import generic
from . import views

app_name='blogs'
urlpatterns = [
    # ex: /blogs/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
   ]