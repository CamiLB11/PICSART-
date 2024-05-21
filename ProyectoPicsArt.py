import random
import sys
from time import sleep

import pygame
import pygame.time
from pygame import *

pygame.init()  #Iniciando la librería

sizeScreen = (950, 700)  #Definiendo tamaño de ventana
tipografia = font.SysFont("Helvetica", 30, bold=True)  #Tipografía

# ---- Definiendo colores ----
colores = [
    pygame.Color("#E6E3E3"),pygame.Color("#FFE73A"), pygame.Color("#73FF3A"), pygame.Color("#3AFFD8"), pygame.Color("#3A3DFF"), 
    pygame.Color("#943AFF"), pygame.Color("#FF3AC9"), pygame.Color("#FF3A3A"), pygame.Color("#FF9F3A"), 
    pygame.Color("#000000")
]
color_seleccionado = 0

# ---- Definiendo posiciones específicas para los colores ----
posiciones_colores = [
    (100, 50), (100, 130), (50, 50), (50, 130),
    (50, 210), (50, 290), (50, 370), (50, 450),
    (50, 530), (50, 610)
]

# ----------------------------------- Iniciando la Ventana Principal -----------------------------------
def screenPrincipal():
    ventanaPrincipal = pygame.display.set_mode(sizeScreen)  #Creando Ventana
    fondoVentanaPrincipal = pygame.image.load("Imagenes//PICSART Fondo.png")  #Agregando fondo de pantalla principal
    ventanaPrincipal.blit(fondoVentanaPrincipal, (0, 0))  #Visualizar el fondo
    
    # ---- Botón para comenzar con el editor ----
    botonInicio = pygame.image.load("Imagenes//BotonInicio.png")
    botonInicio = pygame.transform.scale(botonInicio, (350, 350))
    posicionBotonInicio = ventanaPrincipal.blit(botonInicio, (320, 335))

       # ---- Boton ASCII art ----
    botonASCII = pygame.image.load("Imagenes//asccimoment.jpg")  #Agregando Imagen representativa de botón de rotación
    botonASCII = pygame.transform.scale(botonASCII, (45, 45))  #Ajustando el tamaño
    posicionbotonASCII = ventanaPrincipal.blit(botonASCII, (98, 510))
    
    # ---- Bucle de Ventana Principal ----
    while True:
        for event in pygame.event.get():  #Iterando sobre eventos
            if event.type == pygame.QUIT:  #Si el usuario intenta cerrar ventana
                pygame.quit()  #Saliendo del juego
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  #Detectar clic del mouse
                if (event.button == 1):  #Verificar si fue clic izquierdo
                    x, y = event.pos  #Guardando en variables donde se hizo clic
                    #Verificar si el clic fue dentro de alguno de los botones de la Ventana Principal
                    if posicionBotonInicio.collidepoint(event.pos):  #Botón de Inicio
                        screenEditor()  #Ir a ventana de edición
                    if posicionbotonASCII.collidepoint(event.pos):#Botón de ASCII
                        screenASCII()
        pygame.display.flip()
# ----------------------------------- Finalizando la Ventana Principal -----------------------------------

