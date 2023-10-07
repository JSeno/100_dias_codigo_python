"""
        Conversor de Temperatura
"""
your_choice_text = "Qual tipo de conversão gostaria de fazer?"
your_choice_text_2 = "Escolha uma das opções abaixo:"
your_choice = float(input("Celsius para Farenheit (1)| Celsius para Kevin (2) | Farenheit para Kevin (3): "))
your_temp = float(input("Agora digite a temperatura que deseja converter: "))
if your_choice == 1:
    convert_c_f = (your_temp * 9/5) + 32
    print(f'Sua temperatura em Celsius é: {your_temp}ºC e em Farenheit é {convert_c_f:.2f}ºF')
elif your_choice == 2:
    convert_c_f = your_temp + 273.15
    print(f'Sua temperatura em Celsius é: {your_temp}ºC e em Kevin é {convert_c_f:.2f}ºK')
elif your_choice == 3:
    convert_c_f = (your_temp - 32) * 5/9 + 273.15
    print(f'Sua temperatura em Farenheit é: {your_temp}ºF e em Kevin é {convert_c_f:.2f}ºK')
else:
    print('Escolha inválida!!!')
