import random

#Definir colores
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

juego = {"piedra", "papel", "tijera"}

def pedirInput():
  while(True):
    entrada = input("Piedra papel o tijera: ").lower()
    if(entrada in juego):
      return (entrada)
    else: print("Error. Intenta de nuevo")
  

def jugarRonda():
  usuario = pedirInput()
  maquina = random.choice(list(juego))
  print(YELLOW + maquina + RESET)
  if(maquina == usuario): return 0,0
  elif(maquina == "piedra" and usuario == "tijera"): return 0,1
  elif(maquina == "papel" and usuario == "tijera"): return 0,1
  elif(maquina == "tijera" and usuario == "piedra"): return 0,1
  else: return 1,0
  

numeroRondas = 0
puntuacionUsuario = 0
puntuacionMaquina = 0

while(numeroRondas < 3):
  numeroRondas += 1
  puntuacion = jugarRonda()
  puntuacionUsuario += puntuacion[1]
  puntuacionMaquina += puntuacion[0]
  if(int(puntuacion[1]) > 0): print(GREEN +"Ronda para el usuario." + RESET)
  elif(puntuacion[1] == puntuacion[0]): 
    print(YELLOW + "empate, esta ronda no cuenta" + RESET) 
    numeroRondas -= 1
  else: print(RED + "Ronda para la máquina" + RESET)
  print(f"Puntuaciones:\nUsuario {puntuacionUsuario}\nMáquina {puntuacionMaquina}")
if(puntuacionUsuario > puntuacionMaquina): print(GREEN + "Ha ganado el usuario!" + RESET)
else: print(RED + "Ha ganado la máquina!" + RESET)