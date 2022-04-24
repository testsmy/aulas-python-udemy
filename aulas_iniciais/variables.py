#Return IMC Luiz Otavio
name = 'Luiz Otavio'
age = 32
height = 1.80
weight = 85
imc = weight / (height ** 2)

print('O IMC de ', name, ' -> ', imc)  # format 1, whitout rounding
print(f'O nome do usuário é {name}, sua altura é de {height}cm e seu peso é {weight}kg, sendo assim seu IMC é de {imc:.2f}')  # format 2, formatted text and rounding
print('O nome do usuário é {}, sua altura é de {}cm e seu peso é {}kg, sendo assim seu IMC é de {:.2f}'.format(name, height, weight, imc))  # format 3, formatted text other format
print('O nome do usuário é {0}, sua altura é de {1}cm e seu peso é {2}kg, sendo assim o IMC de {0} é {3:.2f}'.format(name, height, weight, imc))  # format 4, numbered positions
print('O nome do usuário é {n}, sua altura é de {hg}cm e seu peso é {wg}kg, sendo assim o IMC de {n} é {i:.2f}'.format(n=name, hg=height, wg=weight, i=imc))  # format 5, named positions