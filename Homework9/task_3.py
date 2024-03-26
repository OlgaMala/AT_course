# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt', mode='r') as file:
    purchase = 0
    purchase_list = []
    for st in file.readlines():
        if not st == '\n':
            purchase += int(st)
        else:
            purchase_list.append(purchase)
            purchase = 0
            continue
    res = sorted(purchase_list, reverse=True)[:3]
    three_most_expensive_purchases = res[0] + res[1] + res[2]


assert three_most_expensive_purchases == 202346
