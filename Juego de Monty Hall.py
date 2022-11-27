import random

lista = ["Cabra1","Cabra2","Auto"] #Se crea la lista

def mezclar_lista(lista_original): #Funcion para mezclar la lista
    lista = lista_original[:]
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        indice_aleatorio = random.randint(0, longitud_lista - 1)
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
    return lista

lista_mezclada = mezclar_lista(lista) #Se mezcla la lista

op = 4 #Se elige una opcion (1,2,3)
opciones = [1,2,3]

while op < 1 or op > 3:
  op = int(input("Elige la puerta 1, 2 o 3: "))
  premio_elegido = lista_mezclada[op-1]

while True:
  ran = random.choice(lista_mezclada)
  if ran != premio_elegido and ran != "Auto":
    op_abierta = lista_mezclada.index(ran)
    print("Se abre la puerta {} que contenia una Cabra".format(op_abierta+1))
    lista_mezclada[lista_mezclada.index(ran)] = "Abierta"
    break

opciones.remove(op_abierta+1)

op = "z"
while op != "y" or op != "n" :
  op = input("Desea quedarse con la puerta o quiere cambiar (y/n): ")
  if op == "n":
    if premio_elegido == "Auto":
      print("Usted a ganado el Auto")
    else:
      print("No ha acertado, se ha llevado una Cabra")
    break
  elif op == "y":
    if premio_elegido == "Auto":
      print("No ha acertado, se ha llevado una Cabra")
    else:
      print("Usted a ganado el Auto")
    break