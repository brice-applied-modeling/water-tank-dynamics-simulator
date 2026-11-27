# Project Structure

> **Status:** Planned full-build architecture. Phase 01 is the MVP; Phases 02 and 03 are future extensions. Paths below are target paths, not a claim that files already exist.

## 1. Purpose

This document defines repository organization, module responsibilities, dependency boundaries and implementation sequencing for the Water Tank Dynamics Simulator, including scientific experiments, applied engineering deliverables and generated results. The project progresses from scalar nonlinear ODEs to linear reaction and mixing models and finally coupled reservoir systems.

## 2. Full-build repository tree

```text
water-tank-dynamics/
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .python-version
├── docs/
│   ├── 00_overview/
│   │   ├── 01_project_scope.md
│   │   ├── 02_mathematical_model.md
│   │   ├── 03_numerical_methods.md
│   │   └── 04_verification.md
│   ├── 01_architecture/
│   │   └── 00_structure.md
│   ├── 02_checklists/
│   │   └── 01_phase_01_checklist.md
│   ├── 03_research/
│   ├── 04_logs/
│   │   ├── 00_scientific_log_template.md
│   │   ├── 01_learning_log_template.md
│   │   ├── phase_01/
│   │   │   └── YYYYMMDD_session_001.md
│   │   ├── phase_02/
│   │   └── phase_03/
│   └── 05_applied_projects/
│       └── 01_phase_01_tank_drawdown.md
│
├── src/
│   └── tank_dynamics/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── single_tank/
│       │   │   ├── __init__.py
│       │   │   ├── tank.py
│       │   │   ├── parameters.py
│       │   │   ├── equations.py
│       │   │   ├── analytical.py
│       │   │   └── events.py
│       │   ├── chlorine/
│       │   │   ├── __init__.py
│       │   │   ├── decay.py
│       │   │   ├── mixing.py
│       │   │   ├── parameters.py
│       │   │   ├── equations.py
│       │   │   └── analytical.py
│       │   └── coupled_reservoirs/
│       │       ├── __init__.py
│       │       ├── reservoir.py
│       │       ├── system.py
│       │       ├── connection.py
│       │       ├── parameters.py
│       │       ├── equations.py
│       │       ├── analytical.py
│       │       └── events.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── constants.py
│       │   ├── units.py
│       │   ├── types.py
│       │   ├── exceptions.py
│       │   ├── protocols.py
│       │   └── validation.py
│       ├── hydraulics/
│       │   ├── __init__.py
│       │   ├── geometry.py
│       │   ├── discharge.py
│       │   └── flow.py
│       ├── solvers/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── euler.py
│       │   ├── heun.py
│       │   ├── rk4.py
│       │   └── scipy_solver.py
│       ├── simulation/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── runner.py
│       │   ├── state.py
│       │   ├── events.py
│       │   └── results.py
│       ├── analysis/
│       │   ├── __init__.py
│       │   ├── error_metrics.py
│       │   ├── convergence.py
│       │   ├── stability.py
│       │   ├── conservation.py
│       │   ├── equilibrium.py
│       │   ├── sensitivity.py
│       │   └── benchmarking.py
│       └── visualization/
│           ├── __init__.py
│           ├── time_series.py
│           ├── hydraulics.py
│           ├── concentration.py
│           ├── phase_space.py
│           ├── convergence.py
│           └── comparison.py
│
├── experiments/                        # Scientific exploration, numerical investigations and learning
│   ├── phase_01/
│   │   ├── 01_gravity_drainage.py
│   │   ├── 02_solver_comparison.py
│   │   └── 03_variable_inflow.py
│   ├── phase_02/
│   │   ├── 01_batch_decay.py
│   │   ├── 02_continuous_mixing.py
│   │   └── 03_decay_sensitivity.py
│   └── phase_03/
│       ├── 01_closed_equalization.py
│       ├── 02_forced_reservoirs.py
│       └── 03_flow_reversal.py
│
├── review/
│   ├── README.md
│   ├── phase_01/
│   │   ├── 01_mathematical_review.py
│   │   ├── 02_hydraulic_foundations.py
│   │   ├── 03_numerical_integration.py
│   │   ├── 04_numerical_verification.py
│   │   └── 05_benchmark_exercises.py
│   ├── phase_02/
│   └── phase_03/
│
├── projects/                               # Completed applied engineering assignments and presentation of findings
│   ├── README.md
│   │
│   ├── phase_01/
│   │   ├── README.md
│   │   ├── 01_baseline_analysis.py
│   │   ├── 02_numerical_verification.py
│   │   ├── 03_outlet_alternatives.py
│   │   ├── 04_variable_inflow.py
│   │   ├── 05_final_analysis.py
│   │   ├── findings.md
│   │   ├── figures/
│   │   └── tables/
│   ├── phase_02/
│   │   └── README.md
│   └── phase_03/
│       └── README.md
│
├── outputs/                               # Automatically generated figures, CSV files and simulation results
│   ├── phase_01/
│   ├── phase_02/
│   └── phase_03/
│
└── tests/
    ├── unit/
    │   ├── core/
    │   │   └── test_validation.py
    │   ├── hydraulics/
    │   │   ├── test_geometry.py
    │   │   ├── test_discharge.py
    │   │   └── test_flow.py
    │   ├── models/
    │   │   ├── single_tank/
    │   │   │   ├── test_equations.py
    │   │   │   ├── test_analytical.py
    │   │   │   └── test_events.py
    │   │   ├── chlorine/
    │   │   │   ├── test_decay.py
    │   │   │   └── test_mixing.py
    │   │   └── coupled_reservoirs/
    │   │       ├── test_connection.py
    │   │       ├── test_equations.py
    │   │       ├── test_analytical.py
    │   │       └── test_events.py
    │   ├── solvers/
    │   │   ├── test_euler.py
    │   │   ├── test_heun.py
    │   │   ├── test_rk4.py
    │   │   ├── test_scipy_solver.py
    │   │   └── test_solver_contract.py
    │   ├── simulation/
    │   │   ├── test_config.py
    │   │   ├── test_runner.py
    │   │   ├── test_events.py
    │   │   └── test_results.py
    │   └── analysis/
    │       ├── test_error_metrics.py
    │       ├── test_convergence.py
    │       └── test_conservation.py
    ├── integration/
    │   ├── test_single_tank.py
    │   ├── test_chlorine.py
    │   └── test_coupled_reservoirs.py
    ├── conftest.py
    └── fixtures/
        └── README.md
```

