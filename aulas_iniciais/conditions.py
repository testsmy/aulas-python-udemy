# IF, ELSE, ELIF

name = input('Digite o seu nome: ')
age = int(input('Digite a sua idade: '))
print('Estamos analisando se você pode dirigir...')

if age < 18:
    print('Vixe! Você não pode dirigir boy!')
elif age >= 18 and age <= 60:
    print('Parabéns, você pode dirigir sem restrições')
else:
    print('Legal, você pode dirigir, mas com restrições!')