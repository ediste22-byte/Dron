"""
Simulacion 3D y Telemetria Analitica de un Dron de Entregas
Materia: Matematica Aplicada
Instituto Superior Tecnologico Cordillera

1. Mueve un objeto 3D (el dron) siguiendo h(t)
2. Muestra en pantalla la altitud, la velocidad (derivada)
   y los datos acumulados (integral) en tiempo real
3. Al terminar, abre 3 graficas de resumen con Matplotlib
---------------------------------------------------------
"""

from vpython import canvas, box, curve, vector, color, rate, label
import numpy as np
import matplotlib.pyplot as plt

# ===========================================================
# 1. FUNCIONES MATEMATICAS DEL DRON (Fases 1 y 3)
# ===========================================================

def h(t):
    """Altitud del dron h(t)"""
    return -0.1*t**4 + 1.6*t**3 - 7.2*t**2 + 10*t + 5

def v(t):
    """Velocidad instantanea v(t) = h'(t)  (primera derivada de h)"""
    return -0.4*t**3 + 4.8*t**2 - 14.4*t + 10

def D(t):
    """Tasa de transferencia de datos D(t) en MB/s"""
    return 3*t**2 + 2*t + 5

# ===========================================================
# 2. ESCENA 3D
# ===========================================================

escena = canvas(title="Simulacion 3D - Telemetria del Dron",
                 width=900, height=500,
                 background=color.gray(0.9))

# El dron representado como una caja pequena
dron = box(pos=vector(0, h(0), 0), size=vector(0.6, 0.3, 0.6), color=color.red)

# Linea que va dibujando la trayectoria del dron
trayectoria = curve(color=color.blue, radius=0.02)

# Texto de telemetria en pantalla (HUD)
hud = label(pos=vector(0, 12, 0), text="", box=False, height=14, align='left')

# ===========================================================
# 3. SIMULACION: de t = 0 a t = 10 segundos
# ===========================================================

dt = 0.05                  # paso de tiempo (mas pequeno = animacion mas suave)
t = 0.0
datos_acumulados = 0.0     # acumulador de la integral (Datos Totales)

# Listas para guardar la telemetria y graficarla despues
lista_t = []
lista_h = []
lista_v = []
lista_D = []

while t <= 10:
    rate(60)  # 60 cuadros por segundo

    # Posicion actual del dron: eje x = tiempo, eje y = altitud h(t)
    dron.pos = vector(t, h(t), 0)
    trayectoria.append(dron.pos)

    # Acumulacion de datos: integral numerica (regla del rectangulo/trapecio simple)
    datos_acumulados += D(t) * dt

    # Actualizar el HUD con la telemetria en tiempo real
    hud.text = (f"t = {t:.2f} s\n"
                f"Altitud h(t) = {h(t):.2f} m\n"
                f"Velocidad h'(t) = {v(t):.2f} m/s\n"
                f"Datos acumulados = {datos_acumulados:.2f} MB")

    # Guardar datos para las graficas finales
    lista_t.append(t)
    lista_h.append(h(t))
    lista_v.append(v(t))
    lista_D.append(D(t))

    t += dt

print("Simulacion 3D finalizada. Abriendo graficas de resumen...")

# ===========================================================
# 4. GRAFICAS DE RESUMEN CON MATPLOTLIB
# ===========================================================

lista_t = np.array(lista_t)
lista_h = np.array(lista_h)
lista_v = np.array(lista_v)
lista_D = np.array(lista_D)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9, 10))

# --- Grafica 1: Altitud h(t) ---
ax1.plot(lista_t, lista_h, color='blue')
ax1.set_title("Altitud del Dron h(t)")
ax1.set_xlabel("t (s)")
ax1.set_ylabel("Altitud (m)")
ax1.grid(True)

# --- Grafica 2: Velocidad v(t) con recta tangente en el punto maximo ---
ax2.plot(lista_t, lista_v, color='green', label="v(t) = h'(t)")

indice_max = np.argmax(lista_v)
t_max = lista_t[indice_max]
v_max = lista_v[indice_max]

# Recta tangente en el maximo (pendiente = 0, porque ahi h''(t) = 0)
recta_tangente = np.full_like(lista_t, v_max)
ax2.plot(lista_t, recta_tangente, '--', color='orange', label="Tangente en el maximo")
ax2.plot(t_max, v_max, 'o', color='red')
ax2.set_title("Velocidad Instantanea v(t) = h'(t)")
ax2.set_xlabel("t (s)")
ax2.set_ylabel("Velocidad (m/s)")
ax2.legend()
ax2.grid(True)

# --- Grafica 3: Transferencia de datos D(t) con area sombreada entre t=1 y t=4 ---
ax3.plot(lista_t, lista_D, color='purple')
mascara = (lista_t >= 1) & (lista_t <= 4)
ax3.fill_between(lista_t, lista_D, where=mascara, color='purple', alpha=0.3)
ax3.set_title("Transferencia de Datos D(t) - Area bajo la curva entre t=1 y t=4")
ax3.set_xlabel("t (s)")
ax3.set_ylabel("D(t) (MB/s)")
ax3.grid(True)

plt.tight_layout()
plt.show()