import os
import pickle
import random
import sys
import tkinter as tk
from time import sleep
from tkinter import filedialog

import pygame
import pygame.time
from pygame import *

pygame.init()  #Iniciando la librería

sizeScreen = (950, 700)  #Definiendo tamaño de ventana
tipografia = font.SysFont("Helvetica", 30, bold=True)  #Tipografía

# ---- Definiendo colores ----
colores = [
    pygame.Color("#E6E3E3"),pygame.Color("#FFE73A"), pygame.Color("#FF9F3A"), pygame.Color("#FF3A3A"),
    pygame.Color("#FF3AC9"), pygame.Color("#73FF3A"), pygame.Color("#3AFFD8"), pygame.Color("#3A3DFF"),
    pygame.Color("#943AFF"), pygame.Color("#000000"), pygame.Color("#FFFFFF")
]
color_seleccionado = 0

# ---- Definiendo posiciones específicas para los colores ----
posiciones_colores = [
    (50, 50), (100, 50), (50, 130), (100, 130), (50, 210),
    (100, 210), (50, 290), (100, 290), (50, 370), (100, 370)
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
    botonASCII = pygame.image.load("Imagenes//asccimoment.jpg")  #Agregando Imagen representativa de botón de ASCII Art
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
colores_celdas = []
def screenEditor():
    global color_seleccionado, colores_celdas
    ventanaEditor = pygame.display.set_mode(sizeScreen)  # Creando Ventana
    ventanaEditor.fill("#FFFFFF")  # Agregando color de fondo
    ventanaEditorStatus = True

    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  # Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (30, 30))  # Ajustando el tamaño
    posicionBotonRegreso = ventanaEditor.blit(botonRegreso, (10, 10))  # Visualizar la imagen con su posición

    # ---- Botón de Rotación Derecha ----
    botonRotarDer = pygame.image.load("Imagenes//rot-der.png")  # Agregando Imagen representativa de botón de rotación derecha
    botonRotarDer = pygame.transform.scale(botonRotarDer, (45, 45))  # Ajustando el tamaño
    posicionBotonRotarDerecha = ventanaEditor.blit(botonRotarDer, (805, 130))  # Visualizar la imagen con su posición

    # ---- Botón de Rotación Izquierda ----
    botonRotarIz = pygame.image.load("Imagenes//rot-iz.png")  # Agregando Imagen representativa de botón de rotación izquierda
    botonRotarIz = pygame.transform.scale(botonRotarIz, (45, 45))  # Ajustando el tamaño
    posicionBotonRotarIzquierda = ventanaEditor.blit(botonRotarIz, (855, 130))  # Visualizar la imagen con su posición

    # ---- Botones de zoom ----
    botonZoomIn = pygame.image.load("Imagenes//zoomIn.png")  # Agregando Imagen representativa de botón de zoom in
    botonZoomIn = pygame.transform.scale(botonZoomIn, (45, 45))  # Ajustando el tamaño
    posicionbotonZoomIn = ventanaEditor.blit(botonZoomIn, (805, 210))

    botonZoomOut = pygame.image.load("Imagenes//zoomOut.png")  # Agregando Imagen representativa de botón de zoom out
    botonZoomOut = pygame.transform.scale(botonZoomOut, (45, 45))  # Ajustando el tamaño
    posicionbotonZoomOut = ventanaEditor.blit(botonZoomOut, (855, 210))

    # ---- Boton de guardar ----
    botonGuardar = pygame.image.load("Imagenes//BotonGuardar.png")  # Agregando Imagen representativa de botón de guardar
    botonGuardar = pygame.transform.scale(botonGuardar, (47, 47))  # Ajustando el tamaño
    posicionbotonGuardar = ventanaEditor.blit(botonGuardar, (855, 50))
    
    # ---- Boton de cargar imágen ----
    botonCargar = pygame.image.load("Imagenes//Upload.png")  # Agregando Imagen representativa de botón de cargar
    botonCargar = pygame.transform.scale(botonCargar, (43, 43))  # Ajustando el tamaño
    posicionbotonCargar = ventanaEditor.blit(botonCargar, (805, 50))
    
    # ---- Boton de borrador ----
    botonBorrar = pygame.image.load("Imagenes//borrador.png")  # Agregando Imagen representativa de botón de borrar
    botonBorrar = pygame.transform.scale(botonBorrar, (45, 45))  # Ajustando el tamaño
    posicionbotonBorrar = ventanaEditor.blit(botonBorrar, (805, 290))
    
    # ---- Boton de limpieza ----
    botonLimpiar = pygame.image.load("Imagenes//limpieza.png")  # Agregando Imagen representativa de botón de limpiar
    botonLimpiar = pygame.transform.scale(botonLimpiar, (45, 45))  # Ajustando el tamaño
    posicionbotonLimpiar = ventanaEditor.blit(botonLimpiar, (855, 290))
    
    # ---- Boton para invertir horizontalmente ----
    botonInvhorizontal = pygame.image.load("Imagenes//InvHorizontal.png")  # Agregando Imagen representativa de botón de invertir horizontalmente
    botonInvhorizontal = pygame.transform.scale(botonInvhorizontal, (45, 45))  # Ajustando el tamaño
    posicionbotonInvhorizontal = ventanaEditor.blit(botonInvhorizontal, (805, 370))
    
    # ---- Boton para invertir verticalmente ----
    botonInvvertical = pygame.image.load("Imagenes//InvVertical.png")  # Agregando Imagen representativa de botón de invertir verticalmente
    botonInvvertical = pygame.transform.scale(botonInvvertical, (45, 45))  # Ajustando el tamaño
    posicionbotonInvvertical = ventanaEditor.blit(botonInvvertical, (855, 370))
    
    # ---- Boton para el alto contraste ----
    botonAltoContraste = pygame.image.load("Imagenes//altocontraste.png")  # Agregando Imagen representativa de botón de alto contraste
    botonAltoContraste = pygame.transform.scale(botonAltoContraste, (45, 45))  # Ajustando el tamaño
    posicionbotonAltoContraste = ventanaEditor.blit(botonAltoContraste, (805, 450))
    
    # ---- Boton para el negativo ----
    botonNegativo = pygame.image.load("Imagenes//negativo.png")  # Agregando Imagen representativa de botón de negativo
    botonNegativo = pygame.transform.scale(botonNegativo, (45, 45))  # Ajustando el tamaño
    posicionbotonNegativo = ventanaEditor.blit(botonNegativo, (855, 450))

    # ---- Dibujando paleta de colores ----
    def dibujar_paleta(ventana, colores, posiciones):
        for i, pos in enumerate(posiciones):
            pygame.draw.rect(ventana, colores[i], (*pos, 40, 40))
            if i == color_seleccionado:
                pygame.draw.rect(ventana, (0, 0, 0), (*pos, 40, 40), 2)

    # ---- Función para dibujar la cuadrícula ----
    def dibujar_cuadricula(ventana, num_celdas, tamaño_celda, offset_x, offset_y, colores_celdas):
        for i in range(num_celdas):
            for j in range(num_celdas):
                if i < len(colores_celdas) and j < len(colores_celdas[i]):  # Verificando si el índice está dentro de los límites
                    x1 = offset_x + i * tamaño_celda
                    y1 = offset_y + j * tamaño_celda
                    color = colores_celdas[j][i]
                    pygame.draw.rect(ventana, color, (x1, y1, tamaño_celda, tamaño_celda))
                    pygame.draw.rect(ventana, pygame.Color("#000000"), (x1, y1, tamaño_celda, tamaño_celda), 1)

    # ---- Función para rotar la cuadrícula a la derecha ----
    def rotar_cuadricula_derecha(matriz):
        return [list(reversed(col)) for col in zip(*matriz)]

    # ---- Función para rotar la cuadrícula a la izquierda ----
    def rotar_cuadricula_izquierda(matriz):
        return rotar_cuadricula_derecha(rotar_cuadricula_derecha(rotar_cuadricula_derecha(matriz)))
    
    # ---- Lista para guardar las matrices de colores de todas las imágenes guardadas ----
    matrices_guardadas = []
    
    # ---- Función para guardar la matriz de colores en el archivo ----
    def guardar_imagen(matriz_colores):
        matrices_guardadas.append(matriz_colores) # Agregando la matriz de colores a la lista de matrices guardadas
        with open("imagenes_guardadas.pkl", "wb") as f: # Guardando todas las matrices de colores en un solo archivo
            pickle.dump(matrices_guardadas, f)
            
    # ---- Función para cargar la matriz de colores desde el archivo ----
    def cargar_imagen():
        nombre_archivo = filedialog.askopenfilename(filetypes=[("Archivos de imágenes", "*.pkl")]) # Permitir al usuario seleccionar un archivo guardado
        if nombre_archivo:
            with open(nombre_archivo, "rb") as f: # Cargar la matriz de colores desde el archivo seleccionado
                matriz_colores = pickle.load(f)
            return matriz_colores # Usar la matriz de colores cargada para la edición
        else:
            return None
    
    # ---- Función del borrador ----
    def seleccionar_color_blanco():
        global color_seleccionado
        color_seleccionado = 10
    
    # ---- Función para limpiar la matriz ----
    def limpiar_matriz():
        global colores_celdas
        colores_celdas = [[("#FFFFFF") for _ in range(num_celdas)] for _ in range(num_celdas)]  #Restablecer a todos los blancos
    
    # ---- Función para invertir la matriz verticalmente ----
    def invertir_vertical():
        global colores_celdas
        colores_celdas = colores_celdas[::-1]
    
    # ---- Función para invertir la matriz horizontalmente ----
    def invertir_horizontal():
        global colores_celdas
        colores_celdas = [fila[::-1] for fila in colores_celdas]
        
    # ---- Función para aplicar alto contraste ----
    def alto_contraste(matriz):
        num_celdas = len(matriz)
        for i in range(num_celdas):
            for j in range(num_celdas):
                color_actual = matriz[i][j]
                # Verificar si el color actual está en el rango del alto contraste (índices 0-4)
                if color_actual in colores[:5]:
                    matriz[i][j] = colores[0] # Si está en el rango, convertirlo al color del índice 0
                # Verificar si el color actual está en el rango del alto contraste (índices 5-9)
                elif color_actual in colores[5:10]: # Si está en el rango, convertirlo al color del índice 9
                    matriz[i][j] = colores[9]

    # ---- Función para aplicar el negativo ----
    def negativo(matriz):
        num_celdas = len(matriz)
        for i in range(num_celdas):
            for j in range(num_celdas):
                color_actual = matriz[i][j]
                # Verificar si el color actual está en la lista de colores y no es el color del borrador
                if color_actual in colores[:10]:
                    indice_color = colores.index(color_actual)
                    indice_invertido = 9 - indice_color # Calculando el índice invertido
                    matriz[i][j] = colores[indice_invertido] # Asignando el nuevo color basado en el índice invertido
                elif color_actual == colores[10]:
                    continue # Si es el color del borrador, no hacer nada

    # ---- Configuración inicial de la cuadrícula ----
    num_celdas = 80
    tamaño_celda = 8
    offset_x = (sizeScreen[0] - num_celdas * tamaño_celda) // 2  # Centrar horizontalmente
    offset_y = (sizeScreen[1] - num_celdas * tamaño_celda) // 2  # Centrar verticalmente
    colores_celdas = [[("#FFFFFF") for _ in range(num_celdas)] for _ in range(num_celdas)]  # Inicialmente todas las celdas blancas

    # ---- Bucle de Ventana Editor ----
    while ventanaEditorStatus:
        for event in pygame.event.get():  # Iterando sobre eventos
            if event.type == pygame.QUIT:  # Si el usuario intenta cerrar ventana
                pygame.quit()  # Saliendo del juego
                sys.exit()
            if event.type == pygame.MOUSEMOTION:  # Detectar movimiento del mouse
                if pygame.mouse.get_pressed()[0]:  # Verificar si el botón izquierdo del mouse está presionado
                    x, y = event.pos  # Guardar la posición del mouse

                    # ---- Verificar si el mouse está dentro de la cuadrícula ----
                    if offset_x <= x < (offset_x + num_celdas * tamaño_celda) and offset_y <= y < (offset_y + num_celdas * tamaño_celda):
                        celda_x = (x - offset_x) // tamaño_celda
                        celda_y = (y - offset_y) // tamaño_celda
                        colores_celdas[celda_y][celda_x] = colores[color_seleccionado]

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, pos in enumerate(posiciones_colores):
                    if pos[0] <= x < pos[0] + 40 and pos[1] <= y < pos[1] + 40:
                        color_seleccionado = i
                if posicionBotonRegreso.collidepoint(x, y):
                    ventanaEditorStatus = False
                    screenPrincipal()
                elif posicionBotonRotarDerecha.collidepoint(event.pos):
                    colores_celdas = rotar_cuadricula_derecha(colores_celdas)
                elif posicionBotonRotarIzquierda.collidepoint(event.pos):
                    colores_celdas = rotar_cuadricula_izquierda(colores_celdas)
                elif posicionbotonZoomIn.collidepoint(event.pos):
                    tamaño_celda = int(tamaño_celda * 1.4)
                elif posicionbotonZoomOut.collidepoint(event.pos):
                    tamaño_celda = int(tamaño_celda * 0.8)
                elif posicionbotonGuardar.collidepoint(event.pos):
                    guardar_imagen(colores_celdas)
                    print("Imagen guardada correctamente")
                elif posicionbotonCargar.collidepoint(event.pos):
                    matriz_cargada = cargar_imagen()
                    if matriz_cargada:
                        colores_celdas = matriz_cargada
                    else:
                        print("No se seleccionó ninguna imagen")
                elif posicionbotonBorrar.collidepoint(event.pos):
                    seleccionar_color_blanco()  #Borra pixel por pixel
                elif posicionbotonLimpiar.collidepoint(event.pos):
                    limpiar_matriz()  #Limpia la matriz al hacer clic en el botón de limpieza
                elif posicionbotonInvvertical.collidepoint(event.pos):
                    invertir_vertical()  # Invierte la matriz verticalmente al hacer clic en el botón correspondiente
                elif posicionbotonInvhorizontal.collidepoint(event.pos):
                    invertir_horizontal()  # Invierte la matriz horizontalmente al hacer clic en el botón correspondiente
                elif posicionbotonAltoContraste.collidepoint(event.pos):
                    alto_contraste(colores_celdas)
                elif posicionbotonNegativo.collidepoint(event.pos):
                    negativo(colores_celdas)

                    # ---- Verificar si el clic fue dentro de alguno de los botones de la paleta de colores ----
                    for i, pos in enumerate(posiciones_colores):
                        if pos[0] <= x < pos[0] + 40 and pos[1] <= y < pos[1] + 40:
                            color_seleccionado = i
                            print(colores_celdas)

        # ---- Redibujando la cuadrícula y la paleta en cada iteración del bucle ----
        ventanaEditor.fill("#FFFFFF")
        dibujar_cuadricula(ventanaEditor, num_celdas, tamaño_celda, offset_x, offset_y, colores_celdas)
        dibujar_paleta(ventanaEditor, colores, posiciones_colores)  # Paleta de colores en posiciones específicas
        ventanaEditor.blit(botonRegreso, (5, 5))
        ventanaEditor.blit(botonRotarDer, (805, 130))
        ventanaEditor.blit(botonRotarIz, (855, 130))
        ventanaEditor.blit(botonZoomIn, (805, 210))
        ventanaEditor.blit(botonZoomOut, (855, 210))
        ventanaEditor.blit(botonGuardar, (855, 50))
        ventanaEditor.blit(botonCargar, (805, 50))
        ventanaEditor.blit(botonBorrar, (805, 290))
        ventanaEditor.blit(botonLimpiar, (855, 290))
        ventanaEditor.blit(botonInvhorizontal, (805, 370))
        ventanaEditor.blit(botonInvvertical, (855, 370))
        ventanaEditor.blit(botonAltoContraste, (805, 450))
        ventanaEditor.blit(botonNegativo, (855, 450))
        pygame.display.flip()
# ----------------------------------- Finalizando la Ventana Editor ------------------------------------

#---------------------------------- Función que transforma el dibujo en ascii ----------------------------
def screenASCII():
    file = open("guardados.txt", "r")
    matrizGuardada=file.readline()
    file.close()
    print(matrizGuardada)
    ventanaASCII = pygame.display.set_mode(sizeScreen)  #Creando Ventana
    ventanaASCII.fill("#FFFFFF") #Agregando color de fondo
    ventanaASCIIStatus=True

    # ---- Botón de Regreso ----
    botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
    botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
    posicionBotonRegreso = ventanaASCII.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición

    def transfomarASCII(matriz):
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
                        matriz[i][j]='%'
                    if matriz[i][j]==9:
                        matriz[i][j]='@'
        return matriz
    
    matrizASCII=transfomarASCII(matrizGuardada)
    print(matrizASCII)

    # ---- Bucle de Ventana Editor ----
    while ventanaASCIIStatus:
        
        for event in pygame.event.get():  #Iterando sobre eventos
            if event.type == pygame.QUIT:  #Si el usuario intenta cerrar ventana
                pygame.quit()  #Saliendo del juego
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                if (event.button == 1):  #Verificar si fue clic izquierdo
                    x, y = event.pos  #Guardar en variables donde se hizo clic
                    
                    if(posicionBotonRegreso.collidepoint(event.pos)):
                        ventanaASCIIStatus=False
                        screenPrincipal()
        
        # ---- Redibujando la cuadrícula y la paleta en cada iteración del bucle ----
        ventanaASCII.fill("#FFFFFF")
        ventanaASCII.blit(botonRegreso, (10, 10))
        pygame.display.flip()

#-----------------------------------funcion main-----------------------------------------------------------
def main():
    screenPrincipal()
#--------------------------------------------------------------------------------------------------------

#-------------------------------------------while principal------------------------------------------------
while True:
    main()

pygame.quit()