# Glide Trajectory Optimization

A Python-based aerospace optimization project for maximizing glide range using time-varying angle-of-attack control.

## Project Overview

This project simulates the trajectory of a gliding aircraft using:

- Newtonian flight dynamics
- Aerodynamic lift and drag models
- Euler numerical integration
- Open-loop optimal control
- Nonlinear constrained optimization (SLSQP)

The optimizer computes the optimal angle-of-attack profile over time to maximize horizontal range while satisfying a final altitude constraint.

---

## Features

- Time-varying control input
- Nonlinear flight dynamics
- Lift and drag force modeling
- Trajectory simulation
- Constrained optimization using SciPy
- Visualization of:
  - Control profile
  - Altitude history
  - Speed history

---

## Equations Used

Lift force:

\[
L = \frac{1}{2}\rho V^2 S C_L
\]

Drag force:

\[
D = \frac{1}{2}\rho V^2 S C_D
\]

Drag polar:

\[
C_D = C_{D0} + K C_L^2
\]

Optimization objective:

\[
\max x(t_f)
\]

subject to:

\[
h(t_f)=0
\]

---

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib

---

## Results

Example optimization output:

![Optimization Result](results.png)

---

## Run the Project

Install dependencies:

```bash
pip install numpy scipy matplotlib
```

Run:

```bash
python3 main.py
```

---

## Future Improvements

- RK4 integration
- Atmospheric density variation
- 3D trajectory optimization
- Closed-loop feedback control
- MPC guidance
- Reinforcement learning control

---

## Author

Tasbi Kaspiya Osrow