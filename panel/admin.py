from django.contrib import admin
from .models import Category, People, Transaction

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)

class PeopleAdmin(admin.ModelAdmin):
	list_display = ('fullname', 'username')


admin.site.register(People, PeopleAdmin)


class TransactionAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'category', 'amount', 'payer', 'people_to_str')

admin.site.register(Transaction, TransactionAdmin)