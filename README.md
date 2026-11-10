# AF5 · Simulación de un péndulo-robot

Modelado y Simulación de Sistemas Mecatrónicos · FIME, UANL.

La notebook `AF5_Pendulo_Robot.ipynb` contiene el modelo de Euler–Lagrange, la representación en espacio de estados, una simulación de 10 segundos y las gráficas de posición y velocidad. Se incluyen las salidas de ejecución.

## Reproducción

Instalar las dependencias con `pip install -r requirements.txt`, abrir la notebook en Jupyter y ejecutar todas las celdas. También puede abrirse en Google Colab. `simulacion_af5.py` permite ejecutar el mismo cálculo como programa.

## Parámetros y supuestos

- Ir = 0.16 kg·m², masa = 5 kg, gravedad = 9.81 m/s².
- Distancia al centro de masa = 0.01 m.
- Fricción viscosa = 0.14 N·m·s/rad; fricción de Coulomb = 0.45 N·m.
- Posición y velocidad iniciales: cero.
- Par constante supuesto: 1 N·m; no está especificado en la consigna.
- Ángulo desde la vertical inferior; Ir interpretada respecto de la articulación.
- Fricción regularizada con tanh y epsilon = 0.001 rad/s. No modela adherencia estática exacta.

Los supuestos deben cotejarse con el ejemplo de clase. La notebook comprueba convergencia, sensibilidad de la regularización, balance de energía y reposo sin par motor.

## Documento del equipo

[Documento de AF5 en Prism](https://prism.openai.com/?u=1eb8506f-eb59-4978-9170-48f4db936aa4&pg=1). La conclusión grupal se mantiene pendiente para el equipo.

## Referencias

- Consigna AF5_Modelado.pdf proporcionada para la actividad.
- [Tedrake, Underactuated Robotics: The Simple Pendulum](https://underactuated.mit.edu/pend.html).
- [SciPy: solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).
