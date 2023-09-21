from django.core.validators import MaxValueValidator
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=255, db_index=True)
    position = models.CharField(max_length=255)
    salary = models.IntegerField()
    age = models.IntegerField(validators=[MaxValueValidator(60)])
    emp_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.last_name