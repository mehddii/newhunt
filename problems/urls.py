from django.urls import path
from . import views

urlpatterns = [
    path('', views.problem_set, name='problems'),
    path('<int:id>/', views.problem, name="problem"),
]
