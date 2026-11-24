# Phase 01 — Single Tank Dynamics: Development and Learning Checklist

## Purpose

Develop a verified single-tank ODE simulator independently in Spyder using Python 3.12, uv, NumPy, SciPy, Matplotlib and pytest. This is a learning assignment, not a code solution. Phase 02 (chlorine) and Phase 03 (coupled reservoirs) are outside this phase, but numerical interfaces must accommodate future vector-valued states.

Related documents: [Project scope](../00_overview/01_project_scope.md), [Mathematical model](../00_overview/02_mathematical_model.md), [Numerical methods](../00_overview/03_numerical_methods.md), [Verification](../00_overview/04_verification.md), [Architecture](../01_architecture/00_structure.md).

## 0. Independent development workflow

- [x] Configure Spyder to use the repository's Python 3.12 virtual environment; install a compatible spyder-kernels version if required by Spyder.
- [x] Verify the interpreter and imports in the IPython console.
- [x] Confirm uv.lock, pyproject.toml and .python-version are tracked.
- [x] Confirm NumPy, SciPy and Matplotlib are runtime dependencies and pytest is a development dependency.
- [x] Verify the src-layout package is importable in Spyder and from the terminal.
- [x] Disable AI code generation if enabled; use ordinary editor completion, debugger, official documentation and textbooks.
- [x] Maintain a short learning log: hypothesis, attempted approach, observed error, diagnosis and resolution.
- [ ] Run experiments interactively, then move reproducible calculations into modules and tests.

**Completion gate:** A fresh console can import the package and `uv run pytest` can discover tests once written.

## 1. Mathematical foundations

- [ ] Review derivatives, initial-value problems, separable ODEs and definite integration.
- [ ] Draw the tank, define the control volume and identify inflow, outflow and stored volume.
- [ ] State assumptions: rigid constant-area tank, incompressible fluid, atmospheric outlet and free surface, quasi-steady discharge.
- [ ] Derive conservation of volume and substitute the tank geometry relationship.
- [ ] Derive or justify Torricelli discharge including the discharge coefficient.
- [ ] Obtain the first-order nonlinear water-depth ODE.
- [ ] Check dimensional consistency of each term in SI units.
- [ ] Derive the zero-inflow analytical solution by separation of variables without consulting implementation code.
- [ ] Derive the emptying time and explain why the analytical expression must not be extended past emptying without a physical boundary condition.
- [ ] Determine the equilibrium condition for constant positive inflow; explain the sign of the derivative above and below equilibrium.

**Deliverable:** Handwritten or Markdown derivation with assumptions, units and initial conditions.

## 2. Physical model and hydraulic functions

Suggested modules: `core/constants.py`, `core/validation.py`, `hydraulics/geometry.py`, `hydraulics/discharge.py`, `models/single_tank/parameters.py`, `tank.py`, `equations.py`, `analytical.py`.

- [ ] Define gravity and SI conventions; use seconds internally.
- [ ] Decide how to represent tank area, outlet area or diameter, discharge coefficient and initial depth.
- [ ] Validate finite parameters, positive tank area and outlet dimensions, nonnegative depth and physically appropriate discharge coefficient.
- [ ] Implement geometry and orifice discharge calculations independently.
- [ ] Implement the governing derivative with a documented time/state interface.
- [ ] Represent scalar depth internally as a one-dimensional NumPy array of length one.
- [ ] Implement the analytical solution and emptying time independently of numerical solvers.
- [ ] Check the derivative at initial depth, zero depth and equilibrium where applicable.
- [ ] Decide how invalid physical inputs differ from small numerical excursions near a boundary.
- [ ] Write unit tests for geometry, discharge, parameters, derivative and analytical solution.

**Completion gate:** Physical functions can be exercised in Spyder without importing a numerical solver.

## 3. Shared solver contract

Suggested modules: `core/types.py`, `core/protocols.py`, `solvers/base.py`, `simulation/results.py` (introduce only as needed).

