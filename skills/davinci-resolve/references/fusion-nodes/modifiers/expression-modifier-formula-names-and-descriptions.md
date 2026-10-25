# Expression modifier formula names and descriptions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Expression.
[Chapter index](INDEX.md) / [Previous section](custom-poly-and-expression.md) / [Next section](expression-image-gradient-key-stretcher-and-midi.md) / [Expression](custom-poly-and-expression.md)
<a id="source-expression-syntax-formulas"></a> <a id="source-modifiers-part-2"></a>

### Expression Syntax Formulas

Within an expression, formulas go into either the Number Out tab or the Point Out tab. They may be assembled from the following functions:

n1...n9 p1x...p9x p1y...p9y time pi e log(x) ln(x) sin(x) cos(x) tan(x) asin(x) acos(x) atan(x) atan2(x, y) abs(x) int(x) frac(x) sqrt(x) rand(x, y) rands(x, y, s) min(x, y) max(x, y) dist(x1, y1, x2, y2) dist3d(x1,y1,z1,x2,y2,z2)


Whatever Number Input 1..9 holds. The X belonging to Positional Control 1..9. The Y belonging to Positional Control 1..9. Where you are in time now (the frame number). What pi equals. What e equals. Logarithm of x to base 10. Logarithm of x to base e (the natural one). Sine of x, with x given in degrees. Cosine of x, with x given in degrees. Tangent of x, with x given in degrees. Arcsine of x, returned in degrees. Arccosine of x, returned in degrees. Arctangent of x, returned in degrees. Arctangent of x,y, returned in degrees. How big x is regardless of sign (its absolute value). x rounded to its whole-number part. The part of x past the decimal point. The Square Root of x. Some random figure that lands between x and y. Some random figure between x and y, governed by seed s. Whichever of x and y is smaller. Whichever of x and y is larger. How far apart point x1,y2 and x2,y2 are. How far apart the 3D points x1,y2,z1 and x2,y2,z2 are

`noise(x)` `noise2(x, y)` `noise3(x, y, z)` `if(c, x, y)`

A Perlin noise figure that varies smoothly off x A Perlin noise figure that varies smoothly off x and y A Perlin noise figure that varies smoothly off x, y and z Hands back x when c isn't 0, and y when it is.
