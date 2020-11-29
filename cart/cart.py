from decimal import Decimal
from django.conf import settings
from apps.products.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}# save an empty cart in the session
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart# Обновление сессии
        self.session.modified = True# Отметить как "измененный", чтобы убедиться, что он сохранен

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)# получение объектов product и добавление их в корзину

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())#Подсчет всех товаров в корзине

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in# Подсчет стоимости товаров в корзине.
            self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]# удаление корзины из сессии
        self.session.modified = True
        