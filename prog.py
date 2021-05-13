while True: """Vamos utilizar o while para repetir a programa"""

    n = int(input('Digite um número: ')) """Aqui o n representa uma variável para armazenar os dados que estamos solicitando. 
INT é para o programa entender que estamos informado a entrada de um número. INPUT para que o usuário possa colocar a informação"""

    print('- - - - '* 5) """PRINT imprime a informação. Quando informo o texto e multiplico (*) por algum valor ele irá repetir a quantidade de vezes que for informado. Exemplo: - - - -- - - -- - - -- - - -- - - - irá aparecer desta forma para o usuário"""
    
    print('[1] Binário') """dentro do parenteses posso utilizar as aspas simples (' ') ou duplas (" ") """
    
    print('[2] Octal')
    print('[3] Hexadecimal')
    print('[x] Sair')
    
    perguntanum = str(input('Digite a opção que deseja converter: ')) """Variavável para armazenar a informação no caso aqui informado como str(string) que é o formato de texto"""
 
    if perguntanum == 'x'or perguntanum == 'X': """ Aqui o comando SE(if) vai validar se o usuário desessa fechar o programa, tem duas opções o X em minusculo e em maiusculo, então essa linha vai validar qual a informação que o usuário inseriu na variável."""
    
        break ""SE o usuário apertou X para fechar. O código será encerrado"""

    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3': """nessa linha do SENÃO vamos validar se o usuário inseriu alguma opção do menu, para que o usuário não insira qualquer número ou letra.
    
        if perguntanum == '1': """ dentro do elif vamos inserir as opções do menu e validar se o que usuário inseriu e uma opção do menu.
        
            rio = str(bin(n)) """bin() método leva um único parâmetro e retornar a string binária equivalente ao inteiro fornecido. Se não for especificado um inteiro, ele levanta uma TypeErrorexceção destacando que o tipo não pode ser interpretado como um inteiro.Observação NÃO colocar o nome da variável de binario como bin, pois o sistema irá entender que se trata do método assim retornando erro'""

            print(rio) """Imprime o resultado da variável"""

        elif perguntanum == '2': 
            cta = str(oct(n)) """oct() método leva um único"""
            print(cta)

        elif perguntanum == '3':
            exa = str(hex(n)) """hex() método leva um único"""
            print(exa)

    else:
        print('Opção invalida!') 
