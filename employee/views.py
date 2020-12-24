from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm, EmployeeProfileForm

# @login_required(login_url='/login/')
def employee_list(request):
    context = {}
    context['title'] = 'Employees'
    context['users'] = User.objects.all()
    return render(request, 'employee/employee_list.html', context)

def employee_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    return render(request, 'employee/employee_details.html', context)

def employee_edit(request, id=None):
    context = {}
    context['title'] = 'Employees'
    return render(request, 'employee/employee_edit.html', context)

def employee_delete(request, id=None):
    context = {}
    context['title'] = 'Employees'
    return render(request, 'employee/employee_delete.html', context)

def employee_add(request):
    form = EmployeeProfileForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        context['message'] = 'This is POST request'
    else:
        context['message'] = 'This is GET request'

    context['title'] = 'Employee Profile'
    context['form'] = form

    return render(request, 'employee/employee_add.html', context)
