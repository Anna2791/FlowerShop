from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from flower_shop.models import Flower, Order
from flower_shop.telegram_bot import send_order_to_telegram

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def catalog(request):
    flowers = Flower.objects.all()
    return render(request, 'catalog.html', {'flowers': flowers})



def order(request, flower_id):
    if request.method == 'POST':
        flower = Flower.objects.get(id=flower_id)
        order = Order.objects.create(
            user=request.user,
            flower=flower,
            delivery_address=request.POST['address'],
            delivery_time=request.POST['time'],
            comment=request.POST.get('comment', '')
        )
        send_order_to_telegram(order)
        return redirect('profile')
    flower = Flower.objects.get(id=flower_id)
    return render(request, 'order.html', {'flower': flower})

def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})
