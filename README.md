🛸 Simulación 3D y Telemetría Analítica de un Dron de Entregas

Motor de simulación 3D en Python que modela la trayectoria, la velocidad instantánea, la temperatura del motor y el consumo de datos de un dron de entregas, aplicando Cálculo Diferencial e Integral (derivadas, optimización y el Teorema Fundamental del Cálculo) para la lectura de telemetría en tiempo real.

Institución: Instituto Tecnológico Superior Cordillera Carrera: Desarrollo de Software Asignatura: Matemática Aplicada — Ing. Andrés Cangui H. Trabajo Autónomo — Tercer Bimestre (Agosto–Septiembre 2026)


Nombre 
Edison Troncozo 1 "A" Nocturna

🎯 Objetivo del proyecto

Desarrollar un motor de simulación 3D en Python que represente:

La posición/altitud del dron h(t).
Su velocidad instantánea v(t) = h'(t) (primera derivada).
La optimización de vuelo mediante puntos críticos (máximos y mínimos).
La temperatura del motor T(t), reconstruida a partir de su tasa de cambio T'(t) (antiderivada).
El consumo acumulado de datos de la cámara 4K, calculado mediante la integral definida y el Teorema Fundamental del Cálculo.
📐 Fundamento matemático
Fase 1 — Altitud y velocidad instantánea

Función de altitud (t en segundos, 0 ≤ t ≤ 10):

h(t)=−0.1t4+1.6t3−7.2t2+10t+5+10t+5

Velocidad vertical (primera derivada):

v(t)=h′(t)=−0.4t3+4.8t2−14.4t+10−14.4t+10

Puntos críticos: se obtienen resolviendo h'(t) = 0, y se clasifican con el criterio de la segunda derivada h''(t) para determinar la altura máxima y el valle de estabilidad.

Fase 2 — Temperatura del motor (antiderivada)

Tasa instantánea de calentamiento:

T′(t)=0.6t2−2t+4

Función de temperatura reconstruida (con T(0) = 22 °C):

T(t)=0.2t3−t2+4t+22

Fase 3 — Transferencia de datos (integral definida)

Consumo de ancho de banda de la cámara 4K:

D(t)=3t2+2t+5[MB/s]

Datos totales transferidos entre t = 1 y t = 4 segundos:

Datos Totales = ∫14​(3t2+2t+5) dt = [F(t)]14​=F(4)−F(1)

El desarrollo analítico completo (paso a paso) de las tres fases se encuentra en docs/Reporte_Analitico_Calculo.pdf.

🖥️ Tecnologías utilizadas
Python 3.x
vpython — renderizado e interfaz 3D
numpy — vectorización de los modelos matemáticos
matplotlib — gráficos comparativos de telemetría
📂 Estructura del repositorio
dron-simulacion-3d/
├── README.md
├── requirements.txt
├── dron_simulation3d.py
├── docs/
│   └── Reporte_Analitico_Calculo.pdf
├── screenshots/
│   ├── simulacion_3d.png
│   ├── hud_telemetria.png
│   └── graficas_matplotlib.png
└── .gitignore
⚙️ Instalación
bash
git clone https://github.com/tu-usuario/dron-simulacion-3d.git
cd dron-simulacion-3d
pip install -r requirements.txt
▶️ Ejecución
bash
python dron_simulation3d.py

Al ejecutarlo se abrirá una ventana 3D con el dron moviéndose según h(t), mostrando en tiempo real la altitud, la velocidad instantánea y los datos acumulados. Al finalizar los 10 segundos de simulación se abrirá automáticamente una ventana de matplotlib con las tres gráficas de resumen (posición, velocidad con recta tangente, y transferencia de datos con el área bajo la curva sombreada entre t=1 y t=4).

📸 Capturas de pantalla
Simulación 3D del dron

<img width="952" height="651" alt="image" src="https://github.com/user-attachments/assets/8bf65165-1a7d-432a-804f-52e81f1017d5" />

Gráficas de resumen (Matplotlib)

<img width="952" height="1017" alt="image" src="https://github.com/user-attachments/assets/ca4bcdbf-6441-428c-9d24-877bb0d6e5cb" />

