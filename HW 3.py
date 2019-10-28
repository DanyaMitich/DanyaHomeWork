#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

n = int(input('Give me your number between 1 and 9, please '))
number = 3*n + 2*10*n + 100*n
print(f'n + nn + nnn = {number}')