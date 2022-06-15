from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    return render(request, "constructor.html")


def take_color(request):
    print(request)
    r1 = 0
    if request.method == 'POST':
        r1 = request.POST.get('r1')
        print(r1)
        print(request.POST)
    return render(request, "take_color.html", context={'r': r1})


def take_images(request):
    if request.method == 'POST':
        img = request.FILES.get("file")
    return render(request, "take_images.html")


def take_info(request):
    return render(request, "take_info.html")


def template_uc1(request):
    return render(request, "template_uc1.html")


def final_page(request):
    return render(request, "final_page.html")
