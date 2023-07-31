#Как следует из названия, __init__ означает инициализацию, 
#которая отвечает за процесс установки начального состояния созданного экземпляра класса. 
#Есть соглашение, согласно которому первый параметр должен называться self, хотя это и не обязательно. 
#Отмечу, что self – это не ключевое слово в Python, в отличие от многих других языков, 
#где используется this, self или it.

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price  
    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

iphone = Phone("Iphone 7+", 300)

samsung = Phone("Samsung s20", 1400)
print(samsung.price)
print(samsung.brand)
samsung.call(999)