# Water Tank Dynamics Simulator

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-ODE_Solvers-8CAAE6?logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)
![uv](https://img.shields.io/badge/uv-Package_Management-DE5FE9?logo=uv&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Testing_Framework-0A9EDC?logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Status-Planned-orange)
![Domain](https://img.shields.io/badge/Domain-Scientific_Computing-64748B)

## Overview

The Water Tank Dynamics Simulator is a small scientific Python project exploring ordinary differential equations (ODEs), numerical integration, and time-dependent hydraulic behavior.

The project models the changing water depth in a tank subject to gravity drainage and, as an extension, external inflow. Its primary purpose is to develop practical knowledge of numerical methods by implementing solvers independently and verifying their results against an analytical solution.

## Project scope and progression

| Phase | Model | Mathematical focus | Status |
|---|---|---|---|
| 01 | Water Tank Dynamics | First-order nonlinear ODEs | MVP planned |
| 02 | Chlorine Decay and Mixing | First-order linear ODEs, reaction kinetics and mass balance | Future |
| 03 | Coupled Reservoir Dynamics | Systems of coupled ODEs | Future |

Phase 01 is the initial deliverable. Later phases will reuse the numerical integration and verification framework without expanding the MVP requirements.

## Mathematical model (Phase 01)

Conservation of volume for an incompressible fluid gives:

$$
\frac{dV}{dt}=Q_{in}-Q_{out}
$$

For a tank with constant cross-sectional area and a gravity outlet governed by Torricelli's law:

$$
\frac{dh}{dt}=\frac{Q_{in}(t)-C_d a\sqrt{2gh}}{A}
$$

where:

| Symbol | Description | SI unit |
|---|---|---|
| $h$ | Water depth above outlet | m |
| $A$ | Tank cross-sectional area | m² |
| $a$ | Outlet cross-sectional area | m² |
| $C_d$ | Discharge coefficient | Dimensionless |
| $g$ | Gravitational acceleration | m/s² |
| $Q_{in}$ | Inflow rate | m³/s |
| $t$ | Elapsed time | s |

For zero inflow, the analytical solution is:

$$
h(t)=\left[\max\left(0,\sqrt{h_0}-\frac{C_da\sqrt{2g}}{2A}t\right)\right]^2
$$

This solution provides an independent benchmark for numerical verification.

## Learning objectives

- Derive a first-order nonlinear ODE from physical conservation principles.
- Implement fixed-step numerical integration methods from first principles.
- Apply adaptive integration using `scipy.integrate.solve_ivp`.
- Compare numerical accuracy, convergence and computational cost.
- Handle physical boundaries and tank-emptying events.
- Develop reproducible scientific experiments and automated verification tests.

## Planned numerical methods

| Method | Formal global error order |
|---|---|
| Analytical solution | Exact under model assumptions |
| Forward Euler | First order |
| Heun's method | Second order |
| Classical Runge–Kutta (RK4) | Fourth order |
| SciPy RK45 | Adaptive embedded 5(4) method |

Formal convergence orders assume sufficient solution smoothness; convergence studies will exclude the tank-emptying boundary when assessing these orders.

## Documentation

| Document | Purpose |
|---|---|
| [Project scope](docs/00_overview/01_project_scope.md) | Requirements, deliverables, roadmap and repository organization |
| [Mathematical model](docs/00_overview/02_mathematical_model.md) | Governing equations, assumptions and analytical derivation |
| [Numerical methods](docs/00_overview/03_numerical_methods.md) | Integration algorithms and implementation requirements |
| [Verification](docs/00_overview/04_verification.md) | Benchmark cases, convergence studies and acceptance criteria |
| [Project Structure](docs/01_architecture/00_structure.md) | Documents project repository structure |

## Development environment

- Python 3.12
- uv for dependency and environment management
- NumPy and SciPy for scientific computing
- Matplotlib for visualization
- pytest for automated verification
- Spyder (optional) for interactive scientific experimentation

### Installation

Once the repository and its `pyproject.toml` are initialized, run the following from the repository root:

```bash
uv python install 3.12
uv sync
```

If initializing dependencies for the first time:

```bash
uv add numpy scipy matplotlib
uv add --dev pytest
```

### Running tests

Once the test suite is implemented:

```bash
uv run pytest
```

## Planned experiments (Phase 01)

| Experiment | Objective |
|---|---|
| Gravity drainage | Compare numerical and analytical water-depth histories |
| Solver comparison | Quantify error, convergence and computational effort |
| Variable inflow | Explore dynamic response and equilibrium conditions (extension) |

Expected outputs include water-depth and discharge time series, solver comparison plots, error metrics, convergence plots and benchmark results.

## Development roadmap

### Phase 01: Water Tank Dynamics (MVP)

- [ ] Establish mathematical model and analytical benchmark.
- [ ] Implement Forward Euler and Heun solvers.
- [ ] Implement RK4 and SciPy RK45 integration.
- [ ] Verify results and perform convergence studies.
- [ ] Document findings and limitations.
- [ ] Explore variable inflow and equilibrium behavior (optional).

### Phase 02: Chlorine Decay and Mixing (future)

Extend the simulator to model chlorine concentration in a completely mixed tank using first-order reaction kinetics. For a constant-volume tank with balanced inflow and outflow, constant flow rate $Q$, and first-order decay coefficient $k$:

$$
\frac{dC}{dt}=\frac{Q}{V}(C_{in}-C)-kC
$$

Here, $C$ is tank concentration, $C_{in}$ is influent concentration, and $V$ is tank volume. The initial closed-tank benchmark ($Q=0$) is:

$$
C(t)=C_0e^{-kt}
$$

- [ ] Derive the chlorine mass balance and analytical benchmarks.
- [ ] Simulate batch decay and constant-volume flow-through mixing.
- [ ] Investigate decay coefficients, residence time and equilibrium concentration.
- [ ] Verify concentration histories and mass balance.

### Phase 03: Coupled Reservoir Dynamics (future)

Extend the framework to interconnected tanks with simultaneous changes in water depth. For two constant-area tanks with a submerged connection and an external outlet from tank 2:

$$
\begin{aligned}
A_1\frac{dh_1}{dt}&=Q_{in}-Q_{12}\\
A_2\frac{dh_2}{dt}&=Q_{12}-Q_{out}
\end{aligned}
$$

For a quasi-steady connection between tanks with a common elevation datum and atmospheric free surfaces, a simplified bidirectional flow law is:

$$
Q_{12}=C_d a\,\operatorname{sgn}(h_1-h_2)\sqrt{2g|h_1-h_2|}
$$

This assumes both depths are measured from the same datum and the connection remains submerged. The state vector is $\mathbf{y}=[h_1,h_2]^T$.

- [ ] Extend numerical solvers to vector-valued states.
- [ ] Model inter-tank flow, external inflow and discharge.
- [ ] Investigate equalization, equilibrium and flow reversal.
- [ ] Verify conservation of total stored volume and compare against reference solutions.

## Numerical architecture

Keep physical models separate from numerical integration algorithms. Use a common derivative interface, `f(t, y)`, with model parameters supplied independently. Design solvers to support scalar and, eventually, NumPy array states without embedding tank-specific physics in the integration routines. Physical boundary handling and event definitions belong to the model or simulation layer.

## Engineering relevance

The underlying methods are applicable to wet-well dynamics, reservoir operations, hydraulic storage, pump control, disinfectant residual modeling and other time-dependent infrastructure processes. The project provides a foundation for more advanced dynamic simulation and infrastructure decision analytics.

## Limitations

This is an educational scientific computing project, not a production engineering design tool. The baseline assumes a rigid tank, constant cross-sectional area, incompressible fluid, quasi-steady orifice discharge and atmospheric pressure at the free surface and outlet. It does not model water hammer, pipe-network transients or detailed pump hydraulics.

## References

- [SciPy: solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [NumPy documentation](https://numpy.org/doc/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [uv documentation](https://docs.astral.sh/uv/)
- [pytest documentation](https://docs.pytest.org/)
