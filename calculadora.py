#!/usr/bin/env python3
def calculadora():
  print('==================')
  print('Operações')
  print('1 - Adição')
  print('2 - Subtração')
  print('3 - Divisão')
  print('4 - Multiplicação')
  print('5 - Porcentagem')
  print('6 - Média')
  print('0 - Sair')
  print('==================')

  while True:
    escolha = input('Escolha uma operação: ')
    if escolha == '0':
      print("Encerrando...")
      break
    if escolha in ('0', '1', '2', '3', '4', '5', '6'):
      num1 = float(input('Digite o primeiro número: '))
      num2 = float(input('Digite o segundo número: '))
      if escolha == '1':
        soma = num1 + num2
        print('A soma é de: ', soma)
      elif escolha == '2':
        sub = num1 - num2
        print('A subtração é de: ', sub)
      elif escolha == '3':
        if num2 == 0:
          print('Não é possivel dividir por 0')
        else:
          div = num1 / num2
        print('A divisão é de: ', div)
      elif escolha == '4':
        multi = num1 * num2
        print('A multiplicação é de: ', multi)
      elif escolha == '5':
        percent = (num1 / num2) * 100
        print('A porcentagem é de: ', percent)
      elif escolha == '6':
        media = (num1 + num2) / 2
        print('A média é de: ', media)
  else:
      print('Opção invalida')

calculadora()
