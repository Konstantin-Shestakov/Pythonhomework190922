# Вам уже приходилось писать таблицу умножения. 
# Но в этот раз вас попросили сделать в плюс к таблице и 
# умножения еще таблицу сложения, 
# а также таблицу возведения в степень.
# Что бы не копировать один и тот же код и обобщить все три функции до единой 
# рисования таблиц (бинарных) арифметических операций, 
# напишите функцию print_operation_table(operation, num_rouws=9, num_colums=9), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. 
# Нумерация строк и столбцов идёт с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.


# def print_operation_table (op, num_rouws=9, num_colums=9):
#     print()
#     if op(num_rouws, num_colums) != num_rouws + num_colums:
#         for i in range(1, num_rouws+1):
#             for j in range(1, num_colums+1):
#                 print(f'{op(i,j):2}', end= '\t')
            
#             print()

#     else:
#          for i in range(num_rouws+1):
#             for j in range(num_colums+1):
#                 print(f'{op(i,j):2}', end= '\t')
            
#             print()

          
              
# print_operation_table(lambda x,y : x+y)


# print_operation_table(lambda x,y : x*y, 5)


# print_operation_table(lambda x,y : x**y, 3)

# 2. Мимикрия
# У вас есть код, который вы не можите менять (так часто бывает, когда код  глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# trasformed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи не нужно никак преобразовывать список значений, а нужно получить его как есть.

# Напишите такое лямбда-выражение transformation, чтобы trasformed_values получился копией values.
# Переменная transformation должна быть глобальной, чтобы проверяющая система смогла ее найти.
# Кроме transformation вам ничего писать не нужно. Печать на экран - тоже.


#values = [1, 23, 42, "asdfg"]
#transformed_values = list(map(lambda x: x, values))
#if values == transformed_values:
#     print('ok')
#else:
#     print('fail')



# 3 Самая далекая планета

# import math
# def find_farthest_orbit(orb):
#     return max([((math.pi * x[0] * x[1]), x) for x in orb if x[0] != x[1]])[1]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


# 4 Вини пух

#def viny_song(song):
#    vowels = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
#    lst = [len(list(filter(lambda x: x in vowels,i))) for i in song.split()]
#    return ('Пам парам','Парам пам-пам')[len(set(lst)) == 1]

#s = 'пара-ра-рам рам-пем-папам па-ра-па-дам'
#s2 = 'пара-ра-рам рам-пем-папам па-ра-па-дам пара-ра-рам рам-пем-папам па-ра-пб-дам'
#s3 = 'пара-ра-рам рам-пем-папам па-ра-па-дам пара-ра-рам рам-пем-папам па-ра-пя-дам'

#print(viny_song(s))
#print(viny_song(s2))
#print(viny_song(s3))



# 5 Задача Все равны как на подбор
#def same_by(characteristic, val):
#     r = list(map(characteristic, val))
#     if len(set(r)) == 1 and r[0] == 0:
#         return True
#     else:
#         return False

#value = [0, 2, 10, 6]
#value = list(range(1, 5))
#if same_by(lambda x: x % 2, value):
#     print('same')
#else:
#     print('different')   