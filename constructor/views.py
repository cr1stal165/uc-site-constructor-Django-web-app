from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

from constructor.models import Site


def index(request):

    return render(request, "constructor.html")


def take_color(request):
    site = Site.objects.create(colors="", template="", domain="", bg_colors="", logo=None, banner=None)
    print(request)
    if request.method == 'POST':
        r1 = request.POST.get('r1')
        if r1 == "t1":
            site.template = 'template_uc1'
        elif r1 == "t2":
            site.template = 'template_uc2'
        else:
            site.template = 'template_uc3'
        site.save()
    return render(request, "take_color.html", context={'curr': site.template, 'site': site})


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
                  context={'color': site.colors, 'curr': site.template, 'background_color': site.bg_colors, 'site': site})


def take_info(request):
    site = None
    if request.method == 'POST':
        site_id = request.POST.get('site_id')
        site = Site.objects.get(id=site_id)
        site.logo = request.FILES.get("fileLogo")
        site.save()
    return render(request, "take_info.html", context={'image': site.logo, 'color': site.colors, 'curr': site.template, 'site': site})


def template_uc1(request):
    request.GET.get('param')
    return render(request, "template_uc1.html")


def template_uc2(request):
    return render(request, "template_uc2.html")


def template_uc(request):
    template_name = request.GET.get('param')
    template_color = request.GET.get('param_color')
    template_image = request.GET.get('param_image')
    template_bg_color = request.GET.get('param_bg_color')
    print(request.GET)
    return render(request, f'{template_name}.html',
                  context={'color': template_color, 'bg_color': template_bg_color, 'image': template_image})


def final_page(request):
    return render(request, "final_page.html")


