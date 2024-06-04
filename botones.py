import pygame
from pygame import *



pygame.init()
screenSize = (950, 700)  #Definiendo tamaño de ventana
clock=pygame.time.Clock()

#-------------ventana principal del editor---------------------
screen = pygame.display.set_mode(screenSize)  #Creando Ventana




#cargar imagenes de los botones
botonRegreso = pygame.image.load("Imagenes/BotonRegreso.png")
botonInicio = pygame.image.load("Imagenes/BotonInicio.png")
botonRotarDer = pygame.image.load("Imagenes/rot-der.png")
botonRotarIz = pygame.image.load("Imagenes/rot-iz.png")
botonZoomIn = pygame.image.load("Imagenes/zoomIn.png")
botonZoomOut = pygame.image.load("Imagenes/zoomOut.png")
botonGuardar =  pygame.image.load("Imagenes/BotonGuardar.png")
botonCargar = pygame.image.load("Imagenes/Upload.png")
botonBorrar = pygame.image.load("Imagenes/borrador.png")
botonLimpiar = pygame.image.load("Imagenes/limpieza.png")
botonInvhorizontal = pygame.image.load("Imagenes/InvHorizontal.png")
botonInvvertical = pygame.image.load("Imagenes/InvVertical.png")
botonAltoContraste = pygame.image.load("Imagenes/altocontraste.png")
botonNegativo = pygame.image.load("Imagenes/negativo.png")
botonAscii = pygame.image.load("Imagenes/ascii.png")
botonNumerico = pygame.image.load("Imagenes/numeros.jpg")

#===================variables generales de los botones==================#

# ---- Definiendo colores ----
colores = [
    (230,227,227), (255, 231, 58), (255, 159, 58), (255, 58, 58), (255, 58, 201), (115, 255, 58),  (58, 255, 216), 
    (58, 61, 255), (148, 58, 255), (0, 0, 0), (255,255,255)
]
color_seleccionado = 0

# ---- Definiendo posiciones específicas para los colores ----
posiciones_colores = [
    (40, 60), (100, 60), (40, 140), (100, 140), (40, 220),
    (100, 220), (40, 300), (100, 300), (40, 380), (100, 380)
]

#---------------------clase boton
class Boton():
      #---atributos generales de los botones
      def __init__(self, coords, image, scale):
            x = coords[0]
            y = coords[1] 
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

      # ------metodo para pegar imagenes
      def blitImage(self):
            screen.blit(self.image, (self.rect.x,self.rect.y))

      # ------metodo para crear botones de colores
      def buttonColor(self, color):
            pygame.draw.rect(screen, color, self.rect)
            return color

      # ------metodo para verificar colision
      def collision(self):
            #obtener posicion del mouse para verificar colision
            pos= pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                  if pygame.mouse.get_pressed()[0] and self.clicked == False:
                        self.clicked = True
                        return True
                  if pygame.mouse.get_pressed()[0] == False:
                        self.clicked = False


#---------------------funciones para asignar posicion y color a cada boton cuadrado-----------

def crearColores(listaPosicion):
      listaBotonesposiciones=[]
      for i in range(len(listaPosicion)):
            listaBotonesposiciones.append(Boton(listaPosicion[i],botonInicio, 0.1))
      return listaBotonesposiciones
listaBotonesposiciones=crearColores(posiciones_colores)

def crearColores(listaPosicion):
      listaBotonesColores=[]
      for i in range(len(listaPosicion)):
            listaBotonesColores.append(Boton(listaPosicion[i],botonInicio, 0.1))
      return listaBotonesColores


#=============creacion instancias botones=============#
yblit = 50
boton_Inicio = Boton((320, 335), botonInicio, 0.7)
boton_Regreso = Boton((10, 10), botonRegreso, 0.08)

boton_RotarDer = Boton((830, yblit), botonRotarDer, 0.1)
boton_RotarIz = Boton((890, yblit), botonRotarIz, 0.1)

boton_ZoomIn = Boton((835, yblit+75*1), botonZoomIn, 0.17)
boton_ZoomOut = Boton((895, yblit+75*1), botonZoomOut, 0.13)

boton_Guardar = Boton((830, yblit+75*2), botonGuardar, 0.1)
boton_Cargar = Boton((890, yblit+75*2), botonCargar, 0.1)

boton_Borrar = Boton((830, yblit+75*3), botonBorrar, 0.1)
boton_Limpiar = Boton((890, yblit+75*3), botonLimpiar, 0.1)

boton_InvHorizontal = Boton((830, yblit+75*4), botonInvvertical, 0.1)
boton_InvVertical = Boton((890, yblit+75*4), botonInvhorizontal, 0.1)


boton_AltoContraste = Boton((830, yblit+75*5), botonAltoContraste, 0.1)
boton_Negativo = Boton((890, yblit+75*5), botonNegativo, 0.1)


boton_Ascii = Boton((830, yblit+75*6), botonAscii, 0.1)
boton_Numerico = Boton((890, yblit+75*6), botonNumerico, 0.1)

#------- Lista para crear los botones en el main-------
listaBotonesAcciones=[boton_Regreso, boton_RotarDer, boton_RotarIz, boton_ZoomIn, boton_ZoomOut, boton_Guardar, boton_Cargar,
      boton_Borrar, boton_Limpiar, boton_InvHorizontal, boton_InvVertical, boton_AltoContraste, boton_Negativo, boton_Ascii, boton_Numerico]