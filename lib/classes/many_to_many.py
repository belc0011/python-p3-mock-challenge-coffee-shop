class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.all.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("customer must be of type Customer")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("coffee must be of type Coffee")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, '_price'):
            print("Cannot reassign price")
        elif isinstance(price, float):
            if price >= 1.0 and price <= 10.0:
                self._price = price
class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            print("Cannot reassign name")
        elif isinstance(name, str):
            if len(name) >= 3:
                self._name = name
        else:
            raise ValueError("Name must be of type string and must be at least 3 characters")
    def orders(self):
        coffee_list = []
        for order in Order.all:
            if order.coffee == self:
                if isinstance(order, Order):
                    coffee_list.append(order)
        return coffee_list
    
    def customers(self):
        customer_list = []
        for order in Order.all:
            if order.coffee == self:
                if isinstance(order.customer, Customer):
                    customer_list.append(order.customer)
        customer_set = set(customer_list)
        customer_list = list(customer_set)
        return customer_list
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        count = 0
        sum = 0
        for order in Order.all:
            if order.coffee == self:
                sum += order.price
                count += 1
        if (count):
            return sum/count
        else:
            return 0

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if len(name) >= 1 and len(name) <= 15:
                self._name = name
        else:
            print("Name must be of type string")
    def orders(self):
        order_list = []
        for order in Order.all:
            if order.customer == self:
                if isinstance(order, Order):
                    order_list.append(order)
        return order_list
    
    def coffees(self):
        coffee_list = []
        for order in Order.all:
            if order.customer == self:
                if isinstance(order.coffee, Coffee):
                    coffee_list.append(order.coffee)
        coffee_set = set(coffee_list)
        coffee_list_unique = list(coffee_set)
        return coffee_list_unique
    
    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee):
            if isinstance(self, Customer):
                new_order = Order(self, coffee, price)
        return new_order
    
