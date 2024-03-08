import os
from biblioteca.conversao_de_temperatura import celsius_to_kelvin, kelvin_to_celsius, kelvin_to_fahrenheit, fahrenheit_to_kelvin, celsius_to_fahrenheit, fahrenheit_to_celsius

#PROGRAMA PRINCIPAL
os.system('cls')
print("----Conversor Térmico----")

#OPÇÃO E TRATANDO OS NUMEROS DE 1 A 6
while True:
        os.system('cls')
        print("\n (1) celsius para fahrenheit\n (2) fahrenheit para celsius\n (3) celsius para kelvin\n (4) kelvin para celsius\n (5) fahrenheit para kelvin\n (6) kelvin para fahrenheit")
        escolha = input("Escolha: ")
        if escolha.isnumeric():
            escolha = int(escolha)
            if escolha >= 1 and escolha <= 6:
                break
            print("Opção invalida")

#QUANTOS °C - RESULTADO DAS CONVERSÕES    
while True:
        
        cod = float(input("\n Por favor, insira o número que deseja: ")) 
        if escolha == 1:
            result = celsius_to_fahrenheit(cod)
            print("O resultado da Conversão é {:.2f} fahrenheit".format(result))
            os.system('pause')
        
        elif escolha == 2:
             result = fahrenheit_to_celsius(cod)
             print("O resultado da Conversão é {:.2f} °C".format(result))
             os.system('pause')
        
        elif escolha == 3:
             result = celsius_to_kelvin(cod)
             print("O resultado da Conversão é {:.2f} kelvin".format(result))
             os.system('pause')

        elif escolha == 4:
             result = kelvin_to_celsius(cod)
             print("O resultado da Conversão é {:.2f} °C".format(result))
             os.system('pause')

        elif escolha == 5:
             result = fahrenheit_to_kelvin(cod)
             print("O resultado da Conversão é {:.2f} Kelvin".format(result))
             os.system('pause')

        else:
             result = kelvin_to_fahrenheit(cod)
             print("O resultado da Conversão é {:.2f} fahrenheit".format(result))   
             os.system('pause')
 