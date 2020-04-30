from django.urls import path
from .views import Second, first

urlpatterns = [
    path('', first),
    path('second', Second.as_view())
]