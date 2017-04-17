from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede usar o no el endpoint de quiere usar
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :return: True si puede, False si no puede
        """

        # cualquiera autenticado puede acceder al detalle para ver, actualizar o borrar
        if request.user.is_authenticated() and view.action in ("retrieve", "update", "destroy"):
            return True

        # si es superusuario y quiere acceder al listado
        if request.user.is_superuser and view.action == "list":
            return True

        # cualquiera puede crear un usuario (POST)
        if view.action == "create":
            return True

        # si está autenticado y quiere hacer algo sobre el detalle o es superusuario y quiere hacer algo sobre el listado
        if request.user.is_authenticated() and (request.user.is_superuser or isinstance(view, UserDetailAPI)):
            return True

        return False


    def has_object_permission_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la acción sobre el objeto que quiere realizarla
        :param request: HttpRequest
        :param view: UsersAPI/UserDetailAPI
        :param obj: User
        :return: True si puede, False si no puede
        """
        # si es admin o es él mismo le dejamos
        return request.user.is_superuser or request.user == obj