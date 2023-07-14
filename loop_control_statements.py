# Loop Control Statements

# break - полное завершение

#while True:
    #name = input("Enter your name: ")
    #if name != "":
        #break

# control - пропускает какой то элемент и продолжает цикл

#phone_number = "123-456-4212"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

# pass - пропускает элемент

for i in range(1,15):
    if i == 13:
        pass
    else:
        print(i)
