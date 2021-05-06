from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, FieldsMixin, CategoryOwnerMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from .models import Category, Transaction

# Create your views here.
# @login_required
# def home(request):
# 	return render(request, 'panel/home.html')

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'panel/home.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class CategoryCreate(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Category
    template_name = 'panel/category-create-update.html'

class CategoryUpdate(CategoryOwnerMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Category
    template_name = 'panel/category-create-update.html'


class CategoryDelete(CategoryOwnerMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('panel:home')
    template_name = 'panel/category-confirm-delete.html'


class TransactionList(LoginRequiredMixin, ListView):
    template_name = 'panel/transaction-list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        return category.transactions.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class TransactionCreateView(LoginRequiredMixin, FormValidMixin, CreateView):
    model = Transaction
    template_name = 'panel/transaction-create-update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        category = get_object_or_404(Category, pk=pk)
        context['category'] = category
        return context
