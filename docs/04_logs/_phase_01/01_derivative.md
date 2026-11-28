## Differentiation of an Exponential Function Using First Principles

### Objective

Determine the derivative of the following exponential function
using the limit definition rather than the chain rule.

$$
f(x)=e^{-0.2x}
$$

### 1. Apply the Limit Definition

The derivative is defined as:

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}
$$

Substituting the function:

$$
f'(x)=\lim_{h\to0}\frac{e^{-0.2(x+h)}-e^{-0.2x}}{h}
$$

### 2. Apply Exponential Properties

Using the exponential identity:

$$
e^{a+b}=e^ae^b
$$

Expand the exponent:

$$
f'(x)=\lim_{h\to0}\frac{e^{-0.2x}e^{-0.2h}-e^{-0.2x}}{h}
$$

Factor out the common exponential term:

$$
f'(x)=e^{-0.2x}\lim_{h\to0}\frac{e^{-0.2h}-1}{h}
$$

### 3. Rearrange the Expression

Multiply the numerator and denominator by -0.2 to obtain
the fundamental exponential limit without changing the
value of the expression.

$$
f'(x)=-0.2e^{-0.2x}\lim_{h\to0}\frac{e^{-0.2h}-1}{-0.2h}
$$

### 4. Evaluate the Limit

The fundamental exponential limit is:

$$
\lim_{u\to0}\frac{e^u-1}{u}=1
$$

Let:

$$
u=-0.2h
$$

As h approaches zero, u also approaches zero. Therefore:

$$
\lim_{h\to0}\frac{e^{-0.2h}-1}{-0.2h}=1
$$

Although direct substitution produces the undefined expression
0/0, the limit exists because the expression approaches 1
from both directions.

### 5. Final Result

Substitute the evaluated limit:

$$
f'(x)=-0.2e^{-0.2x}(1)
$$

Therefore:

$$
f'(x)=-0.2e^{-0.2x}
$$

### 6. Verification Using SymPy

```python
import sympy as sp

x, h = sp.symbols("x h")

f = sp.exp(-0.2*x)

# Verify the exponential limit
expression = (sp.exp(-0.2*h) - 1) / (-0.2*h)
limit_result = sp.limit(expression, h, 0)

# Verify the derivative
derivative = sp.diff(f, x)

print(limit_result)
print(derivative)