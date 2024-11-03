
from decimal import Decimal

#Trecho para escolher a opção do serviço
op = int(input( 'Entre com a opção desejada: \n 1-Impressão Digital \n 2-Impressão Plotter \n 3-Recorte \n' ))

servico = op
match servico:
        case 1:
            print('Impressão Digital')             
            quantidade_papel = int(input('Entre com a quantidade de impressão: '))

            if quantidade_papel >= 10:
                 valor_papel = quantidade_papel * 6.0
                 
            else:          
                valor_papel = quantidade_papel * 8.0
            print(f'O valor total de impressão é R$: {valor_papel:,.2f}')
        
        case 2:
            print('Impressão Plotter')
            op_p = int(input('\n 1-Adesivo \n 2-Banner \n 3-Perfurado \n Entre com a opção: '))
            servico_1 = op_p

            match servico_1:
                case 1:
                    print('Adesivo')
#Caso 2
                      
                case 2:                    
                    altura_lona = float(input('Entre com a altura do banner em metro: '))
                    largura_lona = float(input('Entre com a largura do banner em metro: '))
                    
                    tamanho = altura_lona * largura_lona
                    print(f'\n O tamanho total do banner é: {tamanho} \n')

                    #condição pra saber se o valor cai no mínimo    
                    tamanho_m = 1.00
                    if tamanho <= tamanho_m:
                        valor_total = 40.0
                        print(f'Valor da lona entra no valor mínino R$: {valor_total}')
                    
                    else:
                        valor_total = tamanho * 40.0
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
                                valor_total = 40.0
                                print(f'Valor do Adesivo Perfurado entra no valor mínino R$: {valor_total}')
                                
                        else:
                                valor_total = tamanho_perfurado * 40.0
                                print(f'O valor total do Adesivo perdurado R$: {valor_total}')
#Caso 3               

        case 3:
            print('Recorte')
            
            op_r = int(input('\n 1-Recorte Especial \n 2-Corte Reto \n Entre com a opção:'))
            servico_recorte = op_r

            match servico_recorte:
                case 1:
                    print('O Valor é R$: 40.00')
                      
                case 2:
                    print('O Valor é R$: 20.00')
                    