## 3. Root files

| File | Responsibility |
|---|---|
| `README.md` | Public project introduction, badges, installation instructions and roadmap. |
| `pyproject.toml` | Package metadata, Python requirements, dependencies, build configuration and tool settings. |
| `uv.lock` | Resolved dependency versions for reproducible environments; commit this file. |
| `.gitignore` | Excludes local environments, IDE settings, caches and generated outputs. |
| `.python-version` | Pins the development interpreter to Python 3.12. |

### 3.1 Root directories

| Directory | Responsibility |
|---|---|
| `docs/` | Engineering requirements, theory, architecture, research and learning records. |
| `src/` | Installable, reusable scientific computing package. |
| `experiments/` | Reproducible scientific investigations and numerical learning exercises. |
| `review/` | Mathematical exercises and exploratory calculations |
| `projects/` | Applied engineering case studies, executable analysis scripts and selected final deliverables. |
| `outputs/` | Automatically generated simulation data, figures and tables; excluded from Git. |
| `tests/` | Automated unit and integration verification. |

## 4. Documentation

All paths in this section are relative to `docs/`. The overview documents initially describe Phase 01; extend or add phase-specific technical documents when those phases begin.

| File | Responsibility |
|---|---|
| `00_overview/01_project_scope.md` | Project requirements, phase boundaries, deliverables and completion criteria. |
| `00_overview/02_mathematical_model.md` | Phase 01 governing equations, assumptions and analytical benchmarks. |
| `00_overview/03_numerical_methods.md` | Integration algorithms, accuracy, stability and solver requirements. |
| `00_overview/04_verification.md` | Verification cases, tolerances and convergence procedures. |
| `01_architecture/00_structure.md` | This architecture reference and target repository layout. |
| `02_checklists/01_phase_01_checklist.md` | Independent development, learning, verification and release requirements for Phase 01. |
| `03_research/` | Technical references, literature notes and independent research supporting model assumptions and numerical methods. |
| `04_logs/00_scientific_log_template.md` | Template for recording scientific experiments, hypotheses, methods and results. |
| `04_logs/01_learning_log_template.md` | Template for recording learning objectives, attempted approaches, difficulties and resolutions. |
| `04_logs/phase_01/` | Dated learning and scientific session records for single-tank dynamics. |
| `04_logs/phase_02/` | Future session records for chlorine decay and mixing. |
| `04_logs/phase_03/` | Future session records for coupled reservoir dynamics. |
| `05_applied_projects/` | Engineering problem statements, input requirements, deliverables and acceptance criteria for applied assignments. |
| `05_applied_projects/01_phase_01_tank_drawdown.md` | Municipal storage tank drawdown and maintenance drainage assignment; defines the baseline and alternatives, not their solutions. |

