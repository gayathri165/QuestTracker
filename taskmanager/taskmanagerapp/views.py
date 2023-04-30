from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateTaskForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task


# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    msg = None

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_login')
        else:
            msg = 'form is not valid'
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context=context)


def head_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.groups.filter(name='admin').exists():
                    auth.login(request, user)
                    return redirect('dashboard')
    context = {'form': form}
    return render(request, 'login.html', context=context)
def manager_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.groups.filter(name='manager').exists():
                    auth.login(request, user)
                    return redirect('manager_dashboard')
    context = {'form': form}
    return render(request, 'manager_login.html', context=context)

def staff_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.groups.filter(name='staff').exists():
                    auth.login(request, user)
                    return redirect('staff_dashboard')
    context = {'form': form}
    return render(request, 'staff_login.html', context=context)

def teamlead_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.groups.filter(name='teamlead').exists():
                    auth.login(request, user)
                    return redirect('teamlead_dashboard')
    context = {'form': form}
    return render(request, 'teamlead_login.html', context=context)





def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard1')
    context = {'form': form}
    return render(request, 'user_login.html', context=context)


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'profile/dashboard.html')


@login_required(login_url='user_login')
def dashboard1(request):
    return render(request, 'profile/dashboard1.html')

@login_required(login_url='manager_login')
def manager_dashboard(request):
    return render(request, 'profile/manager_dashboard.html')

@login_required(login_url='staff_login')
def staff_dashboard(request):
    return render(request, 'profile/staff_dashboard.html')

@login_required(login_url='teamlead_login')
def teamlead_dashboard(request):
    return render(request, 'profile/teamlead_dashboard.html')


@login_required(login_url='login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user
            task.save()
            return redirect('view-tasks')
    context = {'form': form}
    return render(request, 'profile/create-task.html', context=context)


@login_required(login_url='manager_login')
def manager_createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user
            task.save()
            return redirect('manager_view-tasks')
    context = {'form': form}
    return render(request, 'profile/manager_create-task.html', context=context)

@login_required(login_url='staff_login')
def staff_createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user
            task.save()
            return redirect('staff_view-tasks')
    context = {'form': form}
    return render(request, 'profile/staff_create-task.html', context=context)

@login_required(login_url='teamlead_login')

def teamlead_createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user
            task.save()
            return redirect('teamlead_view-tasks')
    context = {'form': form}
    return render(request, 'profile/teamlead_create-task.html', context=context)


@login_required(login_url='login')
def viewTask(request):
    user = request.user.id

    task = Task.objects.all()

    context = {'task': task}
    return render(request, 'profile/view-tasks.html', context=context)


@login_required(login_url='manager_login')
def manager_viewTask(request):
    user = request.user.id

    task = Task.objects.all()

    context = {'task': task}
    return render(request, 'profile/manager_view-tasks.html', context=context)

@login_required(login_url='staff_login')
def staff_viewTask(request):
    user = request.user.id

    task = Task.objects.all()

    context = {'task': task}
    return render(request, 'profile/staff_view-tasks.html', context=context)

@login_required(login_url='teamlead_login')
def teamlead_viewTask(request):
    user = request.user.id

    task = Task.objects.all()

    context = {'task': task}
    return render(request, 'profile/teamlead_view-tasks.html', context=context)


@login_required(login_url='user_login')
def viewTask1(request):
    current_user = request.user.id
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'profile/view-tasks1.html', context=context)


@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
    context = {'form': form}
    return render(request, 'profile/update-task.html', context=context)


@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('view-tasks')
    return render(request, 'profile/delete-task.html')


def user_logout(request):
    auth.logout(request)
    return redirect("")
