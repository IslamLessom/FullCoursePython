#dictionary - это изменяемый неупорядоченный набор уникальных пар ключ-значение , они быстрее потому что используют хеширование
#и они позволяют нам получить доступ к значению быстро

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

#capitals.update({'Germany': "Berlin"}) #добавляет элемент
#capitals.update({'USA': "Las Vegas"}) #изменяет элемент
#capitals.pop('China') #удаляет элемент
#capitals.clear() #удаляет все элементы

#print(capitals["Russia"])
#print(capitals.get('Russia')) # более безопасный способ вывода , так как не возврашает ошибку , если такого ключ элемента не найдет , возврашает none
#print(capitals.keys()) #dict_keys(['USA', 'India', 'China', 'Russia'])
#print(capitals.values()) #dict_values(['Washington DC', 'New Dehli', 'Beijing', 'Moscow'])
#print(capitals.items()) #dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

for key, value in capitals.items():
    print(key, "-", value)

