import time

tiempo = 0

tiempo = int(input("Escriba cuantos segundos quieres cronometrar (Ten en cuenta que deben ser positivos y enteros)\n"))

while tiempo > 0:
    print (tiempo)
    tiempo -=1
    time.sleep(1)

print("La cuenta atras ha finalizado")

input("Pulse cualquier enter para cerrar el programa")