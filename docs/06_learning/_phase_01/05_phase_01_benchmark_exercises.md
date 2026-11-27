# Phase 01 Common Benchmark Exercises

These are proposed mathematical test problems, not facility data. Derive analytical solutions independently before running numerical methods. Use abstract consistent units for time and state; coefficients carry the units necessary for the stated derivative.

| Benchmark | ODE | Initial state at t=0 | End time |
|---|---|---|---:|
| Constant | $dy/dt=2$ | 5 | 2 |
| Zero | $dy/dt=0$ | 10 | 2 |
| Time-dependent | $dy/dt=3t^2$ | 5 | 2 |
| Exponential | $dy/dt=-0.2y$ | 10 | 2 |
| Nonlinear | $dy/dt=-0.5\sqrt{y}$ | 16 | 2 |
| Vector component 1 | $dy_1/dt=-y_1$ | 10 | 2 |
| Vector component 2 | $dy_2/dt=-2y_2$ | 5 | 2 |

$y$ is scalar state; $y_1,y_2$ are components of one two-state problem; $t$ is time. The vector components are independent but must be integrated together in one solver call. The nonlinear benchmark interval is strictly before emptying.

## Procedure

1. Derive each reference solution and verify its derivative and initial condition.
2. Use proposed fixed steps 0.2, 0.1, 0.05 and 0.025 for smooth convergence tests; use a separate non-divisible step such as 0.3 to test final partial steps.
3. Manually compute the first three Euler steps and one Heun and RK4 step for exponential decay.
4. Compare all methods at common output times, including RK45 with documented tolerances.
5. Test result shapes, preservation of initial state, exact final time within floating-point tolerance, and invalid inputs.
6. Use exponential and time-dependent benchmarks for convergence; exact or nearly exact constant/zero results are not useful for estimating order. Avoid roundoff-dominated errors.
7. Record expected values, actual values, tolerances, pass/fail and explanation. Do not use SciPy as the exact reference.

The separate hydraulic benchmark uses the facility parameters in the development checklist. No analytical answers or implementation code are supplied here.
