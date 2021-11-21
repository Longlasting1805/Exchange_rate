from django.urls import path

from x_change.views import CurrencyConverter

urlpatterns = [
    path('exchange-rate/', CurrencyConverter.as_view())
]
