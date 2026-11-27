# SymPy Quick Reference

## Overview

SymPy is a Python library for symbolic mathematics. It supports
algebraic manipulation, differentiation, integration, limits,
and analytical solutions to differential equations.

For this project, SymPy is primarily used to independently verify
mathematical derivations and analytical solutions.

## Installation

Install as a development dependency using uv:

```bash
uv add --dev sympy
```

## Imports

```python
import sympy as sp
```

## Symbolic Variables

```python
x = sp.Symbol("x")
x, y, t = sp.symbols("x y t")
```

## Common Mathematical Operations

| Function | Description |
|---|---|
| `Symbol()` | Define a symbolic variable |
| `symbols()` | Define multiple symbolic variables |
| `diff()` | Evaluate a derivative |
| `Derivative()` | Construct a symbolic derivative |
| `integrate()` | Evaluate an integral |
| `Integral()` | Construct a symbolic integral |
| `simplify()` | Simplify an expression |
| `expand()` | Expand an expression |
| `factor()` | Factor an expression |
| `solve()` | Solve algebraic equations |
| `dsolve()` | Solve differential equations |
| `limit()` | Evaluate a limit |
| `Eq()` | Define an equation |
| `Function()` | Define a symbolic function |
| `pprint()` | Display formatted mathematical expressions |

## Differentiation

```python
x = sp.Symbol("x")
f = x**3 + 2*x

# Direct differentiation
result = sp.diff(f, x)

# Symbolic differentiation
derivative = sp.Derivative(f, x)
result = derivative.doit()

# Second derivative
result = sp.diff(f, x, 2)
```

## Integration

```python
# Indefinite integration
result = sp.integrate(f, x)

# Definite integration
result = sp.integrate(f, (x, 0, 5))

# Symbolic integration
integral = sp.Integral(f, x)
result = integral.doit()
```

SymPy does not automatically include the arbitrary constant of
integration for indefinite integrals.

## Substitution and Numerical Evaluation

```python
# Substitute a value
result = f.subs(x, 2)

# Evaluate numerically
result = f.subs(x, 2).evalf()
```

## Algebraic Equations

```python
equation = sp.Eq(x**2, 16)
result = sp.solve(equation, x)
```

## Ordinary Differential Equations

```python
t = sp.Symbol("t")
y = sp.Function("y")

equation = sp.Eq(sp.diff(y(t), t), -2*y(t))

# General solution
result = sp.dsolve(equation, y(t))

# Initial-value problem
result = sp.dsolve(
    equation,
    y(t),
    ics={y(0): 10}
)
```

## Displaying Results

```python
print(result)
sp.pprint(result)
```

## Project Usage

SymPy should be used to:

- Verify handwritten mathematical derivations.
- Verify derivatives and integrals.
- Determine independent analytical benchmark solutions.
- Verify initial-value problems.
- Simplify governing equations.
- Investigate mathematical relationships.

SymPy should not replace independent mathematical derivations
or the implementation of numerical integration methods.

## References

- [SymPy Documentation](https://docs.sympy.org/)
- [SymPy Tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html)
