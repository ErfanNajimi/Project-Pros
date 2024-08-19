from django.shortcuts import render, redirect
from django.views import View
from .models import project_detail
from .forms import EmojiSelection, project_detailForm

# Create your views here.

class ProjectView(View):
    def get(self, request):
        approved_projects = project_detail.objects.filter(approved=True)

        return render(
            request, 
            "project/project.html",
            {'projects':approved_projects}
        )

class HomeView(View):
    def get(self, request):

        return render(
            request, 
            "project/index.html",
        )


def dashboard_content(request):

    queryset = project_detail.objects.all().filter(account = request.user)
    projects = queryset.order_by("-favourite")

    projects_count = queryset.count()
    awaiting_approval = queryset.filter(approved=False).count()

    search = request.GET.get("project-search")
    search_results = project_detail.objects.filter(title__icontains=search).values() if search != None else ''

    if request == 'POST':
        emoji_form = EmojiSelection(data=request.POST)
        if emoji_form.is_valid():
            emoji = emoji_form.save(commit=False)
            emoji.account = request.user
            emoji.save()
    
    emoji_form = EmojiSelection()

    return render(
        request,
        'project/dashboard.html',
        {
            'projects' : projects,
            'search_results' : search_results,
            'emoji_form' : emoji_form,
            'projects_count': projects_count,
            'awaiting_approval': awaiting_approval,
        },
    )


def project_create_view(request):
    if request.method == 'POST':
        form = project_detailForm(request.POST)
        if form.is_valid():
            return redirect('dashboard') 
    else:
        form = project_detailForm()
    return render (request, 'add.html', {'form':form})
