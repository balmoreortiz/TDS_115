# Programa de sistema basado en token
print("\nUNIVERSIDAD DE EL SALVADOR \nFACULTAD DE INGENIERIA Y ARQUITECTURA \nESCUELA DE INGENIERIA EN SISTEMAS INFORMATICOS \nTÉCNICAS DE SIMULACIÓN T.E")
M = int(input("Ingrese número de nodos a simular: ") )

if M <= 4:
    print(M, " nodos a simular ingresados")
elif M > 4:
    print("No puede haver más de diez nodos, M se redondeará a 10")
    M = 4
    print(M, " nodos a simular ingresados")

# ahora tenemos que hacer que se llene un arreglo
# cada posicion será un nodo
arregloDeNodos = []
# ahora llenamos ese arreglo con los números de los nodos
for i in range(M):
    arregloDeNodos.append(i + 1)

print(arregloDeNodos)

