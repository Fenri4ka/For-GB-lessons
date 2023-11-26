# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


my_list = [1, 'a', 2, 'b', 1, 'c', 2, 'a', 5, 'b', 'c', 3, 6, 'u', 9]
new_list = []
my_set = set(my_list)

for item in my_set:
    if my_list.count(item) > 1:
        new_list.append(item)

print(new_list)

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


my_text = """Тип данных характеризует одновременно: множество допустимых значений, которые могут принимать данные, 
принадлежащие к этому типу; 
набор операций, которые можно осуществлять над данными, принадлежащими к этому типу. 
Первое свойство можно рассматривать как теоретико-множественное определение понятия типа; 
второе — как процедурное (или поведенческое) определение. 
Кроме этого, в программировании используется низкоуровневое определение типа — как заданных размерных и структурных 
характеристик ячейки памяти, 
в которую можно поместить некое значение, соответствующее этим характеристикам. 
Такое определение является частным случаем теоретико-множественного. 
На практике, с ним связан ряд важных свойств (обусловленных особенностями организации памяти компьютера), 
требующих отдельного рассмотрения.
Теоретико-множественное определение, особенно в низкоуровневом варианте, чаще всего используется в императивном 
программировании. 
Процедурное определение в большей степени связывается с параметрическим полиморфизмом. 
Объектно-ориентированное программирование использует процедурное определение при описании взаимодействия 
компонентов программы, 
и теоретико-множественное — при описании реализации этих компонентов на ЭВМ, соответственно, 
рассматривая «класс-как-поведение» и «класс-как-объект в памяти"""

my_dict = {}
preposition_list = ['в', 'на', 'под', 'над', 'из', 'и', 'к', 'у', 'о', 'с', 'от', 'до', 'по', 'за']
txt_list = my_text.lower().split()
txt_list_new = [''.join(filter(str.isalpha, a)) for a in txt_list]

while '' in txt_list_new:
    txt_list_new.remove('')

for word in txt_list_new:
    if word not in preposition_list:
        my_dict.setdefault(word, txt_list_new.count(word))

num_words = 1
while num_words <= 10:
    num_words += 1
    max_key = max(my_dict, key=my_dict.get)
    print(f'{max_key:>5}  =  {my_dict[max_key]}')
    my_dict.pop(max_key)


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import random

bag_capacity = int(input('Введите грузоподъёмность Вашего рюкзака, округлив до целого числа в меньшую сторону: '))

item_dict = {'Еда': 2, 'Вода': 2, 'Палатка': 5, 'Шампура': 1, 'Сменная одежда': 3, 'Дождевик': 1, 'Зонт': 2,
             'Купальник': 1, 'Аптечка': 2, 'Powerbank': 1, 'Ноутбук': 2, 'GPS навигатор': 1, 'Плед': 1, 'Мачете': 3,
             'Одеяло': 3}
weight = 0
scrab_list = []

for key, value in item_dict.items():
    weight += value
    if weight <= bag_capacity:
        scrab_list.append(key)
    else:
        weight -= value

print(f'В рюкзак грузоподъёмностью {bag_capacity} кг можно вместить {scrab_list}')
