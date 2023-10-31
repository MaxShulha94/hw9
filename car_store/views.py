from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ClientForm, CarTypeForm, CarForm, DealershipForm, OrderForm

from .models import Client, CarType, Car, Dealership, Order

"""Client"""


def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_order')
    else:
        form = ClientForm()

    return render(request, "client_form.html", {"form": form})


def client_edit(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "GET":
        form = ClientForm(instance=client)
        return render(request, "client_edit.html", {"form": form})

    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        form.save()

        return redirect("client_list")
    return render(request, "client_edit.html", {"form": form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients})


"""CarType"""


def add_car_type(request):
    if request.method == "GET":
        form = CarTypeForm()
        return render(request, "car_type_form.html", {"form": form})
    form = CarTypeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("car_type_list"))

    return render(request, "car_type_form.html", {"form": form})


def car_type_list(request):
    car_type = CarType.objects.all()
    return render(request, "car_type_list.html", {"car_type": car_type})


"""Car"""


def add_car(request):
    if request.method == "GET":
        form = CarForm()
        return render(request, "car_form.html", {"form": form})
    form = CarForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("car_list"))

    return render(request, "car_form.html", {"form": form})


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        form = CarForm(instance=car)
        return render(request, "car_edit.html", {"form": form})

    form = ClientForm(request.POST, instance=car)
    if form.is_valid():
        form.save()

        return redirect("car_list")
    return render(request, "car_edit.html", {"form": form})


def car_list(request):
    car = Car.objects.all()
    return render(request, "car_list.html", {"car": car})


"""Dealership"""


def add_dealership(request):
    if request.method == "GET":
        form = DealershipForm()
        return render(request, "dealership_form.html", {"form": form})
    form = DealershipForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("dealership_list"))

    return render(request, "dealership_form.html", {"form": form})


def dealership_edit(request, pk):
    client = Dealership.objects.get(pk=pk)
    if request.method == "GET":
        form = DealershipForm(instance=client)
        return render(request, "dealership_edit.html", {"form": form})

    form = DealershipForm(request.POST, instance=client)
    if form.is_valid():
        form.save()

        return redirect("dealership_list")
    return render(request, "dealership_edit.html", {"form": form})


def dealership_list(request):
    dealership = Dealership.objects.all()
    return render(request, "dealership_list.html", {"dealership": dealership})


"""Order"""

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, "order_form.html", {"order_form": form})
def order_list(request):
    order = Order.objects.all()
    return render(request, "order_list.html", {"order": order})
