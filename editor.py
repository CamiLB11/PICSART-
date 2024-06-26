import pygame
from pygame import *
import json
from tkinter import Tk, filedialog



pygame.init()
screenSize = (950, 700)  #Definiendo tamaño de ventana
tipografia = font.SysFont("Arial", 13)  #Tipografía
clock=pygame.time.Clock() #clock de la pantalla

#-------------ventana principal del editor---------------------
screen = pygame.display.set_mode(screenSize)  #Creando Ventana

#----- clase editor---------
class Editor():
      #-------atributos generales-------
      def __init__(self, ventana, num_celdas, tamaño_celda, colores, size_screen, posiciones_colores):
            self.ventana = ventana
            self.num_celdas = num_celdas
            self.tamaño_celda = tamaño_celda
            self.colores = colores
            self.size_screen = size_screen
            self.posiciones_colores = posiciones_colores
            self.offset_x = (size_screen[0] - num_celdas * tamaño_celda) // 1.7
            self.offset_y = (size_screen[1] - num_celdas * tamaño_celda) // 2
            self.color_blanco = 10  # Índice del color blanco en la lista colores
            self.matrix = [[self.color_blanco for _ in range(num_celdas)] for _ in range(num_celdas)]
            self.color_seleccionado = self.color_blanco
            self.matrices_guardadas = []

      # ------metodo para dibujar la cuadricula
      def dibujar_cuadricula(self):
            for i in range(self.num_celdas):
                  for j in range(self.num_celdas):
                        x1 = self.offset_x + i * self.tamaño_celda
                        y1 = self.offset_y + j * self.tamaño_celda
                        color = self.colores[self.matrix[i][j]]
                        pygame.draw.rect(self.ventana, color, (x1, y1, self.tamaño_celda, self.tamaño_celda))
                        pygame.draw.rect(self.ventana, (0,0,0), (x1, y1, self.tamaño_celda, self.tamaño_celda), 1)
      
      # ------metodo para actualizar/pintar el color
      def actualizar_color_cuadricula(self):
            pos= pygame.mouse.get_pos()
            x, y = pos[0], pos[1]
            if self.offset_x <= x < (self.offset_x + self.num_celdas * self.tamaño_celda) and self.offset_y <= y < (self.offset_y + self.num_celdas * self.tamaño_celda):
                  celda_x = int((x - self.offset_x) // self.tamaño_celda)
                  celda_y = int((y - self.offset_y) // self.tamaño_celda)
                  self.matrix[celda_x][celda_y] = self.color_seleccionado
            for i, pos in enumerate(self.posiciones_colores):
                  if pos[0] <= x < pos[0] + 40 and pos[1] <= y < pos[1] + 40:
                        self.color_seleccionado = i
                    
      # ------metodos para rotar la imagen
      def rotar_Derecha(self):
            self.matrix = [list(reversed(col)) for col in zip(*self.matrix)]
            return self.matrix


      def rotar_Izquierda(self):
            self.rotar_Derecha()
            self.rotar_Derecha()
            self.rotar_Derecha()
            return self.matrix
      

      def rotar_InvHor(self):
            self.matrix = self.matrix[::-1]  # Reverse the rows to get the upside-down order
            return self.matrix
      

      def rotar_InvVert(self):
            self.rotar_Derecha()
            self.rotar_Derecha()
            return self.matrix
      
      # ------metodos para cambiar contraste y poner negativo
      def alto_contraste(self):
            for i in range(self.num_celdas):
                  for j in range(self.num_celdas):
                        color_actual = self.matrix[i][j]
                        # Verificar si el color actual está en el rango del alto contraste (índices 0-4)
                        if color_actual in range(5):
                              self.matrix[i][j] = 0  # Si está en el rango, convertirlo al color del índice 0
                        # Verificar si el color actual está en el rango del alto contraste (índices 5-9)
                        elif color_actual in range(5, 10):  # Si está en el rango, convertirlo al color del índice 9
                              self.matrix[i][j] = 9
            return self.matrix
      

      def negativo(self):
            for i in range(self.num_celdas):
                  for j in range(self.num_celdas):
                        color_actual = self.matrix[i][j]
                        if self.colores[color_actual] in self.colores[:10] and not self.colores[color_actual] == self.colores[0]:
                              indice_invertido = 9 - color_actual 
                              self.matrix[i][j] = indice_invertido

      # ------metodos para borrar/limpiar matriz
      def limpiar_cuadricula(self):
            self.matrix = [[self.color_blanco for _ in range(self.num_celdas)] for _ in range(self.num_celdas)]
      

      def borrar(self):
            self.color_seleccionado = 10

      # ------metodos para hacer zoom
      def zoomIn(self):
            self.tamaño_celda *= 1.1 


      def zoomOut(self):
            self.tamaño_celda *= (10/11)

      # ------ Metodos para guardar y abrir imagen ------
      def guardar(self):
            root = Tk()
            root.withdraw()  # Ocultando la ventana principal
            filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if filepath:
                  with open(filepath, 'w') as file:
                        json.dump(self.matrix, file)
                  print(f"Imagen guardada como {filepath}")
            root.destroy()

      def abrirImagen(self):
            root = Tk()
            root.withdraw()  # Ocultando la ventana principal
            filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if filepath:
                  try:
                        with open(filepath, 'r') as file:
                              self.matrix = json.load(file)
                        print(f"Imagen cargada desde {filepath}")
                  except FileNotFoundError:
                        print("No se encontró el archivo.")
                  except json.JSONDecodeError:
                        print("Error al decodificar el archivo.")
            root.destroy()

      # ------ Metodos para mostrar la matriz y transformarla en ascii -----
      def mostrarMatriz(self):
            x,y=75,10
            matrix1 = self.matrix[::-1]
            matrix1 = [list(reversed(col)) for col in zip(*matrix1)]
            for i in range(len(self.matrix)):
                  y+=8
                  x=100
                  for j in range(len(self.matrix)):
                        x+=9
                        if matrix1[i][j]==10:
                              num=tipografia.render(f'{0}', True, (0,0,0))  
                        else:
                              num=tipografia.render(f'{matrix1[i][j]}', True, (0,0,0))
                        screen.blit(num, (x,y))

      def transformarAscii(self):
            x,y=75,10
            matrix1 = self.matrix[::-1]
            matrix1 = [list(reversed(col)) for col in zip(*matrix1)]


            for i in range(len(self.matrix)):
                  y+=8
                  x=100
                  for j in range(len(self.matrix)):
                        x+=9
                        valormatriz=matrix1[i][j]
                        valorAscii=''
                        # ------ comprobacion para asignar valor ascii -----
                        if valormatriz == 0 or valormatriz == 10:
                              valorAscii = ' '
                        if valormatriz == 1:
                              valorAscii = '.'
                        if valormatriz == 2:
                              valorAscii = ':'
                        if valormatriz == 3:
                              valorAscii = '-'
                        if valormatriz == 4:
                              valorAscii = '='
                        if valormatriz == 5:
                              valorAscii = '!'
                        if valormatriz == 6:
                              valorAscii = '&'
                        if valormatriz == 7:
                              valorAscii = '$'
                        if valormatriz == 8:
                              valorAscii = '%'       
                        if valormatriz == 9:
                              valorAscii = '@'
                        ascii=tipografia.render(valorAscii, True, (0,0,0))  
                        screen.blit(ascii, (x,y))
