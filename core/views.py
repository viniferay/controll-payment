from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render

from core.forms import RegisterForm

def home(request):
    return render(request, 'index.html')

def register(request):
    form = RegisterForm(request.POST or None)
    args = {'form': form}

    if form.is_valid():
        user = form.save()
        user.password = make_password(form.cleaned_data.get('password'))
        user.save()
        args['return'] = 'Usuários cadastrado com sucesso'
        return render(request, 'register.html', args)

    return render(request, 'register.html', args)
