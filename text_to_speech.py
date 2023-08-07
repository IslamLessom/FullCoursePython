#У нас есть программа которая выводит шутки , мы создадим программу которая эти шутки будет воспроизводить
#Будем делать при помоши библиотеки pyttsx3
#pip3 install pyttsx3

from urllib import request
import json
import pyttsx3

#преобразование голоса
engine = pyttsx3.init() # создание объекта
voices = engine.getProperty('voices') #получение сведений о текущем голосе
engine.setProperty('voice', voices[1].id) #изменение индекса, изменение голоса. 1 для женского пола

#громкость голоса
volume = engine.getProperty('volume') #узнавание текущего уровня громкости (мин. =0 и max=1)
print (volume) # печать текущего уровня громкости
engine.setProperty('volume',1) # установка уровня громкости от 0 до 1


url = "http://joke.deno.dev/all"
r = request.urlopen(url)

data = r.read()
jsonData = json.loads(data)

print(jsonData)

class Joke:
    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline
    def __str__(self):
        return f"\nsetup - {self.setup} \npunchline - {self.punchline}"


jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The Punchline")
    pyttsx3.speak(joke.punchline)
    # Сохранение голоса в файл
    # В Linux убедитесь, что установлены 'espeak' и 'ffmpeg'
    engine.save_to_file(joke.punchline, 'punchline.mp3')
    engine.save_to_file(joke.setup, 'setup.mp3')



