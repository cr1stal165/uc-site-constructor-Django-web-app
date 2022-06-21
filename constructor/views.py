from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

from constructor.models import Site
import main


def index(request):
    return render(request, "constructor.html")


def take_color(request):
    site_id = request.GET.get('site_id')
    site = Site.objects.filter(id=site_id).first()
    if not site:
        site = Site.objects.create(colors="", template="", domain="", bg_colors="", logo=None, banner=None)

    print(request.user)
    if request.method == 'POST':
        r1 = request.POST.get('r1')
        if r1 == "t1":
            site.template = 'template_uc1'
        elif r1 == "t2":
            site.template = 'template_uc2'
        else:
            site.template = 'template_uc3'
        site.save()
    return render(request, "take_color.html", context={'site': site})


def take_images(request):
    site = None
    if request.method == 'POST':
        r2 = request.POST.get('r2')
        site_id = request.POST.get('site_id')
        site = Site.objects.get(id=site_id)
        if r2 == "color1":
            site.colors = "3B2A1D"
            site.bg_colors = "F1F1F1"
        elif r2 == "color2":
            site.colors = "A61212"
            site.bg_colors = "FFFFFF"
        elif r2 == "color3":
            site.colors = "77CC44"
            site.bg_colors = "FEFAEF"
        else:
            site.colors = "5B7FED"
            site.bg_colors = "FFFFFF"
        site.save()
    return render(request, "take_images.html",
                  context={'site': site})


def take_info(request):
    site = None
    if request.method == 'POST':
        site_id = request.POST.get('site_id')
        site = Site.objects.get(id=site_id)
        site.logo = request.FILES.get("fileLogo")
        site.save()
    return render(request, "take_info.html",
                  context={'site': site})


def template_uc1(request):
    request.GET.get('param')
    return render(request, "template_uc1.html")


def template_uc2(request):
    return render(request, "template_uc2.html")


def template_uc(request):
    site_id = request.GET.get('site_id')
    site = Site.objects.get(id=site_id)
    print(request.GET)
    return render(request, f'{site.template}.html',
                  context={'site': site})


def final_page(request):
    site = None
    inn = ""
    domain = ""
    list = main.Main()
    info = list.get_company("id_123", "id_123")
    if request.method == 'POST':
        site_id = request.POST.get('site_id')
        site = Site.objects.get(id=site_id)
        inn = request.POST.get('input1')
        domain = request.POST.get('input2')
    print(info)
    return render(request, "final_page.html",
                  context={'site': site})




