from django.urls import path
from .views import index,second

urlpatterns = [
    path('second/', second, name="second"),
]