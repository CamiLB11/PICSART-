import pygame
from pygame import *
import sys
#from buttons import *

pygame.init()

screenSize = (950, 700)  #Definiendo tamaño de ventana
tipografia = font.SysFont("Helvetica", 30, bold=True)  #Tipografía
clock=pygame.time.Clock()

#-------------ventana principal del editor---------------------
screen = pygame.display.set_mode(screenSize)  #Creando Ventana
fondoVentanaPrincipal = pygame.image.load("Imagenes//PICSART Fondo.png")  #Agregando fondo de pantalla principal
screen.blit(fondoVentanaPrincipal, (0, 0))  #Visualizar el fondo

# ---- Botón para comenzar con el editor ----
botonInicio = pygame.image.load("Imagenes//BotonInicio.png")
botonInicio = pygame.transform.scale(botonInicio, (350, 350))
posicionBotonInicio = screen.blit(botonInicio, (320, 335))

#================================Creacion del editor==================
class Editor():
      def __init__(self, pixels) -> None:
            self.matrix=[[pixels for _ in range(pixels)] for _ in range(pixels)]

#=================creacion de los botones====================
class Buttons():
      def __init__(self, x, y, width, height, color) -> None:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color


      def drawButtons(self, screen):
            pygame.draw.rect(screen, self.x, self.y, self.width, self.height)
            

            botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
            botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
            posicionBotonRegreso = screen.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición
            # # ---- Botón de Regreso ----
            # botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
            # botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
            # posicionBotonRegreso = screen.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición

            # # ---- Botón de Rotación ----
            # botonRotar = pygame.image.load("Imagenes//rotacion.png")  #Agregando Imagen representativa de botón de rotación
            # botonRotar = pygame.transform.scale(botonRotar, (45, 45))  #Ajustando el tamaño
            # posicionBotonRotar = screen.blit(botonRotar, (98, 210))  #Visualizar la imagen con su posición
      
      def clicked(self, position):
            x, y = position

            if not (x>=self.x and x<=self.x+self.width):
                  return False
            if not (y>=self.y and y<=self.y+self.height):
                  return False
            return True


buttons=[
      Buttons(100, 50, 50, 50, pygame.Color("#E6E3E3"))
]



def draw(screen):
      screen.fill("#FFFFFF")


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

num_celdas = 80
tamaño_celda = 8
offset_x = (screenSize[0] - num_celdas * tamaño_celda) // 2  #Centrar horizontalmente
offset_y = (screenSize[1] - num_celdas * tamaño_celda) // 2  #Centrar verticalmente
color_blanco = 0  #Índice del color blanco en la lista colores
colores_celdas = [[color_blanco for _ in range(num_celdas)] for _ in range(num_celdas)]

# ---- Definiendo colores ----
colores = [
    pygame.Color("#E6E3E3"),pygame.Color("#FFE73A"), pygame.Color("#73FF3A"), pygame.Color("#3AFFD8"), pygame.Color("#3A3DFF"), 
    pygame.Color("#943AFF"), pygame.Color("#FF3AC9"), pygame.Color("#FF3A3A"), pygame.Color("#FF9F3A"), 
    pygame.Color("#000000")
]
color_seleccionado = 0

# ---- Definiendo posiciones específicas para los colores ----
posiciones_colores = [
    (100, 50), (100, 130), (810, 50), (810, 130),
    (810, 210), (810, 290), (810, 370), (810, 450),
    (810, 530), (810, 610)
]


def main():
      ventanaPrincipalCorriendo, screenEditorCorriendo = True, False
      clock.tick(60)
      while True:
            for event in pygame.event.get():  #Iterando sobre eventos
                        if event.type == pygame.QUIT:  #Si el usuario intenta cerrar ventana
                              pygame.quit()  #Saliendo del juego
                              sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                              if (event.button == 1):  #Verificar si fue clic izquierdo
                                    x, y = event.pos  #Guardar en variables donde se hizo clic
                                    print(x,y)
                              
            # ---- Bucle de Ventana Principal ----
            if ventanaPrincipalCorriendo==True:
                  if event.type == pygame.MOUSEBUTTONDOWN:  #Detectar clic del mouse
                        if (event.button == 1):  #Verificar si fue clic izquierdo
                              x, y = event.pos  #Guardando en variables donde se hizo clic

                        #Verificar si el clic fue dentro de alguno de los botones de la Ventana Principal
                              if posicionBotonInicio.collidepoint(event.pos):
                                    #Botón de Inicio
                                    ventanaPrincipalCorriendo = False 
                                    screenEditorCorriendo = True
                                    print('ventana editor') #Ir a ventana de edición
            
            if screenEditorCorriendo:
                  #Agregando color de fondo
                  draw(screen)
                  dibujar_cuadricula(screen, num_celdas, tamaño_celda, offset_x, offset_y, colores_celdas)
                  # ---- Botón de Regreso ----
                  botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
                  botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
                  posicionBotonRegreso = screen.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición

                  # ---- Botón de Rotación ----
                  botonRotar = pygame.image.load("Imagenes//rotacion.png")  #Agregando Imagen representativa de botón de rotación
                  botonRotar = pygame.transform.scale(botonRotar, (45, 45))  #Ajustando el tamaño
                  posicionBotonRotar = screen.blit(botonRotar, (98, 210))  #Visualizar la imagen con su posición
                  #dibujar_paleta(screen,colores,posiciones_colores )


            pygame.display.flip()


main()
