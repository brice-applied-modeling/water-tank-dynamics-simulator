# Project Structure

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