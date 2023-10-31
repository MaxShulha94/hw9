import phonenumbers
from django import forms

from .models import Client, CarType, Car, Dealership, Order


class ClientForm(forms.ModelForm):
    # cars = forms.ModelMultipleChoiceField(queryset=Car.objects.all(), required=False)
    # dealerships = forms.ModelMultipleChoiceField(queryset=Dealership.objects.all(), required=False)
    # orders = forms.ModelMultipleChoiceField(queryset=Order.objects.all(), required=False)

    class Meta:
        model = Client
        fields = ["first_name", "last_name", "phone"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone:
            raise forms.ValidationError("Phone cannot be empty.")
        try:
            parsed = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException as e:
            raise forms.ValidationError(e.args[0])
        return phonenumbers.format_number(
            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) > 50:
            raise forms.ValidationError("Name is too long!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(last_name) > 50:
            raise forms.ValidationError("Surname is too long!")
        return last_name


class CarTypeForm(forms.ModelForm):
    cars = forms.ModelMultipleChoiceField(queryset=Car.objects.all(), required=False)
    dealerships = forms.ModelMultipleChoiceField(
        queryset=Dealership.objects.all(), required=False
    )

    class Meta:
        model = CarType
        fields = ["brand", "model", "price"]

    def clean_name(self):
        brand = self.cleaned_data["brand"]
        model = self.cleaned_data["model"]
        if len(model) > 20:
            raise forms.ValidationError("Model name is too long")
        if len(brand) > 20:
            raise forms.ValidationError("Brand name is too long")
        return brand, model


class CarForm(forms.ModelForm):
    dealerships = forms.ModelMultipleChoiceField(
        queryset=Dealership.objects.all(), required=False
    )

    class Meta:
        model = Car
        fields = ["car_type", "color", "year", "blocked_by_order", "owner"]

    def block(self, order):
        self.fields.blocked_by_order = order
        self.save()

    def unblock(self):
        self.fields.blocked_by_order = None
        self.save()

    def sell(self):
        if not self.fields.blocked_by_order:
            raise Exception("Car is not reserved")
        self.fields.owner = self.fields.blocked_by_order.client
        self.save()


class DealershipForm(forms.ModelForm):
    class Meta:
        model = Dealership
        fields = ["name", "available_car_types", "clients"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 50:
            raise forms.ValidationError("This name is too long")
        return name




class OrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ['client', 'dealership', 'is_paid']