# ----------------------------------- Iniciando la Ventana Editor -----------------------------------
def screenEditor():
    global color_seleccionado
    
    ventanaEditor = pygame.display.set_mode(sizeScreen)  #Creando Ventana
    ventanaEditor.fill("#FFFFFF") #Agregando color de fondo
    ventanaEditorStatus=True
    
    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
    posicionBotonRegreso = ventanaEditor.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición

    # ---- Botón de Rotación ----
    botonRotar = pygame.image.load("Imagenes//rotacion.png")  #Agregando Imagen representativa de botón de rotación
    botonRotar = pygame.transform.scale(botonRotar, (45, 45))  #Ajustando el tamaño
    posicionBotonRotar = ventanaEditor.blit(botonRotar, (98, 210))  #Visualizar la imagen con su posición

    # ---- Botones de zoom ----
    botonZoomIn = pygame.image.load("Imagenes//zoomIn.png")  #Agregando Imagen representativa de botón de rotación
    botonZoomIn = pygame.transform.scale(botonZoomIn, (45, 45))  #Ajustando el tamaño
    posicionbotonZoomIn = ventanaEditor.blit(botonZoomIn, (98, 310))

    botonZoomOut = pygame.image.load("Imagenes//zoomOut.png")  #Agregando Imagen representativa de botón de rotación
    botonZoomOut = pygame.transform.scale(botonZoomOut, (45, 45))  #Ajustando el tamaño
    posicionbotonZoomOut = ventanaEditor.blit(botonZoomOut, (98, 410))

    # ---- Boton de guardar ----
    botonGuardar = pygame.image.load("Imagenes//BotonGuardar.png")  #Agregando Imagen representativa de botón de rotación
    botonGuardar = pygame.transform.scale(botonGuardar, (45, 45))  #Ajustando el tamaño
    posicionbotonGuardar = ventanaEditor.blit(botonGuardar, (98, 510))

    # ---- Dibujando paleta de colores ----
    def dibujar_paleta(ventana, colores, posiciones):
        for i, (color, pos) in enumerate(zip(colores, posiciones)):
            pygame.draw.rect(ventana, color, (*pos, 40, 40))
            if (i == color_seleccionado):
                pygame.draw.rect(ventana, pygame.Color("#000000"), (*pos, 40, 40), 2)
    
    # ---- Función para dibujar la cuadrícula ----
    def dibujar_cuadricula(ventana, num_celdas, tamaño_celda, offset_x, offset_y, colores_celdas):
        for i in range(num_celdas):
            for j in range(num_celdas):
                x1 = offset_x + i * tamaño_celda
                y1 = offset_y + j * tamaño_celda
                color = colores[colores_celdas[i][j]]
                pygame.draw.rect(ventana, color, (x1, y1, tamaño_celda, tamaño_celda))
                pygame.draw.rect(ventana, pygame.Color("#000000"), (x1, y1, tamaño_celda, tamaño_celda), 1)
    
    # ---- Función para rotar la cuadrícula ----
    def rotar_cuadricula(matriz):
        return [list(reversed(col)) for col in zip(*matriz)]

    # ---- Variables de la cuadrícula ----
    num_celdas = 80
    tamaño_celda = 8
    offset_x = (sizeScreen[0] - num_celdas * tamaño_celda) // 2  #Centrar horizontalmente
    offset_y = (sizeScreen[1] - num_celdas * tamaño_celda) // 2  #Centrar verticalmente
    color_blanco = 0  #Índice del color blanco en la lista colores
    colores_celdas = [[color_blanco for _ in range(num_celdas)] for _ in range(num_celdas)]
    
    # ---- Bucle de Ventana Editor ----
    while ventanaEditorStatus:
        
        for event in pygame.event.get():  #Iterando sobre eventos
            if event.type == pygame.QUIT:  #Si el usuario intenta cerrar ventana
                pygame.quit()  #Saliendo del juego
                sys.exit()
            if event.type == pygame.MOUSEMOTION:  #Detectar movimiento del mouse
                if pygame.mouse.get_pressed()[0]:  #Verificar si el botón izquierdo del mouse está presionado
                    x, y = event.pos  #Guardar la posición del mouse
                    
                    # ---- Verificar si el mouse está dentro de la cuadrícula ----
                    if offset_x <= x < (offset_x + num_celdas * tamaño_celda) and offset_y <= y < (offset_y + num_celdas * tamaño_celda):
                        celda_x = (x - offset_x) // tamaño_celda
                        celda_y = (y - offset_y) // tamaño_celda
                        colores_celdas[celda_x][celda_y] = color_seleccionado

            if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                if (event.button == 1):  #Verificar si fue clic izquierdo
                    x, y = event.pos  #Guardar en variables donde se hizo clic
                    
                    if(posicionBotonRegreso.collidepoint(event.pos)):
                        ventanaEditorStatus=False
                        screenPrincipal()
                    elif(posicionBotonRotar.collidepoint(event.pos)):
                        colores_celdas = rotar_cuadricula(colores_celdas)
                    elif(posicionbotonZoomIn.collidepoint(event.pos)):
                        tamaño_celda=int(tamaño_celda*1.4)
                    elif(posicionbotonZoomOut.collidepoint(event.pos)):
                        tamaño_celda=int(tamaño_celda*0.8)
                    elif(posicionbotonGuardar.collidepoint(event.pos)):
                        file=open("guardados.txt", "w+")
                        file.write(f"{colores_celdas}")
                        file.close()
                        

                        
                        
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la paleta de colores ----
                    for i, pos in enumerate(posiciones_colores):
                        if pos[0] <= x < pos[0] + 40 and pos[1] <= y < pos[1] + 40:
                            color_seleccionado = i
                            print(colores_celdas)

        # ---- Redibujando la cuadrícula y la paleta en cada iteración del bucle ----
        ventanaEditor.fill("#FFFFFF")
        dibujar_cuadricula(ventanaEditor, num_celdas, tamaño_celda, offset_x, offset_y, colores_celdas)
        dibujar_paleta(ventanaEditor, colores, posiciones_colores)  # Paleta de colores en posiciones específicas
        ventanaEditor.blit(botonRegreso, (10, 10))
        ventanaEditor.blit(botonRotar, (98, 210))
        ventanaEditor.blit(botonZoomIn, (98, 310))
        ventanaEditor.blit(botonZoomOut, (98, 410))
        ventanaEditor.blit(botonGuardar, (98, 510))
        pygame.display.flip()
