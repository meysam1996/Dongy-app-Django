from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class People(models.Model):
    fullname = models.CharField(max_length=70, verbose_name='نام')
    username = models.CharField(max_length=100, unique=True, default=None, null=True, blank=True, verbose_name='نام کاربری')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "فرد"
        verbose_name_plural = "افراد"

    def __str__(self):
        return self.fullname


class Transaction(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس تراکنش')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    amount = models.CharField(max_length=7, verbose_name='مبلغ به تومان')
    payer = models.ForeignKey(People, null=True, on_delete=models.SET_NULL, related_name='payer', verbose_name='پرداخت کننده')
    people = models.ManyToManyField(People, verbose_name='افراد')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش ها"
    
    def __str__(self):
        return self.title

    def people_to_str(self):
        return ", ".join([people.fullname for people in self.people.all()])
    people_to_str.short_description = "افراد"


