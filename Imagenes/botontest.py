import pygame
from pygame import *
import sys
# from buttons import *

pygame.init()

screenSize = (950, 700)  #Definiendo tamaño de ventana
tipografia = font.SysFont("Helvetica", 30, bold=True)  #Tipografía
clock=pygame.time.Clock()

#-------------ventana principal del editor---------------------
screen = pygame.display.set_mode(screenSize)  #Creando Ventana
fondoVentanaPrincipal = pygame.image.load("Imagenes//PICSART Fondo.png")  #Agregando fondo de pantalla principal
screen.blit(fondoVentanaPrincipal, (0, 0))  #Visualizar el fondo

#===================== test crear botones==========

class Button():
      def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color


      def draw(self, screen):
            pygame.draw.rect(screen, self.x, self.y, self.width, self.height)
            

      def clicked(self, position):
            x, y = position

            if not (x>=self.x and x<=self.x+self.width):
                  return False
            if not (y>=self.y and y<=self.y+self.height):
                  return False
            return True

botones=[
      Button(10,10, 50, 50, (0,0,0)), 
      Button(100,10, 50, 50, (250,150,150)),
]


def draw(sreen):
      screen.fill((255,255,255))
      for button in botones:
            Button.draw(screen, screen)

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
                  draw(screen)
                  if event.type == pygame.MOUSEBUTTONDOWN:  #Detectar clic del mouse
                        if (event.button == 1):  #Verificar si fue clic izquierdo
                              x, y = event.pos  #Guardando en variables donde se hizo clic


            pygame.display.flip()


main()