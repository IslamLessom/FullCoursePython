import random

while True:
    choices = ["камень","ножницы","бумага"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Камень , Ножницы , Бумага?: ").lower()

    if player == computer:
        print("Компьютер: " + computer)
        print("Игрок: " + player)
        print("Ничья!")
    elif player == "камень":
        if computer == "ножницы":
            print("Компьютер: " + computer)
            print("Игрок: " + player)
            print("Вы выиграли!")
        if computer == "бумага":
            print("Компьютер: " + computer)
            print("Игрок: " + player)
            print("Вы проиграли!")
    elif player == "ножницы":
        if computer == "камень":
            print("Компьютер: " + computer)
            print("Игрок: " + player)
            print("Вы проиграли!")
        if computer == "бумага":
            print("Компьютер: " + computer)
            print("Игрок: " + player)
            print("Вы выиграли!")
    elif player == "бумага":
        if computer == "камень":
            print("Компьютер: " + computer)
            print("Игрок: " + player)
            print("Вы выиграли!")
        if computer == "ножницы":
            print("Компьютер: " + computer)
            print("Игрок: " + player)
            print("Вы проиграли!")

    play_again = input("Вы хотите продолжить игру ? (Да/Нет)").lower()

    if play_again != 'да':
        break
print("Пока!")