# ----------------------------------- Finalizando la Ventana Editor ------------------------------------

#----------------------------------funcion que transforma el dibujo en ascii----------------------------
def screenASCII():
    ventanaASCII = pygame.display.set_mode(sizeScreen)  #Creando Ventana
    ventanaASCII.fill("#FFFFFF") #Agregando color de fondo
    ventanaASCIIStatus=True

        # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
    posicionBotonRegreso = ventanaASCII.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición

    # ---- Bucle de Ventana Editor ----
    while ventanaASCIIStatus:
        
        for event in pygame.event.get():  #Iterando sobre eventos
            if event.type == pygame.QUIT:  #Si el usuario intenta cerrar ventana
                pygame.quit()  #Saliendo del juego
                sys.exit()
            if event.type == pygame.MOUSEMOTION:  #Detectar movimiento del mouse
                if pygame.mouse.get_pressed()[0]:  #Verificar si el botón izquierdo del mouse está presionado
                    x, y = event.pos  #Guardar la posición del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                if (event.button == 1):  #Verificar si fue clic izquierdo
                    x, y = event.pos  #Guardar en variables donde se hizo clic
                    
                    if(posicionBotonRegreso.collidepoint(event.pos)):
                        print("Botón de regreso presionado")
                        ventanaEditorStatus=False
                        screenPrincipal()
                        # matrizASCII=transfomarASCII(colores_celdas.copy())
                        # print(matrizASCII)
                    
                    # ---- Verificar si el clic fue dentro de alguno de los botones de la paleta de colores ----
                    for i, pos in enumerate(posiciones_colores):
                        if pos[0] <= x < pos[0] + 40 and pos[1] <= y < pos[1] + 40:
                            color_seleccionado = i
                            

        # ---- Redibujando la cuadrícula y la paleta en cada iteración del bucle ----
        ventanaASCII.fill("#FFFFFF")
        ventanaASCII.blit(botonRegreso, (10, 10))
        pygame.display.flip()

def transfomarASCII(matrix):
    matriz=matrix
    for i in range(len(matriz)):
      for j in range(len(matriz[i])):
            if matriz[i][j]==0:
                  matriz[i][j]=' '
            if matriz[i][j]==1:
                  matriz[i][j]='.'
            if matriz[i][j]==2:
                  matriz[i][j]=':'
            if matriz[i][j]==3:
                  matriz[i][j]='-'
            if matriz[i][j]==4:
                  matriz[i][j]='='
            if matriz[i][j]==5:
                  matriz[i][j]='!'
            if matriz[i][j]==6:
                  matriz[i][j]='&'
            if matriz[i][j]==7:
                  matriz[i][j]='$'
            if matriz[i][j]==8:
                  matriz[i][j]='% '       
            if matriz[i][j]==9:
                  matriz[i][j]='@'
    print(matrix)




#-----------------------------------funcion main-----------------------------------------------------------
def main():
    screenPrincipal()
#--------------------------------------------------------------------------------------------------------

#-------------------------------------------while principal------------------------------------------------
while True:
    main()


pygame.quit()

