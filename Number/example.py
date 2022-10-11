
import string
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.ascii_letters)



s = 'text'
M = [i for i in s]
print(M)

A = [i for i in input("Введите числа через пробел: ").split()]  # метод .split() разбивает строку на список сточных элементов
print(A)

res = ', '.join(A)
print(res)