- [ ] Define inputs: derivative function, initial state, start/end times and fixed step size or adaptive tolerances.
- [ ] Define state shape `(n_states,)` and result history shape `(n_times, n_states)`.
- [ ] Define output times, state history, success/status and useful diagnostics.
- [ ] Validate finite initial state, increasing time interval and positive step size.
- [ ] Decide how to handle a final partial step without exceeding the requested end time.
- [ ] Ensure solvers do not import tank physics or silently clamp state values.
- [ ] Test the contract with a constant derivative and a simple exponential-decay ODE unrelated to hydraulics.

## 4. Forward Euler

- [ ] Review the tangent-line approximation and derive the Euler update.
- [ ] Implement the time-stepping loop yourself in `solvers/euler.py`.
- [ ] Inspect the first three steps manually using a calculator and Spyder's variable explorer.
- [ ] Test constant derivative, zero derivative and exponential decay.
- [ ] Test a two-component state with independently known solutions to establish Phase 03 compatibility.
- [ ] Compare tank drainage against the analytical solution over a smooth pre-emptying interval.
- [ ] Repeat with smaller step sizes and explain the observed change in error.

**Completion gate:** Euler works on generic scalar and vector ODEs and exhibits approximately first-order convergence on a smooth benchmark.

## 5. Heun and classical RK4

- [ ] Derive Heun's predictor-corrector update and identify its two derivative evaluations.
- [ ] Implement `solvers/heun.py` without copying a finished solver.
- [ ] Work through one step by hand and compare with the implementation.
- [ ] Review the four RK4 stages and explain their time/state arguments.
- [ ] Implement `solvers/rk4.py` independently.
- [ ] Verify both methods on the same scalar and vector benchmarks used for Euler.
- [ ] Check that intermediate stages do not mutate the original state.
- [ ] Compare error and derivative evaluation counts at common step sizes.
- [ ] Confirm approximately second- and fourth-order convergence respectively on smooth benchmarks before roundoff dominates.

## 6. SciPy adaptive integration

- [ ] Read the official `scipy.integrate.solve_ivp` documentation.
- [ ] Experiment with RK45, initial states, t_span, t_eval, rtol and atol in Spyder.
- [ ] Explain the difference between output sampling and internal adaptive steps.
- [ ] Implement `solvers/scipy_solver.py` as an adapter to the common result contract.
- [ ] Normalize SciPy's state-history orientation to the project convention.
- [ ] Inspect success, status, message and derivative evaluation counts.
- [ ] Compare against the analytical solution at matching times; do not treat SciPy as an exact solution.

## 7. Physical boundaries and simulation orchestration

Suggested modules: `models/single_tank/events.py`, `simulation/config.py`, `runner.py`, `events.py`, `state.py` as needed.

- [ ] Define the emptying event and the physical behavior after emptying under zero inflow.
- [ ] Investigate how fixed-step methods can cross zero or evaluate invalid intermediate states.
- [ ] Design and document a boundary strategy (step refinement/event localization and termination or physically justified continuation).
- [ ] Ensure the square root is never evaluated at a negative physical depth; do not hide integration failures through indiscriminate clipping.
- [ ] Implement and test SciPy terminal event detection for emptying; investigate near-zero event detection difficulties and document the tolerance or strategy used.
- [ ] Verify no negative accepted depths and no unphysical discharge after emptying.
- [ ] Separate model-specific boundary policy from generic numerical integration.
- [ ] Implement a minimal runner that selects a solver and returns a consistent result.

## 8. Numerical verification and analysis

Suggested modules: `analysis/error_metrics.py`, `convergence.py`, `conservation.py`, `benchmarking.py`.

