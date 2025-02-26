import csv
import random

def leerPalabras(archivo):
  with open(archivo, mode = 'r', encoding = "utf-8") as file:
    reader = csv.reader(file)
    palabras = next(reader)
  return random.choice(palabras)

archivoCSV = "C:/Users/adrit/Desktop/proyectos/python/ahorcado/palabras.csv"
palabra = leerPalabras(archivoCSV)

print(palabra)
print(palabra)

entradaUsuario = ""

for i in range(len(palabra)):
  entradaUsuario += "_"


fin = False

vida = 3

while (fin == False and vida > 0):
  print(entradaUsuario + "\n")
  letra = input("Di una letra: ")
  if(letra in palabra):
    for i in range(len(palabra)):
      if(letra == palabra[i]): entradaUsuario = entradaUsuario[:i] + letra + entradaUsuario[i + 1:]
  else: 
    vida -= 1
    print(f"Pierdes una vida, te quedan {vida} vidas")
  if(entradaUsuario == palabra): fin = True
print("Ganaste!")

