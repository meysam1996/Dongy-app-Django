from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
    FormValidMixin, CategoryFieldsMixin, CategoryOwnerMixin,
    TransactionFieldsMixin, TransactionOwnerMixin,
    PeopleOwnerMixin 
    )
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from .models import Category, Transaction, People

# Create your views here.
# @login_required
# def home(request):
# 	return render(request, 'panel/home.html')

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'panel/home.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class CategoryCreate(LoginRequiredMixin, FormValidMixin, CategoryFieldsMixin, CreateView):
    model = Category
    template_name = 'panel/category-create-update.html'

class CategoryUpdate(CategoryOwnerMixin, FormValidMixin, CategoryFieldsMixin, UpdateView):
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
        pk = self.kwargs.get('pk')
        category = get_object_or_404(Category, pk=pk)
        return category.transactions.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['title', 'slug', 'amount', 'payer', 'people']
    template_name = 'panel/transaction-create-update.html'

    def get_success_url(self):
        return reverse('panel:transaction-list', args=[category.id])

    def get_context_data(self, **kwargs):
        global category
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        kwargs['category'] = category
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.category = category
        return super().form_valid(form)


class TransactionUpdateView(TransactionOwnerMixin, UpdateView):
    model = Transaction
    fields = ['title', 'slug', 'amount', 'payer', 'people']
    template_name = 'panel/transaction-create-update.html'

    def get_success_url(self):
        return reverse('panel:transaction-list', args=[category.id])

    def get_object(self):
        transaction = get_object_or_404(Transaction, id=self.kwargs['tr_pk'])
        return transaction
    
    def get_context_data(self, **kwargs):
        global category
        category = get_object_or_404(Category, id=self.kwargs['c_pk'])
        kwargs['category'] = category
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.category = category
        return super().form_valid(form)


class TransactionDeleteView(TransactionOwnerMixin, DeleteView):
    model = Transaction
    template_name = 'panel/transaction-confirm-delete.html'

    def get_success_url(self):
        return reverse('panel:transaction-list', args=[category.id])

    def get_object(self):
        transaction = get_object_or_404(Transaction, id=self.kwargs['tr_pk'])
        return transaction
    
    def get_context_data(self, **kwargs):
        global category
        category = get_object_or_404(Category, id=self.kwargs['c_pk'])
        kwargs['category'] = category
        return super().get_context_data(**kwargs)


class PeopleListView(LoginRequiredMixin, ListView):
    template_name = 'panel/people-list.html'

    def get_queryset(self):
        global category
        pk = self.kwargs.get('pk')
        category = get_object_or_404(Category, pk=pk)
        return category.people.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class PeopleCreateView(LoginRequiredMixin, CreateView):
    model = People
    fields = ['fullname', 'username']
    template_name = 'panel/people-create-update.html'

    def get_success_url(self):
        return reverse('panel:people-list', args=[category.id])

    def get_context_data(self, **kwargs):
        global category
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        kwargs['category'] = category
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.category = category
        return super().form_valid(form)


class PeopleUpdateView(PeopleOwnerMixin, UpdateView):
    model = People
    fields = ['fullname', 'username']
    template_name = 'panel/people-create-update.html'

    def get_success_url(self):
        return reverse('panel:people-list', args=[category.id])

    def get_object(self):
        people = get_object_or_404(People, id=self.kwargs['p_pk'])
        return people
    
    def get_context_data(self, **kwargs):
        global category
        category = get_object_or_404(Category, id=self.kwargs['c_pk'])
        kwargs['category'] = category
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.category = category
        return super().form_valid(form)