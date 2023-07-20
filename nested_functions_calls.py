# nested functions calls Внутренние функции , также известные как вложенные функции , — это функции ,
# которые вы определяете внутри других функций.
# Python функция такого типа имеет прямой доступ к переменным и именам, определенным во внешней функции.
# Внутренние функции имеют множество применений, особенно в качестве фабрик замыканий и функций-декораторов.

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

num = round(abs(float(input("Enter a whole positive number: "))))
print(num)




