from django.http import request
from django.http.response import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Url_blacklist, Url_crawler_list, Url_crawler_other, Url_home, Url_others, Url_freejobalert, Url_pdf, Url_sarkariresult
import requests
from bs4 import BeautifulSoup
import datetime


def url_save(url_list):
    for x in url_list:
        # print(x)
        url_valid = x.startswith("https://")
        if url_valid:
            qspdf = x.endswith('.pdf') or x.endswith('.PDF')
            if qspdf:
                url = Url_pdf.objects.filter(url=x)
                if url.exists() == False:
                    obj = Url_pdf(url=x)
                    obj.save()
            else:
                url_free = x.startswith("https://www.freejobalert.com")
                url_sarkari = x.startswith("https://www.sarkariresult.com")
                if url_free:
                    url = Url_freejobalert.objects.filter(url=x)
                    if url.exists() == False:
                        obj = Url_freejobalert(url=x)
                        obj.save()
                elif url_sarkari:
                    url = Url_sarkariresult.objects.filter(url=x)
                    if url.exists() == False:
                        obj = Url_sarkariresult(url=x)
                        obj.save()
                else:
                    bl = Url_blacklist.objects.all()
                    flag = False
                    for b in bl:
                        if b.url_blacklist in x:
                            flag = True
                    url = Url_others.objects.filter(url=x)
                    print(x)
                    if (url.exists() == False) and (flag == False):
                        obj = Url_others(url=x)
                        obj.save()
    return None


def single_url_crawler(url):
    url_all = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    for link in soup.find_all('a'):
        ul = link.get('href')
        url_all.append(ul)
    url_removed_last_char = []
    for x in url_all:
        if x:
            last_char = x[-1]
            if last_char == '/':
                ls = x.lstrip(x[-1])
                url_removed_last_char.append(ls)
            else:
                url_removed_last_char.append(x)
    url_unique_list = []
    for x in url_removed_last_char:
        if x not in url_unique_list:
            y = x.lstrip()
            if ((y.startswith("https://")) or (y.startswith("http://"))):
                url_unique_list.append(y)
    return url_unique_list


def home(request):
    if request.method == "POST":
        global url_1
        url_1 = request.POST['url']
        global url_list
        if url_1 is not None:
            if ((("https://" in url_1) == False) and (("http://" in url_1) == False)):
                url_1 = "http://"+url_1
            url_list = single_url_crawler(url_1)
            return JsonResponse({'status': 'ok', 'url_list': url_list})
    return render(request, 'index.html')


def dell(request):
    if request.method == "POST":
        del_url = request.POST['btn-del-id']
        url_list.remove(del_url)
        return JsonResponse({'status': 'ok', 'url_list': url_list})


def url_save_crawler_list(url_list):
    for x in url_list:
        # print(x)
        url_valid = (x.startswith("https://") or x.startswith("http://"))
        if url_valid:
            qspdf = x.endswith('.pdf') or x.endswith('.PDF')
            if qspdf:
                url = Url_pdf.objects.filter(url=x)
                if url.exists() == False:
                    obj = Url_pdf(url=x)
                    obj.save()
            else:
                url_free = x.startswith("https://www.freejobalert.com")
                url_sarkari = x.startswith("https://www.sarkariresult.com")
                if url_free:
                    url = Url_freejobalert.objects.filter(url=x)
                    if url.exists() == False:
                        obj = Url_freejobalert(url=x)
                        obj.save()
                elif url_sarkari:
                    url = Url_sarkariresult.objects.filter(url=x)
                    if url.exists() == False:
                        obj = Url_sarkariresult(url=x)
                        obj.save()
                else:
                    bl = Url_blacklist.objects.all()
                    flag = False
                    for b in bl:
                        if b.url_blacklist in x:
                            flag = True
                    url = Url_crawler_other.objects.filter(url=x)
                    print(x)
                    if (url.exists() == False) and (flag == False):
                        obj = Url_crawler_other(url=x)
                        obj.save()
    return None


def save_home(request):
    print('save button clicked')
    if request.method == 'POST':
        x = url_1
        url = Url_crawler_list.objects.filter(url=x)
        if url.exists() == False:
            obj = Url_crawler_list(url=x)
            obj.save()
        url_save_crawler_list(url_list)
        # url_save(url_list)
        return JsonResponse({'status': 'save'})


def hm(request):
    obj = Url_crawler_list.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'home.html', context)


