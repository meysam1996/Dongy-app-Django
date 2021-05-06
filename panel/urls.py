from django.contrib.auth import views
from django.urls import path
from .views import (
    CategoryListView, CategoryCreate, CategoryUpdate, CategoryDelete,
    TransactionList, TransactionCreateView
    )

app_name= "panel"
# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     # path('logout/', views.LogoutView.as_view(), name='logout'),

#     # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#     # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#     # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('panel/', CategoryListView.as_view(), name='home'),
    path('panel/New-Categort/', CategoryCreate.as_view(), name='category-create'),
    path('panel/Categort/update/<int:pk>', CategoryUpdate.as_view(), name='category-update'),
    path('panel/Categort/delete/<int:pk>', CategoryDelete.as_view(), name='category-delete'),
    path('panel/Categort/<slug:slug>/transactionlist/', TransactionList.as_view(), name='transaction-list'),
    path('panel/Categort/<int:pk>/create-transaction/', TransactionCreateView.as_view(), name='transaction-create')

]