# Water Tank Dynamics — Mathematical Model

## Physical system and assumptions

Consider a tank with a constant horizontal cross-sectional area, an inlet, and a gravity discharge orifice at its base.

Assumptions:

- Water is incompressible.
- Tank cross-sectional area is constant.
- Tank and outlet discharge are at atmospheric pressure.
- Water surface velocity is negligible relative to outlet velocity.
- Discharge coefficient is constant.
- Outflow is quasi-steady and follows Torricelli's law.
- No evaporation, leakage, overflow, or transient pipe effects are modeled.
- Internal calculations use SI units.

### Model parameters

| Symbol | Description | Units | Baseline value |
|---|---|---|---:|
| $A$ | Tank cross-sectional area | m² | 10 |
| $h_0$ | Initial water depth above outlet | m | 3 |
| $d$ | Outlet diameter | m | 0.075 |
| $a$ | Outlet area | m² | $\pi d^2/4$ |
| $C_d$ | Discharge coefficient | dimensionless | 0.62 |
| $g$ | Gravitational acceleration | m/s² | 9.81 |
| $Q_{in}(t)$ | Inflow | m³/s | 0 |
| $t$ | Elapsed time | s | 0 initially |

## Mathematical model

### Conservation of volume

For an incompressible fluid:

$$
\frac{dV}{dt}=Q_{in}(t)-Q_{out}(t)
$$

For a constant-area tank:

$$
V=Ah, \qquad \frac{dV}{dt}=A\frac{dh}{dt}
$$

### Gravity discharge

Using Torricelli's law with a discharge coefficient:

$$
Q_{out}=C_da\sqrt{2gh}
$$

### Governing ODE

$$
\boxed{\frac{dh}{dt}=\frac{Q_{in}(t)-C_da\sqrt{2gh}}{A}}
$$

Initial condition:

$$
h(0)=h_0
$$

This is a first-order nonlinear initial-value problem. The square-root term makes the equation nonlinear in water depth.

### Analytical solution: gravity drainage

For zero inflow, define:

$$
k=\frac{C_da\sqrt{2g}}{A}
$$

Then:

$$
\frac{dh}{dt}=-k\sqrt{h}
$$

Separate variables and integrate:

$$
\int_{h_0}^{h(t)}\frac{dh}{\sqrt{h}}=-k\int_0^t dt
$$

$$
2\sqrt{h(t)}-2\sqrt{h_0}=-kt
$$

The physically valid solution, including the empty-tank condition, is:

$$
h(t)=\left[\max\left(0,\sqrt{h_0}-\frac{kt}{2}\right)\right]^2
$$

The theoretical emptying time is:

$$
t_{empty}=\frac{2\sqrt{h_0}}{k}=\frac{2A\sqrt{h_0}}{C_da\sqrt{2g}}
$$

For the baseline parameters, the initial volume is 30 m³ and the emptying time is approximately 47.59 minutes.

### Constant-inflow equilibrium (extension)

At equilibrium, inflow equals outflow and the derivative is zero:

$$
h_{eq}=\frac{1}{2g}\left(\frac{Q_{in}}{C_da}\right)^2
$$

For positive constant inflow, depths above equilibrium decrease and depths below equilibrium increase, assuming the tank does not overflow.


## References

- [Project scope](01_project_scope.md)
- [Numerical methods](03_numerical_methods.md)
- [MIT Differential Equations](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/)
