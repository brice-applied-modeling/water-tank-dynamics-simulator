# Phase 01 Hydraulic Foundations

## Governing relationships to review

$$
V=Ah
$$

$$
a=\frac{\pi d^2}{4}
$$

$$
\frac{dV}{dt}=Q_{in}-Q_{out}
$$

$$
\frac{dV}{dt}=\frac{dV}{dh}\frac{dh}{dt}
$$

$$
\frac{P}{\gamma}+\frac{v^2}{2g}+z=\mathrm{constant}
$$

$$
v=\sqrt{2gh}
$$

$$
Q_{out}=C_d a\sqrt{2gh}
$$

| Symbol | Definition | Unit |
|---|---|---|
| $V$ | Stored volume | ft³, gal |
| $A$ | Tank area | ft² |
| $h$ | Water depth above outlet | ft |
| $a$ | Outlet area | ft² |
| $d$ | Outlet diameter | in, ft |
| $\pi$ | Circle constant | Dimensionless |
| $Q_{in},Q_{out}$ | Inflow and outflow | cfs, gpm |
| $t$ | Time | s, min |
| $P$ | Pressure | lbf/ft², psi |
| $\gamma$ | Specific weight | lbf/ft³ |
| $v$ | Velocity | fps |
| $g$ | Gravity (32.174) | ft/s² |
| $z$ | Elevation | ft |
| $C_d$ | Discharge coefficient | Dimensionless |

Bernoulli's equation is the ideal steady, incompressible, lossless energy relationship along a streamline. Justify neglecting free-surface velocity and using atmospheric pressure at both endpoints for the simplified orifice model. The discharge coefficient accounts empirically for departure from ideal discharge. Use a consistent elevation datum. The geometry assumes the outlet reference is at the tank bottom.

The displayed geometry and discharge equations directly yield ft³ and cfs with compatible feet and seconds; this is not a project-wide unit mandate. Convert inches to feet when calculating area in ft², psi to lbf/ft² for the pressure-head term, and flow/volume as necessary. For example, 1 ft³ = approximately 7.48052 gal, and 1 cfs = approximately 448.831 gpm. With gpm and minutes, conservation becomes:

$$
7.48052 A\frac{dh}{dt}=Q_{in}-Q_{out}
$$

Here the numerical factor has units gal/ft³. Depth derivative is ft/min.

## Independent derivation assignment

- Draw and label the control volume, outlet and datum; state assumptions and initial conditions.
- Derive the depth ODE from conservation and geometry; justify the orifice law from Bernoulli.
- Reduce the ODE for zero inflow and solve by separation of variables. Derive emptying time and verify the solution by differentiation and initial condition.
- Explain why the solution cannot be extended as a squared expression beyond emptying. Define zero depth and zero discharge after emptying for zero inflow.
- Derive the constant positive inflow equilibrium from zero net flow; explain derivative signs on either side. Implementation of variable inflow is optional.
- Calculate the baseline outlet area, initial volume, initial discharge and emptying time independently using the checklist inputs. Record units and conversions.

Completion: a handwritten or Markdown derivation with all assumptions, units and physical limits. No worked solution is supplied.
