from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("",views.expense_list,name="expense_list"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("expense/<int:pk>",views.expense_detail,name="expense_detail"),
    path("expense/create/",views.expense_create,name="expense_create"),
    path("expense/<int:pk>/update/", views.expense_update, name="expense_update"),
    path("expense/<int:pk>/delete/", views.expense_delete, name="expense_delete"),
    path("category/",views.category_list,name="category_list"),
    path("category/create/",views.category_create,name="category_create"),
    path("category/<int:pk>/update/",views.category_update,name="category_update"),
    path("category/<int:pk>/delete/",views.category_delete,name="category_delete"),
]
