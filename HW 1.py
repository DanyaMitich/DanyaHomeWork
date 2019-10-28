#Поработайте с переменными, создайте несколько,
#выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
#выведите на экран.
first_name = 'Lulu'
age = 18
print('My girlfriend is ' + first_name + ". She is " + str(age))
next_one = input('What is your name?')
new_age = int(input('How old are you?'))
if new_age >= 18:
    print('Nice to meet you')
else:
    print('Oh...ok...bye bye')