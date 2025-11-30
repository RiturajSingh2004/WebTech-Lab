from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register'),
    path('success/<int:student_id>/', views.success, name='success'),
]
