# Phase 01 — Single Tank Dynamics: Development and Learning Checklist

## Purpose

Develop a verified single-tank ODE simulator independently in Spyder using Python 3.12, uv, NumPy, SciPy, Matplotlib and pytest. This is a learning assignment, not a code solution. Phase 02 (chlorine) and Phase 03 (coupled reservoirs) are outside this phase, but numerical interfaces must accommodate future vector-valued states.

**Unit convention:** US water and wastewater industry-standard units. Use ft for depth and head, in for outlet diameter, ft² for area, gal/ft³/MG for volume, gpm/cfs/MGD for flow, fps for velocity, and s/min/hr/days for time as appropriate. Maintain dimensional consistency within each calculation and simulation; document necessary conversions. No universal computational unit system is prescribed. Future chlorine concentrations remain in mg/L; numerical solvers remain unit-independent.

Related documents: [Project scope](../00_overview/01_project_scope.md), [Mathematical model](../00_overview/02_mathematical_model.md), [Numerical methods](../00_overview/03_numerical_methods.md), [Verification](../00_overview/04_verification.md), [Architecture](../01_architecture/00_structure.md).

## 0. Independent development workflow

- [x] Configure Spyder to use the repository's Python 3.12 virtual environment; install a compatible spyder-kernels version if required by Spyder.
- [x] Verify the interpreter and imports in the IPython console.
- [x] Confirm uv.lock, pyproject.toml and .python-version are tracked.
- [x] Confirm NumPy, SciPy and Matplotlib are runtime dependencies and pytest is a development dependency.
- [x] Verify the src-layout package is importable in Spyder and from the terminal.
- [x] Disable AI code generation if enabled; use ordinary editor completion, debugger, official documentation and textbooks.
- [x] Maintain a short learning log: hypothesis, attempted approach, observed error, diagnosis and resolution.
- [ ] Verify imports without manually modifying `sys.path`.
- [ ] Run experiments interactively, then move reproducible calculations into modules and tests.

**Completion gate:** A fresh console can import the package and `uv run pytest` can discover tests once written.

## 1. Mathematical foundations

- [ ] Review derivatives, initial-value problems, separable ODEs and definite integration using the [mathematical review](../06_learning/01_phase_01_mathematical_review.md).
- [ ] Complete the independent exercises in that review and record the results.
- [ ] Review the [hydraulic foundations](../06_learning/02_phase_01_hydraulic_foundations.md).
- [ ] Draw the tank, define the control volume and identify inflow, outflow and stored volume.
- [ ] State assumptions: rigid constant-area tank, incompressible fluid, atmospheric outlet and free surface, quasi-steady discharge.
- [ ] Derive conservation of volume and substitute the tank geometry relationship.
- [ ] Derive or justify Torricelli discharge including the discharge coefficient.
- [ ] Obtain the first-order nonlinear water-depth ODE.
- [ ] Check dimensional consistency of each term using the selected engineering units and necessary conversions.
- [ ] Derive the zero-inflow analytical solution by separation of variables without consulting implementation code.
- [ ] Derive the emptying time and explain why the analytical expression must not be extended past emptying without a physical boundary condition.
- [ ] Determine the equilibrium condition for constant positive inflow; explain the sign of the derivative above and below equilibrium.

- [ ] Define the valid depth domain and zero-inflow behavior after emptying before implementing solvers.
- [ ] Verify the derived solution by differentiation and substitution of the initial condition.

**Completion gate:** Independently explain and verify the governing ODE, analytical solution, emptying time and equilibrium condition.

**Deliverable:** Handwritten or Markdown derivation with assumptions, units and initial conditions.

## 2. Physical model and hydraulic functions

Suggested modules: `core/constants.py`, `core/units.py`, `core/validation.py`, `hydraulics/geometry.py`, `hydraulics/discharge.py`, `models/single_tank/parameters.py`, `tank.py`, `equations.py`, `analytical.py`.

