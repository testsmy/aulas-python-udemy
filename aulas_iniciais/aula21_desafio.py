name = 'Maria Priscila'
age = 25
height = 1.68
weight = 65.0
year_actual = 2022
year_birth = year_actual - age
imc = weight / (height ** 2)

print(f'Nome: {name}, ano de nascimento: {year_birth}, idade: {age}, altura: {height}, peso: {weight}, IMC: {imc:.2f}')