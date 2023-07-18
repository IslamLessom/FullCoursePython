#index

name = "bro Code!"
#if (name[0].islower()):
    #name = name.capitalize() # переводит первую букву в верхний регистр

first_name = name[0:3].upper() #переводит в верхний регистр
last_name = name[4:].lower() #переводит в нижний регистр
last_character = name[-1]


print(first_name)
print(last_name)
print(last_character)
