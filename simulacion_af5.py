import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import scipy
Ir, m, g, lc, b, fc = 0.16, 5.0, 9.81, 0.01, 0.14, 0.45
tau0 = 1.0  # N m: supuesto de trabajo, no especificado en la consigna
eps = 0.001  # rad/s, regularizacion de Coulomb
t = np.linspace(0.0, 10.0, 2001)
x0 = [0.0, 0.0]
def torque(t):
    return tau0
def modelo(t, x, epsilon=eps):
    theta, omega = x
    return [omega, (torque(t)-b*omega-fc*np.tanh(omega/epsilon)
                    -m*g*lc*np.sin(theta))/Ir]
print('NumPy:', np.__version__, '| SciPy:', scipy.__version__)

sol = solve_ivp(modelo, (0, 10), x0, t_eval=t, rtol=1e-9, atol=1e-11, max_step=0.01)
assert sol.success, sol.message
theta, omega = sol.y
print(f'Posicion a 10 s: {theta[-1]:.6f} rad ({np.degrees(theta[-1]):.3f} grados)')
print(f'Velocidad a 10 s: {omega[-1]:.6f} rad/s')
print(f'Velocidad maxima muestreada: {omega.max():.6f} rad/s')

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True, constrained_layout=True)
for ax, y, label in zip(axes, [theta, omega], ['Posición angular (rad)', 'Velocidad angular (rad/s)']):
    ax.plot(t, y, color='#184d7a', linewidth=1.8)
    ax.set_ylabel(label); ax.grid(alpha=0.22); ax.set_xlim(0,10)
axes[0].set_title('Péndulo-robot: par constante supuesto de 1 N·m')
axes[1].set_xlabel('Tiempo (s)')
plt.show()

ref = solve_ivp(modelo, (0,10), x0, t_eval=t, rtol=1e-11, atol=1e-13, max_step=0.005)
error = np.max(np.abs(sol.y-ref.y),axis=1)
assert ref.success and np.all(error < 1e-5)
print('Diferencias máximas con tolerancia más estricta [rad, rad/s]:', error)
for epsilon in [0.002, 0.0005]:
    alt = solve_ivp(lambda tt,xx: modelo(tt,xx,epsilon), (0,10), x0,
                    t_eval=t, rtol=1e-9, atol=1e-11, max_step=0.01)
    assert alt.success
    print('epsilon:',epsilon,'; diferencia máxima [rad, rad/s]:', np.max(np.abs(sol.y-alt.y),axis=1))
# Comprobación independiente: trabajo del motor = energía + disipación.
from scipy.integrate import cumulative_trapezoid
energia = 0.5*Ir*omega**2 + m*g*lc*(1-np.cos(theta))
potencia = tau0*omega - b*omega**2 - fc*np.tanh(omega/eps)*omega
residuo = energia - cumulative_trapezoid(potencia,t,initial=0)
assert np.max(np.abs(residuo)) < 1e-3
print('Residuo máximo de balance energético (J):', np.max(np.abs(residuo)))
reposo = solve_ivp(lambda tt,xx: [xx[1],(-b*xx[1]-fc*np.tanh(xx[1]/eps)-m*g*lc*np.sin(xx[0]))/Ir],
                   (0,10), x0, t_eval=t)
assert np.allclose(reposo.y,0)
print('Sin par y desde el equilibrio: posición y velocidad permanecen en cero.')
