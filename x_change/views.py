from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from google_currency import convert
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json


class CurrencyConverter(APIView):
    def post(self, request):
        received_json_data = json.loads(request.body.decode("utf-8"))
        try:
            currency1 = received_json_data['currency1']
            currency2 = received_json_data['currency2']
        except Exception:
            return Response({"status": "error", "data": "rate checking failed, check the currencies and try again"},
                            status=status.HTTP_400_BAD_REQUEST)

        if currency1 and currency2:
            result = convert(currency1, currency2, 1)
            result = json.loads(result)
            converted = result['converted']
            if converted:
                return Response({"rate": float(result['amount'])}, status=status.HTTP_200_OK)
            else:
                return Response({"data": "rate checking failed, check the currencies,your network and try again"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"data": "invalid currency"}, status=status.HTTP_400_BAD_REQUEST)
