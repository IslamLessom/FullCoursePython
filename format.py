# format = Метод format()форматирует указанные значения и вставляет их в заполнитель строки.

animal = "cow"
item= "moon"

#print("The" + animal + " jumped over the " + item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {1}".format(animal,item))# position argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "Bro"

#print("Hello, my name is {}".format(name))

#Пробелы после name

#print("Hello, my name is {:10}. Nice to meet you".format(name))
#print("Hello, my name is {:<10}. Nice to meet you".format(name))
#print("Hello, my name is {:>10}. Nice to meet you".format(name))
#print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 3.14159
print("The number pi is {:.2f}".format(number)) #{:.2f} округление до 2 значений после точки

