#1)

class DeleteMixin:
    def delete(self, key):
        return self.todos.pop(key,1111)
    
class CreateMixin:
    def create(self, todo, key):
        if key in self.todos.keys():
            return "Задача под таким ключом уже существует"
        self.todos[key] = todo
        return self.todos
class ReadMixin:
    def read(self):
        return sorted(self.todos.items())
class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
    todos = {}

    def set_deadline(self, date):
        import datetime
        date = date.split('/')
        date_now = datetime.datetime.now()
        date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        return -(date_now - date).days



#2)
class Person:
    def __init__(self,name = None,last_name = None,age = None,email = None):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n_name):
        self.__name = n_name
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self,n_last_name):
        self.__last_name = n_last_name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,n_age):
        self.__age = n_age
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,n_email):
        self.__email = n_email
john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com

#3)
class Dog:
    def voice(self):
        print('Гав')
class Cat:
    def voice(self):
        print('Мяу')

def to_pet(animal):
    animal.voice()
    
barsik = Cat()
rex = Dog()

to_pet(barsik)
to_pet(rex)