from django.urls import path,include
from api_app.views import get_expenses,LoginAPI

urlpatterns = [
    path("expense/", get_expenses.as_view(), name="expense_api"),
    path("login/",LoginAPI.as_view(),name="login_api")
]
