# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(my_list))

for i in my_list:
    my_list = [i.lower() for i in my_list]
    #print(my_list)
    my_list = ' '.join(my_list)
    #print(my_list)
    my_list = my_list.split()
    #print(my_list)
igor = my_list[1].capitalize()
marina = my_list[4].capitalize()
nikolay = my_list[8].capitalize()
print(f'Привет, {igor}!')
print(f'Привет, {marina}!')
print(f'Привет, {nikolay}!')

print(f'{igor}')
print(f'{marina}')
print(f'{nikolay}')

name1 = 1
my_list[name1] = igor
name2 = 4
my_list[name2] = marina
name3 = 8
my_list[name3] = nikolay
my_list = ' '.join(my_list)

print(my_list)
print(id(my_list))
#
# for i in my_list:
#     print("Привет,", i.split()[-1].capitalize()) # гениально!