from Item import Item
from Catalog import Catalog


class ItemList:
    __last_id = 0
    __dictionary = dict()

    def __init__(self, item, catalog):
        ItemList.__last_id += 1
        self.__id = ItemList.__last_id
        self.item = item                        # товар
        self.catalog = catalog                  # каталог
        ItemList.__dictionary[ItemList.__last_id] = self

    @staticmethod
    def get_dict():
        return ItemList.__dictionary

    def __str__(self):
        return 'ID: ' + str(self.__id) + '\n' + 'Catalog: ' + str(self.__catalog) + '\n' + 'Item: ' + str(self.__item)

    @property
    def item(self):
        return self.__item

    #  проверка на корректность поля item
    @item.setter
    def item(self, item):
        if type(item) == Item:
            self.__item = item
        else:
            raise TypeError('item must be an object of class Item')

    @property
    def catalog(self):
        return self.__catalog

    #  проверка на корректность поля catalog
    @catalog.setter
    def catalog(self, catalog):
        if type(catalog) == Catalog:
            self.__catalog = catalog
        else:
            raise TypeError('catalog must be an object of class Catalog')

    # метод, возвращающий список всех каталогов, в которых есть товар item
    @staticmethod
    def get_catalogs_by_item(item):
        catalog_list = list()
        for key in ItemList.__dictionary:
            if ItemList.__dictionary[key].__item == item:
                catalog_list.append(ItemList.__dictionary[key].__catalog)
        return catalog_list

    # метод, возвращающий список всех товаров, которые есть в каталоге catalog
    @staticmethod
    def get_items_by_catalog(catalog):
        item_list = list()
        for key in ItemList.__dictionary:
            if ItemList.__dictionary[key].__catalog == catalog:
                item_list.append(ItemList.__dictionary[key].__item)
        return item_list
