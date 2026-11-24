# Water Tank Dynamics — Numerical Methods

## Numerical integration methods

Implement the fixed-step methods independently before introducing SciPy.

Let $f(t,h)$ denote the governing ODE and $\Delta t$ the integration time step.

### Forward Euler

$$
h_{n+1}=h_n+\Delta t f(t_n,h_n)
$$

### Heun's method (improved Euler)

$$
\tilde h=h_n+\Delta t f(t_n,h_n)
$$

$$
h_{n+1}=h_n+\frac{\Delta t}{2}[f(t_n,h_n)+f(t_n+\Delta t,\tilde h)]
$$

### Classical fourth-order Runge-Kutta (RK4)

$$
\begin{aligned}
k_1&=f(t_n,h_n)\\
k_2&=f(t_n+\Delta t/2,h_n+\Delta t k_1/2)\\
k_3&=f(t_n+\Delta t/2,h_n+\Delta t k_2/2)\\
k_4&=f(t_n+\Delta t,h_n+\Delta t k_3)\\
h_{n+1}&=h_n+\frac{\Delta t}{6}(k_1+2k_2+2k_3+k_4)
\end{aligned}
$$

### SciPy adaptive RK45

Use `scipy.integrate.solve_ivp()` with `method="RK45"`, explicit relative and absolute tolerances, and an empty-tank terminal event for gravity drainage.

| Method | Nominal global error order | Purpose |
|---|---|---|
| Analytical | Exact under assumptions | Independent reference |
| Euler | First | Basic numerical integration |
| Heun | Second | Predictor-corrector integration |
| RK4 | Fourth | Higher-order fixed-step integration |
| SciPy RK45 | Adaptive embedded 5(4) | Numerical reference and comparison |

These convergence orders assume sufficient solution smoothness. Measure formal convergence on an interval strictly before the tank empties, because the square-root right-hand side is not smooth at zero depth.

### Physical boundaries and numerical safeguards

- Validate positive tank area, gravity, outlet diameter, and discharge coefficient.
- Reject negative initial depths and invalid time steps.
- Prevent square-root evaluations at negative depths, including intermediate RK stages.
- For zero inflow, detect emptying, stop drainage, and keep subsequent depths at zero.
- Document any clipping, step reduction, or event interpolation used near the boundary.
- For positive inflow, allow the tank to refill from zero depth.
- Do not silently treat clipping as proof of numerical accuracy.


## Implementation contract

Use a generic derivative function and return time and state arrays. Shorten the final step to land exactly on the requested end time. Keep tank-specific boundary handling separate from generic integration where practical. For RK45, report solver status and tolerances; event detection at zero can be delicate because the analytical depth touches zero with zero slope. Check emptying time independently and document the detection threshold or interpolation method.

## References

- [Mathematical model](02_mathematical_model.md)
- [SciPy solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
