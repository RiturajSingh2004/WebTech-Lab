from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    return render(request, 'employees/employee_detail.html', {'employee': employee})
