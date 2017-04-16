from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login a un usuario
        :param request:  HttpRequest
        :return: HttpResponse
        """
        return render(request, 'login.html')

    def post(self, request):
        """
        Hace login de un usuario
        :param request:  HttpRequest
        :return: HttpResponse
        """
        context = dict()
        username = request.POST.get("usr")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user is not None:
            # usuario autenticado
            django_login(request, user)
            url = request.GET.get('next', 'tasks_list')
            return redirect(url)
        else:
            # usuario no autenticado
            context["error"] = "Wrong username or password."

        return render(request, 'login.html', context)


def logout(request):
    """
    Hace logout de un usuario
    :param request:  HttpRequest
    :return: HttpResponse
    """
    django_logout(request)
    return redirect('login')