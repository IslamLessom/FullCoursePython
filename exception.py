# exception - ещё один тип данных в python. Исключения необходимы для того, чтобы сообщать программисту об ошибках.

try:
    numerator = int(input("Enter am number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:  #as e - указывает на ошибку
    print(e)
    print("You can`t divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong : (")
else:
    print(result)
finally: # всегда выводит в конце
    print("The will always execute")


