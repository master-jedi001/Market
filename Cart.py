from OrderDetails import OrderDetails
from Admin import *


#  класс корзина (корзин может быть много, но у каждого пользователя только одна корзина)
class Cart:
    __last_id = 0
    __dictionary = dict()   # справочник корзин

    def __init__(self, user):
        Cart.__last_id += 1
        self.__status = True                           # нужен для того, чтобы у корзины не мог поменяться пользователь
        self.__id = Cart.__last_id                          # id корзины
        self.__history = list()                             # история корзины
        self.user = user                                    # пользователь
        self.__items = list()                               # список товаров в корзине, добавленных пользователем
        self.__created = datetime.datetime.now()            # время создания
        self.__status = False
        Cart.__dictionary[Cart.__last_id] = self

    #  метод, который возвращает справочник корзин
    @staticmethod
    def get_dict():
        return Cart.__dictionary

    #  метод, который проверяет, существует ли у пользователя user корзина
    @staticmethod
    def is_cart_exist(user):
        is_exist = False
        for key in Cart.__dictionary:
            if Cart.__dictionary[key].__user == user:
                is_exist = True
                break
        return is_exist

    @property
    def user(self):
        return self.__user

    #  проверка на корректность поля user
    @user.setter
    def user(self, user):
        if self.__status:
            if type(user) != User and type(user) != Admin:
                raise TypeError('user must be an object of class User or class Admin')
            elif Cart.is_cart_exist(user):
                raise ValueError('Shopping cart for this user already exists')
            else:
                self.__user = user
        else:
            print('field user can not be changed')

    def __str__(self):
        return 'Cart ID: ' + str(self.__id) + ', ' + 'Items: ' + str(list(map(str, self.__items)))

    # метод нахождения корзины по её id
    @staticmethod
    def get_cart_by_id(cart_id):
        for key in Cart.__dictionary:
            if Cart.__dictionary[key].__id == cart_id:
                return Cart.__dictionary[key]
        raise ValueError('Shopping Cart not found')

    # метод нахождения корзины по её пользователю
    @staticmethod
    def get_cart_by_user(user):
        if type(user) != User:
            raise TypeError('user must be an object of class User')
        else:
            for key in Cart.__dictionary:
                if Cart.__dictionary[key].__user == user:
                    return Cart.__dictionary[key]
            raise ValueError('Shopping Cart not found')

    #  метод по добавлению заказа в корзину (предполагается, что один и тот же товар можно добавлять в корзину по
    #  нескольку раз)
    def add_item_to_cart(self, item):
        if type(item) == Item:
            item_list = ItemList.get_catalogs_by_item(item)
            if len(item_list):
                self.__items.append(item)
                date_time = datetime.datetime.now()
                string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': ' + str(item) + ' was added to shopping cart'
                self.__history.append(string)
                OrderDetails(self, item)
            else:
                print('There is no such item in any catalogs')
        else:
            raise TypeError('item must be object of class Item')

    #  метод, проверяющий есть ли товар в корзине
    def is_item_in_cart(self, item):
        is_find = False
        if item in self.__items:
            is_find = True
        return is_find

    #  метод, определяющий количество единиц товара item в корзине
    def get_item_count_in_cart(self, item):
        count = 0
        for i in self.__items:
            if i == item:
                count += 1
        return count

    #  метод по удалению товара из корзины
    def delete_item_from_cart(self, item):
        if self.is_item_in_cart(item):
            self.__items.remove(item)
            date_time = datetime.datetime.now()
            string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': ' + str(item) + ' was deleted from shopping cart'
            self.__history.append(string)
            for key in OrderDetails.get_dict():
                if OrderDetails.get_dict()[key].item == item:
                    del OrderDetails.get_dict()[key]
                    break
        else:
            print('There is no such item in the shopping cart')

    #  метод, возвращающий список заказов в корзине
    def get_items_list(self):
        return self.__items

    #  метод, возвращающий время создания корзины
    def get_time_created(self):
        return self.__created.strftime('%d.%m.%Y %H:%M:%S')

    #  метод, возвращающий историю корзины
    def get_object_history(self):
        return self.__history
