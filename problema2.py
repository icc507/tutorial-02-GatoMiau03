#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)

t = input()
t1 = []
for elemento in t.split():
    if elemento.isdigit():  
        t1.append(int(elemento))
    else:
        t1.append(elemento) 
t1_invertida = t1[::-1]
resultado = tuple(t1_invertida)
print(resultado)