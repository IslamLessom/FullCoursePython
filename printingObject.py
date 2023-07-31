class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price  
    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")
    def __str__(self) -> str: # -> это означает что он возврашает строковый метод , мы можем убрать его , но что бы быть точным оставим
        return f"\nBrand - {self.brand} \nPrice = {self.price}\n"

iphone = Phone("Iphone 7+", 300)
samsung = Phone("Samsung s20", 1400)

# пытаемся вывести iphone and samsung , получаем ответ - 
# <__main__.Phone object at 0x000001F479C7ED10>
# <__main__.Phone object at 0x000001F479C7EE50>
# что бы избежать это мы создаем функцию которая переводит этот набор символов в строку 
#   def __str__(self) -> str:
            #return f"Brand - {self.brand} \nPrice = {self.price}"

print(iphone)
print(samsung)