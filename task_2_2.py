# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list))

my_str = ' '.join(my_list)
my_str = my_str[0] + " '" + '05' + "'" + my_str[3:10] + "'" + my_str[10:12] + "'" + my_str[12:44] + "'" + '+05' + "'" + my_str[-9:]
print(my_str)
print(id(my_str))


my_str2 = ' '.join(my_list)
my_str2 = my_str2[0] + " ' " + '05' + " '" + my_str2[3:10] + "' " + my_str2[10:12] + " '" + my_str2[12:44] + "' " + '+05' + " '" + my_str2[-9:]
my_list2 = my_str2.split(' ')

print(my_list2)
print(id(my_list2))
print(my_str)