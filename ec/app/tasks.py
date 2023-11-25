from ec.celery import app
from django.core.mail import send_mail
from django.db.models import Q
import time
from .models import OrderPlaced
import schedule
from django.utils import timezone
from celery import shared_task


@app.task
def send(user_email):
    send_mail(
        'Ваш заказ принят!',
        'Оплата получена! Ваш заказ принят!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
    time.sleep(20)
    send_mail(
        'Ваш заказ готов! Ожидаем курьера! Ссылка на трекер: http://127.0.0.1:8000/orders/',
        'Ваш заказ готов! Ожидаем курьера',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
    time.sleep(20)
    send_mail(
        'Ваш заказ в пути! ',
        'Ваш заказ в пути!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )
    time.sleep(20)
    send_mail(
        'Ваш заказ доставлен!',
        'Ваш заказ доставлен!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
    )

@app.task
def send2(user_email):
    time.sleep(200)
    send_mail(
        'Ваш промокод!',
        'Вы сделали первый заказ! Ваш промокод!',
        'angelatim11111@gmail.com',
        [user_email],
        fail_silently=False,
        )

@app.task
def set_status(pk):
    order = OrderPlaced.objects.get(id=pk)
    if order.status == 'Принят':
        time.sleep(60)
        order.status = 'Готов'
        order.save()
        time.sleep(50)
        order.status = 'В пути'
        order.save()
        time.sleep(40)
        order.status = 'Доставлен'
        order.save()


@app.task
def send_mail_func():
    time.sleep(300)
    today = timezone.now()
    t = today.day - 1
    ex = OrderPlaced.objects.filter(
        Q(status='Доставлен') & Q(ordered_date__day__lte=today.day, ordered_date__day__gte=t))
    for e in ex:
        user1 = e.customer.user
        send_mail(
            'Ваш промокод',
            f" Получите {e.customer.name} ваш промокод за заказ {e.product.title}!",
            'angelatim11111@gmail.com',
            [user1.email],
            fail_silently=False,
        )
    return "Task Successfull"

# @app.task
# def job():
#     time.sleep(300)
#     today = timezone.now()
#     t = today.day - 1
#     ex = OrderPlaced.objects.filter(
#         Q(status='Доставлен') & Q(ordered_date__day__lte=today.day, ordered_date__day__gte=t))
#     for e in ex:
#         user1 = e.customer.user
#         send_mail(
#             'Ваш промокод',
#             f" Получите {e.customer.name} ваш промокод за заказ {e.product.title}!",
#             'angelatim11111@gmail.com',
#             [user1.email],
#             fail_silently=False,
#         )


# schedule.every(3).minutes.do(job)
# schedule.every(2).days.at("23:30").do(job)

# while True:
#     run_pending()
    # time.sleep(1)

