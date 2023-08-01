from datetime import datetime
from  datetime import date

#  2023-08-01 16:30:33.872629
now = datetime.now()
print(now)

#01-08-2023 16:33:59
redact = now.strftime("%d-%m-%Y %H:%M:%S") # так мы изменяем вывод даты
redactMonth = now.strftime("%d-%b-%Y %H:%M:%S") # что бь месяц вывести полностью мы используем вместо "%m" - "%B"
# при использование "%B"-(August) - "%b"-(Aug)
print(redactMonth)

print(date.today().strftime(("%d-%m-%Y")))