# Функции и модули
# 💡 Функция — это фрагмент программы, используемый многократно
# Мы знакомы уже с функциями с C#, давайте теперь посмотрим, как создаются и
# используются функции внутри Python.
# def function_name(x):
# # body line 1
# # ...
# # body line n
# # optional return

# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.

# def sum_numbers(n):
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     print(summa)

# sum_numbers(5)

#изменим 
# def sum_numbers(n):
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     return summa

# a=sum_numbers(5)
# print(a)

# def sum_numbers(n):
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     return summa
#     print('stop')

# a=sum_numbers(5)
# print(a)

#представим что мы хотим передать два аргумента

# def sum_numbers(n):
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     return summa

# a=sum_numbers(5,'dfdf') #ошибка типа
# print(a)

#исправим ошибку типа в обратном порядке

# def sum_numbers(n,y):
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     return summa

# a=sum_numbers(5)
# print(a)

#ошибка в том что пропустили

# def sum_numbers(n,y='Hello'):
#     print(y)
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     return summa

# a=sum_numbers(5,'qwerty')
# print(a)

# если никакой аргумент не передаем,то берется по умолчанию,если передаем то переменная будет иметь значения того аргумента которого передали