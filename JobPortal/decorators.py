from django.http import HttpResponse
from django.shortcuts import redirect
from .models import UserWithRole
from django.contrib.auth.decorators import login_required


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_users(request_role):
    def outer_func(view_func):
        @login_required
        def wrapper_func(request, *args, **kwargs):
            role=UserWithRole.objects.get(username=request.user.username).role
            if role == request_role:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return outer_func

admin_required = allowed_users('admin')
hr_required = allowed_users('hr')
candidate_required = allowed_users('candidate')