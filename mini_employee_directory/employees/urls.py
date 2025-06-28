from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_directory, name='employee_directory'),
    path('api/employees/', views.employee_list, name='employee_list'),
    path('api/employees/add/', views.add_employee, name='add_employee'),
] 