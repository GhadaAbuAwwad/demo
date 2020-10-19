from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Post
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(is_published=True).order_by('-pub_date')

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows post to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-pub_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class DetailView(generic.DetailView):
        model = Post
        template_name = 'blogs/detail.html'