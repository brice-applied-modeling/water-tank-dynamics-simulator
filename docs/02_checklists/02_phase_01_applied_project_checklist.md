# Phase 01 — Applied Engineering Project Checklist

## Municipal Water Storage Tank Drawdown and Maintenance Drainage Analysis

**Project ID:** WTD-01  
**Environment:** Python 3.12, Spyder, uv, NumPy, SciPy, Matplotlib, pytest  
**Engineering units:** US municipal water and wastewater industry conventions

## Purpose

Apply the verified Phase 01 scientific computing library to a hypothetical municipal storage tank maintenance problem. Evaluate drainage behavior, numerical reliability and outlet alternatives, and communicate defensible engineering findings.

This checklist complements the development and learning checklist. Implement reusable calculations in `src/tank_dynamics/`, investigate numerical behavior in `experiments/`, and assemble the applied analysis in `projects/phase_01/`. Do not duplicate solver or hydraulic implementations in project scripts. Complete the work independently in Spyder; this checklist supplies no numerical answers or implementation code.

Related documents: [Applied project scope](../05_applied_projects/01_phase_01_tank_drawdown.md), [Development checklist](01_phase_01_checklist.md), [Architecture](../01_architecture/00_structure.md), [Verification](../00_overview/04_verification.md).

## 0. Project readiness and organization

- [ ] Review the applied project scope and identify all nine engineering questions.
- [ ] Reconcile SI references and benchmark values in the development and verification documentation with the US customary baseline below.
- [ ] Confirm required physical-model, solver and integration tests pass before relying on the library for final engineering results.
- [ ] Create `projects/phase_01/README.md` and the required analysis scripts as work progresses.
- [ ] Use Spyder `# %%` cells to organize inputs, execution, postprocessing, visualization and interpretation.
- [ ] Confirm scripts import the installed `tank_dynamics` package from the uv environment without hard-coded machine-specific paths.
- [ ] Configure generated results to be written under `outputs/phase_01/`; retain selected final figures and tables under `projects/phase_01/`.
- [ ] Confirm `/outputs/` is excluded from Git while applied scripts and selected deliverables are tracked.

**Completion gate:** The engineering assignment, unit conventions and execution environment are established. Preliminary analysis may proceed alongside development, but final findings require a verified library.

## 1. Engineering design basis and independent benchmarks

| Parameter | Baseline value |
|---|---:|
| Tank cross-sectional area | 100 ft² |
| Initial depth above outlet | 10 ft |
| Outlet diameter | 3 in |
| Discharge coefficient | 0.62 |
| Gravitational acceleration | 32.174 ft/s² |
| Inflow | 0 cfs |
| Initial elapsed time | 0 s |
| Maintenance planning window | 60 min |
| Residual-depth threshold | 0.33 ft |
| Reporting interval | 5 min |

- [ ] Document the hypothetical facility, control volume, outlet geometry and flow directions in a schematic.
- [ ] Record the constant-area, incompressible, atmospheric and quasi-steady free-discharge assumptions.
- [ ] Document exclusions: downstream backwater, pipe friction, pumps, valve transients, leakage and evaporation.
- [ ] Confirm internal units are ft, ft², ft³, cfs and seconds; convert outlet diameter from inches to feet before calculating area.
- [ ] Confirm reporting units are ft, US gallons, gpm or cfs, and minutes; report depth errors in ft or in.
- [ ] Independently calculate outlet area, initial storage volume and initial discharge.
- [ ] Complete or reference the independently derived volume balance, governing ODE and zero-inflow analytical solution from the development checklist.
- [ ] Independently calculate time to the residual-depth threshold and theoretical emptying time.
- [ ] Complete or reference the constant-positive-inflow equilibrium derivation and explain the analytical solution's physical domain.
- [ ] Record benchmark values before numerical verification and establish justified acceptance tolerances.
- [ ] State that the residual threshold is a reporting milestone, not maintenance or personnel-entry authorization.

**Deliverable:** Schematic, assumptions, derivation and Table 1 (independent analytical benchmarks). Reference existing development work rather than repeating it.

## 2. Baseline drainage analysis

**Script:** `projects/phase_01/01_baseline_analysis.py`

