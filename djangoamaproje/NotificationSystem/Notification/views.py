from django.shortcuts import render
from.models import student
from django.views import generic
# Create your views here.
class IndexView(generic.ListView):
    template_name = "notification/index.html"
    context_object_name = "student"
    model = student

class CagirSistemi(generic.DetailView):
    template_name = "notification/student.html"