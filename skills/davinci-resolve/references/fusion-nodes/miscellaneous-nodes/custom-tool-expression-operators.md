# Custom tool expression operators

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom tool.
[Chapter index](INDEX.md) / [Previous section](custom-tool-math-functions.md) / [Next section](custom-tool-neighborhood-filter.md) / [Custom Tool CT](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md)


### Fusion expression operators

These are Fusion Custom Tool expressions, not C. Comparisons and logical operations return 1.0 or 0.0.

| Operator | Meaning |
| --- | --- |
| `!x` | 1 when x is zero; otherwise 0. |
| `-x` | Negation. |
| `+x` | Identity. |
| `x^y` | Exponentiation. |
| `x*y` | Multiplication. |
| `x/y` | Division. |
| `x%y` | Remainder. |
| `x+y` | Addition. |
| `x-y` | Subtraction. |
| `x<y` | Less than. |
| `x>y` | Greater than. |
| `x<=y` | Less than or equal. |
| `x>=y` | Greater than or equal. |
| `x=y; x==y` | Equality. |
| `x<>y; x!=y` | Inequality. |
| `x&y; x&&y` | Both operands nonzero. |
| `x\|y; x\|\|y` | Either operand nonzero. |

