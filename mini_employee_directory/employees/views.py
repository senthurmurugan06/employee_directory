from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


def employee_directory(request):
    return render(request, 'employees/employee_directory.html')

def employee_list(request):
    employees = list(Employee.objects.values())
    return JsonResponse({'employees': employees})


@csrf_exempt  
@require_POST
def add_employee(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    department = request.POST.get('department')
    if not all([name, email, department]):
        return HttpResponseBadRequest('Missing fields')
    emp = Employee.objects.create(name=name, email=email, department=department)
    return JsonResponse({'id': emp.id, 'name': emp.name, 'email': emp.email, 'department': emp.department, 'date_joined': emp.date_joined})