The applied assignment scopes define what must be solved; the root `projects/` directory contains the executable analyses and findings that answer those assignments.

## 5. Source package

`src/tank_dynamics/` contains installable scientific Python code. Package `__init__.py` files establish package boundaries and may expose a small public interface; they should not execute simulations or perform expensive work on import. `models/__init__.py` groups the physical models without requiring eager imports of every model.

### 5.1 `core/`

Shared numerical contracts and infrastructure; must not import physical models.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `constants.py` | Physical and conversion constants for US water and wastewater industry conventions, including gravity in ft/s²; document units, provenance and applicable assumptions. |
| `units.py` | Explicit conversions between engineering reporting units and consistent computational units, including inches/feet, gallons/ft³, gpm/cfs/MGD and time; support constituent mass conversions when Phase 02 requires them. |
| `types.py` | Shared array and callable type aliases, including the state vector and derivative function. |
| `exceptions.py` | Domain-specific exceptions for invalid inputs, integration failures and unsupported configurations. |
| `protocols.py` | Structural interfaces for derivative functions, solvers and optional event functions. |
| `validation.py` | Reusable checks for finite values, array dimensions, time intervals and positive parameters. |

### 5.2 `hydraulics/`

Reusable hydraulic relationships, independent of numerical integration.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `geometry.py` | Cross-sectional area and volume-depth relationships for supported tank geometries. |
| `discharge.py` | Gravity outlet discharge using Torricelli’s law and documented applicability limits. |
| `flow.py` | Shared signed-flow conventions and flow relationships; extend for bidirectional connections in Phase 03. |

### 5.3 `models/single_tank/`

Phase 01 scalar nonlinear water-depth model.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `tank.py` | Physical tank representation and model-facing interface; delegates calculations to equations and hydraulics. |
| `parameters.py` | Validated tank area, outlet area, discharge coefficient and initial conditions. |
| `equations.py` | Derivative function for water depth under gravity drainage and prescribed inflow. |
| `analytical.py` | Exact zero-inflow depth history and emptying time; independent verification reference. |
| `events.py` | Model-specific emptying and overflow event functions and boundary policies. |

### 5.4 `models/chlorine/`

Phase 02 batch decay and completely mixed constant-volume tank models.
 Initial implementation: Phase 02.

| Module | Responsibility |
|---|---|
| `decay.py` | Batch first-order chlorine decay model interface. |
| `mixing.py` | Continuous-flow, completely mixed tank interface with balanced inflow and outflow. |
| `parameters.py` | Validated volume, flow, initial concentration, inlet concentration and reaction rate. |
| `equations.py` | Pure derivative functions for batch decay and continuous-flow mixing. |
| `analytical.py` | Exponential decay and constant-input mixing solutions for independent benchmarks. |

### 5.5 `models/coupled_reservoirs/`

Phase 03 interconnected reservoirs with vector-valued water levels.
 Initial implementation: Phase 03.

| Module | Responsibility |
|---|---|
| `reservoir.py` | Individual reservoir geometry and storage representation. |
| `system.py` | Assembles reservoirs, connections and boundary flows into a coupled model. |
| `connection.py` | Connection parameters and signed inter-reservoir flow; delegates reusable hydraulic calculations. |
| `parameters.py` | Validated reservoir and connection configuration, including common elevation datum. |
| `equations.py` | Vector derivative from individual reservoir volume balances; internal flows cancel in the total balance. |
| `analytical.py` | Independent exact benchmarks for simplified cases, such as closed two-reservoir equalization. |
| `events.py` | Reservoir emptying, overflow and equalization event functions; equalization need not terminate a forced simulation. |

### 5.6 `solvers/`

Generic numerical integration; no imports from models or hydraulics.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `base.py` | Common solver contract and shared input/output conventions; no model-specific boundary logic. |
| `euler.py` | Fixed-step Forward Euler integration. |
| `heun.py` | Fixed-step explicit trapezoidal (improved Euler) integration. |
| `rk4.py` | Fixed-step classical fourth-order Runge–Kutta integration. |
| `scipy_solver.py` | Adapter for scipy.integrate.solve_ivp, initially RK45, with normalized results and status. |

