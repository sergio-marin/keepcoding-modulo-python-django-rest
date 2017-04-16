from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect


def login(request):
    """
    Hace login de un usuario
    :param request:  HttpRequest
    :return: HttpResponse
    """
    context = dict()
    if request.method == "POST":
        username = request.POST.get("usr")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user is not None:
            # usuario atenticado
            django_login(request, user)
            url = request.GET.get('next', 'tasks_list')
            return redirect(url)
        else:
            # usuario no atenticado
            context["error"] = "Wrong username or password."

    return render(request, 'login.html', context)