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
state1 = np.array([1.0, 1.0, 1.0])  # Condizioni iniziali sistema 1
state2 = np.array([1.0001, 1.0, 1.0])  # Condizioni iniziali sistema 2 (leggermente diverse)
trajectory1 = np.zeros((N, 3))
trajectory2 = np.zeros((N, 3))

# Simulazione del sistema di Lorenz per entrambe le condizioni iniziali
for i in range(N):
    trajectory1[i] = state1
    trajectory2[i] = state2
    state1 = state1 + lorenz_system(state1, sigma, rho, beta) * dt
    state2 = state2 + lorenz_system(state2, sigma, rho, beta) * dt

# Creazione delle figure
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

# Configurazione del plot 3D
ax1.set_title("Attrattore di Lorenz - Sensibilità alle Condizioni Iniziali")
ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")
ax1.set_zlabel("Z Axis")
ax1.set_xlim([np.min(trajectory1[:, 0]), np.max(trajectory1[:, 0])])
ax1.set_ylim([np.min(trajectory1[:, 1]), np.max(trajectory1[:, 1])])
ax1.set_zlim([np.min(trajectory1[:, 2]), np.max(trajectory1[:, 2])])
lorenz_line1, = ax1.plot([], [], [], 'b-', lw=1, label="Sistema 1")
lorenz_line2, = ax1.plot([], [], [], 'r-', lw=1, label="Sistema 2")
lorenz_point1, = ax1.plot([], [], [], 'bo', markersize=5)
lorenz_point2, = ax1.plot([], [], [], 'ro', markersize=5)
ax1.legend()

# Configurazione del plot X vs tempo
ax2.set_title("X vs Tempo")
ax2.set_xlim(0, T)
ax2.set_ylim(min(np.min(trajectory1[:, 0]), np.min(trajectory2[:, 0])), max(np.max(trajectory1[:, 0]), np.max(trajectory2[:, 0])))
ax2.grid()
x_line1, = ax2.plot([], [], 'g-', lw=1, label="Sistema 1")
x_line2, = ax2.plot([], [], 'r-', lw=1, label="Sistema 2")
x_point1, = ax2.plot([], [], 'go', markersize=5)
x_point2, = ax2.plot([], [], 'ro', markersize=5)
ax2.legend()

# Configurazione del plot Z vs tempo
ax3.set_title("Z vs Tempo")
ax3.set_xlim(0, T)
ax3.set_ylim(min(np.min(trajectory1[:, 2]), np.min(trajectory2[:, 2])), max(np.max(trajectory1[:, 2]), np.max(trajectory2[:, 2])))
ax3.grid()
z_line1, = ax3.plot([], [], 'm-', lw=1, label="Sistema 1")
z_line2, = ax3.plot([], [], 'r-', lw=1, label="Sistema 2")
z_point1, = ax3.plot([], [], 'mo', markersize=5)
z_point2, = ax3.plot([], [], 'ro', markersize=5)
ax3.legend()

time = np.linspace(0, T, N)

# Funzione di aggiornamento per l'animazione
def update(frame):
    lorenz_line1.set_data(trajectory1[:frame, 0], trajectory1[:frame, 1])
    lorenz_line1.set_3d_properties(trajectory1[:frame, 2])
    lorenz_line2.set_data(trajectory2[:frame, 0], trajectory2[:frame, 1])
    lorenz_line2.set_3d_properties(trajectory2[:frame, 2])
    lorenz_point1.set_data([trajectory1[frame, 0]], [trajectory1[frame, 1]])
    lorenz_point1.set_3d_properties([trajectory1[frame, 2]])
    lorenz_point2.set_data([trajectory2[frame, 0]], [trajectory2[frame, 1]])
    lorenz_point2.set_3d_properties([trajectory2[frame, 2]])
    x_line1.set_data(time[:frame], trajectory1[:frame, 0])
    x_line2.set_data(time[:frame], trajectory2[:frame, 0])
    x_point1.set_data([time[frame]], [trajectory1[frame, 0]])
    x_point2.set_data([time[frame]], [trajectory2[frame, 0]])
    z_line1.set_data(time[:frame], trajectory1[:frame, 2])
    z_line2.set_data(time[:frame], trajectory2[:frame, 2])
    z_point1.set_data([time[frame]], [trajectory1[frame, 2]])
    z_point2.set_data([time[frame]], [trajectory2[frame, 2]])
    return lorenz_line1, lorenz_point1, lorenz_line2, lorenz_point2, x_line1, x_line2, x_point1, x_point2, z_line1, z_line2, z_point1, z_point2

# Creazione dell'animazione
ani = animation.FuncAnimation(fig, update, frames=N, interval=dt*1000, blit=True)
plt.show()
