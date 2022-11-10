#esto será utilizado para obtener la posición y el color de ciertas áreas en la pantalla 

import pyautogui as pt
from time import sleep 

while True: #wh
    position_XY = pt.position() #Nos dice la posición del puntero 
    print (position_XY, pt.pixel(position_XY[0], position_XY[1])) #imprimimos la posición y el color 
    sleep (1) #como es un bucle infinito, le ponemos un retraso de 1 sec 
    if position_XY[0] == 0: #condición para salir del bucle 
        break

