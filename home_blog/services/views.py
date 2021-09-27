from django.shortcuts import render

def service_page(request):
    return render(request, "service.html", {})
