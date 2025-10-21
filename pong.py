import pygame
import random

# ====================================================================
# PASO 1: CONFIGURACIÓN INICIAL
# ====================================================================

pygame.init()

# Definición de Constantes (Tamaños y Colores)
ANCHO = 800
ALTO = 600
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de la Ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong Clásico")

# Control de la velocidad del juego (FPS)
reloj = pygame.time.Clock()
FPS = 60 # Frames por segundo

# ====================================================================
# PASO 3: CREAR LOS OBJETOS DEL JUEGO
# ====================================================================

# --- PALETAS ---
ANCHO_PALETA = 10
ALTO_PALETA = 80
VELOCIDAD_PALETA = 5

# Paleta Izquierda (Jugador 1)
paleta_izq = pygame.Rect(50, ALTO // 2 - ALTO_PALETA // 2, ANCHO_PALETA, ALTO_PALETA)
score_izq = 0

# Paleta Derecha (Jugador 2)
paleta_der = pygame.Rect(ANCHO - 50 - ANCHO_PALETA, ALTO // 2 - ALTO_PALETA // 2, ANCHO_PALETA, ALTO_PALETA)
score_der = 0

# --- PELOTA ---
TAMANO_BOLA = 15
# Creamos la bola en el centro
bola = pygame.Rect(ANCHO // 2 - TAMANO_BOLA // 2, ALTO // 2 - TAMANO_BOLA // 2, TAMANO_BOLA, TAMANO_BOLA)

# Velocidad inicial de la bola (empieza aleatoriamente)
VELOCIDAD_BOLA_X = 5 * random.choice((1, -1))
VELOCIDAD_BOLA_Y = 5 * random.choice((1, -1))

# --- Puntuación ---
fuente = pygame.font.Font(None, 74) # Usamos la fuente por defecto de Pygame

# ====================================================================
# Funciones Auxiliares
# ====================================================================

def dibujar_objetos():
    """Dibuja todas las paletas, la bola y la línea central."""
    # Dibuja paletas
    pygame.draw.rect(pantalla, BLANCO, paleta_izq)
    pygame.draw.rect(pantalla, BLANCO, paleta_der)
    # Dibuja la bola
    pygame.draw.ellipse(pantalla, BLANCO, bola)
    # Dibuja la línea central
    pygame.draw.aaline(pantalla, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))

def actualizar_puntuacion():
    """Renderiza y dibuja la puntuación en la pantalla."""
    texto_izq = fuente.render(str(score_izq), True, BLANCO)
    texto_der = fuente.render(str(score_der), True, BLANCO)
    
    # Dibujar la puntuación (posición estratégica)
    pantalla.blit(texto_izq, (ANCHO // 2 - 80, 10))
    pantalla.blit(texto_der, (ANCHO // 2 + 50, 10))

def movimiento_bola():
    """Mueve la bola y gestiona las colisiones con bordes."""
    global VELOCIDAD_BOLA_X, VELOCIDAD_BOLA_Y, score_izq, score_der

    # Mover la bola (PASO 5A)
    bola.x += VELOCIDAD_BOLA_X
    bola.y += VELOCIDAD_BOLA_Y

    # Colisión con bordes superior e inferior (PASO 5B)
    if bola.top <= 0 or bola.bottom >= ALTO:
        VELOCIDAD_BOLA_Y *= -1

    # Colisión con bordes izquierdo y derecho (Punto) (PASO 6)
    if bola.left <= 0:  # Punto para el jugador derecho
        score_der += 1
        reiniciar_bola()

    if bola.right >= ANCHO:  # Punto para el jugador izquierdo
        score_izq += 1
        reiniciar_bola()

def reiniciar_bola():
    """Coloca la bola en el centro y le da una dirección inicial aleatoria."""
    global VELOCIDAD_BOLA_X, VELOCIDAD_BOLA_Y
    bola.center = (ANCHO // 2, ALTO // 2)

    # Invierte la dirección para el "saque"
    VELOCIDAD_BOLA_X *= random.choice((1, -1))
    VELOCIDAD_BOLA_Y *= random.choice((1, -1))

def chequear_colisiones():
    """Gestiona las colisiones de la bola con las paletas."""
    global VELOCIDAD_BOLA_X
    
    # Colisión con Paleta Izquierda (PASO 5C)
    if bola.colliderect(paleta_izq):
        # Aseguramos que la bola solo rebote si va hacia la paleta
        if VELOCIDAD_BOLA_X < 0:
            VELOCIDAD_BOLA_X *= -1 # Invertir dirección X (PASO 5D)
    
    # Colisión con Paleta Derecha
    if bola.colliderect(paleta_der):
        # Aseguramos que la bola solo rebote si va hacia la paleta
        if VELOCIDAD_BOLA_X > 0:
            VELOCIDAD_BOLA_X *= -1 # Invertir dirección X

def mover_paletas(keys):
    """Maneja el movimiento de las paletas basado en la entrada de teclado (PASO 4)."""
    
    # Jugador 1 (W/S)
    if keys[pygame.K_w]:
        paleta_izq.y -= VELOCIDAD_PALETA
    if keys[pygame.K_s]:
        paleta_izq.y += VELOCIDAD_PALETA

    # Jugador 2 (Flechas Arriba/Abajo)
    if keys[pygame.K_UP]:
        paleta_der.y -= VELOCIDAD_PALETA
    if keys[pygame.K_DOWN]:
        paleta_der.y += VELOCIDAD_PALETA

    # Límites de la Pantalla (PASO 4D)
    # Clamp (asegurar) que la posición Y esté entre 0 y el límite
    paleta_izq.top = max(0, paleta_izq.top)
    paleta_izq.bottom = min(ALTO, paleta_izq.bottom)
    
    paleta_der.top = max(0, paleta_der.top)
    paleta_der.bottom = min(ALTO, paleta_der.bottom)


# ====================================================================
# PASO 2: EL BUCLE PRINCIPAL DEL JUEGO
# ====================================================================

jugando = True
while jugando:
    
    # --- PASO 2B: Manejo de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # PASO 2C: Salir
            jugando = False

    # Obtener el estado de todas las teclas presionadas
    keys = pygame.key.get_pressed()
    
    # --- Actualizaciones de Lógica ---
    mover_paletas(keys)
    movimiento_bola()
    chequear_colisiones()
    
    # --- PASO 2D: Dibujar / Refrescar ---
    # 1. Fondo
    pantalla.fill(NEGRO) 
    
    # 2. Dibujar objetos y puntuación
    dibujar_objetos()
    actualizar_puntuacion()
    
    # 3. Actualizar la pantalla
    pygame.display.flip()
    
    # Controlar los FPS
    reloj.tick(FPS)

# PASO 2E: Terminar Pygame
pygame.quit()