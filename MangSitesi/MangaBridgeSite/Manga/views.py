from django.shortcuts import render
from django.views import generic
from . import models
# Create your views here.
class IndexView(generic.ListView):
    template_name = "manga/index.html"
    model = models.Manga
    context_object_name = "mangalist"

class MangaView(generic.DetailView):
    template_name = "manga/details.html"
    model = models.Manga

class MainPageView(generic.ListView):
    template_name = "manga/mainpage.html"
    model = models.Chapter
    context_object_name= "latest_relase"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manga_list'] = models.Manga.objects.all()
        return context 

    def get_queryset(self):   
        return models.Chapter.objects.order_by('-pub_date')[:20]