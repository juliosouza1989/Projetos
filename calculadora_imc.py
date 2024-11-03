#Programa para calcular IMC
from decimal import Decimal

peso = float(input('Entre com seu peso: '))
altura = float(input('Entre com com sua altura: '))

imc = peso / (altura * altura)

print(f'Seu Indice de Massa Corporal é: {imc:.1f}')

#condições para saber qual a situação do seu peso

if imc <= 18.5:    
    print('Você está abaixo do peso')

if imc == 18.6:
    print('Você está com o Peso Normal')

elif imc <= 24.9:
    print('Você está com o Peso Normal')

elif imc == 25.0:   
    print('Você está com Sobrepeso')

elif imc <= 29.9:
    print('Você está com muito acima do peso')

else:
    print('Você está com obesidade')
    