### 5.7 `simulation/`

Coordinates model inputs, integration and output handling.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `config.py` | Simulation time span, solver choice, step size, tolerances and output options. |
| `runner.py` | Connects model derivative, initial state and selected solver; applies explicit model event policies. |
| `state.py` | State names, units and initial-state mapping; does not implement physical equations. |
| `events.py` | Generic event metadata and detection/termination conventions; model-specific event functions remain in models. |
| `results.py` | Simulation result container with time, state history, status, event records and optional diagnostics. |

### 5.8 `analysis/`

Postprocessing and independent numerical assessment.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `error_metrics.py` | Absolute error, RMSE and relative error with explicit handling of zero reference values. |
| `convergence.py` | Step refinement and observed convergence order on smooth solution intervals. |
| `stability.py` | Numerical stability studies using appropriate test equations and step sizes. |
| `conservation.py` | Volume balance residuals; extend to constituent mass accounting in Phase 02. |
| `equilibrium.py` | Steady-state residual and equilibrium calculations for supported models. |
| `sensitivity.py` | Parameter perturbation studies and response metrics; introduce in Phase 02. |
| `benchmarking.py` | Runtime, derivative evaluation counts and accuracy-cost comparisons. |

### 5.9 `visualization/`

Presentation of computed results; must not alter numerical states.
 Initial implementation: Phase 01.

| Module | Responsibility |
|---|---|
| `time_series.py` | Generic state-versus-time plots. |
| `hydraulics.py` | Water depth, discharge and reservoir level plots. |
| `concentration.py` | Chlorine concentration and mixing plots; introduce in Phase 02. |
| `phase_space.py` | State-space trajectories for coupled systems; introduce in Phase 03. |
| `convergence.py` | Error versus step-size plots and reference slopes. |
| `comparison.py` | Analytical versus numerical overlays and solver comparison figures. |

## 6. Experiments

Experiments are reproducible executable examples, not library modules or final engineering deliverables. Use ordinary Python scripts with optional Spyder `# %%` cells to investigate numerical behavior, inspect intermediate states and test hypotheses. Import reusable calculations from `tank_dynamics`, keep inputs explicit and write disposable results to the corresponding phase under the ignored root `outputs/` directory.

### 6.1 `experiments/phase_01/`

| Script | Purpose |
|---|---|
| `01_gravity_drainage.py` | Compare drainage history and emptying time against the exact solution. |
| `02_solver_comparison.py` | Compare solver errors, convergence and computational cost. |
| `03_variable_inflow.py` | Explore time-dependent inflow and equilibrium (optional Phase 01 extension). |

### 6.2 `experiments/phase_02/`

| Script | Purpose |
|---|---|
| `01_batch_decay.py` | Compare numerical chlorine decay with exponential decay. |
| `02_continuous_mixing.py` | Verify constant-input mixing and equilibrium concentration. |
| `03_decay_sensitivity.py` | Explore reaction rate and residence-time sensitivity. |

### 6.3 `experiments/phase_03/`

| Script | Purpose |
|---|---|
| `01_closed_equalization.py` | Verify equalization and total volume conservation in a closed system. |
| `02_forced_reservoirs.py` | Explore external inflow, discharge and dynamic reservoir response. |
| `03_flow_reversal.py` | Verify signed connection flows and changing head differences. |

## 7. Applied engineering projects

`projects/` contains version-controlled applied analyses that answer the engineering assignments defined in `docs/05_applied_projects/`. Scripts import the installed `tank_dynamics` package rather than duplicating physical equations, solvers or reusable plotting functions. Use standard `.py` files with optional Spyder `# %%` cells; each script should also run from a clean Python environment without relying on prior interactive console state.

Keep case-specific inputs, scenario selection, execution and interpretation in the project scripts. Use `outputs/` for generated results and retain selected final figures and tables in the project directory for review and portfolio presentation.

### 7.1 `projects/`

| File / directory | Responsibility |
|---|---|
| `README.md` | Index of applied engineering case studies, phase status and links to their execution instructions and findings. |
| `phase_01/` | Municipal storage tank drawdown and maintenance drainage analysis. |
| `phase_02/` | Future chlorine decay and mixing case study. |
| `phase_03/` | Future coupled reservoir dynamics case study. |

### 7.2 `projects/phase_01/`

