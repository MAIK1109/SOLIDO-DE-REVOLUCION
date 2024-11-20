import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones por tramos
def funcion(x):
    if np.isscalar(x):
        if 0.02 <= x <= 0.05:
            return 72 * x - 1.38
        elif 0.05 <= x <= 0.78:
            return -1.82 * x**2 + 0.2 * x + 2.21
        elif 0.78 <= x <= 1.69:
            return 1.09 * x**2 - 2.91 * x + 2.86
        elif 1.72 <= x <= 2.91:
            return -0.11 * x**2 + 0.92 * x - 0.18
        elif 2.91 <= x <= 3.98:
            return -0.06 * x**2 + 0.78 * x - 0.16
        elif 4 <= x <= 5.04:
            return -0.1 * x**2 + 1.14 * x - 0.95
        elif 5.04 <= x <= 5.98:
            return 0.01 * x**2 + 2
        elif 5.98 <= x <= 6.54:
            return 0.09 * x + 1.8
        elif 6.53 <= x <= 6.75:
            return 9.36 * x**2 - 126.42 * x + 428.79
        elif 6.74 <= x <= 7.28:
            return 0.64 * x**2 - 9.17 * x + 34.66
        elif 7.27 <= x <= 7.75:
            return 0.08 * x + 1.25
        elif 7.73 <= x <= 7.78:
            return -16.42 * x + 128.77
        elif 7.78 <= x <= 7.82:
            return -25.82 * x + 201.89
        else:
            return np.nan  # Fuera de los límites
    else:
        return np.array([funcion(xi) for xi in x])  # Para arreglos

# Crear listas para almacenar x e y por tramos
x_vals = []
y_vals = []

# Definir los intervalos de las funciones
intervalos = [
    (0.02, 0.05), (0.05, 0.78), (0.78, 1.69), (1.72, 2.91),
    (2.91, 3.98), (4, 5.04), (5.04, 5.98), (5.98, 6.54),
    (6.53, 6.75), (6.74, 7.28), (7.27, 7.75), (7.73, 7.78),
    (7.78, 7.82)
]

# Generar los valores de x e y para cada intervalo
for intervalo in intervalos:
    x_tramo = np.linspace(intervalo[0], intervalo[1], 100)
    y_tramo = funcion(x_tramo)
    x_vals.append(x_tramo)
    y_vals.append(y_tramo)

# Concatenar todos los tramos
x_total = np.concatenate(x_vals)
y_total = np.concatenate(y_vals)

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la función original
ax.plot(x_total, y_total, np.zeros_like(x_total), 'b-')

# Crear la malla de revolución sobre el eje X
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, y_grid = np.meshgrid(theta, y_total)

# Rotación sobre el eje X
x_grid = np.tile(x_total, (100, 1)).T  # Repetir x_total
z_grid = y_grid * np.sin(theta_grid)
y_grid = y_grid * np.cos(theta_grid)

# Graficar la superficie de revolución
ax.plot_surface(x_grid, y_grid, z_grid, color='b', alpha=0.5)

# Ajustar los ejes para mejorar la visualización
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Sólido de Revolución - Copa Champions")

# Mostrar la figura
plt.show()