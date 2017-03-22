from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Task


def tasks_list(request):
    """
    Recupera todas las tareas de la BD y las pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todas las tareas de la BD
    tasks = Task.objects.all()

    # crear la presentación de los datos
    html = "<ul>"
    for task in tasks:
        html += "<li>" + task.name + "</li>"
    html += "</ul>"

    # devolver la respuesta
    return HttpResponse(html)