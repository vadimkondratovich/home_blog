from django.shortcuts import render

def blog_grid(request):
    return render(request, "blog_grid.html", {})
