#slicing

name = "Bro Code"

first_name = name[0:3]
last_name = name[4:]
funky_name = name[0:8:2]
reversed_name = name[::-1]# edoC orB

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4) #google #wikipedia
print(website1[slice])
print(website2[slice])