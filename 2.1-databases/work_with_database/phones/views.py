
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    content = Phone.objects.all()
    if request.GET.get("sort") == "name":
        content = Phone.objects.order_by("name")
    elif request.GET.get("sort") == "min_price":
        content = Phone.objects.order_by("price")
    elif request.GET.get("sort") == "max_price":
        content = Phone.objects.order_by("-price")
    context = {'phones': content}
    return render(request, template, context)


# record = Phone.objects.all().filter("slug")
def show_product(request, slug):

    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
