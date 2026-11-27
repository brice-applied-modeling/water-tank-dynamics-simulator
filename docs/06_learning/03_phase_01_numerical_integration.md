# Phase 01 Numerical Integration

Review the generic initial-value problem $dy/dt=f(t,y)$, with $y(t_0)=y_0$.

## Euler

$$
y_{n+1}=y_n+\Delta t f(t_n,y_n)
$$

Derive from the tangent-line approximation. Compute three steps by hand using a common benchmark. Review local truncation error, global error and stability.

## Heun

$$
y^*=y_n+\Delta t f(t_n,y_n)
$$

$$
y_{n+1}=y_n+\frac{\Delta t}{2}[f(t_n,y_n)+f(t_{n+1},y^*)]
$$

Explain the predictor and averaged slopes. Compute one step by hand.

## Classical RK4

$$
k_1=f(t_n,y_n)
$$

$$
k_2=f(t_n+\Delta t/2,y_n+\Delta t k_1/2)
$$

$$
k_3=f(t_n+\Delta t/2,y_n+\Delta t k_2/2)
$$

$$
k_4=f(t_n+\Delta t,y_n+\Delta t k_3)
$$

$$
y_{n+1}=y_n+\frac{\Delta t}{6}(k_1+2k_2+2k_3+k_4)
$$

Explain the four derivative evaluations and their weights. Compute one step by hand.

| Symbol | Meaning |
|---|---|
| $n$ | Step index |
| $t_n,t_{n+1}$ | Current and next time |
| $\Delta t$ | Step duration |
| $y_n,y_{n+1}$ | Current and next state |
| $y^*$ | Predicted state |
| $f(t,y)$ | Derivative function |
| $k_1,k_2,k_3,k_4$ | Stage derivatives, in state units per time |
| $t_0,y_0$ | Initial time and state |

All methods are unit-independent; time and derivatives must be compatible. For smooth problems, expected global orders are 1, 2 and 4 respectively. Study stability using exponential decay; distinguish stability from accuracy. Do not compare convergence across emptying events.

## SciPy RK45

Read [solve_ivp documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html). Review embedded error estimates, adaptive steps, `rtol`, `atol`, `t_eval`, event detection, and result diagnostics. Explain why requested output times are not internal steps. Absolute tolerance has state units; relative tolerance is dimensionless. Implement only an adapter, not RK45 itself.

Completion: explain each method, independently implement fixed-step methods, compare manual steps, and run the common benchmarks. Use smooth pre-emptying intervals until boundary handling is implemented.
