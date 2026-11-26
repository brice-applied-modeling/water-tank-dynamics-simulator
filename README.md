# Water Tank Dynamics Simulator

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-ODE_Solvers-8CAAE6?logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)
![uv](https://img.shields.io/badge/uv-Package_Management-DE5FE9?logo=uv&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Testing_Framework-0A9EDC?logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Status-In_Development-orange)
![Domain](https://img.shields.io/badge/Domain-Scientific_Computing-64748B)
![Units](https://img.shields.io/badge/Units-US_Customary-blue)

## Overview

The Water Tank Dynamics Simulator is a scientific Python project exploring ordinary differential equations (ODEs), numerical integration, and time-dependent hydraulic behavior within municipal water infrastructure systems.

The project models the changing water depth in a tank subject to gravity drainage and, as an extension, external inflow. Its primary purpose is to develop practical knowledge of numerical methods by implementing solvers independently and verifying their results against analytical solutions.

The project combines three complementary activities:

- Development of reusable scientific computing software.
- Investigation of mathematical and numerical behavior through scientific experiments.
- Application of computational methods to practical municipal engineering problems.

All physical models and engineering analyses follow US customary and US municipal water and wastewater industry unit conventions.

## Project Scope and Progression

| Phase | Model | Mathematical Focus | Status |
|---|---|---|---|
| 01 | Water Tank Dynamics | First-order nonlinear ODEs | In development |
| 02 | Chlorine Decay and Mixing | First-order linear ODEs, reaction kinetics and mass balance | Future |
| 03 | Coupled Reservoir Dynamics | Systems of coupled ODEs | Future |

Phase 01 is the initial deliverable. Later phases will reuse the numerical integration and verification framework without expanding the MVP requirements.

Each phase includes an applied engineering project that demonstrates the practical application of the corresponding physical models and numerical methods.

## Engineering Unit Conventions

The simulator follows US customary engineering units and established US municipal water and wastewater industry practices.

Hydraulic calculations use a consistent foot-second computational system. Engineering inputs and reported results may use other customary industry units, provided that appropriate conversions are performed.

### Computational and Reporting Units

| Quantity | Internal Computational Unit | Engineering Reporting Unit |
|---|---|---|
| Length | ft | ft, in |
| Water depth | ft | ft |
| Elevation | ft | ft |
| Outlet diameter | ft | in |
| Area | ft² | ft² |
| Volume | ft³ | gal, MG |
| Flow rate | ft³/s (cfs) | cfs, gpm, MGD |
| Velocity | ft/s | fps |
| Acceleration | ft/s² | ft/s² |
| Time | s | s, min, hr, days |
| Pressure | lbf/ft², if required | psi |
| Pressure head | ft | ft |
| Mass density | lbm/ft³ | lbm/ft³ |
| Specific weight | lbf/ft³ | lbf/ft³ |
| Concentration | mg/L | mg/L |
| Chemical mass | lbm | lb |
| Chemical mass rate | lbm/s, if required | lb/day |
| Reaction coefficient | s⁻¹ | hr⁻¹, day⁻¹ |
| Numerical depth error | ft | ft, in |

Water quality concentrations remain in mg/L, consistent with US water and wastewater industry practices.

Numerical integration algorithms are unit-independent. Physical models are responsible for maintaining dimensional consistency.

### Physical Constants and Conversion Factors

| Constant or Conversion | Value |
|---|---:|
| Standard gravitational acceleration | 32.174 ft/s² |
| Nominal water mass density | 62.4 lbm/ft³ |
| Nominal water specific weight | 62.4 lbf/ft³ |
| Inches per foot | 12 |
| US gallons per cubic foot | 7.48052 |
| GPM per CFS | 448.831 |
| GPM per MGD | 694.444 |
| CFS per MGD | 1.54723 |
| Seconds per minute | 60 |
| Seconds per hour | 3,600 |
| Seconds per day | 86,400 |
| Gallons per million gallons | 1,000,000 |
| Approximate feet of water head per psi | 2.31 |
| Conventional water quality loading factor | 8.34 |

Water density, specific weight and pressure-head conversion values are nominal approximations and depend on fluid properties and temperature.

Physical constants and conversion factors are maintained in:

- `src/tank_dynamics/core/constants.py`
- `src/tank_dynamics/core/units.py`

## Mathematical Model (Phase 01)

Conservation of volume for an incompressible fluid gives:

$$
\frac{dV}{dt}=Q_{in}-Q_{out}
$$

For a tank with constant cross-sectional area:

$$
V=Ah
$$

Therefore:

$$
A\frac{dh}{dt}=Q_{in}-Q_{out}
$$

For a gravity outlet governed by Torricelli's law:

$$
Q_{out}=C_da\sqrt{2gh}
$$

Substituting the gravity discharge relationship into the conservation equation gives:

$$
\frac{dh}{dt}
=
\frac{Q_{in}(t)-C_da\sqrt{2gh}}{A}
$$

### Model Variables

| Symbol | Description | Computational Unit |
|---|---|---|
| $h$ | Water depth above outlet | ft |
| $h_0$ | Initial water depth | ft |
| $A$ | Tank cross-sectional area | ft² |
| $a$ | Outlet cross-sectional area | ft² |
| $d$ | Outlet diameter | ft |
| $V$ | Stored water volume | ft³ |
| $C_d$ | Discharge coefficient | Dimensionless |
| $g$ | Gravitational acceleration | ft/s² |
| $Q_{in}$ | Inflow rate | cfs |
| $Q_{out}$ | Outflow rate | cfs |
| $t$ | Elapsed time | s |
| $dh/dt$ | Rate of change in water depth | ft/s |

Outlet diameters specified in inches must be converted to feet before calculating outlet cross-sectional area.

### Analytical Solution

For zero inflow, the analytical solution is:

$$
h(t)=
\left[
\max\left(
0,
\sqrt{h_0}
-
\frac{C_da\sqrt{2g}}{2A}t
\right)
\right]^2
$$

The analytical solution provides an independent benchmark for numerical verification.

The zero-depth continuation represents the physical condition of an empty tank under zero inflow.

### Baseline Facility Parameters

| Parameter | Value | Unit |
|---|---:|---|
| Tank cross-sectional area | 100 | ft² |
| Initial water depth | 10.0 | ft |
| Outlet diameter | 3.0 | in |
| Discharge coefficient | 0.62 | Dimensionless |
| Gravitational acceleration | 32.174 | ft/s² |
| Initial inflow | 0 | cfs |
| Initial elapsed time | 0 | s |

These parameters establish the common baseline for Phase 01 development, scientific experiments, numerical verification and the applied engineering project.

## Learning Objectives

- Derive a first-order nonlinear ODE from physical conservation principles.
- Apply dimensional analysis using US customary engineering units.
- Implement fixed-step numerical integration methods from first principles.
- Apply adaptive integration using `scipy.integrate.solve_ivp`.
- Compare numerical accuracy, convergence and computational cost.
- Handle physical boundaries and tank-emptying events.
- Develop reusable hydraulic and unit conversion functions.
- Develop reproducible scientific experiments and automated verification tests.
- Apply verified computational methods to practical municipal engineering problems.
- Interpret computational results and communicate engineering findings.

## Planned Numerical Methods

| Method | Formal Global Error Order |
|---|---|
| Analytical solution | Exact under model assumptions |
| Forward Euler | First order |
| Heun's method | Second order |
| Classical Runge–Kutta (RK4) | Fourth order |
| SciPy RK45 | Adaptive embedded 5(4) method |

Formal convergence orders assume sufficient solution smoothness. Convergence studies will exclude the tank-emptying boundary when assessing these orders.

## Repository Organization

| Directory | Responsibility |
|---|---|
| `docs/` | Engineering requirements, mathematical models, architecture, research and learning documentation |
| `src/` | Reusable scientific computing software |
| `experiments/` | Scientific exploration and numerical investigations |
| `projects/` | Applied engineering analyses and presentation of findings |
| `outputs/` | Automatically generated simulation data, figures and tables |
| `tests/` | Automated numerical and physical model verification |

Scientific experiments and applied engineering projects consume the reusable functionality provided by the source package.

Generated outputs are excluded from version control by default. Selected final engineering figures and tables may be retained within the corresponding applied project directory.

## Documentation

### Project Overview and Architecture

| Document | Purpose |
|---|---|
| [Project Scope](docs/00_overview/01_project_scope.md) | Requirements, deliverables and roadmap |
| [Mathematical Model](docs/00_overview/02_mathematical_model.md) | Governing equations, assumptions and analytical derivation |
| [Numerical Methods](docs/00_overview/03_numerical_methods.md) | Integration algorithms and implementation requirements |
| [Verification](docs/00_overview/04_verification.md) | Benchmark cases, convergence studies and acceptance criteria |
| [Project Structure](docs/01_architecture/00_structure.md) | Repository organization, module responsibilities and dependency boundaries |

### Development and Applied Project Checklists

| Document | Purpose |
|---|---|
| [Phase 01 Development Checklist](docs/02_checklists/01_phase_01_checklist.md) | Independent scientific computing development and learning requirements |
| [Phase 01 Applied Project Checklist](docs/02_checklists/02_phase_01_applied_project_checklist.md) | Applied engineering analysis and deliverable requirements |

### Applied Engineering Projects

| Project | Purpose |
|---|---|
| [Phase 01: Municipal Storage Tank Drawdown](docs/05_applied_projects/01_phase_01_tank_drawdown.md) | Evaluate gravity drainage, maintenance planning and alternative outlet configurations |
| Phase 02: Chlorine Decay and Mixing | Future water quality modeling assignment |
| Phase 03: Coupled Reservoir Dynamics | Future interconnected storage modeling assignment |

## Development Environment

- Python 3.12
- uv for dependency and environment management
- NumPy and SciPy for scientific computing
- Matplotlib for visualization
- pytest for automated verification
- Spyder for interactive scientific development and experimentation

Spyder is the primary development environment for mathematical investigations, scientific calculations, numerical experiments and applied engineering analyses.

Applied project scripts may use Spyder's `# %%` cell delimiters to organize calculations into independently executable sections while retaining standard Python source files.

### Installation

Run the following from the repository root:

```bash
uv python install 3.12
uv sync
```

To initialize dependencies for the first time:

```bash
uv add numpy scipy matplotlib
uv add --dev pytest
```

Configure Spyder to use the repository's Python virtual environment and install a compatible version of `spyder-kernels` if required.

### Running Tests

Once the test suite is implemented:

```bash
uv run pytest
```

## Planned Scientific Experiments (Phase 01)

| Experiment | Objective |
|---|---|
| Gravity drainage | Compare numerical and analytical water-depth histories |
| Solver comparison | Quantify error, convergence and computational effort |
| Variable inflow | Explore dynamic response and equilibrium conditions (optional extension) |

Expected outputs include:

- Water depth versus elapsed time in feet and minutes.
- Gravity discharge versus elapsed time in gpm or cfs.
- Stored water volume versus elapsed time in gallons.
- Numerical depth error in feet or inches.
- Solver comparison plots.
- Numerical convergence plots.
- Emptying-time verification.
- Volume conservation results.

Scientific experiments are maintained in `experiments/phase_01/`.

## Phase 01 Applied Engineering Project

### Municipal Water Storage Tank Drawdown and Maintenance Drainage Analysis

The applied engineering project evaluates the time-dependent drainage behavior of a hypothetical municipal water storage tank that must be isolated and drained for inspection and maintenance.

### Operating Criteria

| Criterion | Value |
|---|---:|
| Maintenance planning window | 60 minutes |
| Residual-depth reporting threshold | 0.33 ft |
| Reporting interval | 5 minutes |
| Baseline outlet diameter | 3 in |
| Restricted outlet alternative | 2 in |
| Enlarged outlet alternative | 4 in |

### Engineering Objectives

- Determine initial stored water volume.
- Determine initial gravity discharge.
- Evaluate water depth, discharge and stored volume over time.
- Determine the time required to reach the residual-depth threshold.
- Determine theoretical complete drainage time.
- Evaluate compliance with the maintenance planning window.
- Compare alternative outlet configurations.
- Evaluate the limitations of a constant-discharge approximation.
- Recommend an appropriate numerical integration method.
- Document engineering findings, assumptions and limitations.

### Applied Project Deliverables

| Deliverable | Responsibility |
|---|---|
| `01_baseline_analysis.py` | Baseline tank drainage analysis |
| `02_numerical_verification.py` | Numerical accuracy, convergence and conservation assessment |
| `03_outlet_alternatives.py` | Comparison of alternative outlet configurations |
| `04_variable_inflow.py` | Optional inflow and equilibrium analysis |
| `05_final_analysis.py` | Consolidated engineering results |
| `findings.md` | Engineering interpretation, recommendations and limitations |
| `figures/` | Selected final engineering figures |
| `tables/` | Selected final engineering results tables |

Applied project deliverables are maintained in `projects/phase_01/`.

## Development Roadmap

### Phase 01: Water Tank Dynamics (MVP)

- [ ] Establish mathematical model and analytical benchmark.
- [ ] Establish US customary engineering constants and unit conversions.
- [ ] Implement reusable tank geometry and gravity discharge functions.
- [ ] Implement Forward Euler and Heun solvers.
- [ ] Implement RK4 and SciPy RK45 integration.
- [ ] Establish physical boundary and event-handling conventions.
- [ ] Verify results and perform convergence studies.
- [ ] Complete scientific experiments.
- [ ] Complete the municipal storage tank drawdown applied project.
- [ ] Document findings and limitations.
- [ ] Explore variable inflow and equilibrium behavior (optional).

### Phase 02: Chlorine Decay and Mixing (Future)

Extend the simulator to model chlorine concentration in a completely mixed tank using first-order reaction kinetics.

For a constant-volume tank with balanced inflow and outflow, constant flow rate $Q$, and first-order decay coefficient $k$:

$$
\frac{dC}{dt}
=
\frac{Q}{V}(C_{in}-C)-kC
$$

| Symbol | Description | Computational Unit |
|---|---|---|
| $C$ | Tank chlorine concentration | mg/L |
| $C_0$ | Initial chlorine concentration | mg/L |
| $C_{in}$ | Influent chlorine concentration | mg/L |
| $Q$ | Balanced inflow and outflow rate | cfs |
| $V$ | Constant tank volume | ft³ |
| $k$ | First-order decay coefficient | s⁻¹ |
| $t$ | Elapsed time | s |
| $dC/dt$ | Rate of concentration change | (mg/L)/s |

Flow and volume must use compatible units so that $Q/V$ has units of inverse time.

Reaction coefficients specified in hr⁻¹ or day⁻¹ must be converted to s⁻¹ before numerical integration.

The initial closed-tank benchmark ($Q=0$) is:

$$
C(t)=C_0e^{-kt}
$$

#### Chemical Mass Loading

For engineering reporting, chemical mass loading may be calculated using the conventional US water and wastewater industry relationship:

$$
W=8.34QC
$$

where:

| Symbol | Description | Unit |
|---|---|---|
| $W$ | Chemical mass loading | lb/day |
| $Q$ | Flow rate | MGD |
| $C$ | Chemical concentration | mg/L |

The 8.34 conversion factor applies specifically to the stated combination of reporting units.

For a stored constituent mass:

$$
M=8.34VC
$$

where $M$ is constituent mass in pounds, $V$ is stored volume in million gallons, and $C$ is concentration in mg/L.

#### Development Objectives

- [ ] Derive the chlorine mass balance and analytical benchmarks.
- [ ] Simulate batch decay and constant-volume flow-through mixing.
- [ ] Investigate decay coefficients, residence time and equilibrium concentration.
- [ ] Verify concentration histories and constituent mass balance.
- [ ] Evaluate chemical mass loading and stored constituent mass.
- [ ] Complete scientific experiments.
- [ ] Complete a water quality applied engineering project.

### Phase 03: Coupled Reservoir Dynamics (Future)

Extend the framework to interconnected tanks with simultaneous changes in water depth.

For two constant-area tanks with a submerged connection and an external outlet from tank 2:

$$
\begin{aligned}
A_1\frac{dh_1}{dt}&=Q_{in}-Q_{12}\\
A_2\frac{dh_2}{dt}&=Q_{12}-Q_{out}
\end{aligned}
$$

For a quasi-steady connection between tanks with a common elevation datum and atmospheric free surfaces, a simplified bidirectional flow law is:

$$
Q_{12}
=
C_da\operatorname{sgn}(h_1-h_2)
\sqrt{2g|h_1-h_2|}
$$

| Symbol | Description | Computational Unit |
|---|---|---|
| $A_1$ | Tank 1 cross-sectional area | ft² |
| $A_2$ | Tank 2 cross-sectional area | ft² |
| $h_1$ | Tank 1 water surface head relative to common datum | ft |
| $h_2$ | Tank 2 water surface head relative to common datum | ft |
| $a$ | Connection cross-sectional area | ft² |
| $C_d$ | Connection discharge coefficient | Dimensionless |
| $Q_{in}$ | External inflow | cfs |
| $Q_{12}$ | Signed inter-tank flow | cfs |
| $Q_{out}$ | External discharge | cfs |
| $g$ | Gravitational acceleration | ft/s² |
| $t$ | Elapsed time | s |

This relationship assumes both water surface heads are measured from the same elevation datum and the connection remains submerged.

The state vector is:

$$
\mathbf{y}=[h_1,h_2]^T
$$

#### Development Objectives

- [ ] Apply and verify the existing vector-compatible numerical solvers.
- [ ] Model inter-tank flow, external inflow and discharge.
- [ ] Investigate equalization, equilibrium and flow reversal.
- [ ] Verify conservation of total stored volume.
- [ ] Compare numerical results against independent reference solutions.
- [ ] Complete scientific experiments.
- [ ] Complete an interconnected storage applied engineering project.

## Numerical Architecture

Physical models are maintained separately from numerical integration algorithms.

The generic initial-value problem is:

$$
\frac{d\mathbf{y}}{dt}=f(t,\mathbf{y})
$$

Use a common derivative interface, `f(t, y)`, with model parameters supplied independently.

### Numerical Conventions

| Convention | Requirement |
|---|---|
| Time | Seconds internally |
| State vector | One-dimensional NumPy array |
| State shape | `(n_states,)` |
| Time history shape | `(n_times,)` |
| State history shape | `(n_times, n_states)` |
| Hydraulic computational units | Feet, cubic feet and seconds |
| Concentration | mg/L |
| Reaction coefficients | s⁻¹ |
| Numerical solvers | Unit-independent |
| Physical boundaries | Managed by physical models and simulation orchestration |
| Unit conversions | Managed by the core package |

Even scalar physical models use a one-dimensional state array containing a single state variable.

Numerical solvers must support both scalar and vector-valued physical models without embedding tank-specific physics in the integration routines.

Physical boundary handling and event definitions belong to the model or simulation layer.

## Engineering Relevance

The underlying mathematical and computational methods are applicable to:

- Wet-well dynamics.
- Water storage tank operations.
- Reservoir operations.
- Hydraulic storage and attenuation.
- Pump control and operating scenarios.
- Disinfectant residual modeling.
- Constituent mass balance.
- Interconnected storage systems.
- Infrastructure operational planning.
- Infrastructure decision analytics.

The project provides a foundation for more advanced dynamic simulation and applied scientific computing within municipal water and wastewater engineering.

## Limitations

This is an educational scientific computing project, not a production engineering design tool.

The baseline model assumes:

- A rigid tank.
- Constant cross-sectional area.
- Incompressible fluid.
- Quasi-steady orifice discharge.
- Atmospheric pressure at the free surface and outlet.
- Constant discharge coefficient.
- No downstream backwater.
- No detailed outlet piping losses.

The project does not model water hammer, pipe-network transients, detailed pump hydraulics or full distribution-system behavior.

Applied engineering scenarios are hypothetical and do not constitute approved engineering designs, maintenance procedures or personnel-entry authorization.

## References

- [SciPy: solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Spyder Documentation](https://docs.spyder-ide.org/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [pytest Documentation](https://docs.pytest.org/)