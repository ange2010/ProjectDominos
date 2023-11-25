from django.db.models import Count
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, OrderPlacedSerializer
from django.conf import settings
import time
from .tasks import send, send2, set_status
# from .tasks import job
from .tasks import send_mail_func
from django.core.mail import send_mail
from django.utils import timezone

def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/home.html', locals())

def about(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/about.html', locals())

def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/contact.html', locals())

class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # send(form.instance.email)
            messages.success(request, "Поздравлянм! Регистрация прошла успешно")
        else:
            messages.warning(request, "Введите корректные данные")
        return render(request, "app/customerregistration.html", locals())

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        form = CustomerProfileForm()
        return render(request, "app/profile.html", locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Поздравляем! Профиль успешно сохранен')
        else:
            messages.warning(request, 'Ошибка ввода')
        return render(request, "app/profile.html", locals())

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

@method_decorator(login_required, name='dispatch')
class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "app/updateAddress.html", locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Поздравляем! Профиль успешно обновлен')
        else:
            messages.warning(request, 'Ошибка ввода')
        return redirect("address")

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.selling_price
        amount = amount + value
    totalamount = amount + 0
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html', locals())

@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.selling_price
            famount = famount + value
        totalamount = famount + 0
        return render(request, "app/checkout.html", locals())

@login_required
def payment_done(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    famount = 0
    for p in cart_items:
        value = p.quantity * p.product.selling_price
        famount = famount + value
    totalamount = famount + 0
    payment = Payment(user=user, amount=totalamount)
    payment.paid = True
    payment.save()
    customer = Customer.objects.get(user=user)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()
        messages.success(request, 'Оплата получена! Ваш заказ выполняется!')
        order = OrderPlaced.objects.filter(user=user)
        send.delay(user.email)
        for o in order:
            set_status.delay(o.id)
        if customer.promotional_code == False:
            send2.delay(user.email)
            customer.promotional_code = True
            customer.save()
    # job.delay()
    return redirect('orders')

@login_required
def payment_status1(request):
    return redirect('orders')

@login_required
def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    orderplaced = OrderPlaced.objects.filter(user=request.user)
    return render(request, "app/orders.html", locals())

def send_mail_to_all_users(request):
    send_mail_func.delay()
    return HttpResponse('Бонусы отправлены покупателям!')

@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)

def search(request):
    query = request.GET['search']
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html", locals())



class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderPlacedView(ModelViewSet):
    queryset = OrderPlaced.objects.all()
    serializer_class = OrderPlacedSerializer




# @login_required
# def show_wishlist(request):
#     user = request.user
#     totalitem = 0
#     wishlist = 0
#     if request.user.is_authenticated:
#         totalitem = len(Cart.objects.filter(user=request.user))
#         wishlist = len(Wishlist.objects.filter(user=request.user))
#     product = Wishlist.objects.filter(user=user)
#     return render(request, 'app/wishlist.html', locals())

# def plus_wishlist(request):
#     if request.method == 'GET':
#         prod_id = request.GET['prod_id']
#         product = Product.objects.get(id=prod_id)
#         user = request.user
#         Wishlist(user=user, product=product).save()
#         data = {
#             'message': 'Wishlist Added Successfully',
#         }
#         return JsonResponse(data)
#
# def minus_wishlist(request):
#     if request.method == 'GET':
#         prod_id = request.GET['prod_id']
#         product = Product.objects.get(id=prod_id)
#         user = request.user
#         Wishlist.objects.filter(user=user, product=product).delete()
#         data = {
#             'message': 'Wishlist Remove successfully',
#         }
#         return JsonResponse(data)

# today = timezone.now()
    # t = today.day - 1
    # ex = OrderPlaced.objects.filter(Q(status='Доставлен') & Q(ordered_date__day__lte=today.day, ordered_date__day__gte=t))
    # print(ex)
    # for e in ex:
    #     print(e)
    #     user1 = e.customer.user
    #     send_mail(
    #         'Ваш промокод',
    #         f" Получите {e.customer.name} ваш промокод за заказ {e.product.title}!",
    #         'angelatim11111@gmail.com',
    #         [user1.email],
    #         fail_silently=False,
    #     )
    #     print(e.ordered_date)