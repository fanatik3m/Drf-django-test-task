from django.contrib.auth.models import User
from django.db.models import Count, Avg, Sum
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.viewsets import GenericViewSet

from .models import Employee, Department
from .serializers import EmployeeSerializer, UserSerializer, DepartmentSerializer
from .paginators import EmployeePagination


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = EmployeePagination


class EmployeeFilterAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = EmployeePagination

    def get_queryset(self):
        if self.request.query_params.get('last_name'):
            return Employee.objects.filter(last_name=self.request.query_params.get('last_name'))
        if self.request.query_params.get('department_id'):
            return Employee.objects.filter(emp_department=self.request.query_params.get('department_id'))
        return Employee.objects.filter(pk=1)


class DepartmentListAPIView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.annotate(
        total_employees_count=Count('employee'),
        total_salary=Sum('employee__salary')
    )
    permission_classes = (permissions.IsAuthenticated, )


class RegisterUserView(generics.CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer
