import datetime
import re
from random import randint

regex_phone = re.compile(r'^((8)[\- ]?)?\(?\d{3,5}\)?[\- ]?\d{1}[\- ]?\d{1}[\- ]?\d{1}[\- ]?\d{1}[\- ]?\d{1}(([\- ]?\d{1})?[\- ]?\d{1})?$')
regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


#  класс пользователь
class User:
    __last_id = 0
    __dictionary = dict()  # справочник всех пользователей

    def __init__(self, name, surname, phone, email):
        User.__last_id += 1
        self.__status = True                        # нужен для того, чтобы пользователь не мог изменить имя и фамилию
        self.__id = User.__last_id                  # id пользователя
        self.__history = list()                     # история изменений
        self.name = name                            # имя пользователя
        self.surname = surname                      # фамилия пользователя
        self.phone = phone                          # телефон пользователя
        self.email = email                          # почта пользователя
        self.__created = datetime.datetime.now()    # время создания
        self.__status = False
        User.__dictionary[User.__last_id] = self

    #  метод, который возвращает справочник пользователей
    @staticmethod
    def get_dict():
        return User.__dictionary

    #  метод, проверяющий, что строка сосотит только из букв, дефисов и пробелов
    @staticmethod
    def is_alpha_space_dash(string):
        result = True
        for s in string:
            test_1 = ord(s) < 65 or 90 < ord(s) < 97 or 122 < ord(s)
            test_2 = ord(s) != 32 and ord(s) != 45
            if test_1 and test_2:
                result = False
                break
        return result

    @property
    def name(self):
        return self.__name

    #  проверка на корректность имени пользователя
    @name.setter
    def name(self, name):
        if self.__status:
            if type(name) != str:
                raise TypeError('Name must be string')
            elif User.is_alpha_space_dash(name):
                self.__name = name
            else:
                raise ValueError('Name can contain only letters, hyphens and spaces')
        else:
            print('Name can not be changed')

    @property
    def surname(self):
        return self.__surname

    #  проверка на корректность фамилии пользователя
    @surname.setter
    def surname(self, surname):
        if self.__status:
            if type(surname) != str:
                raise TypeError('Surname must be string')
            elif User.is_alpha_space_dash(surname):
                self.__surname = surname
            else:
                raise ValueError('Surname can contain only letters, hyphens and spaces')
        else:
            print('Surname can not be changed')

    @property
    def phone(self):
        return self.__phone

    #  проверка на корректность номера телефона пользователя
    @phone.setter
    def phone(self, phone):
        if re.fullmatch(regex_phone, str(phone)):
            verification_code = randint(100000, 999999)
            print('To confirm the number, enter the code:', verification_code)
            code = input()
            if code == str(verification_code):
                self.__phone = phone
                date_time = datetime.datetime.now()
                string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': user phone was changed on: ' + str(phone)
                self.__history.append(string)
            else:
                raise ValueError('Invalid code')
        else:
            raise ValueError('Invalid phone')

    @property
    def email(self):
        return self.__email

    #  проверка на корректность почты пользователя
    @email.setter
    def email(self, email):
        if re.fullmatch(regex_email, str(email)):
            verification_code = randint(100000, 999999)
            print('To confirm the email, enter the code:', verification_code)
            code = input()
            if code == str(verification_code):
                self.__email = email
                date_time = datetime.datetime.now()
                string = date_time.strftime('%d.%m.%Y %H:%M:%S') + ': user email was changed on: ' + str(email)
                self.__history.append(string)
            else:
                raise ValueError('Invalid code')
        else:
            raise ValueError('Invalid email')

    def __str__(self):
        return str(self.__id) + ': ' + self.__name + ' ' + self.__surname + ' (' + str(self.__phone) + ')'

    #  метод поиска пользователя по его id
    @staticmethod
    def get_user_by_id(user_id):
        for key in User.__dictionary:
            if User.__dictionary[key].__id == user_id:
                return User.__dictionary[key]
        raise ValueError('User not found')

    #  метод поиска пользователя по его номеру телефона
    @staticmethod
    def get_user_by_phone(phone):
        for key in User.__dictionary:
            if User.__dictionary[key].__phone == phone:
                return User.__dictionary[key]
        raise ValueError('User not found')

    #  метод поиска пользователя по его почте
    @staticmethod
    def get_user_by_email(email):
        for key in User.__dictionary:
            if User.__dictionary[key].__email == email:
                return User.__dictionary[key]
        raise ValueError('User not found')

    #  метод, возвращающий время создания пользователя
    def get_time_created(self):
        return self.__created.strftime('%d.%m.%Y %H:%M:%S')

    #  метод, возвращающий историю пользователя
    def get_object_history(self):
        return self.__history
