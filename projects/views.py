from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def project(request):
    projects = Project.objects.all().order_by('-id')
    context = {'projects': projects,
               'project': 'active'}
    return render(request, 'projects/projects.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('project')  # Redirect to the project page after successful submission
    else:
        form = ProjectForm()
    return render(request, 'projects/add_projects.html', {'form': form})
