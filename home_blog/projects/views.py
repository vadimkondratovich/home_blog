from django.shortcuts import render

def project_page(request):
    return render(request, "project.html", {})
