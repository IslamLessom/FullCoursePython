#if else elif
age = int(input("How okd are you ? : "))
if age >= 18:
    print("You are an abult!")
elif age == 100:
    print("You old")
elif age < 0:
    print("error!")
else:
    print("You are a child")