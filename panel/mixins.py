from django.http import Http404

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