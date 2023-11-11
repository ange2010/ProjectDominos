import time
from django.conf import settings
from celery import shared_task
from ec.celery import app
from django.core.mail import send_mail

@app.task
def send(user_email):
    send_mail(
        'Ваш заказ принят!',
        'Оплата получена! Ваш заказ принят!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
    time.sleep(5)
    send_mail(
        'Ваш заказ готов! Ожидаем курьера',
        'Ваш заказ готов! Ожидаем курьера',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
    time.sleep(5)
    send_mail(
        'Ваш заказ в пути! ',
        'Ваш заказ в пути!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
    time.sleep(5)
    send_mail(
        'Ваш заказ доставлен!',
        'Ваш заказ доставлен!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