| File / directory | Responsibility |
|---|---|
| `README.md` | Case overview, assignment link, assumptions, units, execution instructions and deliverable index. |
| `01_baseline_analysis.py` | Execute the 3-inch outlet baseline, calculate depth, discharge, storage and drainage duration, and compare with the analytical benchmark. |
| `02_numerical_verification.py` | Present solver agreement, convergence, emptying-time accuracy, volume balance and computational effort using reusable analysis functions. |
| `03_outlet_alternatives.py` | Compare 2-, 3- and 4-inch outlets against the residual-depth threshold and maintenance planning window; report discharge implications. |
| `04_variable_inflow.py` | Optional constant and variable inflow scenarios, equilibrium and operational response; execute only after the required MVP is verified. |
| `05_final_analysis.py` | Reproduce consolidated engineering metrics and final comparison tables and figures from the shared package and documented scenario inputs. |
| `findings.md` | Engineering interpretation, recommendations, verification evidence, assumptions and limitations. |
| `figures/` | Selected final, publication-ready plots with units and scenario identifiers. |
| `tables/` | Selected final engineering and verification results with units and scenario identifiers. |

### 7.3 `projects/phase_02/` and `projects/phase_03/`

Each phase currently contains a planned `README.md` describing its case study status and, when defined, the assignment, execution instructions and deliverable index. Detailed scripts and deliverables will be established when the respective applied scopes are developed.

## 8. Generated outputs

`outputs/` is a disposable, root-level directory for automatically generated figures, CSV tables and simulation histories. Scripts create required directories at runtime; do not rely on pre-existing folders or commit routine generated files. Use `/outputs/` in `.gitignore`.

| Directory | Responsibility |
|---|---|
| `outputs/phase_01/` | Generated single-tank experiments and applied drainage results. |
| `outputs/phase_02/` | Future generated chlorine decay and mixing results. |
| `outputs/phase_03/` | Future generated coupled reservoir results. |

Within each phase, create `figures/`, `tables/` or `data/` subdirectories as needed. Resolve output paths consistently relative to the repository rather than depending on Spyder's current working directory. Generated results are not reusable calculation modules; selected final deliverables may be copied into the corresponding `projects/` directory with their provenance.

## 9. Tests

Unit tests isolate individual equations and algorithms; integration tests exercise complete simulations. `conftest.py` holds shared pytest fixtures. `fixtures/README.md` documents reference inputs and provenance; retain small independent benchmarks in version control.

| Directory / file | Verification responsibility |
|---|---|
| `unit/core/test_validation.py` | Invalid parameters, shapes and time intervals. |
| `unit/hydraulics/test_geometry.py` | Area and volume relationships. |
| `unit/hydraulics/test_discharge.py` | Gravity discharge and boundary cases. |
| `unit/hydraulics/test_flow.py` | Signed flow and zero-head behavior. |
| `unit/models/single_tank/test_equations.py` | Depth derivatives and boundary behavior. |
| `unit/models/single_tank/test_analytical.py` | Exact depth and emptying time. |
| `unit/models/single_tank/test_events.py` | Emptying and overflow event definitions. |
| `unit/models/chlorine/test_decay.py` | Batch decay derivatives and analytical solution. |
| `unit/models/chlorine/test_mixing.py` | Mixing derivatives, analytical solution and equilibrium. |
| `unit/models/coupled_reservoirs/test_connection.py` | Connection direction and zero-head flow. |
| `unit/models/coupled_reservoirs/test_equations.py` | Coupled derivatives and cancellation of internal flows. |
| `unit/models/coupled_reservoirs/test_analytical.py` | Simplified analytical benchmarks. |
| `unit/models/coupled_reservoirs/test_events.py` | Reservoir-specific event definitions. |
| `unit/solvers/test_euler.py` | Euler accuracy and step handling. |
| `unit/solvers/test_heun.py` | Heun accuracy and step handling. |
| `unit/solvers/test_rk4.py` | RK4 accuracy and step handling. |
| `unit/solvers/test_scipy_solver.py` | Adapter accuracy, tolerances and status. |
| `unit/solvers/test_solver_contract.py` | Shared scalar/vector shape and time-grid conventions. |
| `unit/simulation/test_config.py` | Configuration validation. |
| `unit/simulation/test_runner.py` | Model-to-solver orchestration. |
| `unit/simulation/test_events.py` | Supported event handling and termination. |
| `unit/simulation/test_results.py` | Result shapes and metadata. |
| `unit/analysis/test_error_metrics.py` | Error calculations and zero-reference cases. |
| `unit/analysis/test_convergence.py` | Observed order calculations. |
| `unit/analysis/test_conservation.py` | Volume and constituent balance residuals. |
| `integration/test_single_tank.py` | End-to-end gravity drainage benchmark. |
| `integration/test_chlorine.py` | End-to-end decay and mixing benchmarks (Phase 02). |
| `integration/test_coupled_reservoirs.py` | End-to-end equalization and flow reversal (Phase 03). |

