import datetime


#  класс каталог
class Catalog:
    __last_id = 0
    __dictionary = dict()          # справочник каталогов

    def __init__(self):
        Catalog.__last_id += 1
        self.__history = list()                     # история каталога
        self.__id = Catalog.__last_id               # id каталога
        self.__item_list = list()                     # список товаров в каталоге
        self.__created = datetime.datetime.now()    # время создания
        Catalog.__dictionary[Catalog.__last_id] = self

    #  метод, который возвращает справочник каталогов
    @staticmethod
    def get_dict():
        return Catalog.__dictionary

    def __str__(self):
        return 'Catalog ID: ' + str(self.__id) + ' (' + str(list(map(str, self.__item_list))) + ')'

    #  метод, находящий нужный каталог в базе по его id
    @staticmethod
    def get_catalog_by_id(catalog_id):
        for key in Catalog.__dictionary:
            if Catalog.__dictionary[key].__id == catalog_id:
                return Catalog.__dictionary[key]
        raise ValueError('Catalog not found')

    #  метод, возвращающий список товаров в каталоге
    def get_items_list(self):
        return self.__item_list

    #  метод, возвращающий время создания каталога
    def get_time_created(self):
        return self.__created.strftime('%d.%m.%Y %H:%M:%S')

    #  метод, возвращающий историю каталога
    def get_object_history(self):
        return self.__history
