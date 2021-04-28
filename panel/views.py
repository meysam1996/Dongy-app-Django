from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, FieldsMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.conf import settings
from .models import Category

# Create your views here.
# @login_required
# def home(request):
# 	return render(request, 'panel/home.html')

class CategoryList(LoginRequiredMixin, ListView):
    template_name = 'panel/home.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class CategoryCreate(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Category
    template_name = 'panel/category-create-update.html'
