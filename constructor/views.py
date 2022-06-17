from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse





def index(request):
    return render(request, "constructor.html")


def take_color(request):
    print(request)
    temp = ""
    if request.method == 'POST':
        r1 = request.POST.get('r1')
        if r1 == "t1":
            temp = 'template_uc1'
        elif r1 == "t2":
            temp = 'template_uc2'
        else:
            temp = 'template_uc3'
    return render(request, "take_color.html", context={'curr': temp})


def take_images(request):
    list_colors = ["#F1F1F1", "#3B2A1D",
                   "#A61212", "#FFFFFF",
                   "#77CC44", "#FEFAEF",
                   "#5B7FED", "#FFFFFF"]
    color = ""
    bg_color = ""
    template_name = ""
    if request.method == 'POST':
        img = request.FILES.get("file")
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
    temp_name = ""
    if request.method == 'POST':
        temp_name = request.POST.get('r1')
    return render(request, "take_info.html", context={'curr': temp_name})


def template_uc1(request):
    request.GET.get('param')
    return render(request, "template_uc1.html")


def template_uc2(request):
    return render(request, "template_uc2.html")


def template_uc(request):
    template_name = request.GET.get('param')
    template_color = request.GET.get('param_color')
    template_bg_color = request.GET.get('param_bg_color')
    print(request.GET)
    return render(request, f'{template_name}.html', context={'color': template_color, 'bg_color': template_bg_color})


def final_page(request):
    return render(request, "final_page.html")
