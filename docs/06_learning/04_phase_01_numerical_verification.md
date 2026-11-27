# Phase 01 Numerical Verification

## Error and convergence

$$
e_i=|y_i-\hat{y}_i|
$$

$$
E_{max}=\max_i(e_i)
$$

$$
RMSE=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y}_i)^2}
$$

$$
p=\frac{\ln(E_1/E_2)}{\ln(\Delta t_1/\Delta t_2)}
$$

| Symbol | Definition | Unit |
|---|---|---|
| $y_i,\hat{y}_i$ | Numerical and analytical depth at matched sample | ft |
| $e_i,E_{max},RMSE$ | Absolute, maximum absolute and root mean square error | ft or in consistently |
| $i,N$ | Sample index and number of samples | Dimensionless |
| $E_1,E_2$ | Same error metric at two step sizes | ft or in consistently |
| $\Delta t_1,\Delta t_2$ | Two distinct step sizes | s, min |
| $p$ | Observed convergence order | Dimensionless |

Absolute value gives magnitude; max selects the largest value; sum adds all indexed terms; ln is natural logarithm. Use positive errors for order calculations. Avoid relative error near zero. Expected error reduction on halving the step is approximately 2, 4 and 16 for Euler, Heun and RK4 in the smooth asymptotic regime.

## Conservation and quadrature

$$
R_V=V(t)-V(0)-\int_0^t[Q_{in}(\tau)-Q_{out}(\tau)]d\tau
$$

$$
\int_a^b f(x)dx\approx\sum_{j=0}^{M-1}\frac{x_{j+1}-x_j}{2}[f(x_j)+f(x_{j+1})]
$$

| Symbol | Definition | Unit |
|---|---|---|
| $R_V$ | Volume balance residual | gal, ft³ |
| $V(t),V(0)$ | Current and initial volume | gal, ft³ |
| $Q_{in},Q_{out}$ | Inflow and outflow | gpm, cfs |
| $t,\tau$ | Elapsed time and integration variable | min, s |
| $a,b$ | Integration limits | Problem-dependent |
| $x_j,x_{j+1}$ | Adjacent integration samples | Problem-dependent |
| $f(x_j)$ | Integrand at sample | Problem-dependent |
| $j,M$ | Interval index and number of intervals | Dimensionless |

The trapezoidal sum uses M intervals and M+1 samples. Use gpm with minutes for gallons or cfs with seconds for ft³; convert when necessary. Quadrature has its own error and can mask solver accuracy. Refine quadrature or compare to an independent integral where available.

## Assignment

Choose tolerances before final runs. Compare at matched times over a common smooth interval using at least four successively halved steps. Calculate error metrics and observed orders, plot log-log convergence, and explain departures. Separately compare emptying time and conservation residuals. Record derivative evaluations and repeat timings if making performance claims. Report failed tests rather than hiding them.
