import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definizione delle costanti
L = 1.0  # Lunghezza del pendolo
g = 9.81  # Accelerazione di gravità
b = 0.25  # Coefficiente di attrito

# Condizioni iniziali
theta0 = np.pi / 3  # Angolo iniziale (60 gradi)
omega0 = 0.0  # Velocità angolare iniziale

dt = 0.05  # Passo temporale
T = 100  # Durata totale dell'animazione
N = int(T / dt)  # Numero di passi temporali
time = np.linspace(0, T, N+1)  # Tempo per i grafici

def pendulum_dynamics(theta, omega, dt):
    """Calcola la dinamica del pendolo con attrito usando il metodo di Eulero."""
    alpha = - (g / L) * np.sin(theta) - b * omega  # Accelerazione angolare con attrito
    omega_new = omega + alpha * dt  # Nuova velocità angolare
    theta_new = theta + omega_new * dt  # Nuova posizione angolare
    return theta_new, omega_new

# Inizializzazione delle variabili
angles = [theta0]
angular_velocities = [omega0]

# Simulazione del moto del pendolo
for _ in range(N):
    theta_new, omega_new = pendulum_dynamics(angles[-1], angular_velocities[-1], dt)
    angles.append(theta_new)
    angular_velocities.append(omega_new)

# Conversione delle coordinate per la visualizzazione
x_positions = L * np.sin(angles)
y_positions = -L * np.cos(angles)

# Creazione delle figure
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(10, 5))
ax2, ax4 = fig.add_axes([0.55, 0.55, 0.35, 0.35]), fig.add_axes([0.55, 0.15, 0.35, 0.35])

# Configurazione della prima finestra (pendolo)
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_aspect('equal')
ax1.grid()
ax1.set_title("Moto del Pendolo")
pendulum_line, = ax1.plot([], [], 'o-', lw=2)

# Configurazione della seconda finestra (grafici temporali)
ax2.set_xlim(0, T)
ax2.set_ylim(min(angles), max(angles))
ax2.set_title("Posizione vs Tempo")
ax2.grid()
posizione_line, = ax2.plot([], [], 'b-', lw=1)
posizione_point, = ax2.plot([], [], 'ro', markersize=5)

ax4.set_xlim(0, T)
ax4.set_ylim(min(angular_velocities), max(angular_velocities))
ax4.set_title("Velocità vs Tempo")
ax4.grid()
velocita_line, = ax4.plot([], [], 'g-', lw=1)
velocita_point, = ax4.plot([], [], 'ro', markersize=5)

# Funzione di aggiornamento dell'animazione
def update(frame):
    pendulum_line.set_data([0, x_positions[frame]], [0, y_positions[frame]])
    posizione_line.set_data(time[:frame], angles[:frame])
    posizione_point.set_data([time[frame]], [angles[frame]])
    velocita_line.set_data(time[:frame], angular_velocities[:frame])
    velocita_point.set_data([time[frame]], [angular_velocities[frame]])
    return pendulum_line, posizione_line, posizione_point, velocita_line, velocita_point

# Creazione dell'animazione
ani = animation.FuncAnimation(fig, update, frames=N, interval=dt*1000, blit=True)
plt.show()
