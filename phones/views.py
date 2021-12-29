from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    phones = Phone.objects.all()

    sort_filter = request.GET.get('sort')
    if sort_filter:
        phones = phones.order_by(sort_filter)

    context['phones'] = phones
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phones = Phone.objects.filter(slug=slug)
    context['phones'] = phones
    return render(request, template, context=context)




