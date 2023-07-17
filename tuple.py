#tuple - Кортеж (tuple) представляет последовательность элементов,
#которая во многом похожа на список за тем исключением,
#что кортеж является неизменяемым (immutable) типом.
#Поэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.

student = ("bro", 21, 'male')

#print(student.count("bro")) #считает сколько bro в списке
#print(student.index("male")) #указывает индекс элемента

for x in student:
    print(x)
if "bro" in student:
    print("Bro is here")