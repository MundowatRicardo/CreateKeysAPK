# Generador de Contraseñas Profesional

Una aplicación de escritorio creada con Flet (Flutter + Python) para generar contraseñas seguras de forma profesional.

## Características

- Interfaz gráfica moderna y amigable
- Generación de contraseñas personalizables
- Opciones para incluir mayúsculas, números y símbolos
- Control deslizante para ajustar la longitud (8-128 caracteres)
- Función de copiado al portapapeles
- Tema oscuro por defecto

## Estructura del Proyecto

```
CreateKeysAPK/
├── main.py                 # Archivo principal de la aplicación
├── assets/                 # Recursos gráficos
│   ├── icon.ico           # Icono de la aplicación
│   └── terre-19.gif       # GIF animado del título
├── requirements.txt        # Dependencias del proyecto
└── README.md              # Este archivo
```

## Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/MundowatRicardo/CreateKeysAPK
cd CreateKeysAPK
```

2. Crear un entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install flet
```

## Uso

Para ejecutar la aplicación:
```bash
python3 main.py
```

## Funcionalidades

- **Generación de Contraseñas**: Crea contraseñas aleatorias con diferentes opciones
- **Personalización**: Elige incluir mayúsculas, números y símbolos
- **Longitud Ajustable**: Define el largo de la contraseña mediante slider
- **Copiado Rápido**: Botón para copiar la contraseña al portapapeles
- **Interfaz Intuitiva**: Diseño moderno y fácil de usar

## Tecnologías Utilizadas

- Python 3
- Flet (Framework UI)
- Random (Generación de números aleatorios)
- String (Manejo de caracteres)

## Autor

WORD WAT SOLUTIONS
Ricardo San José Tejedor

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.