from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .decorators import *

# Create your views here.

def logoutPage(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username OR Password incorrect")

    return render(request, 'tasks/login.html')


def register(request):
    form = UserForm()
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            emailid = form.cleaned_data.get('email')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Customer.objects.create(
                user=user,
                email=emailid,
            )

            messages.success(request, "Account was created for " + username)
            return redirect('login')

    content = {'form': form}
    return render(request, 'tasks/register.html', content)


@admin_only
def homePage(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/mainPage.html', context)

@login_required(login_url='login')
def userPage(request):
    tasks = request.user.customer.task_set.all()

    context = {'tasks': tasks}
    return render(request, 'tasks/userPage.html', context)

@login_required(login_url='login')
def createPage(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'tasks/createPage.html', context)

@login_required(login_url='login')
def updatePage(request, pk):
    item = Task.objects.get(id=pk)
    form = TaskForm(instance=item)
    context = {'form': form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'tasks/updatePage.html', context)

@login_required(login_url='login')
def deletePage(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'tasks/deletePage.html', context)
