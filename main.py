import pygame
import os

from glapp.Utils import create_program
from glapp.PyOGLApp import *
from glapp.Material import *

# from glapp.Cube import *
from glapp.LoadMesh import *
from glapp.Light import *
from glapp.Axes import *


# from glApp.MovingCube import *

# Obtener la ruta absoluta del directorio actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def join_path(object1, object2):
    return os.path.join(BASE_DIR, object1, object2)

def join_nested_path(folder1, folder2, file_name):
    """Para archivos en subcarpetas"""
    return os.path.join(BASE_DIR, folder1, folder2, file_name)

class TexturedObjects(PyOGLApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 600)
        self.lights = []
        self.light_pos = pygame.Vector3(-2, 2, 2)      # Luz 1: izquierda-arriba-adelante
        self.light2_pos = pygame.Vector3(2, 2, 2)      # Luz 2: derecha-arriba-adelante
        self.material_textured = None
        self.key_pressed = False  # Para evitar múltiples cambios por una presión
        self.animate = False  # DESACTIVADA POR DEFECTO
        self.rotation_angle = 0
        self.light1_enabled = True
        self.light2_enabled = True
        self.light_is_white = True
        self.main_model = None
        
        # Imprimir controles al inicializar
        self.print_controls()

        glEnable(GL_CULL_FACE)

    def print_controls(self):
        print("\n" + "="*50)
        print("        CONTROLES DE LA ESCENA 3D")
        print("="*50)
        print("NAVEGACIÓN:")
        print("  W/A/S/D - Mover cámara")
        print("  Ratón    - Rotar vista")
        print("  ESC      - Mostrar cursor")
        print("  ESPACIO  - Ocultar cursor")
        print("\nLUCES:")
        print("  ↑/↓/←/→  - Mover Luz 1 (BLANCA)")
        print("  1        - Encender/Apagar Luz 1 (BLANCA)")
        print("  2        - Encender/Apagar Luz 2 (ROJA)")
        print("\nOBJETOS:")
        print("  R        - Alternar animación de rotación")
        print("\nMODELOS DISPONIBLES:")
        print("  3        - Cargar Tetera")
        print("  4        - Cargar Ferrari")
        print("="*50)

    def initialise(self):
        self.material_textured = Material(join_path("shaders", "texturedvert.vs"), join_path("shaders", "texturedfrag.vs"))
        
        axesmat = Material(join_path("shaders", "vertexcolvert.vs"), join_path("shaders", "vertexcolfrag.fs"))
        self.axes = Axes(pygame.Vector3(0, 0, 0), axesmat)

        # Modelo principal - Tetera con animación DESACTIVADA por defecto
        self.main_model = LoadMesh(
                    join_path("models", "teapot.obj"),
                    join_path("images", "gold.png"),
                    location=pygame.Vector3(0, 0, 0),
                    scale=pygame.Vector3(0.5, 0.5, 0.5),
                    material=self.material_textured)

        # Crear dos luces - BLANCA y ROJA
        self.lights.append(Light(self.light_pos, pygame.Vector3(1.0, 1.0, 1.0), 0))   # Luz blanca - índice 0
        self.lights.append(Light(self.light2_pos, pygame.Vector3(1.0, 0.3, 0.3), 1))  # Luz roja

        self.camera = Camera(self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def load_model(self, model_name, texture_name):
        """Cargar un nuevo modelo principal"""

        if model_name == "formula_1.obj":
            scale_factor = pygame.Vector3(0.05, 0.05, 0.05)  # MUCHÍSIMO más pequeño
            location = pygame.Vector3(0, 0, -3)
        else:
            scale_factor = pygame.Vector3(0.5, 0.5, 0.5)
            location = pygame.Vector3(0, 0, 0)
        
        if model_name == "formula_1.obj":
            model_path = join_path("models/formula_1", model_name)
        else:
            model_path = join_path("models", model_name)

        self.main_model = LoadMesh(
            model_path,
            join_path("images", texture_name),
            location=location,
            scale=scale_factor,
            material=self.material_textured)
        self.rotation_angle = 0  # Resetear rotación
        print(f"Modelo cargado: {model_name}")

    def camera_init(self):
        # Mover la lógica de input aquí para evitar conflictos con el bucle principal
        keys = pygame.key.get_pressed()
        
        # Movimiento de la luz 1 con flechas
        if keys[pygame.K_LEFT]:
            self.light_pos.x -= 0.1
            if self.light1_enabled:
                self.lights[0].position = self.light_pos  # Ahora sí manipula la luz blanca
        if keys[pygame.K_RIGHT]:
            self.light_pos.x += 0.1
            if self.light1_enabled:
                self.lights[0].position = self.light_pos
        if keys[pygame.K_UP]:
            self.light_pos.y += 0.1
            if self.light1_enabled:
                self.lights[0].position = self.light_pos
        if keys[pygame.K_DOWN]:
            self.light_pos.y -= 0.1
            if self.light1_enabled:
                self.lights[0].position = self.light_pos

        # Controles de teclas (con debounce)
        if keys[pygame.K_r]:
            if not self.key_pressed:
                self.animate = not self.animate
                self.key_pressed = True
                print(f"Animación: {'ON' if self.animate else 'OFF'}")
        elif keys[pygame.K_1]:
            if not self.key_pressed:
                self.light_is_white = not self.light_is_white
                if self.light1_enabled:  # Solo cambiar color si la luz está encendida
                    if self.light_is_white:
                        self.lights[0].color = pygame.Vector3(1.0, 1.0, 1.0)  # Blanca
                        print("Luz cambiada a: BLANCA")
                    else:
                        self.lights[0].color = pygame.Vector3(1.0, 0.3, 0.3)  # Roja
                        print("Luz cambiada a: ROJA")
                else:
                    print(f"Color cambiado a: {'BLANCA' if self.light_is_white else 'ROJA'} (luz apagada)")
                self.key_pressed = True
        elif keys[pygame.K_2]:
            if not self.key_pressed:
                self.light1_enabled = not self.light1_enabled
                if self.light1_enabled:
                    # Encender con el color actual
                    if self.light_is_white:
                        self.lights[0].color = pygame.Vector3(1.0, 1.0, 1.0)  # Blanca
                    else:
                        self.lights[0].color = pygame.Vector3(1.0, 0.3, 0.3)  # Roja
                    print(f"Luz ENCENDIDA ({'BLANCA' if self.light_is_white else 'ROJA'})")
                else:
                    self.lights[0].color = pygame.Vector3(0, 0, 0)  # Apagada
                    print("Luz APAGADA")
                self.key_pressed = True
        elif keys[pygame.K_3]:
            if not self.key_pressed:
                self.load_model("teapot.obj", "gold.png")
                self.key_pressed = True
        elif keys[pygame.K_4]:
            if not self.key_pressed:
                self.load_model("formula_1.obj", "formula1.png")
                scale_factor = pygame.Vector3(0.2, 0.2, 0.2)
                self.key_pressed = True
        else:
            self.key_pressed = False

        # Animación de rotación del modelo principal
        if self.animate:
            self.rotation_angle += 1
            if self.rotation_angle >= 360:
                self.rotation_angle = 0

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        self.axes.draw(self.camera, self.lights)
        
        # Dibujar SOLO el modelo principal con o sin animación
        if self.main_model:
            # Aplicar rotación solo si la animación está activada
            if self.animate:
                self.main_model.move_rotation = Rotation(self.rotation_angle, pygame.Vector3(0, 1, 0))
            else:
                self.main_model.move_rotation = Rotation(0, pygame.Vector3(0, 1, 0))
            
            self.main_model.draw(self.camera, self.lights)

# Crear instancia de la aplicación y ejecutar el bucle principal
TexturedObjects().mainloop()