- [ ] Define absolute error, RMSE and maximum absolute error at matched output times.
- [ ] Avoid relative error at zero or document a denominator threshold.
- [ ] Choose a smooth pre-emptying interval and at least four successively halved step sizes.
- [ ] Calculate observed convergence order from error ratios.
- [ ] Plot error versus step size on logarithmic axes and interpret departures from theoretical slopes.
- [ ] Compare estimated emptying time with the analytical benchmark separately from smooth convergence tests.
- [ ] Check volume balance: change in storage equals integrated net inflow, within a documented numerical tolerance.
- [ ] Document the quadrature used for flow integration and its own error contribution.
- [ ] Record runtime and derivative evaluations; repeat timing measurements if making performance claims.
- [ ] Define and justify acceptance tolerances before final verification runs.
- [ ] Add regression tests for representative cases and invalid inputs.

### Baseline benchmark

| Parameter | Value |
|---|---:|
| Tank area | 10 m² |
| Initial depth | 3 m |
| Outlet diameter | 0.075 m |
| Discharge coefficient | 0.62 |
| Gravity | 9.81 m/s² |
| Inflow | 0 m³/s |

- [ ] Independently calculate outlet area, initial volume, initial discharge and analytical emptying time.
- [ ] Record expected values before executing the numerical model.
- [ ] Compare results against the existing verification document and reconcile any differences in assumptions or tolerances.

## 9. Scientific experiments and visualization

- [ ] Create `experiments/phase_01/01_gravity_drainage.py`: plot analytical and numerical depth and discharge histories.
- [ ] Create `experiments/phase_01/02_solver_comparison.py`: compare all four solvers at matched times and produce convergence plots.
- [ ] Label plots with units, parameters, solver and step size/tolerances.
- [ ] Keep plotting functions separate from integration algorithms.
- [ ] Save reproducible experiment inputs and selected reference figures; keep disposable outputs in ignored directories.
- [ ] Write a short interpretation of each experiment, including limitations and unexpected behavior.

## 10. Optional extension — variable inflow

Do not begin until the gravity-drainage MVP is verified.

- [ ] Implement constant and time-dependent inflow functions.
- [ ] Verify constant inflow equilibrium and approach from above and below.
- [ ] Explore a piecewise inflow scenario, accounting for discontinuities in integration.
- [ ] Define behavior for an empty tank receiving inflow.
- [ ] Define overflow behavior explicitly or terminate at a specified maximum depth if capacity is modeled.
- [ ] Create `experiments/phase_01/03_variable_inflow.py`.
- [ ] Verify volume balance and document results.

## 11. Phase 01 release gate

- [ ] All required physical-model and solver unit tests pass.
- [ ] Integration tests verify gravity drainage against an independent analytical solution.
- [ ] Euler, Heun, RK4 and RK45 share consistent output conventions.
- [ ] Fixed-step solvers pass a generic vector-state benchmark.
- [ ] Convergence and emptying verification are documented separately.
- [ ] Physical boundaries and numerical limitations are documented.
- [ ] Experiments run from a clean environment using uv.
- [ ] README reflects actual implementation status; architecture distinguishes planned modules from implemented modules.
- [ ] Review staged changes and commit with a descriptive multi-line message.
- [ ] Explain each solver and its failure modes in your own words without relying on generated code.

## Suggested work sessions

| Session | Focus | Approximate effort |
|---|---|---:|
| 1 | Environment and mathematical derivation | 2–3 h |
| 2 | Physical model and analytical tests | 2–3 h |
| 3 | Generic contract and Euler | 2–3 h |
| 4 | Heun and RK4 | 3–4 h |
| 5 | SciPy and boundary handling | 3–5 h |
| 6 | Verification and experiments | 3–5 h |
| 7 | Documentation and release review | 1–2 h |

Allow approximately 16–25 hours for independent learning, excluding the optional extension. Treat this as a planning estimate, not a deadline.

## References for independent study

- [SciPy solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [NumPy user guide](https://numpy.org/doc/stable/user/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [Spyder documentation](https://docs.spyder-ide.org/)
- [pytest documentation](https://docs.pytest.org/)
- [uv documentation](https://docs.astral.sh/uv/)

Use references to understand concepts and API contracts, then close the reference and implement the algorithm independently. Phase 02 and Phase 03 remain future work.
