#  класс делатей заказа
class OrderDetails:
    __last_id = 0
    __dictionary = dict()

    def __init__(self, cart, item):
        OrderDetails.__last_id += 1
        self.__id = OrderDetails.__last_id
        self.cart = cart                    # корзина
        self.item = item                    # товар
        OrderDetails.__dictionary[OrderDetails.__last_id] = self

    #  метод, который возвращает справочник обектов OrderDetails
    @staticmethod
    def get_dict():
        return OrderDetails.__dictionary

    @property
    def cart(self):
        return self.__cart

    @cart.setter
    def cart(self, cart):
        self.__cart = cart

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, item):
        self.__item = item

    def __str__(self):
        return 'ID: ' + str(self.__id) + '\n' + 'Cart: ' + str(self.__cart) + '\n' + 'Item: ' + str(self.__item)

    #  метод поиска всех пользователей с товаром item в корзине
    @staticmethod
    def get_users_by_item(item):
        user_list = list()
        for key in OrderDetails.__dictionary:
            if OrderDetails.__dictionary[key].__item == item:
                user_list.append(OrderDetails.__dictionary[key].__cart.user)
        return user_list

    #  метод поиска всех товаров, лежащих в корзине у пользователя user
    @staticmethod
    def get_items_by_user(user):
        item_list = list()
        for key in OrderDetails.__dictionary:
            if OrderDetails.__dictionary[key].__cart.user == user:
                item_list.append(OrderDetails.__dictionary[key].__item)
        return item_list
