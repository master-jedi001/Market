import datetime


#  класс товар
class Item:
    __last_id = 0
    __dictionary = dict()    # справочник товаров

    def __init__(self, title, description, price):
        Item.__last_id += 1
        self.__id = Item.__last_id                # id товара
        self.__history = list()                   # история изменений
        self.title = title                        # название товара
        self.description = description            # описание товара
        self.price = price                        # цена товара
        self.__created = datetime.datetime.now()  # время создания
        Item.__dictionary[Item.__last_id] = self

    #  метод, который возвращает справочник товаров
    @staticmethod
    def get_dict():
        return Item.__dictionary

    @property
    def title(self):
        return self.__title

    #  проверка на корректность названия товара
    @title.setter
    def title(self, title):
        if type(title) == str:
            self.__title = title
            date_time = datetime.datetime.now()
            string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': title was changed on: ' + title
            self.__history.append(string)
        else:
            raise TypeError('title must be string')

    @property
    def description(self):
        return self.__description

    #  проверка на корректность описания товара
    @description.setter
    def description(self, description):
        if type(description) == str:
            self.__description = description
            date_time = datetime.datetime.now()
            string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': description was changed on: ' + description
            self.__history.append(string)
        else:
            raise TypeError('description must be string')

    @property
    def price(self):
        return self.__price

    #  проверка на корректность цены товара
    @price.setter
    def price(self, price):
        if type(price) != float:
            raise TypeError('Price must be float')
        elif price > 0:
            self.__price = price
            date_time = datetime.datetime.now()
            string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': price was changed on: ' + str(price)
            self.__history.append(string)
        else:
            raise ValueError('Price must be positive')

    def __str__(self):
        return str(self.__id) + ': ' + self.__title + ', ' + str(self.__price)

    #  метод, возвращающий время создания объекта класса Item
    def get_time_created(self):
        return self.__created.strftime('%d.%m.%Y %H:%M:%S')

    #  метод, возвращающий историю объекта класса Item
    def get_object_history(self):
        return self.__history

    #  метод поиска товара по его названию
    @staticmethod
    def get_item_by_title(item_title):
        for key in Item.__dictionary:
            if Item.__dictionary[key].__title == item_title:
                return Item.__dictionary[key]
        raise ValueError('Item not found')

    #  метод поиска товара по его цене
    @staticmethod
    def get_item_by_price(item_price):
        for key in Item.__dictionary:
            if Item.__dictionary[key].__price == item_price:
                return Item.__dictionary[key]
        raise ValueError('Item not found')
