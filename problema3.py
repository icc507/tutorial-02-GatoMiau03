#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
def insertar_trinario(arbol, valor):
    if not arbol:
        return [valor, [], [], []]
    if valor < arbol[0]:
        arbol[1] = insertar_trinario(arbol[1], valor)
    elif valor > arbol[0]:
        arbol[3] = insertar_trinario(arbol[3], valor)
    else:
        arbol[2] = insertar_trinario(arbol[2], valor)
    return arbol
t = input()
numeros = map(int, t.split())

arbol_trinario = []
for numero in numeros:
    arbol_trinario = insertar_trinario(arbol_trinario, numero)

print(arbol_trinario)