## 10. Dependency boundaries

```text
projects / experiments / integration tests
    -> simulation.runner
        -> models -> hydraulics -> core
        -> solvers -> core
        -> simulation.results
    -> analysis / visualization (consume results)
```

The runner composes models and solvers. Models do not import solvers; solvers do not import models, hydraulics, plotting or the runner. Shared result contracts must not create circular imports: keep a minimal solver result type in `core/types.py` and let `simulation/results.py` enrich it with physical metadata. Analysis and visualization consume results without changing them. Applied projects, experiments and tests may import the installed source package; the source package must not import them. Generated outputs are written by executable scripts, not by package imports.

## 11. Numerical interface and conventions

The generic initial-value problem is $d\mathbf{y}/dt=f(t,\mathbf{y})$. Use a one-dimensional NumPy array even for scalar problems. A derivative returns an array of the same shape.

```python
def rhs(t: float, y: np.ndarray) -> np.ndarray:
    ...

# Fixed-step solver contract (conceptual)
solve(rhs, t_span, y0, *, dt, events=None)

# Adaptive solver contract (conceptual)
solve_adaptive(rhs, t_span, y0, *, rtol, atol, events=None)
```

| Convention | Requirement |
|---|---|
| Time | Seconds internally; increasing time grid; shorten final fixed step to reach end time. |
| State | Shape `(n_states,)`; single tank `[h]`, chlorine `[C]`, coupled reservoirs `[h1, h2]`. |
| Results | Time shape `(n_times,)`; state history shape `(n_times, n_states)`; transpose SciPy output in adapter. |
| Units | US water and wastewater industry conventions. Hydraulic calculations use ft, ft², ft³, ft³/s and seconds; convert diameter from inches and report flow in gpm or MGD and storage in gal or MG as appropriate. Chlorine concentration remains mg/L; use consistent flow and volume units for Q/V, convert reaction rates to s⁻¹, and explicitly convert constituent mass to lb when reporting mass balances. Generic solvers remain unit-independent. |
| Events | Define supported detection accuracy; stop or restart under explicit model policy. Reject unsupported options rather than silently ignoring them. |
| Boundaries | Do not globally clamp state values in generic solvers; physical models own admissibility and boundary behavior. |
| Errors | Validate finite inputs and derivatives; report integration failure explicitly. |

## 12. Implementation sequence

| Phase | Scope | Completion gate |
|---|---|---|
| 01 | Single tank, generic fixed-step solvers, SciPy adapter, essential results and verification | Analytical drainage agreement, emptying handling and convergence on smooth intervals; completed drainage case study |
| 02 | Batch decay, continuous mixing, constituent balance and sensitivity | Analytical agreement and reaction-adjusted mass balance; completed chlorine case study |
| 03 | Coupled reservoirs, signed flow, vector integration and system events | Equalization benchmark, flow reversal and total volume balance; completed reservoir case study |

Create modules only when their functionality is needed. For the MVP, related responsibilities may initially live together and be separated when complexity justifies it. Do not create empty future modules merely to match the tree. A future combined hydraulic and water-quality model is outside the committed three-phase scope.

## 13. Version control and reproducibility

Track source, tests, experiment scripts, applied project scripts, findings, selected final figures and tables, documentation, `pyproject.toml`, `uv.lock`, and small reference datasets. Exclude virtual environments, IDE-local files, caches and the root `/outputs/` directory. Retain reproducible scripts and record the inputs and settings used to generate selected final deliverables. Record model parameters, solver settings, units and benchmark provenance with published results.

## 14. Related documentation

- [Project scope](../00_overview/01_project_scope.md)
- [Mathematical model](../00_overview/02_mathematical_model.md)
- [Numerical methods](../00_overview/03_numerical_methods.md)
- [Verification](../00_overview/04_verification.md)

- [Phase 01 applied project scope](../05_applied_projects/01_phase_01_tank_drawdown.md)
- [Phase 01 development checklist](../02_checklists/01_phase_01_checklist.md)
- [Applied projects index](../../projects/README.md)
