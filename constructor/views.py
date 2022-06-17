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
    return render(request, "take_color.html", context={'curr': site.template})


def take_images(request):
    color = ""
    bg_color = ""
    template_name = ""
    if request.method == 'POST':
        template_name = request.POST.get('r1')
        r2 = request.POST.get('r2')
        if r2 == "color1":
            color = "3B2A1D"
            bg_color = "F1F1F1"
        elif r2 == "color2":
            color = "A61212"
            bg_color = "FFFFFF"
        elif r2 == "color3":
            color = "77CC44"
            bg_color = "FEFAEF"
        else:
            color = "5B7FED"
            bg_color = "FFFFFF"
    print(color)
    return render(request, "take_images.html", context={'color': color, 'curr': template_name, 'background_color': bg_color})


def take_info(request):
    img = None
    color = ""
    template_name = ""
    if request.method == 'POST':
        template_name = request.POST.get('r1')
        img = request.FILES.get("fileLogo")
    return render(request, "take_info.html", context={'image': img, 'color': color, 'curr': template_name})


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
    return render(request, f'{template_name}.html', context={'color': template_color, 'bg_color': template_bg_color, 'image': template_image})


def final_page(request):
    return render(request, "final_page.html")
