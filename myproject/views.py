
from django.http import HttpResponse
from django.shortcuts import render
from Employees.models import Employee
from django.shortcuts import get_object_or_404
 
def  home(request):
  return render(request,'home.html')


def aboutus(request):
  return render(request,'aboutus.html')

from django.shortcuts import render, redirect, get_object_or_404
from Employees.models import Employee


def register(request):

    if request.method == "POST":
        Employee.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            designation=request.POST.get('designation'),
            password=request.POST.get('password'),
            photo=request.FILES.get('photo')
        )

        return redirect('test')

    return render(request, 'register.html')


def testmonials(request):

    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        employee = Employee.objects.filter(
            first_name=name,
            password=password
        ).first()

        if employee:
            return redirect('employee_details', pk=employee.id)

        return render(request, 'testmonial.html', {
            'error': 'Invalid Name or Password'
        })

    return render(request, 'testmonial.html',
                  {'error': 'Invalid Name or Password'})


from django.shortcuts import render, get_object_or_404
from Employees.models import Employee

def employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    return render(
        request,
        'employee.html',
        {'employee': employee}
    )