def org_name(request):
    if request.method == "POST":
        url_5 = request.POST['url']
        if "www.freejobalert.com" in url_5:
            print("freejob alert data")
            url_list_2 = Url_freejobalert.objects.all().order_by('updated')
            for x5 in url_list_2:
                x = (str(x5)).lstrip()
                obj = Url_freejobalert.objects.get(url=x)
                obj.url = x
                print(obj.pk, " URL: ", obj.url)
                obj.updted = datetime.datetime.now()
                obj.save()
                urlx = single_url_crawler(x)
                url_save(urlx)
        elif "www.sarkariresult.com" in url_5:
            print("sarkari result data")
            url_list_3 = Url_sarkariresult.objects.all().order_by('updated')
            for x5 in url_list_3:
                x2 = (str(x5)).lstrip()
                obj = Url_sarkariresult.objects.get(url=x2)

                obj.url = x2
                print(obj.pk, " URL: ", obj.url)
                obj.updted = datetime.datetime.now()
                obj.save()
                urlx = single_url_crawler(x2)
                url_save(urlx)
        else:
            print("other data")
            url_list_4 = Url_crawler_other.objects.all().order_by('updated')
            for x4 in url_list_4:
                x2 = (str(x4)).lstrip()
                # print(x2)
                obj_4 = Url_crawler_other.objects.get(url=x2)
                # print(obj_4)
                obj_4.url = x2
                print(obj_4.pk, " URL: ", obj_4.url)
                obj_4.updted = datetime.datetime.now()
                obj_4.save()
                urlx = single_url_crawler(x2)
                url_save(urlx)
    return JsonResponse({'status': 'ok'})


def url_short(request):
    if request.method == 'POST':
        url_home(request)
        obj = Url_home.objects.all()
        # print("url short call")
        # print(obj)
        data = serializers.serialize('json', obj)
        # print(data)
        return JsonResponse({"status": "ok", "dt": data})


def home_(request):
    context = {}
    if request.method == "POST":
        url = request.POST.get('inputurl')
        url_table = request.POST.get('tablelist')
        url_home_click = request.POST.get('home_url')
        if url and 'www.' in url:
            url_list = single_url_crawler(url)
            url_save(url_list)
        if url_table and url_table == 'freejobalerts.com':
            url_list = Url_freejobalert.objects.all().order_by('updated')
            for x5 in url_list:
                x = (str(x5)).lstrip()
                obj = Url_freejobalert.objects.get(url=x)
                obj.url = x
                print(obj.pk, " URL: ", obj.url)
                # print(obj.url)
                # print(obj.timestamp)
                # print(obj.updated)
                obj.updted = datetime.datetime.now()
                obj.save()
                urlx = single_url_crawler(x)
                url_save(urlx)
        if url_table and url_table == 'sarkariresult.com':
            url_list = Url_sarkariresult.objects.all().order_by('updated')
            for x5 in url_list:
                x2 = (str(x5)).lstrip()
                obj = Url_sarkariresult.objects.filter(url=x2)
                obj.url = x2
                print(obj.pk, " URL: ", obj.url)
                # print(obj.url)
                # print(obj.timestamp)
                # print(obj.updated)
                obj.updted = datetime.datetime.now()
                obj.save()

                urlx = single_url_crawler(x2)
                url_save(urlx)

        if url_home_click:
            context = {
                "object": Url_home.objects.all()
            }
            url_home(request)

    return render(request, 'index.html', context)


def update(request):
    # print(request)
    if request.method == "POST":
        url = request.POST['id']
        obj = Url_home.objects.get(url=url)
        obj.name = request.POST['org_name']
        obj.save()
        # url_list = Url_home.objects.values()
        # url_data = list(url_list)
        print("org name saved")
        return JsonResponse({'status': 'save'})


def delete(request):
    if request.method == "POST":
        id = request.POST['id']
        obj = Url_home.objects.filter(pk=id)
        obj1 = Url_blacklist.objects.filter(url_blacklist=obj)
        if obj1.exists() == False:
            objbl = Url_blacklist(url_blacklist=obj)
            objbl.save()
        obj.delete()

    return render(request, 'index.html')


def url_home(request):
    url = Url_others.objects.all()
    for x2 in url:
        x = str(x2)
        i = x.find("https://")
        q = x[8:]
        h1 = q.find('/')
        s = 8 + h1
        home_url1 = None
        if h1:
            home_url1 = x[:s]
        else:
            home_url1 = x
        h5 = Url_home.objects.filter(url=home_url1)
        if ((h5.exists() == False) and ((home_url1.startswith('https://')) or ((home_url1.startswith('http://'))))):
            obj = Url_home(url=home_url1)
            # obj.save()
            bl = Url_blacklist.objects.all()
            flag = False
            for b in bl:
                if b.url_blacklist in home_url1:
                    flag = True
            # url = Url_others.objects.filter(url=x)

            if (url.exists() == False) and (flag == False):
                # obj = Url_others(url=x)
                obj.save()
                return "saved"


def vd(request):
    if request.method == 'POST':
        url = "https://www.youtube.com/watch?v=6yTYP39d9Gs"
        url_all = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        for link in soup.find_all('a'):
            ul = link.get('href')
            url_all.append(ul)
            print(ul)
    return render(request, 'vd.html')