from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required
def load_user_manager_page(request):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    users = DesktopUser.objects.filter(group_id=manager.pk)
    return render(request, 'childrens_desktop/load_user_manager_page.html',
                  {'manager': manager, 'users': users, 'movies': manager.movies.all(),
                   'games': manager.games.all()})

def add_new_user_manager(request):
    if(request.method == "POST"):
        form = DesktopUserManagerForm(request.POST)
        if (form.is_valid()):
            desktop_user_manager = form.save(commit=False)
            desktop_user_manager.add_user_manager()
            return redirect('login')
    else:
        form = DesktopUserManagerForm()
    return render(request, 'childrens_desktop/add_new_user_manager.html',
                  {'form': form})


@login_required
def user_detail(request, pk):
    user = get_object_or_404(DesktopUser, pk=pk)
    return render(request, 'childrens_desktop/user_detail.html', {'user': user})


@login_required
def add_new_user(request):
    manager = DesktopUserManager.objects.get(username=request.user.username)
    if (request.method == "POST"):
        form = DesktopUserForm(request.POST)
        if (form.is_valid()):
            desktop_user = form.save(commit=False)
            desktop_user.add_user(manager.pk)
            return redirect('load_user_manager_page')
    else:
        form = DesktopUserForm()
    return render(request, 'childrens_desktop/user_edit.html',
                  {'form': form, 'form_headline': "Add new user"})
