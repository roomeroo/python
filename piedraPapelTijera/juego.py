import random
juego = {"piedra", "papel", "tijera"}

def pedirInput():
  buenaEntrada = False
  while(True):
    entrada = input("Piedra papel o tijera: ").lower
    if(entrada in str):
      return (entrada)
  

def jugarRonda():
  usuario = pedirInput()
  maquina = random.choice(juego)
  if(maquina == usuario): return {0,0}
  elif(maquina == "piedra" and usuario == "tijera"): return{0,1}
  elif(maquina == "piedra" and usuario == "papel"): return{1,0}
  elif(maquina == "papel" and usuario == "tijera"): return{0,1}
  elif(maquina == "papel" and usuario == "piedra"): return{1,0}
  elif(maquina == "tijera" and usuario == "piedra"): return{}