- [ ] Define gravity (32.174 ft/s²) and document the applicable engineering units.
- [ ] Implement and independently test unit conversions in `core/units.py`: inches to feet, cubic feet to US gallons, cfs to gpm, and seconds to minutes. Apply conversions only where required for dimensional consistency; test inverse conversions as applicable.
- [ ] Decide how to represent tank area, outlet area or diameter, discharge coefficient and initial depth.
- [ ] Validate finite parameters, positive tank area and outlet dimensions, nonnegative depth and physically appropriate discharge coefficient.
- [ ] Implement geometry and orifice discharge calculations independently.
- [ ] Implement the governing derivative with a documented time/state interface.
- [ ] Represent scalar depth internally as a one-dimensional NumPy array of length one.
- [ ] Implement the analytical solution and emptying time independently of numerical solvers.
- [ ] Check the derivative at initial depth, zero depth and equilibrium where applicable.
- [ ] Decide how invalid physical inputs differ from small numerical excursions near a boundary.
- [ ] Verify zero discharge at zero depth, proportionality to outlet area, square-root dependence on depth, and inverse dependence of the depth derivative on tank area at fixed net flow.
- [ ] Write unit tests for geometry, discharge, parameters, derivative and analytical solution.

**Completion gate:** Physical functions can be exercised in Spyder without importing a numerical solver.

## 3. Shared solver contract

Start with a callable derivative and a simple result representation. Introduce `core/types.py`, `core/protocols.py`, `solvers/base.py` and `simulation/results.py` only when needed; no abstract class or protocol is required initially. Refine the contract after Euler works.

- [ ] Define inputs: derivative function, initial state, start/end times and fixed step size or adaptive tolerances.
- [ ] Define state shape `(n_states,)` and result history shape `(n_times, n_states)`.
- [ ] Define output times, state history, success/status and useful diagnostics.
- [ ] Validate finite initial state, increasing time interval and positive step size.
- [ ] Decide how to handle a final partial step without exceeding the requested end time.
- [ ] Ensure solvers do not import tank physics or silently clamp state values.
- [ ] Prepare constant-derivative and exponential-decay contract tests using the [benchmark exercises](../06_learning/05_phase_01_benchmark_exercises.md); execute them after implementing Euler.

**Completion gate:** A minimal interface is documented and the benchmark inputs and analytical references are prepared; executable contract tests are completed with Euler.

## 4. Forward Euler

- [ ] Review the [numerical integration guide](../06_learning/03_phase_01_numerical_integration.md) and use its Euler equations.
- [ ] Review the tangent-line approximation and derive the Euler update.
- [ ] Implement the time-stepping loop yourself in `solvers/euler.py`.
- [ ] Inspect the first three steps manually using a calculator and Spyder's variable explorer.
- [ ] Test constant derivative, zero derivative, time-dependent derivative and exponential decay using the common benchmark definitions.
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

**Completion gate:** Heun and RK4 pass the common benchmarks, preserve input states and demonstrate their expected convergence orders.

## 6. SciPy adaptive integration

- [ ] Read the official `scipy.integrate.solve_ivp` documentation.
- [ ] Experiment with RK45, initial states, t_span, t_eval, rtol and atol in Spyder.
- [ ] Explain the difference between output sampling and internal adaptive steps.
- [ ] Implement `solvers/scipy_solver.py` as an adapter to the common result contract.
- [ ] Normalize SciPy's state-history orientation to the project convention.
- [ ] Inspect success, status, message and derivative evaluation counts.
- [ ] Compare against the analytical solution at matching times; do not treat SciPy as an exact solution.

**Completion gate:** RK45 returns the common result format and agrees with independent analytical references within justified tolerances.

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

**Completion gate:** Full zero-inflow drainage terminates or continues physically at emptying, with no negative accepted depths; unresolved event errors are reported explicitly.

## 8. Numerical verification and analysis

Suggested modules: `analysis/error_metrics.py`, `convergence.py`, `conservation.py`, `benchmarking.py`.

- [ ] Review the [numerical verification guide](../06_learning/04_phase_01_numerical_verification.md).
- [ ] Define and justify acceptance tolerances before final verification runs.
- [ ] Define absolute error, RMSE and maximum absolute error at matched output times; report depth errors in ft or in.
- [ ] Avoid relative error at zero or document a denominator threshold.
- [ ] Choose a smooth pre-emptying interval and at least four successively halved step sizes.
- [ ] Calculate observed convergence order from error ratios.
- [ ] Plot error versus step size on logarithmic axes and interpret departures from theoretical slopes.
- [ ] Compare estimated emptying time with the analytical benchmark separately from smooth convergence tests.
- [ ] Check volume balance in gal or ft³: change in storage equals integrated net inflow using compatible flow and time units, within a documented numerical tolerance.
- [ ] Document the quadrature used for flow integration and its own error contribution.
- [ ] Record runtime and derivative evaluations; repeat timing measurements if making performance claims.
- [ ] Add regression tests for representative cases and invalid inputs.

