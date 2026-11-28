# Phase 01 Mathematical Review

Complete independently before implementing the hydraulic model. Show intermediate steps and verify results by differentiation or substitution. The exercises are mathematical examples with consistent abstract units unless stated otherwise.

## Derivatives

$$
f'(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}
$$

Here $x$ is the independent variable, $f$ is a differentiable function, $\Delta x$ is an increment, and the prime denotes a derivative. Review these rules:

| Rule | Equation |
|---|---|
| Constant | $\frac{d}{dx}c=0$ |
| Power | $\frac{d}{dx}x^n=nx^{n-1}$ |
| Constant multiple | $\frac{d}{dx}[cf(x)]=cf'(x)$ |
| Sum | $\frac{d}{dx}[f(x)+g(x)]=f'(x)+g'(x)$ |
| Chain | $\frac{d}{dx}f(g(x))=f'(g(x))g'(x)$ |
| Exponential | $\frac{d}{dx}e^{kx}=ke^{kx}$ |

$c,n,k$ are constants; $g$ is another differentiable function; $e$ is the base of natural logarithms. Apply rules on their valid domains.

Differentiate independently: $3x^2+5x-4$, $\sqrt{x}+6$, $(5-2x)^2$, and $e^{-0.2x}$. Explain why the chain rule matters for tank storage.

## Initial-value problems

$$
\frac{dy}{dt}=f(t,y)
$$

$$
y(t_0)=y_0
$$

$y$ is the dependent variable, $t$ is time, $f$ is the derivative function, $t_0$ is initial time and $y_0$ is initial state. Solve the constant, time-dependent and exponential benchmarks in [benchmark exercises](05_phase_01_benchmark_exercises.md).

## Separation of variables

$$
\frac{dy}{dt}=p(t)q(y)
$$

$$
\int_{y_0}^{y(t)}\frac{1}{q(u)}du=\int_{t_0}^{t}p(\tau)d\tau
$$

$p$ and $q$ are functions of time and state respectively; $u$ and $\tau$ are dummy integration variables. Separation requires nonzero $q$ on the integration interval; check equilibrium solutions separately.

Solve independently with initial time zero: $dy/dt=-3y$, $y_0=12$; $dy/dt=-2y^2$, $y_0=5$; $dy/dt=-0.5\sqrt{y}$, $y_0=16$; $dy/dt=2ty$, $y_0=4$. For the square-root problem, identify the valid interval and behavior at zero.

## Integration

| Rule | Equation |
|---|---|
| Constant | $\int c\,dx=cx+C$ |
| Power | $\int x^n dx=x^{n+1}/(n+1)+C$ |
| Logarithm | $\int dx/x=\ln\lvert x\rvert+C$ |
| Exponential | $\int e^{kx}dx=e^{kx}/k+C$ |
| Inverse square root | $\int dx/\sqrt{x}=2\sqrt{x}+C$ |

$C$ is an integration constant; $\ln$ denotes natural logarithm; absolute value denotes nonnegative magnitude. Power rule requires $n\ne-1$, exponential rule $k\ne0$, logarithmic rule $x\ne0$, and inverse square root $x>0$.

$$
\int_a^b f(x)dx=F(b)-F(a)
$$

$a,b$ are lower and upper limits and $F$ is an antiderivative of $f$.

Evaluate independently: $\int_0^5(10-2t)dt$, $\int_1^4 x^{-1/2}dx$, and $\int_0^{10}100e^{-0.1t}dt$. Interpret the last as gallons if flow is in gpm and time in minutes.

Completion: explain each concept, solve the exercises, and verify the solutions without generated code.
