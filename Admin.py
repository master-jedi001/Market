from User import *
from ItemList import *


class Admin(User):

    #  метод по созданию каталога
    @staticmethod
    def create_catalog():
        return Catalog()

    #  метод по добавлению товара в каталог (считается, что товары в каталоге не повторяются)
    @staticmethod
    def add_item_to_catalog(catalog, item):
        if type(catalog) != Catalog:
            raise TypeError('catalog must an object of class Catalog')
        else:
            if item in catalog.get_items_list():
                print('item already exists in catalog')
            elif type(item) == Item:
                catalog.get_items_list().append(item)
                date_time = datetime.datetime.now()
                string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': ' + str(item) + ' was added to ' + str(catalog)
                catalog.get_object_history().append(string)
                ItemList(item, catalog)
            else:
                raise TypeError('item must be an object of class Item')

    #  метод по удалению товара из каталога
    @staticmethod
    def delete_item_from_catalog(catalog, item):
        if type(catalog) != Catalog:
            raise TypeError('catalog must an object of class Catalog')
        else:
            if not (item in catalog.get_items_list()):
                print('item does not exist in catalog')
            elif type(item) == Item:
                catalog.get_items_list().remove(item)
                date_time = datetime.datetime.now()
                string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': ' + str(item) + ' was deleted from ' + str(catalog)
                catalog.get_object_history().append(string)
                for key in ItemList.get_dict():
                    if ItemList.get_dict()[key].item == item:
                        del ItemList.get_dict()[key]
                        break
            else:
                raise TypeError('item must be an object of class Item')

    # метод, меняющий цену товара
    @staticmethod
    def change_item_price(item, price):
        if type(item) != Item:
            raise TypeError('item must be an object of class Item')
        else:
            item.price = price

    # метод, меняющий название товара
    @staticmethod
    def change_item_title(item, title):
        if type(item) != Item:
            raise TypeError('item must be an object of class Item')
        else:
            item.title = title

    # метод, меняющий описание товара
    @staticmethod
    def change_item_description(item, description):
        if type(item) != Item:
            raise TypeError('item must be an object of class Item')
        else:
            item.description = description
