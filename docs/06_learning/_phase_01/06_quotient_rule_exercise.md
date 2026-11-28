# Quotient Rule – Learning Exercise

## 1. Objective

Develop a basic understanding of symbolic differentiation using Python and SymPy by implementing the power rule and quotient rule.

The exercise should return two values:

- `expression`: The symbolic expression of the derivative.
- `result`: The numerical value of the derivative at the provided argument.

The objective is to understand the mathematical operations rather than replicate SymPy's full differentiation capabilities.

## 2. Mathematical Reference

### Power Rule

$$
f(x)=ax^n
$$

$$
f'(x)=anx^{n-1}
$$

### Quotient Rule

Given:

$$
f(x)=\frac{v(x)}{u(x)}
$$

The derivative is:

$$
f'(x)=\frac{u(x)v'(x)-v(x)u'(x)}{[u(x)]^2}
$$

The original denominator must be nonzero at the evaluation argument.

## 3. Useful SymPy Commands

| Command | Purpose |
|---|---|
| `sp.Symbol('x')` | Define a symbolic variable. |
| `sp.sympify(expression)` | Convert a string into a symbolic expression. |
| `sp.diff(f, x)` | Differentiate an expression with respect to x. |
| `sp.simplify(f)` | Simplify a symbolic expression. |
| `sp.expand(f)` | Expand an algebraic expression. |
| `sp.factor(f)` | Factor an algebraic expression. |
| `f.subs(x, 2)` | Substitute a numerical value for x. |
| `f.evalf()` | Evaluate an expression numerically. |
| `sp.pprint(f)` | Display an expression in readable mathematical notation. |
| `str(f)` | Convert a symbolic expression into a string. |

Use `sp.diff()` primarily to independently verify the manually constructed derivatives.

## 4. Power Rule Test Cases

| Function | Argument | Expected Derivative | Expected Result |
|---|---:|---|---:|
| $x^3$ | 2 | $3x^2$ | 12 |
| $4x^3$ | 2 | $12x^2$ | 48 |
| $5x$ | 3 | $5$ | 5 |
| $7$ | 2 | $0$ | 0 |
| $x^{-2}$ | 2 | $-2x^{-3}$ | -0.25 |
| $x^{1/2}$ | 4 | $\frac{1}{2\sqrt{x}}$ | 0.25 |
| $-3x^4$ | 2 | $-12x^3$ | -96 |
| $3x^2+2x+1$ | 2 | $6x+2$ | 14 |

The final test case requires applying the power rule to each term of a polynomial.

## 5. Quotient Rule Test Cases

| Numerator | Denominator | Argument | Expected Derivative | Expected Result |
|---|---|---:|---|---:|
| $x^2$ | $x+1$ | 1 | $\frac{x^2+2x}{(x+1)^2}$ | 0.75 |
| $x^3$ | $x^2+1$ | 2 | $\frac{x^4+3x^2}{(x^2+1)^2}$ | 1.12 |
| $1$ | $x$ | 2 | $-\frac{1}{x^2}$ | -0.25 |
| $x^2$ | $2$ | 3 | $x$ | 3 |
| $x^3$ | $x^2$ | 2 | $1$ | 1 |
| $x$ | $x$ | 2 | $0$ | 0 |
| $x^2+1$ | $x$ | 2 | $1-\frac{1}{x^2}$ | 0.75 |
| $x+1$ | $x-1$ | 3 | $-\frac{2}{(x-1)^2}$ | -0.50 |

### Undefined Expressions

| Numerator | Denominator | Argument | Expected Result |
|---|---|---:|---|
| $x$ | $x$ | 0 | Undefined |
| $x^2$ | $x-1$ | 1 | Undefined |
| $1$ | $x$ | 0 | Undefined |

Remember that simplifying an expression does not eliminate the domain restrictions of the original function.

## 6. Exercise Checklist

### Power Rule

- [ ] Review the mathematical definition of the power rule.
- [ ] Convert the input string into a symbolic expression.
- [ ] Identify the coefficient and exponent.
- [ ] Apply the power rule manually.
- [ ] Simplify the derivative.
- [ ] Evaluate the derivative at the provided argument.
- [ ] Return the symbolic expression and numerical result.
- [ ] Verify against the provided test cases.
- [ ] Compare results against SymPy differentiation.

### Quotient Rule

- [ ] Review the mathematical definition of the quotient rule.
- [ ] Convert the numerator and denominator into symbolic expressions.
- [ ] Calculate the derivative of the numerator.
- [ ] Calculate the derivative of the denominator.
- [ ] Construct the quotient rule expression manually.
- [ ] Simplify the resulting derivative.
- [ ] Check whether the original denominator is zero at the argument.
- [ ] Evaluate the derivative numerically.
- [ ] Return the symbolic expression and numerical result.
- [ ] Verify against the provided test cases.
- [ ] Compare results against SymPy differentiation.

### Learning Review

- [ ] Explain the quotient rule without referring to documentation.
- [ ] Understand the difference between symbolic and numerical evaluation.
- [ ] Recognize mathematically equivalent symbolic expressions.
- [ ] Understand why domain restrictions remain after simplification.
- [ ] Record any difficulties or observations in the learning log.

## 7. Completion Criteria

The exercise is complete when the derivatives can be constructed manually, the numerical results agree with the expected values, and the mathematical reasoning behind each operation is understood.

Production-level validation, automated testing frameworks, and support for arbitrary mathematical functions are outside the scope of this exercise.