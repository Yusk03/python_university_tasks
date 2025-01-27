# -*- coding: utf-8 -*-
"""
Завдання 4.5

З рядків command1 та command2 одержати список VLANів, які є і в команді
command1 і в команді command2 (перетин). Елементи списку мають бути
відсортовані за зростанням.

В даному випадку, результатом має бути такий список: ['1', '3', '8']

Записати підсумковий список у змінну result (саме ця змінна перевірятиметься у
тесті). У списку result влада повинна бути відсортована за зростанням номерів.
Для отримання підсумкового списку не можна видаляти конкретні vlanи вручну.

Отриманий список результату вивести на стандартний потік виведення (stdout) за
допомогою print.

Це завдання можна виконати без використання циклів і умов.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""
import re

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = re.findall(r'\d+', command1)
vlans2 = re.findall(r'\d+', command2)

result = sorted(set(vlans1) & set(vlans2))

print(result)
