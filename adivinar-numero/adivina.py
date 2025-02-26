import random

def generarRandom(maximo):
  maximo = int(maximo)
  aleatorio = int(random.random() * maximo)
  print(str(aleatorio))
  return (aleatorio)

def comprobarNumero(aleatorio, respuestaUsuario):
  if(respuestaUsuario == aleatorio): return True
  else: return False

numeroIntentos = 5
maximo = int(input("Dime el número máximo: "))
acierto = False
index = 0
numeroAleatorio = generarRandom(maximo)
while(acierto != True and numeroIntentos > 0):
  numero = int(input("Intento numero " + str(index + 1) + "," + "digame un numero: "))
  if(comprobarNumero(numeroAleatorio, numero) == True):
    acierto = True
  else:
    if(numero > numeroAleatorio): print("menor")
    else: print("mayor") 
  numeroIntentos -= 1
  index += 1
if(acierto == True):
  print("Enhorabuena! Has acertado el numero!")
else: print("Eres un pringado, te has quedado sin intentos.")