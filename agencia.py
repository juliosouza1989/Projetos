
from decimal import Decimal

#Trecho para escolher a opção do serviço
op= int(input( 'Entre com a opção desejada: \n 1-Impressão Digital \n 2-Impressão Plotter \n 3-Recorte \n' ))
servico_op = op

#Caso para selecionar impressão Digital
match servico_op:
    case 1:
        print('Impressão Digital')
        op_papel = int(input('Escolha o tamanho da folha desejada \n 1-A4 \n 2-A3 \n'))
        tamanho_papel = op_papel

        match tamanho_papel:
            case 1:
                    print('Tamanho A4')
                    quantidade_papel_a4 = int(input('Entre com a quantidade de papel: '))

                    
                    if quantidade_papel_a4 <= 10:
                            valor_papel_a4 = quantidade_papel_a4 * 3.0
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4:,.2f}')

                    elif quantidade_papel_a4 >= 11 and quantidade_papel_a4 <= 30:
                            valor_papel_a4 = quantidade_papel_a4 * 2.5
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4:,.2f}')

                    else:
                            quantidade_papel_a4 > 31                 
                            valor_papel_a4 = quantidade_papel_a4 * 2.0
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4:,.2f}')
            case 2:
                    print('Tamanho A3')
                    quantidade_papel_a3 = int(input('Entre com a quantidade de papel: '))
                                
                    if quantidade_papel_a3 <= 10:
                            valor_papel_a3 = quantidade_papel_a3 * 5.0
                            print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3:,.2f}')

                    elif quantidade_papel_a3 >= 11 and quantidade_papel_a3 <= 30:
                            valor_papel_a3 = quantidade_papel_a3 * 4.5
                            print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3:,.2f}')

                    else:
                             quantidade_papel_a3 > 31                 
                             valor_papel_a3 = quantidade_papel_a3 * 3.5
                             print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3:,.2f}')      

#Caso para entrar com opção do serviço na Plotter

    case 2:
            print('Impressão Plotter')
            op_plotter = int(input('\n 1-Adesivo \n 2-Banner \n 3-Perfurado \n Entre com a opção: '))
            servico_1 = op_plotter

            match servico_1:
                case 1:
                    print('Adesivo')

#Caso 2 para calcular valor do Banner 
                      
                case 2:                    
                    altura_lona = float(input('Entre com a altura do banner em metro: '))
                    largura_lona = float(input('Entre com a largura do banner em metro: '))
                    
                    tamanho = altura_lona * largura_lona
                    print(f'\n O tamanho total do banner é: {tamanho} \n')

                    #condição pra saber se o valor cai no mínimo    
                    tamanho_m = 1.00

                    if tamanho <= tamanho_m:
                        valor_total = 32.0
                        print(f'Valor da lona entra no valor mínino R$: {valor_total}')
                    
                    else:
                        valor_total = tamanho * 32.0
                        print(f'O valor total do Banner R$: {valor_total}')
#Caso 2.3

                case 3:
                        print('Perfurado')
                        altura_perfurado = float(input('Entre com a altura do Adesivo Perfurado: '))
                        largura_perfurado = float(input('Entre com a largura do Adesivo Perfurado: '))

                        tamanho_perfurado = altura_perfurado * largura_perfurado
                        print(f'\n O tamanho do total do Adesivo Perfurado é: {tamanho_perfurado}' )

                        tamanho_m = 1.00
                        if tamanho_perfurado <= tamanho_m:
                                valor_total = 32.0
                                print(f'Valor do Adesivo Perfurado entra no valor mínino R$: {valor_total}')
                                
                        else:
                                valor_total = tamanho_perfurado * 32.0
                                print(f'O valor total do Adesivo perdurado R$: {valor_total}')
                                
#Caso 3 para opção de recorte             

    case 3:
            print('Recorte')
            
            op_recorte = int(input('\n 1-Recorte Especial \n 2-Corte Reto \n Entre com a opção:'))
            servico_recorte = op_recorte

            match servico_recorte:
                case 1:
                    print('O Valor é R$: 40.00')
                      
                case 2:
                    print('O Valor é R$: 20.00')

