from django.http import HttpResponse
import paypalrestsdk
from paypalrestsdk import CreditCard


def payment(request):
    paypalrestsdk.configure({
        "mode": "sandbox",  # Cambia a "live" para producción
        "client_id": "AfV5JwBkFx9Iufq0yPUxXj8voQc_fuGIHbq10x8tdf-nXoAT8iK-JpfO1zHP5KbHSWsHdbBGr7jSNfy5",
        "client_secret": "EAP7uvUzWCUbjvBathbD3Ov0E3WW6QGCm45Ze5WvktKmzT7C_TSs6JAi1ossKTQOCNiOK_zs5q29_EyT"
    })