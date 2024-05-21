import pygame

class Button():
      def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color


      def draw(self, screen):
            pygame.draw.rect(screen, self.x, self.y, self.width, self.height)
            

            # botonRegreso = pygame.image.load("Imagenes//BotonRegreso.png")  #Agregando Imagen representativa de botón de regreso
            # botonRegreso = pygame.transform.scale(botonRegreso, (40, 40))  #Ajustando el tamaño
            # posicionBotonRegreso = screen.blit(botonRegreso, (10, 10))  #Visualizar la imagen con su posición
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