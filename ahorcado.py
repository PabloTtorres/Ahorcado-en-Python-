import time
import random

palabras_faciles = ["manzana", "arbol", "mango", "perro", "raton", "control", "banana", "avion"]
palabras_dificiles = ["guanabana", "controlador", "python", "murcielago", "dinosaurio", "marinero", "mineria"]

print("Vamos a jugar Ahorcado")
time.sleep(2)
print("Debes de adivinar la palabra letra por letra")
print("Se te van a otorgar un total de cinco vidas para poder ganar el juego")
time.sleep(3)
print("Si pierdes tus cinco vidas, pierdes automaticamente el juego")
time.sleep(3)
print("Seleccione una categoria, ingrese E para palabras faciles o H para palabras dicifiles")

seleccion = input("Ingrece E o H : ")
while True:

   if seleccion.lower() == "e":
     print("Haz seleccionado la categoria de palabras faciles")
     secreta = random.choice(palabras_faciles)
     break
  
   elif seleccion.lower() == "h":
     print("Haz seleccionado la categoria de palabras dificiles")
     secreta = random.choice(palabras_dificiles)
     break
    
   else:
     print("Elige una categoria valida, por favor")
     seleccion = input("Ingrece E o H : ")

vidas = 5
letra_adiv = []
print("_ " * len(secreta))

while True:

  while True:
   adiv = input("Adivina una letra: ")
   
   if adiv.lower() in letra_adiv:
     print("Ya adivinaste esa letra")

   else:
      letra_adiv.append(adiv)
      
      if adiv in secreta:
        time.sleep(1)
        print("Adivinaste una letra, sigue así")
        break
      
      else: 
        vidas = vidas - 1
        print("Has perdido una vida")
        time.sleep(1)
        print("Dale con calma, esta fácil")
        time.sleep(1)
        print("Te quedan" + " " + str(vidas) + " " + "vidas")
        break
      
  if vidas == 0:
    print("Estas verde maestro, sigue intentando")
    time.sleep(1)
    print("La palabra era " + secreta)
    time.sleep(1)
    print("Intentalo de nuevo! :)")
    break
  a = ""
  falt = 0
  for i in secreta:
    if i in letra_adiv:
      a = a + i

    else:
      a = a + "_" 
      falt = falt + 1

  print(a)

  if falt == 0:
    time.sleep(1)
    print("Ganaste, eres increible!")
    time.sleep(1)
    print("La palabra secreta: " + secreta)
    time.sleep(2)
    print("Gracias por participar!")
    break
