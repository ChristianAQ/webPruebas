from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from users.forms import LoginForm, SignupForm
from django.views import View


class LoginView(View):
    def get(self, request):
        """
        Presenta el formulario del login
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {'error': error_message, 'login_form': login_form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrecta"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'photos_home'))
                else:
                    error_message = "Cuenta de usuario inactiva"
        context = {'error': error_message, 'login_form': login_form}
        return render(request, 'users/login.html', context)


class SignupView(View):
    def get(self, request):
        """
        Presenta el formulario del signup
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        signup_form = SignupForm()
        context = {'error': error_message, 'signup_form': signup_form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        """
        Gestiona el signup_form de un usuario
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('pwd')
            password2 = request.POST.get('pwd2')
            user = authenticate(username=username, password=password, password2=password2)
            if user is None:
                error_message = "Usuario o contraseña incorrecta"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'photos_home'))
                else:
                    error_message = "Cuenta de usuario inactiva"
        context = {'error': error_message, 'signup_form': signup_form}
        return render(request, 'users/signup_form', context)


class LogoutView(View):
    def get(self, request):
        """
        Hace el logout de un usuario y redirige al login
        :param request: objeto HtttpRequest con los datos de la peticion
        :return: objeto HttpResponse con los datos de la respuesta
        """
        if request.user.is_authenticated:
            django_logout(request)
        return redirect('photos_home')




