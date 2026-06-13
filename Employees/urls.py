from django.urls import path
from .views import (
    register,
    testmonials,
    employee,
    edit_employee,
    delete_employee,
    logout_user,
    employee_list
)

urlpatterns = [
    path('', register, name='register'),
    path('test/', testmonials, name='test'),
    path('list/', employee_list, name='employee_list'),

    path('<int:pk>/', employee, name='employee_details'),
    path('edit/<int:pk>/', edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', delete_employee, name='delete_employee'),
    path('logout/', logout_user, name='logout'),
]