### Baseline benchmark

Use the rounded US customary facility parameters from the [Phase 01 applied project scope](../05_applied_projects/01_phase_01_tank_drawdown.md). These are replacement inputs, not exact conversions of the previous SI benchmark. Recalculate all analytical reference values independently.

| Parameter | Value |
|---|---:|
| Tank area | 100 ft² |
| Initial depth | 10 ft |
| Outlet diameter | 3 in |
| Discharge coefficient | 0.62 |
| Gravity | 32.174 ft/s² |
| Inflow | 0 cfs |

- [ ] Independently calculate outlet area, initial volume, initial discharge and analytical emptying time.
- [ ] Record expected values before executing the numerical model.
- [ ] Compare results against the existing verification document and reconcile any differences in assumptions or tolerances.

**Completion gate:** Independent references, error metrics, convergence, emptying error and volume balance meet documented acceptance criteria.

## 9. Scientific experiments and visualization

- [ ] Create `experiments/phase_01/01_gravity_drainage.py`: plot analytical and numerical depth and discharge histories.
- [ ] Create `experiments/phase_01/02_solver_comparison.py`: compare all four solvers at matched times and produce convergence plots.
- [ ] Label plots with units, parameters, solver and step size/tolerances. Report depth in ft, volume in US gal, discharge in gpm or cfs, elapsed time in minutes and depth errors in ft or in.
- [ ] Keep plotting functions separate from integration algorithms.
- [ ] Save reproducible experiment inputs and selected reference figures; keep disposable outputs in ignored directories.
- [ ] Investigate how step size affects accuracy and effort, how closely the analytical solution is reproduced, and how solvers behave near emptying.
- [ ] Record objective, hypothesis, methodology, results, interpretation and limitations for each experiment.

**Completion gate:** Both required experiment scripts reproduce their results and answer their investigation questions. Applied facility alternatives and engineering recommendations belong to the separate applied project checklist.

## 10. Optional extension — variable inflow

Do not begin until the gravity-drainage MVP is verified.

- [ ] Implement constant and time-dependent inflow functions.
- [ ] Verify constant inflow equilibrium and approach from above and below.
- [ ] Explore a piecewise inflow scenario, accounting for discontinuities in integration.
- [ ] Define behavior for an empty tank receiving inflow.
- [ ] Define overflow behavior explicitly or terminate at a specified maximum depth if capacity is modeled.
- [ ] Create `experiments/phase_01/03_variable_inflow.py`.
- [ ] Verify volume balance and document results.

**Optional completion gate:** Inflow scenarios satisfy equilibrium, boundary and volume-balance checks. This extension is not required for release.

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

Development release does not imply completion of the [applied engineering project checklist](02_phase_01_applied_project_checklist.md). Complete that milestone separately.

## Suggested work sessions

| Session | Focus | Approximate effort |
|---|---|---:|
| 1 | Mathematical review | 3–5 h |
| 2 | Hydraulic derivation | 2–3 h |
| 3 | Physical model | 2–3 h |
| 4 | Solver contract and Euler | 2–3 h |
| 5 | Heun and RK4 | 3–4 h |
| 6 | SciPy integration | 2–3 h |
| 7 | Boundary handling | 2–4 h |
| 8 | Numerical verification | 3–5 h |
| 9 | Scientific experiments | 2–3 h |
| 10 | Documentation and release | 1–2 h |

Allow approximately 22–35 hours for independent learning, excluding the optional extension and separate applied engineering project. This is a planning estimate, not a deadline.

## References for independent study

- Jaan Kiusalaas, *Numerical Methods in Engineering with Python 3*: review numerical integration and initial-value problems.
- A calculus or differential equations textbook: review differentiation, definite integration and separation of variables.
- [SciPy solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- [NumPy user guide](https://numpy.org/doc/stable/user/)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [Spyder documentation](https://docs.spyder-ide.org/)
- [pytest documentation](https://docs.pytest.org/)
- [uv documentation](https://docs.astral.sh/uv/)

Use references to understand concepts and API contracts, then close the reference and implement the algorithm independently. Phase 02 and Phase 03 remain future work.