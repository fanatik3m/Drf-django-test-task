from django.contrib import admin

from .models import Employee, Department


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'emp_department')
    list_display_links = ('name', 'last_name')
    search_fields = ('last_name', 'emp_department')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'director')
    list_display_links = ('name',)
    search_fields = ('name', 'director')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)