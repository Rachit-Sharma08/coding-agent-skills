# Custom tool math functions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom tool.
[Chapter index](INDEX.md) / [Previous section](custom-tool-channel-variables-and-pixel-sampling.md) / [Next section](custom-tool-expression-operators.md) / [Custom Tool CT](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md)
<a id="source-mathematical-expressions-pi"></a>

### Custom Tool mathematical expressions

Fusion expression trig uses degrees.

| Expression | Meaning |
| --- | --- |
| `pi` | Value of pi. |
| `e` | Value of e. |
| `log(x)` | Base-10 logarithm. |
| `ln(x)` | Natural logarithm. |
| `sin(x)` | Sine, x in degrees. |
| `cos(x)` | Cosine, x in degrees. |
| `tan(x)` | Tangent, x in degrees. |
| `asin(x)` | Arcsine in degrees. |
| `acos(x)` | Arccosine in degrees. |
| `atan(x)` | Arctangent in degrees. |
| `atan2(x,y)` | Two-argument arctangent in degrees. |
| `abs(x)` | Absolute value. |
| `int(x)` | Integer part. |
| `frac(x)` | Fractional part. |
| `sqrt(x)` | Square root. |
| `rand(x,y)` | Random value between x and y. |
| `rands(x,y,s)` | Random value between x and y, using seed s. |
| `min(x,y)` | Minimum. |
| `max(x,y)` | Maximum. |
| `dist(x1,y1,x2,y2)` | Distance between (x1,y1) and (x2,y2). |
| `dist3d(x1,y1,z1,x2,y2,z2)` | Distance between (x1,y1,z1) and (x2,y2,z2). |
| `noise(x)` | Smooth Perlin noise based on x. |
| `noise2(x,y)` | Smooth Perlin noise based on x and y. |
| `noise3(x,y,z)` | Smooth Perlin noise based on x, y and z. |
| `if(c,x,y)` | x when c is nonzero; otherwise y. |
