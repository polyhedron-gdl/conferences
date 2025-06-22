import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Parametri del sistema di Lorenz
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
dt = 0.01
T = 50  # Durata della simulazione
N = int(T / dt)

# Funzione per calcolare la derivata del sistema di Lorenz
def lorenz_system(state, sigma, rho, beta):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

# Inizializzazione delle variabili
state = np.array([1.0, 1.0, 1.0])  # Condizioni iniziali
trajectory = np.zeros((N, 3))

# Simulazione del sistema di Lorenz
for i in range(N):
    trajectory[i] = state
    state = state + lorenz_system(state, sigma, rho, beta) * dt

# Creazione delle figure
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

# Configurazione del plot 3D
ax1.set_title("Attrattore di Lorenz")
ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")
ax1.set_zlabel("Z Axis")
ax1.set_xlim([np.min(trajectory[:, 0]), np.max(trajectory[:, 0])])
ax1.set_ylim([np.min(trajectory[:, 1]), np.max(trajectory[:, 1])])
ax1.set_zlim([np.min(trajectory[:, 2]), np.max(trajectory[:, 2])])
lorenz_line, = ax1.plot([], [], [], 'b-', lw=1)
lorenz_point, = ax1.plot([], [], [], 'ro', markersize=5)

# Configurazione del plot X vs tempo
ax2.set_title("X vs Tempo")
ax2.set_xlim(0, T)
ax2.set_ylim(np.min(trajectory[:, 0]), np.max(trajectory[:, 0]))
ax2.grid()
x_line, = ax2.plot([], [], 'g-', lw=1)
x_point, = ax2.plot([], [], 'ro', markersize=5)

# Configurazione del plot Z vs tempo
ax3.set_title("Z vs Tempo")
ax3.set_xlim(0, T)
ax3.set_ylim(np.min(trajectory[:, 2]), np.max(trajectory[:, 2]))
ax3.grid()
z_line, = ax3.plot([], [], 'm-', lw=1)
z_point, = ax3.plot([], [], 'ro', markersize=5)

time = np.linspace(0, T, N)

# Funzione di aggiornamento per l'animazione
def update(frame):
    lorenz_line.set_data(trajectory[:frame, 0], trajectory[:frame, 1])
    lorenz_line.set_3d_properties(trajectory[:frame, 2])
    lorenz_point.set_data([trajectory[frame, 0]], [trajectory[frame, 1]])
    lorenz_point.set_3d_properties([trajectory[frame, 2]])
    x_line.set_data(time[:frame], trajectory[:frame, 0])
    x_point.set_data([time[frame]], [trajectory[frame, 0]])
    z_line.set_data(time[:frame], trajectory[:frame, 2])
    z_point.set_data([time[frame]], [trajectory[frame, 2]])
    return lorenz_line, lorenz_point, x_line, x_point, z_line, z_point

# Creazione dell'animazione
ani = animation.FuncAnimation(fig, update, frames=N, interval=dt*1000, blit=True)
plt.show()