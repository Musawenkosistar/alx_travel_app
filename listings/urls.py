from django.urls import path
from . import views

urlpatterns = [
    # Example endpoint
    path('test/', views.test_api, name='test_api'),
]
