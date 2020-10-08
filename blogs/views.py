from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Post
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.filter(is_published=True).order_by('-pub_date')

class DetailView(generic.DetailView):
        model = Post
        template_name = 'blogs/detail.html'