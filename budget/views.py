from django.shortcuts import render

def Project_list(request):
    return render(request, 'budget/project-list.html')

def Project_detail(request, project_slug):
    # fetch the correct project
    return render(request, 'budget/project-detail.html')

    
