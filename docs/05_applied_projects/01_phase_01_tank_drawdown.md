# Phase 01 — Applied Engineering Project

## Municipal Water Storage Tank Drawdown and Maintenance Drainage Analysis

**Project ID:** WTD-01  
**Project type:** Hydraulic modeling and scientific computing  
**Client:** Hypothetical municipal water utility  
**Development environment:** Python 3.12, Spyder, uv, NumPy, SciPy, Matplotlib, pytest  
**Estimated effort:** 16–25 hours, inclusive of the Phase 01 development checklist; optional extension excluded.

## 1. Background

A municipal water utility operates a small ground-level water storage tank that must periodically be taken out of service for inspection, cleaning and maintenance. Before maintenance begins, the tank must be isolated from the water supply and drained through a gravity outlet.

Operations staff need to estimate how long drainage will take, how the discharge rate changes during drainage, and when the tank will reach a specified residual water depth. They also want a reproducible computational model that can eventually support more complex operating scenarios.

A constant discharge assumption may be misleading because the available hydraulic head decreases as the tank drains. The utility has therefore requested a time-dependent hydraulic analysis.

The facility and operational criteria in this assignment are hypothetical. The model is an educational representation of a small storage tank, not a site-specific design or an approved maintenance procedure.

## 2. Assignment objective

Develop and independently verify a scientific Python application that predicts the changing water depth, stored volume and gravity discharge of the isolated tank.

Use the analytical solution as an independent reference for evaluating numerical integration methods. Recommend a numerical method and simulation configuration for this simplified application, based on accuracy, computational effort and physical boundary handling.

## 3. Facility data

The baseline parameters are adapted from the Phase 01 development checklist using rounded US customary engineering values. These replace the original SI benchmark for this assignment.

| Parameter | Symbol | Value | Unit |
|---|---|---:|---|
| Constant tank cross-sectional area | A | 100 | ft² |
| Initial water depth above outlet | h₀ | 10.0 | ft |
| Circular outlet diameter | d | 3 | in |
| Discharge coefficient | Cd | 0.62 | dimensionless |
| Gravitational acceleration | g | 32.174 | ft/s² |
| Inflow during drainage | Qin | 0 | ft³/s |
| Initial elapsed time | t₀ | 0 | s |

### 3.1 Operating criteria

The following additional criteria are proposed solely for this assignment:

| Criterion | Value |
|---|---:|
| Maintenance planning window | 60 minutes |
| Residual-depth reporting threshold | 0.33 ft |
| Reporting interval | 5 minutes |
| Alternative outlet diameters | 2 in and 4 in |

The residual-depth threshold is a reporting milestone, not authorization for personnel entry. The idealized emptying condition is zero depth above the outlet.

## 4. Modeling assumptions and boundaries

- The tank is rigid with constant horizontal cross-sectional area.
- Water is incompressible.
- The free surface and outlet discharge are at atmospheric pressure.
- The outlet is represented by a short, freely discharging orifice at the tank bottom.
- Discharge is quasi-steady and follows Torricelli's law with a constant discharge coefficient.
- There is no external inflow during the baseline drainage event.
- Downstream backwater, pipe friction, pumps, valve transients, leakage and evaporation are excluded.
- Internal calculations use feet and seconds, with area in ft², volume in ft³, discharge in ft³/s (cfs), and depth derivatives in ft/s. Convert outlet diameters from inches to feet before calculating area. Report elapsed time in minutes, volume in US gallons, and discharge in gpm or cfs. Use 12 in/ft, approximately 7.48052 US gal/ft³, and 448.831 gpm/cfs. Numerical depth errors are reported in feet or inches.
- The model must not accept negative physical water depths or produce discharge from an empty tank.

## 5. Engineering questions

1. What volume of water is initially stored in the tank?
2. What is the initial gravity discharge rate?
3. How do water depth, stored volume and discharge change over time?
4. When does the tank reach the 0.33 ft residual-depth threshold?
5. What is the theoretical complete drainage time?
6. Does the baseline configuration satisfy the 60-minute maintenance planning window, considering both the residual-depth milestone and theoretical emptying?
7. How would changing the outlet diameter affect drainage duration and initial discharge?
8. How inaccurate would a constant-discharge estimate based on the initial flow be?
9. Which numerical integration method provides an appropriate balance of accuracy, computational cost and robustness for this problem?

