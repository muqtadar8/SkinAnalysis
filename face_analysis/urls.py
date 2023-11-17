from . import views
from django.urls import path

urlpatterns = [
    path('',views.analyze_image, name = 'analyze_image'),
]