- [ ] Define the WTD-01-A baseline inputs explicitly and call the reusable physical model and simulation functions.
- [ ] Reuse verified results or functions from the gravity-drainage investigation; do not duplicate the solver implementation.
- [ ] Simulate drainage through emptying using the analytical reference and Euler, Heun, RK4 and RK45.
- [ ] Calculate depth, stored volume, discharge and cumulative discharged volume histories.
- [ ] Prepare a reporting table every five minutes from 0 through 60 minutes.
- [ ] Record residual-depth and emptying events separately, even when they fall between reporting times or outside the planning window.
- [ ] If integration terminates at emptying, distinguish physical post-emptying zero-depth/zero-flow continuation from actual solver output.
- [ ] Check for negative accepted depths, unphysical discharge and inconsistent units.
- [ ] Assess the 60-minute criterion separately for the residual milestone and theoretical emptying.
- [ ] Explain how decreasing hydraulic head affects the drainage rate.

**Deliverables:** Figures 1–3 and Table 2.

## 3. Numerical verification and solver selection

**Script:** `projects/phase_01/02_numerical_verification.py`

- [ ] Confirm the generic scalar and two-component benchmarks and common solver result conventions are satisfied under the development checklist.
- [ ] Review `experiments/phase_01/02_solver_comparison.py` and reuse the verified analysis functions.
- [ ] Select a common smooth pre-emptying interval using the independent analytical emptying time.
- [ ] Evaluate at least four successively halved fixed steps (suggested: 120, 60, 30 and 15 s; adjust if needed).
- [ ] Compare all four methods against the analytical reference at matching times.
- [ ] Calculate maximum absolute depth error and RMSE; avoid undefined relative errors at zero depth.
- [ ] Estimate observed convergence orders for Euler, Heun and RK4 and explain deviations from expected orders of approximately 1, 2 and 4.
- [ ] Record derivative evaluation counts and repeat runtime measurements if making timing claims.
- [ ] Distinguish RK45 internal adaptive steps from requested reporting times.
- [ ] Compare emptying-time errors separately from smooth-interval convergence.
- [ ] Verify volume balance using documented discharge quadrature; explain quadrature error contribution.
- [ ] Check results against tolerances established before final runs and document any failures or limitations.
- [ ] Select and justify a solver and settings for the outlet alternatives based on accuracy, cost and boundary handling.

**Deliverables:** Figures 4–5 and Tables 3–4; documented solver recommendation.

## 4. Engineering alternatives

**Script:** `projects/phase_01/03_outlet_alternatives.py`

| Scenario | Outlet diameter |
|---|---:|
| WTD-01-A | 3 in |
| WTD-01-B | 2 in |
| WTD-01-C | 4 in |

- [ ] Define all three idealized orifice scenarios; hold other parameters, including discharge coefficient, constant.
- [ ] Run each scenario with the selected verified solver and analytical reference.
- [ ] Compare initial discharge, residual-depth time and theoretical emptying time.
- [ ] Check each scenario against the 60-minute window for both milestones.
- [ ] Verify numerical accuracy and physical boundary behavior for each alternative.
- [ ] Plot the three drainage histories on comparable axes.
- [ ] Compare the baseline analytical drainage time with a constant-discharge estimate based on initial flow; quantify and explain the discrepancy.
- [ ] Discuss faster drainage versus increased peak discharge and identify receiving-system capacity as unknown.
- [ ] Explain why these orifice alternatives are not nominal pipe-size recommendations.
- [ ] Provide a conditional engineering recommendation supported by the results, without assuming downstream capacity is adequate.

**Deliverables:** Figure 6 and Table 5.

## 5. Optional extension — Variable inflow

**Script:** `projects/phase_01/04_variable_inflow.py`

Begin only after the required gravity-drainage MVP is verified. This section is not required for Phase 01 completion.

- [ ] Complete the applicable development checklist extension and review `experiments/phase_01/03_variable_inflow.py`.
- [ ] Evaluate constant inflows of 80 and 160 gpm, converted to cfs before integration.
- [ ] Evaluate 80 gpm for the first 20 minutes followed by zero inflow.
- [ ] Calculate equilibrium depths and examine approach from above and below equilibrium.
- [ ] Determine whether the residual threshold is achievable for each constant inflow.
- [ ] Handle inflow discontinuities explicitly and document behavior when an empty tank receives water.
- [ ] Verify volume balance and document capacity/overflow policy where relevant.
- [ ] Explain implications for maintenance readiness and retain optional figures and tables separately from required deliverables.

## 6. Consolidated engineering analysis

**Script:** `projects/phase_01/05_final_analysis.py`

