#  Ссылка на UML диаграмму
#  https://drive.google.com/drive/folders/1E71EJpcyTZGrGo9QEJlr8UvvTypib2BS?usp=sharing

from Cart import Cart
from Admin import *

user_1 = User('Ivan', 'Ivanov', '89065117346', 'ivanov@yandex.ru')
user_2 = User('Petr', 'Petrov', '89032302671', 'petrov@yandex.ru')
admin = Admin('Sidr', 'Sidorov', '89163372345', 'sidr88@yandex.ru')

catalog = Admin.create_catalog()

Admin.add_item_to_catalog(catalog, Item('Smartphone Samsung Galaxy A22s', '128GB Gray', 25499.0))
Admin.add_item_to_catalog(catalog, Item('Smartphone Apple iPhone 13', '128GB Midnight', 111999.0))
Admin.add_item_to_catalog(catalog, Item('Smartphone Samsung Galaxy A52', '128GB Awesome Black', 37999.0))
Admin.add_item_to_catalog(catalog, Item('Smartphone HUAWEI P40 Lite', '128GB Midnight Black', 19999.0))

cart_1 = Cart(user_1)
cart_2 = Cart(user_2)

cart_1.add_item_to_cart(catalog.get_items_list()[0])
cart_1.add_item_to_cart(catalog.get_items_list()[1])
cart_1.add_item_to_cart(catalog.get_items_list()[3])
cart_2.add_item_to_cart(catalog.get_items_list()[1])
cart_2.add_item_to_cart(catalog.get_items_list()[2])
cart_2.add_item_to_cart(catalog.get_items_list()[3])

print(cart_1)
print(cart_2)
