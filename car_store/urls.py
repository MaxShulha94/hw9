from django.urls import path
from .views import (
    add_client,
    client_list,
    client_edit,
    add_car_type,
    car_type_list,
    add_car,
    car_list,
    car_edit,
    add_dealership,
    dealership_list,
    dealership_edit,
    add_order,
    order_list,
)

urlpatterns = [
    path("client/", add_client, name="add_client"),
    path("clients/", client_list, name="client_list"),
    path("client_edit/<int:pk>", client_edit, name="client_edit"),
    path("car_type/", add_car_type, name="add_car_type"),
    path("cars_type/", car_type_list, name="car_type_list"),
    path("car/", add_car, name="add_car"),
    path("cars/", car_list, name="car_list"),
    path("car_edit/<int:pk>", car_edit, name="car_edit"),
    path("dealership/", add_dealership, name="add_dealership"),
    path("dealerships", dealership_list, name="dealership_list"),
    path("dealership_edit/<int:pk>", dealership_edit, name="dealership_edit"),
    path("order/", add_order, name="add_order"),
    path("orders/", order_list, name="order_list"),
]
