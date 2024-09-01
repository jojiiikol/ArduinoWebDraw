from django.urls import path

from .views import *

urlpatterns = [
    path('', MyView.as_view(), name='index'),
    path('draw/', DrawImageView.as_view(), name='draw'),
]