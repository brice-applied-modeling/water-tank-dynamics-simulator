# Water Tank Dynamics — Verification Plan

## Experiments and verification

### Experiment 1: Gravity drainage

- Implement the governing derivative and analytical solution.
- Plot depth, volume, and discharge versus time.
- Calculate theoretical emptying time.
- Confirm that initial conditions and physical boundaries are respected.

### Experiment 2: Numerical solver comparison

- Run Euler, Heun, RK4, and RK45 using the same physical parameters.
- Compare solutions at common evaluation times against the analytical reference.
- Test fixed steps of 60, 30, 15, and 7.5 seconds.
- Calculate maximum absolute error, RMSE, and emptying-time error.
- Estimate observed convergence order before emptying using $p=\log_2(E_{\Delta t}/E_{\Delta t/2})$.
- Plot error versus time step on logarithmic axes.
- Optionally compare execution times and derivative evaluation counts.

### Experiment 3: Variable inflow (extension)

- Evaluate constant inflow, step changes, and periodic inflow.
- Compare constant-inflow behavior with the analytical equilibrium depth.
- Segment integration at known inflow discontinuities where appropriate.
- Examine how outlet size and tank area affect response time.

### Verification checklist

- [ ] Analytical solution reproduces initial depth.
- [ ] Baseline initial volume equals 30 m³.
- [ ] Analytical emptying time is approximately 47.59 minutes.
- [ ] Zero initial depth and zero inflow produce zero depth.
- [ ] Gravity drainage produces monotonically decreasing, nonnegative depth.
- [ ] Numerical errors decrease under time-step refinement before emptying.
- [ ] Numerical emptying time approaches the analytical reference.
- [ ] Integrated outflow approximately balances the change in stored volume, using independently documented quadrature.
- [ ] Invalid inputs raise appropriate exceptions.
- [ ] Constant-inflow simulation approaches equilibrium (extension).


## Acceptance criteria

- Analytical initial depth and volume: absolute error below 1e-10 in SI units.
- Analytical emptying time: 2855.203 seconds (within 0.1 seconds).
- Convergence: use a smooth interval ending at 50% of the analytical emptying time; compare on common grids and check observed orders near 1, 2 and 4 for Euler, Heun and RK4 respectively, before roundoff dominates.
- RK45: target maximum depth error below 1e-5 m on the smooth interval with rtol=1e-8 and atol=1e-10.
- Emptying-time error: report separately from smooth-interval error; target less than 1% with refinement.
- Volume balance: target residual below 0.1% of initial volume on a refined grid.

## Results record

Record case ID, inputs, solver, step size or tolerances, expected result, actual result, error, pass/fail and notes.

## References

- [Mathematical model](02_mathematical_model.md)
- [Numerical methods](03_numerical_methods.md)
- [pytest documentation](https://docs.pytest.org/)
