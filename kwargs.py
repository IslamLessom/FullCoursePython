#а **kwargs — сокращение от «keyword arguments» (именованные аргументы).
#Каждая из этих конструкций используется для распаковки аргументов соответствующего типа, 
#позволяя вызывать функции со списком аргументов переменной длины

#def hello(first, last):
    #print("Hello" + first +" " + last)
#hello(first="Bro", middle="Dude",last="Code")

def hello(**kwargs):
    #print("Hello" + kwargs['first'] + " " + kwargs['last'] + kwargs['middle'])
    print('Hello', end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
hello(first="Bro", middle="Dude",last="Code")