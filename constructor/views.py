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
    return render(request, "take_color.html", context={'curr': temp})


def take_images(request):
    list_colors = ["#F1F1F1", "#3B2A1D",
                   "#A61212", "#FFFFFF",
                   "#77CC44", "#FEFAEF",
                   "#5B7FED", "#FFFFFF"]

    if request.method == 'POST':
        img = request.FILES.get("file")
        color = request.POST.get('r2')
        if color == 'color1':
            render(request, "template_uc2.html", context={'second_color': list_colors[1]})
    return render(request, "take_images.html")


def take_info(request):
    return render(request, "take_info.html")


def template_uc1(request):
    request.GET.get('param')
    return render(request, "template_uc1.html")


def template_uc2(request):
    return render(request, "template_uc2.html")


def template_uc(request):
    template_name = request.GET.get('param')
    print(template_name)
    return render(request, f'{template_name}.html')


def final_page(request):
    return render(request, "final_page.html")
