# POR FAVOR HACER UNA VALIDACION DE NUMEROS ENTEROS SI ESTOS SON PARES O NO
# LA LISTA DE PRUEBA [3,4,5,10,50,30,100,70,75,63,109,1008,42]
# SE DEBE CREAR UNA FUNCION Y DEBE IMPRMIR EL MUEVO DECIR SI ES PAR O NO
# LA FUNCION DEBE DEVOLVER LA CANTDAD DE PARES
def validar_pates(numeros):
    cantidad_pares = 0 
    for num in numeros:
        if num % 2 ==0:
            print(f"{num}es par")
            cantidad_pares += 1
        else: 
            print(f"{num} es part")
    return cantidad_pares
