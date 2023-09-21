from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('employees/filter', EmployeeFilterAPIView.as_view()),
    path('departments/', DepartmentListAPIView.as_view()),
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
]