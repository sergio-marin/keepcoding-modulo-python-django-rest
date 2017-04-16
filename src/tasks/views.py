from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Task


@login_required()
def tasks_list(request):
    """
    Recupera todas las tareas de la BD y las pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todas las tareas de la BD
    tasks = Task.objects.select_related("owner", "assignee").all()

    # se comprueba si se debe filtrar por tareas creadas por el user autenticado
    if request.GET.get('filter') == 'owned':
        tasks = tasks.filter(owner=request.user)

    # se comprueba si se debe filtrar por tareas asignadas al user autenticado
    if request.GET.get('filter') == 'assigned':
        tasks = tasks.filter(assignee=request.user)

    # devolver la respuesta
    context = {
        'task_objects': tasks
    }

    # renderizar plantilla
    return render(request, 'tasks/list.html', context)


@login_required()
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