## 6. Scope of work

### Task 1 — Physical and mathematical formulation

- Prepare a schematic showing the control volume, water depth, free surface, outlet and flow directions.
- Calculate the outlet cross-sectional area and initial storage volume independently.
- Develop the conservation-of-volume equation and justify the gravity discharge relationship.
- Derive the governing first-order nonlinear ODE and verify dimensional consistency.
- Derive the zero-inflow analytical depth solution and theoretical emptying time.
- Determine the analytical time to reach the residual-depth threshold.
- Determine the equilibrium condition for constant positive inflow as a mathematical exercise.
- Explain the physical domain of the analytical solution and its behavior after emptying.

**Deliverable:** Mathematical derivation, assumptions, units and independent benchmark calculations.

### Task 2 — Physical model implementation

Develop the reusable tank geometry, discharge, parameter validation, governing derivative and analytical reference functions identified in the development checklist.

Evaluate the functions independently in Spyder before connecting them to numerical solvers. Verify initial, zero-depth and applicable equilibrium conditions. Use a one-dimensional NumPy state array even for the scalar tank model.

**Deliverable:** Tested physical-model modules and analytical benchmark functions.

### Task 3 — Numerical integration

Implement Forward Euler, Heun and classical RK4 independently. Integrate SciPy RK45 through the common solver interface.

- Verify the generic solvers on constant-derivative, zero-derivative and exponential-decay problems.
- Include an independently verifiable two-component state benchmark.
- Inspect representative integration steps manually in Spyder.
- Keep physical equations separate from numerical integration algorithms.
- Apply a consistent state-history format and explicit simulation status.
- Investigate and document emptying-event detection and invalid intermediate states.

**Deliverable:** Four numerical methods and a minimal simulation runner with consistent results.

### Task 4 — Baseline drainage experiment

Simulate the baseline tank from its initial condition through emptying using the analytical solution and each numerical method.

Produce a reporting table at five-minute intervals through the 60-minute planning window, including the exact or estimated threshold and emptying events separately. If a solver terminates at emptying, any subsequent reported zero depth and discharge must be explicitly identified as physical post-emptying continuation rather than additional solver output.

Report elapsed time, water depth, stored volume, discharge and cumulative discharged volume. Determine whether the maintenance planning criterion is met.

**Experiment:** `experiments/phase_01/01_gravity_drainage.py`

### Task 5 — Solver comparison and verification

Select a common smooth pre-emptying interval after independently calculating the baseline emptying time. Use at least four successively halved fixed step sizes; suggested starting values are 120, 60, 30 and 15 seconds. Adjust the interval or step sizes if necessary to obtain meaningful convergence measurements.

- Compare Euler, Heun, RK4 and RK45 against the analytical reference at matching output times.
- Calculate maximum absolute depth error and RMSE.
- Estimate observed convergence order for the fixed-step methods.
- Compare derivative evaluation counts and, if useful, repeated runtime measurements.
- Verify volume conservation using documented discharge quadrature.
- Evaluate emptying-time error separately from smooth-interval convergence.
- Distinguish adaptive internal integration steps from requested output sampling.
- Establish and justify numerical acceptance tolerances before final verification runs.

**Experiment:** `experiments/phase_01/02_solver_comparison.py`

### Task 6 — Engineering alternatives

Repeat the drainage analysis for the following configurations using the analytical reference and a verified numerical solver selected in Task 5.

| Scenario | Outlet diameter | Purpose |
|---|---:|---|
| WTD-01-A | 3 in | Baseline configuration |
| WTD-01-B | 2 in | Restricted outlet alternative |
| WTD-01-C | 4 in | Enlarged outlet alternative |

Hold all other parameters constant, including the assumed discharge coefficient. These are idealized orifice alternatives, not nominal pipe-size selections.

Compare initial discharge, time to residual depth, complete drainage time and compliance with the planning window. Discuss the trade-off between faster drainage and increased peak discharge to the receiving system. Receiving-system capacity is unknown and must not be assumed adequate.

