from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Category

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.fields = [
                'title', 'slug'
            ]
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.owner = self.request.user
        return super().form_valid(form)

class CategoryOwnerMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        category = get_object_or_404(Category, pk=pk)
        if  category.owner == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't access this page!")