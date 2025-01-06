
from decimal import Decimal

#Trecho para escolher a opção do serviço
op= int(input( 'Entre com a opção desejada: \n 1-Impressão Digital \n 2-Impressão Plotter \n 3-Recorte \n' ))
servico_op = op

#Caso para selecionar impressão Digital
match servico_op:
    case 1:
        print('Impressão Digital')

        op_impressao_papel = int(input('\n 1-Impressão 4x0 - A4 \n 2-Impressão 4x4 - A4  \n 3-Impressão 4x0 - A3 \n 4-Impressão 4x4 - A3  \n Entre com a opção: \n\n' ))
        tipo_de_impressão = op_impressao_papel

        match tipo_de_impressão:
            case 1:
                    print('A4 - 4x0')
                    quantidade_papel_a4_4x0 = int(input('Entre com a quantidade de papel: '))
                    
                    if quantidade_papel_a4_4x0 <= 10:
                            valor_papel_a4_4x0 = quantidade_papel_a4_4x0 * 3.0
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4_4x0:,.2f}')

                    elif quantidade_papel_a4_4x0 >= 11 and quantidade_papel_a4_4x0 <= 30:
                            valor_papel_a4_4x0 = quantidade_papel_a4_4x0 * 2.5
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4_4x0:,.2f}')

                    else:
                            quantidade_papel_a4_4x0 > 31                 
                            valor_papel_a4_4x0 = quantidade_papel_a4_4x0 * 2.0
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4_4x0:,.2f}')

            case 2:
                    print('A4 - 4x4')
                    quantidade_papel_a4_4x4 = int(input('Entre com a quantidade de papel: '))
                    
                    if quantidade_papel_a4_4x4 <= 10:
                            valor_papel_a4_4x4 = quantidade_papel_a4_4x4 * 3.5
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4_4x4:,.2f}')

                    elif quantidade_papel_a4_4x4 >= 11 and quantidade_papel_a4_4x4 <= 30:
                            valor_papel_a4_4x4 = quantidade_papel_a4_4x4 * 3.0
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4_4x4:,.2f}')

                    else:
                            quantidade_papel_a4_4x4 > 31                 
                            valor_papel_a4_4x4 = quantidade_papel_a4_4x4 * 2.5
                            print(f'O valor total de impressão A4 4x0 é R$: {valor_papel_a4_4x4:,.2f}')

            case 3:
                    print('A3 - 4x0')
                    quantidade_papel_a3_4x0 = int(input('Entre com a quantidade de papel: '))
                                
                    if quantidade_papel_a3_4x0 <= 10:
                            valor_papel_a3_4x0 = quantidade_papel_a3_4x0 * 5.5
                            print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3_4x0:,.2f}')

                    elif quantidade_papel_a3_4x0 >= 11 and quantidade_papel_a3_4x0 <= 30:
                            valor_papel_a3_4x0 = quantidade_papel_a3_4x0 * 5.0
                            print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3_4x0:,.2f}')

                    else:
                             quantidade_papel_a3_4x0 > 31                 
                             valor_papel_a3_4x0 = quantidade_papel_a3_4x0 * 4.0
                             print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3_4x0:,.2f}')

            case 4:
                    print('A3 - 4x4')
                    quantidade_papel_a3_4x4 = int(input('Entre com a quantidade de papel: '))
                                
                    if quantidade_papel_a3_4x4 <= 10:
                            valor_papel_a3_4x4 = quantidade_papel_a3_4x4 * 6.0
                            print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3_4x4:,.2f}')

                    elif quantidade_papel_a3_4x4 >= 11 and quantidade_papel_a3_4x4 <= 30:
                            valor_papel_a3_4x4 = quantidade_papel_a3_4x4 * 5.5
                            print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3_4x4:,.2f}')

                    else:
                             quantidade_papel_a3_4x4 > 31                 
                             valor_papel_a3_4x4 = quantidade_papel_a3_4x4 * 4.5
                             print(f'O valor total de impressão A3 4x0 é R$: {valor_papel_a3_4x4:,.2f}')    


                #Caso para entrar com opção do serviço na Plotter

    case 2:
            print('Impressão Plotter')
            op_plotter = int(input('\n 1-Adesivo \n 2-Banner \n 3-Perfurado  \n 4-Papel \n Entre com a opção: \n\n' ))
            servico_1 = op_plotter

            match servico_1:
                case 1:
                    print('Adesivo')
                    altura_adesivo = float(input('Entre com a altura do adesivo em metros: '))
                    largura_adesivo = float(input('Entra com a largura do adesivo em metros: '))

                    tamanho_adesivo = altura_adesivo * largura_adesivo
                    print(f'O tamanho do adesivo é: {tamanho_adesivo} \n')

                    tamanho_m= 1.00

                    if tamanho_adesivo <= tamanho_m:
                          valor_total = 32.0
                          print(f'Tamanho do adesivo entra no valor mínimo R$: {valor_total} \n')

                    else:
                          valor_total = tamanho_adesivo * 32.0
                          print(f'Valor total do adesivo R$: {valor_total:,.2f} \n')
                          

#Caso 2 para calcular valor do Banner 
                      
                case 2:                    
                    altura_lona = float(input('Entre com a altura do banner em metros: '))
                    largura_lona = float(input('Entre com a largura do banner em metros2: '))
                    
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
                        altura_perfurado = float(input('Entre com a altura do Adesivo Perfurado em metro: '))
                        largura_perfurado = float(input('Entre com a largura do Adesivo Perfurado em metro: '))

                        tamanho_perfurado = altura_perfurado * largura_perfurado
                        print(f'\n O tamanho do total do Adesivo Perfurado é: {tamanho_perfurado}' )

                        tamanho_m = 1.00

                        if tamanho_perfurado <= tamanho_m:
                                valor_total = 32.0
                                print(f'Valor do Adesivo Perfurado entra no valor mínino R$: {valor_total}')
                                
                        else:
                                valor_total = tamanho_perfurado * 32.0
                                print(f'O valor total do Adesivo perdurado R$: {valor_total}')

                case 4:
                        print('Papel')
                        altura_papel = float(input('Entre com a altura do Papel em metro: '))
                        largura_papel = float(input('Entre com a largura do Papel em metro: '))
                        
                        tamanho_m = altura_papel * largura_papel
                        print(f'O tamanho total do Papel é: {tamanho_m}' )

                        tamanho_papel_metro = 1.00
                        
                        if tamanho_m <= tamanho_papel_metro:
                                valor_total = 35.0
                                print(f'O valor total do Papel R$: {valor_total:,.2f}')

                        else:
                                valor_total = tamanho_m * 35.00
                                print(f'O valor total do Papel é R$: {valor_total:,.2f}')                      


                                
#Caso 3 para opção de recorte             

    case 3:
            print('Recorte')
            
            op_recorte = int(input('\n 1-Recorte Especial Adesivo \n 2-Recorte Especial Papel \n 3-Corte Reto \n Entre com a opção:'))
            servico_recorte = op_recorte

            match servico_recorte:
                case 1:
                    print('O Valor é R$: 40.00')
                      
                case 2:
                    print('O Valor é R$: 45.00')

                case 3:
                    print('O Valor é R$: 20.00')

