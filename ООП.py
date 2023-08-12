class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if tupe(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if tupe(value) in (float, int) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)
