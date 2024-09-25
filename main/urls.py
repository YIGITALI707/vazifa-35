from django.contrib import admin
from django.urls import path

from .views import CommentApiView,MovieApiView

urlpatterns = [
    path('', MovieApiView.as_view()),
    path('<int:pk>/',MovieApiView.as_view()),
]