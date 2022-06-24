from django.http import HttpResponse
from django.shortcuts import render
from constructor.models import Site, House, Company
import psycopg2
from psycopg2 import Error


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
        elif r1 == "t3":
            site.template = 'template_uc3'
        site.save()
    return render(request, "take_color.html", context={'site': site})


def take_images(request):
    site_id = request.POST.get('site_id')
    site = Site.objects.get(id=site_id)
    if request.method == 'POST':
        r2 = request.POST.get('r2')
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
    site_id = request.POST.get('site_id')
    site = Site.objects.get(id=site_id)
    if request.method == 'POST':
        site.logo = request.FILES.get("fileLogo")
        site.banner = request.FILES.get("fileBanner")
        site.save()
    return render(request, "take_info.html",
                  context={'site': site})


def template_uc1(request):
    return render(request, "template_uc1.html")


def template_uc2(request):
    return render(request, "template_uc2.html")


def template_uc3(request):
    return render(request, "template_uc3.html")


def template_uc(request):
    site_id = request.GET.get('site_id')
    site = Site.objects.get(id=site_id)

    print(request.GET)
    return render(request, f'{site.template}.html',
                  context={'site': site})


def final_page(request):
    site_id = request.POST.get('site_id')
    site = Site.objects.get(id=site_id)
    company_id = request.POST.get('input1')
    company = Company.objects.get(inn=company_id)
    site.company = company
    site.save()
    try:
        connection = psycopg2.connect(user="sergey",
                                      password="qwerty123",
                                      host="localhost",
                                      port="5432",
                                      database="uc_site_constructor")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from constructor_house"
        cursor.execute(postgreSQL_select_Query)
        houses = cursor.fetchall()
        with open("list_houses.txt", 'w') as file:
            for row in houses:
                file.write("ID - " + str(row[0]) + "\t" + "Address - " + row[1])
                file.write("\n")
            site.list_houses = file
            site.save()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    return render(request, "final_page.html",
                  context={'site': site})


def show_houses(request):
    filename = "list_houses.txt"
    content = ""
    with open("list_houses.txt", 'r') as file:
        for line in file:
            content += line
            content += "\n"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response
