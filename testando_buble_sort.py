def bubble_sort(lista1): 
    # Loop externo para percorrer toda a lista
    for i in range(0,len(lista1)-1): 
        for j in range(len(lista1)-1): 
            if(lista1[j]>lista1[j+1]): 
                temp = lista1[j] 
                lista1[j] = lista1[j+1] 
                lista1[j+1] = temp 
    return lista1 
 
lista1 = [9, 3, 8, 6, 7, 2] 
print("A lista não ordenada é: ", lista1) 

# Chamando a função de classificação por bolha
print("A lista ordena é: ", bubble_sort(lista1))  