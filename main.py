import pygame
from pygame import *
import sys
from botones import *
from editor import *
pygame.init()

screenSize = (950, 700)  #Definiendo tamaño de ventana
clock=pygame.time.Clock() #Definiendo refrescamiento de ventana

# ------------- Ventana principal del editor ---------------------
screen = pygame.display.set_mode(screenSize)  #Creando Ventana
fondoVentanaPrincipal = pygame.image.load("Imagenes//PICSART Fondo.png")  #Agregando fondo de pantalla principal
screen.blit(fondoVentanaPrincipal, (0, 0))  #Visualizar el fondo

# ----- Variables generales ----
listaBotonesColores=crearColores(posiciones_colores)

# ---- Instancia del editor ----
editor1 = Editor(screen, 80, 8, colores, screenSize, posiciones_colores)

# ---- Funcion principal que maneja el programa ----
def main():
      menu, editorpantalla, pantallaAscii, pantallaMatriz = True, False, False, False
      clock.tick(60)
      while True:
            # ---- Bucle de Ventana Principal ----
            if menu:
                  screen.blit(fondoVentanaPrincipal, (0, 0))  #Visualizar el fondo
                  boton_Inicio.blitImage() # Colocando imagen de boton inicio
                  if boton_Inicio.collision(): # Verificacion de colision con boton inicio
                        menu, editorpantalla= False, True

            # ---- Bucle de Ventana editor ----
            if editorpantalla:
                  screen.fill((255,255,255)) # Poniendo la pantalla en blanco
                  editor1.dibujar_cuadricula() # Dibujando la cuadricula
                  for boton in listaBotonesAcciones: # Creando los botones con imagenes
                        boton.blitImage()
                  
                  for x, boton in enumerate(listaBotonesColores): # Creando los botones de colores
                        boton.buttonColor(colores[x]) 

                  # ---- Verificando posibles colisiones con las distintas funciones del editor ----
                  if boton_Regreso.collision():
                        menu, editorpantalla = True, False
                  if boton_RotarIz.collision():
                        editor1.rotar_Derecha()
                  if boton_RotarDer.collision():
                        editor1.rotar_Izquierda()
                  if boton_ZoomIn.collision():
                        editor1.zoomIn()
                  if boton_ZoomOut.collision():
                        editor1.zoomOut()
                  if boton_Guardar.collision():
                        editor1.guardar()
                  if boton_Cargar.collision():
                        editor1.abrirImagen()
                  if boton_Borrar.collision():
                        editor1.borrar()
                  if boton_Limpiar.collision():
                        editor1.limpiar_cuadricula()
                  if boton_InvHorizontal.collision():
                        editor1.rotar_InvHor()
                  if boton_InvVertical.collision():
                        editor1.rotar_InvVert()
                  if boton_AltoContraste.collision():
                        editor1.alto_contraste()
                  if boton_Negativo.collision():
                        editor1.negativo()
                  if boton_Numerico.collision():
                        editorpantalla, pantallaMatriz= False, True
                  if boton_Ascii.collision():
                        editorpantalla, pantallaAscii= False, True
      
            # ------ cambiar a la pantalla que muestra el ascii art -----
            if pantallaAscii:
                  screen.fill((255,255,255))
                  boton_Regreso.blitImage()
                  editor1.transformarAscii()
                  if boton_Regreso.collision():
                        editorpantalla, pantallaAscii = True, False
            
            # ------ cambiar a la pantalla que muestra la matriz numerica -----
            if pantallaMatriz:
                  screen.fill((255,255,255))
                  boton_Regreso.blitImage()
                  editor1.mostrarMatriz()
                  if boton_Regreso.collision():
                        editorpantalla, pantallaMatriz = True, False
                        
            # ---- Manejo de evento en pygame -----
            for event in pygame.event.get():  # Iterando sobre eventos
                  if event.type == pygame.QUIT:  # Si el usuario intenta cerrar ventana
                        pygame.quit()  # Saliendo del juego
                        sys.exit()
                  if event.type == pygame.MOUSEMOTION:  # Detectar movimiento del mouse
                        if pygame.mouse.get_pressed()[0]:
                              editor1.actualizar_color_cuadricula()
            
            pygame.display.flip()

#llamada a la funcion main
if __name__== '__main__':
      main()