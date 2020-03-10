from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('movies_list')
        else:
            messages.info(request, 'Неверно введен логин или пароль!')

    context = {}
    return render(request, "accounts/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('movies_list')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {user} успешно зарегистрирован!')

            return redirect('login_page')
            
    context = {'register_form': form}
    return render(request, "accounts/register.html", context)