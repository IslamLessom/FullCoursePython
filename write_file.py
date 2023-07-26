text = "Hello broooo\nThis is some text\nHave a good one!\n"

with open('test.txt', 'a') as file: # если использовать "a - open('test.txt', 'a')" то он добоавляет текст , если "w open('test.txt', 'w')" , то переписывает полностью
    file.write(text)