import numpy as np
from scipy.integrate import quad

# Definir las funciones en sus respectivos intervalos
def g(x):
    return 72 * x - 1.38 if 0.02 <= x <= 0.05 else 0

def h(x):
    return -1.82 * x**2 + 0.2 * x + 2.21 if 0.05 <= x <= 0.78 else 0

def p(x):
    return 1.09 * x**2 - 2.91 * x + 2.86 if 0.78 <= x <= 1.69 else 0

def q(x):
    return -0.11 * x**2 + 0.92 * x - 0.18 if 1.72 <= x <= 2.91 else 0

def r(x):
    return -0.06 * x**2 + 0.78 * x - 0.16 if 2.91 <= x <= 3.98 else 0

def s(x):
    return -0.1 * x**2 + 1.14 * x - 0.95 if 4 <= x <= 5.04 else 0

def t(x):
    return 0.01 * x**2 + 2 if 5.04 <= x <= 5.98 else 0

def f_1(x):
    return 0.09 * x + 1.8 if 5.98 <= x <= 6.54 else 0

def g_1(x):
    return 9.36 * x**2 - 126.42 * x + 428.79 if 6.53 <= x <= 6.75 else 0

def h_1(x):
    return 0.64 * x**2 - 9.17 * x + 34.66 if 6.74 <= x <= 7.28 else 0

def p_1(x):
    return 0.08 * x + 1.25 if 7.27 <= x <= 7.75 else 0

def q_1(x):
    return -16.42 * x + 128.77 if 7.73 <= x <= 7.78 else 0

def r_1(x):
    return -25.82 * x + 201.89 if 7.78 <= x <= 7.82 else 0

# Lista de funciones y sus intervalos
functions = [
    ("g", g, 0.02, 0.05),
    ("h", h, 0.05, 0.78),
    ("p", p, 0.78, 1.69),
    ("q", q, 1.72, 2.91),
    ("r", r, 2.91, 3.98),
    ("s", s, 4, 5.04),
    ("t", t, 5.04, 5.98),
    ("f_1", f_1, 5.98, 6.54),
    ("g_1", g_1, 6.53, 6.75),
    ("h_1", h_1, 6.74, 7.28),
    ("p_1", p_1, 7.27, 7.75),
    ("q_1", q_1, 7.73, 7.78),
    ("r_1", r_1, 7.78, 7.82)
]

# Función para calcular el volumen
def volume_of_revolution(func, a, b):
    # Calcula el volumen usando la integral
    integral, _ = quad(lambda x: func(x) ** 2, a, b)
    return integral

# Calcular el volumen total
total_integral = 0
for name, func, a, b in functions:
    integral_value = volume_of_revolution(func, a, b)
    total_integral += integral_value
    print(f"Función {name} en el intervalo [{a}, {b}]: Integral = {integral_value:.4f}")

# Imprimir el valor total de la sumatoria antes de multiplicar por pi
print(f"\nValor total de la sumatoria de las integrales: {total_integral:.4f}")

# Multiplicar el total de las integrales por pi para obtener el volumen total
total_volume = np.pi * total_integral
print(f"Volumen total del sólido de revolución: {total_volume:.4f}")