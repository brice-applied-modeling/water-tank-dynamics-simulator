# Water Tank Dynamics — Project Scope

## Project overview

Develop a small Python-based scientific computing application to simulate the time-dependent water depth in a tank using ordinary differential equations (ODEs).

The primary objective is to understand differential equations, numerical integration, and computational verification through a familiar civil engineering problem. This is an educational simulator, not a production hydraulic design tool.

**Repository:** `water-tank-dynamics`  
**Estimated effort:** 9–14 hours  
**Language:** Python 3.12  
**Environment:** uv, Spyder, NumPy, SciPy, Matplotlib, pytest

## Learning objectives

- Translate physical conservation laws into ODEs.
- Derive analytical solutions for separable first-order nonlinear ODEs.
- Implement numerical integration algorithms independently.
- Compare fixed-step and adaptive-step solvers.
- Evaluate numerical error, convergence, and computational performance.
- Perform parameter sensitivity and scenario analysis.
- Develop reusable scientific Python modules and automated tests.

## Repository structure

```text
water-tank-dynamics/
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── docs/
│   ├── 01_project_scope.md
│   ├── 02_mathematical_model.md
│   ├── 03_numerical_methods.md
│   └── 04_verification.md
├── src/
│   └── tank_dynamics/
│       ├── __init__.py
│       ├── tank.py
│       ├── equations.py
│       ├── analytical.py
│       ├── simulation.py
│       ├── visualization.py
│       └── solvers/
│           ├── __init__.py
│           ├── euler.py
│           ├── heun.py
│           ├── rk4.py
│           └── scipy_solver.py
├── experiments/
│   ├── 01_gravity_drainage.py
│   ├── 02_solver_comparison.py
│   └── 03_variable_inflow.py
└── tests/
    ├── test_equations.py
    ├── test_analytical.py
    └── test_solvers.py
```

Keep solvers independent of the tank physics where practical. A generic solver should accept a derivative function, initial condition, time interval, and step size.

## Environment setup

```bash
uv init --lib --python 3.12 water-tank-dynamics
cd water-tank-dynamics
uv add numpy scipy matplotlib
uv add --dev pytest
uv run pytest
```

Adjust the generated package name and build configuration to match `tank_dynamics`. Use Spyder for interactive experiments and the repository modules for reusable implementation.

## Development roadmap

| Phase | Scope | Estimated effort |
|---|---|---:|
| 1 | Mathematical derivation and analytical solution | 1–2 h |
| 2 | Euler and Heun solvers | 2–3 h |
| 3 | RK4 and SciPy RK45 | 2–3 h |
| 4 | Verification, convergence and error analysis | 2–3 h |
| 5 | Variable inflow and equilibrium analysis | 2–3 h |
| | **Total** | **9–14 h** |

### MVP definition of done

- [ ] Complete Phases 1–4.
- [ ] Implement and document all four numerical solvers.
- [ ] Produce analytical and numerical comparison plots.
- [ ] Produce a convergence study and verification summary.
- [ ] Pass automated tests.
- [ ] Provide reproducible setup and execution instructions in README.

Phase 5 is optional. Do not expand the MVP into a full hydraulic network simulator, GUI, digital twin, or web application.

## Future ODE learning projects

| Project | Mathematical focus | Engineering application |
|---|---|---|
| Chlorine decay | First-order linear ODEs | Water quality and reaction kinetics |
| Contaminant mixing | Mass balance and time-dependent forcing | Treatment and storage |
| Coupled tanks | Systems of nonlinear ODEs | Interconnected reservoirs |
| Mass-spring-damper | Second-order ODEs | Structural dynamics |
| Rainfall-runoff reservoir | Forced first-order ODEs | Hydrologic response |
| Pump-controlled wet well | Piecewise dynamics and event detection | Pump cycling and operational simulation |

## Relationship to infrastructure modeling

The Hydraulic Analysis Suite focuses primarily on steady-state hydraulic calculations. This standalone project introduces time-dependent physical behavior and numerical integration. Its methods may later support wet-well dynamics, pump operating cycles, reservoir operation, scenario analysis, and digital twin simulations.

## Guiding principle

The objective is to learn differential equations through scientific programming, not simply learn how to call a library solver. Derive the mathematics, implement the algorithms, verify the results, and only then extend the physical model.

## Supporting documentation

- [Mathematical model](02_mathematical_model.md)
- [Numerical methods](03_numerical_methods.md)
- [Verification](04_verification.md)
