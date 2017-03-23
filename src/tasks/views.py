from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

from tasks.models import Task


def tasks_list(request):
    """
    Recupera todas las tareas de la BD y las pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todas las tareas de la BD
    tasks = Task.objects.select_related("owner", "assignee").all()

    # devolver la respuesta
    context = {
        'task_objects': tasks
    }

    # renderizar plantilla
    return render(request, 'tasks/list.html', context)


def tasks_detail(request, task_pk):
    """
    Recuperamos una tarea de BD y la pintamos con una plantilla
    :param request: HttpRequest
    :param task_pk: Primary key de la tarea a recuperar
    :return: HttpResponse
    """
    # recuperar la tarea
    try:
        task = Task.objects.select_related().get(pk=task_pk)
    except Task.DoesNotExist:
        return render(request, '404.html', {}, status=404)
    except Task.MultipleObjectsReturned:
        return HttpResponse("Existen varias tareas con ese identificador", status=300)

    # preparar el contexto
    context = {
            'task': task
        }

    # renderizar plantilla
    return render(request, 'tasks/detail.html', context)
