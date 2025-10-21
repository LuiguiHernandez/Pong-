🚀 Pygame Pong: Clone Clásico
Un proyecto de juego simple desarrollado en Python utilizando la librería Pygame para recrear el icónico juego de arcade, Pong. Este repositorio contiene el código fuente y la estructura mínima necesaria para jugarlo.


✨ Características Principales
Este proyecto se centra en la lógica fundamental de un juego 2D:

Doble Jugador: Soporte completo para dos jugadores en el mismo teclado (modo couch co-op).

Físicas Simples: Movimiento predecible de la bola y rebotes definidos.

Detección de Colisión: Implementación precisa del choque entre rectángulos (pygame.Rect).

Sistema de Puntuación: Marcador en tiempo real renderizado en pantalla.

Control de Velocidad: Uso de pygame.time.Clock() para mantener una velocidad de fotogramas (FPS) constante.


⚙️ Requisitos e Instalación
Asegúrate de tener Python 3 instalado.

1. Instalación de Dependencias
Solo necesitas Pygame. Instálalo desde tu terminal o símbolo del sistema:
pip install pygame


2. Ejecución del Juego
Navega a la carpeta raíz del proyecto donde se encuentra pong.py y ejecuta:
python pong.py


🎮 Controles
El juego está configurado para un modo de dos jugadores locales:
Jugador  |	Mover Arriba	| Mover | Abajo|
Jugador 1| (Izquierda)	  |   W	  |   S  |
Jugador 2| (Derecha)      |   (↑) |  (↓) |


Para cerrar el juego, presiona la 'X' de la ventana.