- [ ] Assemble the verified baseline, solver comparison and alternatives results into a consistent engineering summary using shared package functions or reproducibly generated results.
- [ ] Confirm scenario identifiers, units, parameters and solver settings agree across all scripts and outputs.
- [ ] Ensure required analyses can be reproduced without relying on variables left in a previous Spyder session.
- [ ] Summarize initial storage, initial flow, time-dependent behavior, residual-depth time and emptying time.
- [ ] Summarize planning-window compliance, alternative trade-offs, constant-flow estimate error and solver recommendation.
- [ ] Check that the consolidated results agree with the underlying analytical benchmarks and verification tables.
- [ ] Export final figures and tables with descriptive filenames and units.

## 7. Figures and tables register

Retain selected final deliverables in `projects/phase_01/figures/` and `projects/phase_01/tables/`. The following filenames are suggested, not additional scope requirements.

| Complete | Output | Suggested filename |
|---|---|---|
| [ ] | Figure 1 — Analytical and numerical depth histories | `01_depth_history.png` |
| [ ] | Figure 2 — Gravity discharge versus time | `02_discharge_history.png` |
| [ ] | Figure 3 — Stored volume versus time | `03_storage_history.png` |
| [ ] | Figure 4 — Numerical depth error on smooth interval | `04_depth_error.png` |
| [ ] | Figure 5 — Log-log fixed-step convergence | `05_convergence.png` |
| [ ] | Figure 6 — Outlet alternative drainage histories | `06_outlet_alternatives.png` |
| [ ] | Table 1 — Independent analytical benchmarks | `01_analytical_benchmarks.csv` |
| [ ] | Table 2 — Baseline operational reporting | `02_baseline_reporting.csv` |
| [ ] | Table 3 — Solver accuracy and computational cost | `03_solver_comparison.csv` |
| [ ] | Table 4 — Emptying-time and volume-balance verification | `04_verification.csv` |
| [ ] | Table 5 — Alternatives and planning-window assessment | `05_outlet_alternatives.csv` |

- [ ] Label axes, units, relevant parameters, solver settings and legends.
- [ ] Verify tables include units and sufficient precision without implying unsupported accuracy.
- [ ] Confirm selected figures and tables match the final verified runs.

## 8. Engineering findings and documentation

**Deliverable:** `projects/phase_01/findings.md` (suggested length: 2–4 pages).

- [ ] Describe the problem, objective, assumptions and modeling approach.
- [ ] Answer all nine engineering questions in Section 5 of the applied scope using computed evidence.
- [ ] Summarize analytical and numerical verification, acceptance tolerances and solver selection.
- [ ] Present maintenance planning implications and outlet trade-offs.
- [ ] Identify limitations and unresolved issues, including unknown receiving-system capacity.
- [ ] Identify additional facility data needed for real-world application, such as actual geometry, outlet configuration and downstream hydraulic conditions.
- [ ] State that this is an educational model, not a site-specific design or approved maintenance procedure.
- [ ] Update the phase README with execution instructions, scenario inputs, links to findings and selected outputs.
- [ ] Update the projects README and root README to reflect actual completion status.
- [ ] Record learning log entries covering discoveries, failed approaches and resolutions.

## 9. Applied project release gate

- [ ] Required development checklist verification gates are satisfied and automated tests pass (`uv run pytest`).
- [ ] All required project scripts execute from a clean uv environment and fresh Spyder console when run as complete scripts.
- [ ] Independent benchmarks, convergence, event accuracy and conservation satisfy justified tolerances; unresolved failures prevent release as verified.
- [ ] No negative accepted physical depths or unphysical post-emptying discharge are reported.
- [ ] All six required figures and five required tables are complete and reproducible.
- [ ] Engineering findings address all nine questions and distinguish hypothetical criteria from actual operating requirements.
- [ ] Published results record model inputs, units, solver settings and benchmark provenance.
- [ ] Generated outputs are excluded from Git; selected final deliverables and scripts are tracked.
- [ ] Review staged changes and commit with a descriptive multi-line message.
- [ ] Mark both Phase 01 checklists complete only when their required gates are satisfied; record optional extension status separately.

## Suggested applied work sessions

| Session | Focus |
|---|---|
| 1 | Design basis, independent benchmarks and project setup |
| 2 | Baseline analysis and operational reporting |
| 3 | Verification synthesis and solver selection |
| 4 | Outlet alternatives and engineering interpretation |
| 5 | Consolidated analysis, findings and release review |

The applied scope estimates 16–25 hours inclusive of development and required applied work, excluding the optional extension. These sessions are a suggested sequence within that combined effort, not an additional 16–25-hour assignment. Reassess the estimate as independent learning and verification progress.
