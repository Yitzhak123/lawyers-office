from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import *
from .forms import *


@login_required
def load_user_page(request):
    lawyer = Lawyer.objects.get(username=request.user.username)
    records = lawyer.records.all()
    links = init_links('new_case')
    return render(request, 'lawyers_office/new_case.html',
                  {'lawyer': lawyer, 'records': records, 'links': links})


def add_new_user(request):
    if request.method == "POST":
        form = LawyerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.add_new_lawyer()
            return redirect('login')
    else:
        form = LawyerForm()
    return render(request, 'lawyers_office/add_new_user.html',
                  {'form': form})


@login_required
def get_left_top_nav_links(request, link_url):
    links = init_links(link_url)
    return render(request, 'lawyers_office/'+link_url+'.html', {'links': links})


# initialize active attribute in all links to False, except from the link with url='active_url'
def init_links(active_url=None, links=None):
    if links is None:
        links = Link.objects.all()
    links.update(active=False)
    active_links = Link.objects.filter(url=active_url)
    active_links.update(active=True)
    return links


@login_required
def load_settings_page(request):
    return render(request, 'lawyers_office/settings.html')


@login_required
def load_info_page(request):
    return render(request, 'lawyers_office/info.html')


@login_required
def upload_file(request):
    return render(request, 'lawyers_office/info.html')


@login_required
def open_file(request):
    return render(request, 'lawyers_office/info.html')


@login_required
def reclassify(request):
    return render(request, 'lawyers_office/info.html')


@login_required
def save_file(request):
    return render(request, 'lawyers_office/info.html')


@login_required
def delete_file(request):
    return render(request, 'lawyers_office/info.html')


@login_required
def more_options(request):
    return render(request, 'lawyers_office/info.html')


# def load_sub_menu_page_after_click_on_icon(request, icon_name):
#     return render(request, 'lawyers_office/')
