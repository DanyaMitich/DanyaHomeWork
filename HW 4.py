#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

num = int(input('Give me your natural number, please'))
i = 1
max = num % 10
check = True
while check == True:
    digit = num // 10**(i) - (num // 10**(i+1))*10
    if digit > max:
        max = digit
    i += 1
    check = (num // 10 ** i > 0)
    continue
print(max)