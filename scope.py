# scope = Локальная область
# Переменная, созданная внутри функции, принадлежит к локальной области действия этой функции
# и может использоваться только внутри этой функции.

name = "bro" #global score
def display_name():
    #name = "code" # local score
                        # для начала функция будет использовать локальные переменные ,
                        # а если не найдет то будет использовать глобальные
    print(name)

display_name()
print(name)