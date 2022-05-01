# Format values modifcators
""" 
:s - strings
:d - numbers intereger
:f - floats numbers
:.2 - quantication floats characters (exempl: 2)
:(CHARACTER) (> OR < OR ^)(QUANTICATION)(TYPE - s, d OR f)

> - LEFT
< - RIGTH
^ - CENTER
 """

number1 = 123456
number2 = 2
division = number1 / number2
print('{:.2f}'.format(division))
print(f'{division:.2f}')
print(f'{number1:2>5}')