Compare the baseline analytical drainage time with an estimate obtained by assuming the initial discharge remains constant. Explain the discrepancy.

This task is a small applied analysis using existing model functions; it does not require a new sensitivity-analysis framework.

### Task 7 — Engineering findings

Prepare a concise technical summary addressing the engineering questions, recommended numerical method, maintenance planning implications, verification results and limitations. Identify what additional facility data would be necessary before applying the model to an actual utility asset.

## 7. Optional extension — Inflow during drainage

Begin only after the required gravity-drainage MVP is verified.

Investigate a hypothetical inlet that cannot be completely isolated. Evaluate constant inflows of 80 and 160 gpm, converting these to cfs before integration, then a piecewise scenario with 80 gpm for the first 20 minutes and zero thereafter.

- Determine equilibrium depths for constant inflow and assess approach from above and below equilibrium.
- Determine whether the residual-depth threshold is achievable under each constant inflow.
- Investigate how continued inflow changes maintenance readiness.
- Handle inflow discontinuities explicitly and define behavior when an empty tank receives water.
- Verify volume conservation and document the modeled capacity/overflow policy if relevant.

**Experiment:** `experiments/phase_01/03_variable_inflow.py`

## 8. Required figures and tables

| Output | Content |
|---|---|
| Figure 1 | Analytical and numerical water depth versus elapsed time |
| Figure 2 | Gravity discharge versus elapsed time |
| Figure 3 | Stored volume versus elapsed time |
| Figure 4 | Numerical depth error versus elapsed time on a smooth interval |
| Figure 5 | Log-log convergence plot for Euler, Heun and RK4 |
| Figure 6 | Drainage histories for the three outlet alternatives |
| Table 1 | Independent analytical benchmark calculations |
| Table 2 | Baseline operational reporting table |
| Table 3 | Solver accuracy, derivative evaluations and computational cost |
| Table 4 | Emptying-time and volume-balance verification |
| Table 5 | Engineering alternatives and planning-window assessment |

Label figures with units, relevant parameters and solver settings. Generated outputs may be stored in the ignored `outputs/` directory; retain selected reference figures and reproducible inputs as appropriate.

## 9. Acceptance criteria

- Analytical benchmarks are independently derived and recorded before numerical verification.
- All required unit and integration tests pass.
- The four solvers use consistent result conventions.
- Fixed-step solvers demonstrate approximately first-, second- and fourth-order convergence respectively on suitable smooth benchmarks, with deviations explained.
- Numerical errors, emptying-time errors and volume-balance residuals satisfy independently justified tolerances.
- No negative accepted physical depths or unphysical post-emptying discharge are reported.
- The operational questions are answered using computed evidence.
- The experiments are reproducible in a clean uv environment.
- Assumptions, numerical limitations and unresolved issues are documented.

## 10. Deliverables and completion

- Mathematical derivation and independent calculations.
- Reusable Python source modules and automated tests.
- Reproducible experiment scripts and documented input parameters.
- Required figures and results tables.
- Short engineering findings report (suggested length: 2–4 pages).
- Learning log entries documenting discoveries, failed approaches and resolutions.
- Updated README and completed Phase 01 checklist.

## 11. Out of scope

Detailed outlet piping design, actual maintenance authorization, confined-space entry, water hammer, pump controls, full distribution-network modeling, chlorine kinetics, coupled reservoirs, GUI development and digital twin integration are excluded.

## 12. Related documentation

The existing checklist, README, architecture and any SI-based verification benchmarks must be reconciled with the US customary unit convention before implementation. The revised facility values are rounded engineering inputs, not exact conversions; independently recalculate all expected benchmark results.

- [Project scope](../00_overview/01_project_scope.md)
- [Mathematical model](../00_overview/02_mathematical_model.md)
- [Numerical methods](../00_overview/03_numerical_methods.md)
- [Verification](../00_overview/04_verification.md)
- [Project structure](../01_architecture/00_structure.md)
- [Phase 01 development checklist](../02_checklists/01_phase_01_checklist.md)

The applied scope defines the engineering assignment; the development checklist remains the controlling software and learning work plan. No completed derivations, numerical answers or implementation code are supplied in this assignment.
