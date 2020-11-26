from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('url_home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_user(allowed_group=[]):
    def decorator_func(view_func):
        def wrapper_func(request, *args, **kwargs):
            group_name = None
            if request.user.groups.exists():
                group_name = request.user.groups.all()[0].name

            if group_name in allowed_group:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed')

        return wrapper_func

    return decorator_func


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group_name = None
        if request.user.groups.exists():
            group_name = request.user.groups.all()[0].name

        if group_name == 'customer':
            return redirect('url_user_page')
        if group_name == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
