#nested loops

rows = int(input("How many 5"))
colums = int(input("How many columps"))
symbol = input("Enter a symbol to use")

for i in range(rows):
    for j in range(colums):
        print(symbol, end="")
    print()

