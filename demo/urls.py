from django.urls import path, include
from .views import Second, First
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first', First.as_view()),
    path('second', Second.as_view())
]