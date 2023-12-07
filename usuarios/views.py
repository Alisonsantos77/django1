from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def validate_password(password):
    min_length = 8
    if len(password) < min_length:
        raise ValidationError(
            _(
                'Senha muito curta. Deve ter no mínimo %(min_length)d caracteres.'
            ),
            code='password_too_short',
            params={'min_length': min_length},
        )


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError:
        return HttpResponse('Email inválido').first()
    if user:
        return HttpResponse ('Email já em uso')
    validate_password(senha)

    user = User.objects.filter(username=username).first()
    if user:
        return HttpResponse('Já existe')
    user = User.objects.create_user(
        username=username, email=email, password=senha
    )
    user.save()
    return redirect('login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user: 
            return HttpResponse('Nome de usuário já em uso')
    senha = request.POST.get('senha')

    user = authenticate(username=username, password=senha)

    if user:
        login_django(request, user)
        return redirect('lista')
    else:
        return HttpResponse('senha ou email invalidos')


@login_required(login_url='/auth/login/')
def plataforma(request):
    return redirect('lista')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
