def ordenar(arr1, arr2):

    # Ahora "sumamos" los arreglos
    arr3 = arr1 + arr2
    
    for x in range(len(arr3)):
        for m in range(len(arr3)):
            if arr3[x] < arr3[m]:
                tmp = arr3[x]
                arr3[x] = arr3[m]
                arr3[m] = tmp
  
    print("Lista ordenada")
    print(arr3)
    
        


lista1= [2, 3, 6, 8]
lista2= [1, 4, 9, 10]

ordenar(lista1, lista2)