# Luces y Texturas - Proyecto OpenGL con Python

Este proyecto implementa un sistema de iluminación y texturas en OpenGL usando Python, pygame y PyOpenGL. Muestra un plano texturizado con controles de cámara, iluminación dinámica y alternancia de texturas.
Fue creado por el desarrollador Byron Serrano de la carrera de Software, de Septimo Semestre

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación y Configuración

### 1. Clonar o Descargar el Proyecto

```bash
git clone <url-del-repositorio>
cd Luces-Texturas
```

### 2. Crear un Entorno Virtual

Es **recomendable** crear un entorno virtual para evitar conflictos con otras librerías:

**En Windows:**
```powershell
python -m venv env
env\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instalar Dependencias

Instala todas las librerías necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Dependencias incluidas:**
- `pygame>=2.0.0` - Para ventana y manejo de eventos
- `PyOpenGL>=3.1.0` - Bindings de OpenGL para Python
- `PyOpenGL-accelerate>=3.1.0` - Aceleración para PyOpenGL
- `numpy>=1.20.0` - Operaciones matemáticas con matrices

### 4. Verificar la Instalación

Puedes verificar que las librerías se instalaron correctamente:

```bash
pip list
```

## 🎮 Ejecución del Programa

### Ejecutar el Programa Principal

```bash
python Exam2P.py
```


## 🎯 Controles del Programa

### 🎦 Cámara
- **W/A/S/D** - Mover cámara (adelante/izquierda/atrás/derecha)
- **Mouse** - Rotar vista de la cámara
- **ESC** - Liberar mouse (mostrar cursor)
- **SPACE** - Capturar mouse (ocultar cursor)

### 💡 Iluminación
- **↑ (UP)** - Mover luz hacia arriba
- **↓ (DOWN)** - Mover luz hacia abajo
- **← (LEFT)** - Mover luz hacia la izquierda
- **→ (RIGHT)** - Mover luz hacia la derecha

### 🖼️ Texturas
- **T** - Alternar entre textura ON/OFF

### 📦 Objetos
- Plano con textura de tierra seca
- Ejes de coordenadas (X=rojo, Y=verde, Z=azul)

## 📁 Estructura del Proyecto

```
Luces-Texturas/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias del proyecto
├── Exam2P.py                # Archivo principal del examen
├── glapp/                   # Librería de clases OpenGL
│   ├── PyOGLApp.py         # Clase base de la aplicación
│   ├── Camera.py           # Manejo de cámara
│   ├── Light.py            # Sistema de iluminación
│   ├── Material.py         # Manejo de materiales
│   ├── Mesh.py             # Renderizado de mallas
│   ├── Texture.py          # Manejo de texturas
│   └── ...                 # Otras clases auxiliares
├── shaders/                # Shaders GLSL
│   ├── texturedvert.vs     # Vertex shader para texturas
│   ├── texturedfrag.vs     # Fragment shader para texturas
│   ├── vertexcolvert.vs    # Vertex shader para colores
│   └── vertexcolfrag.vs    # Fragment shader para colores
├── models/                 # Modelos 3D (.obj)
│   └── plane.obj           # Modelo de plano
├── images/                 # Texturas e imágenes
│   ├── tierra_seca.jpg     # Textura de tierra seca
│   └── gray.png            # Textura gris simple
└── env/                    # Entorno virtual (creado localmente)
```

## 🛠️ Solución de Problemas

### Error de Importación de OpenGL

Si encuentras errores relacionados con OpenGL:

```bash
pip install --upgrade PyOpenGL PyOpenGL-accelerate
```

### Error de pygame

Si pygame no se instala correctamente:

```bash
pip install --upgrade pygame
```

### Problemas con el Entorno Virtual

Si tienes problemas con el entorno virtual, puedes recrearlo:

```bash
# Desactivar entorno actual
deactivate

# Eliminar carpeta env
rmdir /s env  # Windows
rm -rf env    # macOS/Linux

# Crear nuevo entorno
python -m venv env
```

### Rendimiento Lento

Si el programa funciona lento:

1. Asegúrate de tener controladores gráficos actualizados
2. Verifica que PyOpenGL-accelerate esté instalado
3. Cierra otras aplicaciones que usen la GPU

## 🔧 Características Técnicas

- **Motor de Renderizado**: OpenGL 3.3 Core Profile
- **Shading**: Phong/Blinn-Phong con atenuación de luz
- **Texturas**: Soporte para formatos JPG, PNG
- **Modelos**: Soporte para archivos OBJ
- **Iluminación**: Sistema de luces puntuales con atenuación
- **Cámara**: Primera persona con controles tipo FPS

## 📝 Notas Adicionales

- El programa requiere una tarjeta gráfica compatible con OpenGL 3.3 o superior
- Las texturas deben estar en la carpeta `images/`
- Los modelos 3D deben estar en formato OBJ en la carpeta `models/`
- Los shaders están en formato GLSL en la carpeta `shaders/`

## 🤝 Contribuciones

Este es un proyecto académico para la materia de Gráficos por Computadora.
Hecho por Byron Serrano.

---
