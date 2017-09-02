from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import OrderForm
from .models import Pizza


def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})


def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = OrderForm(request.POST or None, initial={
        'pizza': pizza,
    })
    context = {
        'pizza': pizza,
        'form': form,
        'sent': request.GET.get('sent', False),
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('pizza_detail', kwargs={'pizza_id': pizza.id})))
    return render(request, 'pizza_detail.html', context)
