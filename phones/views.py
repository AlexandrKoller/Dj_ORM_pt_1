from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


# def phone_sort(request):
#     sort = request.GET.get('sort', 'name')
#     if sort == 'name':
#         sort_item = Phone.objects.all().order_by('name')
#     elif sort == 'min_price':
#         sort_item = Pho ne.objects.all().order_by('-price')
#     elif sort == 'max_price':
#         sort_item = Phone.objects.all().order_by('price')
#     return  render(request, 'catalog.html', {'sort_item':sort_item,'sort':sort})
def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    print(phone)
    context = {'phone': phone[0]}
    return render(request, template, context)
