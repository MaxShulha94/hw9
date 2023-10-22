from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CarType(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model}"


class Car(models.Model):
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, related_name="cars")
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    blocked_by_order = models.ForeignKey(
        "Order", on_delete=models.SET_NULL, null=True, related_name="reserved_cars"
    )
    owner = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, related_name="cars"
    )


class Licence(models.Model):
    car = models.OneToOneField(
        Car, on_delete=models.SET_NULL, null=True, related_name="licence"
    )
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number


class Dealership(models.Model):
    name = models.CharField(max_length=50)
    available_car_types = models.ManyToManyField(CarType, related_name="dealerships")
    clients = models.ManyToManyField(Client, related_name="dealerships")

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    dealership = models.ForeignKey(
        Dealership, on_delete=models.CASCADE, related_name="orders"
    )
    is_paid = models.BooleanField(default=False)


class OrderQuantity(models.Model):
    car_type = models.ForeignKey(
        CarType, on_delete=models.CASCADE, related_name="order_quantities"
    )
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="car_types")
