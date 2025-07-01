# Made By Byron Serrano
import pygame
import os

from glapp.Utils import create_program
from glapp.PyOGLApp import *
from glapp.Material import *

# from glapp.Cube import *
from glapp.LoadMesh import *
from glapp.Light import *
from glapp.Axes import *


# Obtener la ruta absoluta del directorio actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def join_path(object1, object2):
    return os.path.join(BASE_DIR, object1, object2)

class TexturedObjects(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 600)
        self.lights = []
        self.plane_textured = None
        self.plane_colored = None
        self.show_texture = True
        self.light_pos = pygame.Vector3(-2, 2, 0)
        self.material_textured = None
        self.material_untextured = None
        self.key_pressed = False  # Para evitar múltiples cambios por una presión

        glEnable(GL_CULL_FACE)

    def initialise(self):
        # Print de controles disponibles
        print("=" * 60)
        print("CONTROLES DEL PROGRAMA - TEXTURED OBJECTS")
        print("=" * 60)
        print("CÁMARA:")
        print("  W/A/S/D       - Mover cámara (adelante/izquierda/atrás/derecha)")
        print("  Mouse         - Rotar vista de la cámara")
        print("  ESC           - Liberar mouse (mostrar cursor)")
        print("  SPACE         - Capturar mouse (ocultar cursor)")
        print()
        print("ILUMINACIÓN:")
        print("  ↑ (UP)        - Mover luz hacia arriba")
        print("  ↓ (DOWN)      - Mover luz hacia abajo")
        print("  ← (LEFT)      - Mover luz hacia la izquierda")
        print("  → (RIGHT)     - Mover luz hacia la derecha")
        print()
        print("TEXTURAS:")
        print("  T             - Alternar entre textura ON/OFF")
        print()
        print("OBJETOS:")
        print("  - Plano con textura de tierra seca")
        print("  - Ejes de coordenadas (X=rojo, Y=verde, Z=azul)")
        print("=" * 60)
        print()

        self.material_textured = Material(join_path("shaders", "texturedvert.vs"), join_path("shaders", "texturedfrag.vs"))
        self.material_untextured = Material(join_path("shaders", "texturedvert.vs"), join_path("shaders", "texturedfrag.vs"))
        
        axesmat = Material(join_path("shaders", "vertexcolvert.vs"), join_path("shaders", "vertexcolfrag.vs"))
        self.axes = Axes(pygame.Vector3(0, 0, 0), axesmat)

        # Crear dos planos con diferentes texturas
        self.plane_textured = LoadMesh(
                    join_path("models", "plane.obj"), 
                    join_path("images", "tierra_seca.jpg"),
                    location=pygame.Vector3(0, -0.5, 0),
                    material=self.material_textured)

        # Para el plano sin textura, usa una imagen de color sólido o una textura simple
        self.plane_colored = LoadMesh(
                    join_path("models", "plane.obj"), 
                    join_path("images", "gray.png"),  # Usa una textura simple existente
                    location=pygame.Vector3(0, -0.5, 0),
                    material=self.material_untextured)

        self.lights.append(Light(self.light_pos, pygame.Vector3(1, 1, 1), 0))
        self.camera = Camera(self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def camera_init(self):
        # Mover la lógica de input aquí para evitar conflictos con el bucle principal
        keys = pygame.key.get_pressed()
        
        # Movimiento de la luz con flechas
        if keys[pygame.K_LEFT]:
            self.light_pos.x -= 0.1
            self.lights[0].position = self.light_pos
        if keys[pygame.K_RIGHT]:
            self.light_pos.x += 0.1
            self.lights[0].position = self.light_pos
        if keys[pygame.K_UP]:
            self.light_pos.y += 0.1
            self.lights[0].position = self.light_pos
        if keys[pygame.K_DOWN]:
            self.light_pos.y -= 0.1
            self.lights[0].position = self.light_pos

        # Alternar textura con T
        if keys[pygame.K_t]:
            if not self.key_pressed:
                self.show_texture = not self.show_texture
                self.key_pressed = True
                print(f"Textura: {'ON' if self.show_texture else 'OFF'}")
        else:
            self.key_pressed = False

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        self.axes.draw(self.camera, self.lights)

        # Dibujar el plano según el estado actual
        if self.show_texture:
            self.plane_textured.draw(self.camera, self.lights)
        else:
            self.plane_colored.draw(self.camera, self.lights)

# Crear instancia de la aplicación y ejecutar el bucle principal
TexturedObjects().mainloop()
