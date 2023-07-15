#2d lists = список в списке

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

#print(food[0][0])

for i in food:
    for b in i:
        print(b, end=" ")




