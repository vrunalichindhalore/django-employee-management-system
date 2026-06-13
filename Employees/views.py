from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Employees.models import Employee


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

    return render(request, 'testmonial.html')


def employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    return render(
        request,
        'employee.html',
        {'employee': employee}
    )
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

        return redirect('/test/')

    return render(request, 'register.html')

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.phone_number = request.POST.get('phone_number')
        employee.designation = request.POST.get('designation')

        employee.save()

        return redirect(
            'employee_details',
            pk=employee.id
        )

    return render(
        request,
        'edit_employee.html',
        {'employee': employee}
    )

def logout_user(request):
    return redirect('/test/')

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('/home/')

def employee_list(request):
    search = request.GET.get('search')

    if search:
        employees = Employee.objects.filter(
            first_name__icontains=search
        )
    else:
        employees = Employee.objects.all()

    return render(
        request,
        'employee_list.html',
        {'employees': employees}
    )