# Custom tool image rotation

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom tool.
[Chapter index](INDEX.md) / [Previous section](custom-tool-math-functions.md) / [Next section](custom-tool-neighborhood-filter.md) / [Custom Tool CT](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md)
<a id="source-examples"></a> <a id="source-rotation"></a>

### Examples

What follows is a set of examples meant to deepen your grasp of the Custom Tool node’s various pieces.

### Rotation

Spinning an image around calls for the standard 2D rotation equations:

```text
x' = x * cos(theta) - y * sin(theta)
y' = x * sin(theta) + y * cos(theta)
```

Pressing the n1 slider into service for the angle theta, plus a sample function, lands us at this (for the red channel):

```text
getr1b(x * cos(n1) - y * sin(n1), x * sin(n1) + y * cos(n1))
```

What this works out is the current pixel’s (x,y) position turned about the origin at (0,0) (that bottomleft corner), after which it pulls the red component off the source pixel sitting at this turned position.

To rotate about the center, we have to knock 0.5 off our x and y coordinates ahead of the rotation, then tack 0.5 back on once it is done:

```text
getr1b((x-.5) * cos(n1) - (y-.5) * sin(n1) + .5, (x-.5) * sin(n1) + (y-.5) * cos(n1) + .5)
```

That ushers in the next lesson: Setup and Intermediate Expressions. They earn their place by hastening things along, since they pare down the work shouldered by the Channel expressions. The Setup expressions fire just one time, and what they yield holds steady across every pixel, so you can press these into service for s1 and s2, in turn:

```text
s1: cos(n1)
s2: sin(n1)
```

Intermediate expressions fire once for each pixel, so you can press these into service for i1 and i2:

```text
i1: (x-.5) * s1 - (y-.5) * s2 + .5
i2: (x-.5) * s2 + (y-.5) * s1 + .5
```

These supply the x and y parameters feeding the `getr1b()` function shown earlier, only now with the Setup results, s1 and s2, swapped in so the trig functions fire just once per frame instead of every pixel. From here you can lean on these intermediate results inside your Channel expressions:

```text
red: getr1b(i1, i2)
green: getg1b(i1, i2)
blue: getb1b(i1, i2)
alpha: geta1b(i1, i2)
```

Once the Intermediate expressions are swapped in, all those additions, subtractions, and multiplications fall to a single pass per pixel rather than four. The rule of thumb runs thus: whatever holds steady, compute it but once. This rotation here is a plain one that pays the image aspect no mind whatever. Folding that in is left to you as an exercise (sorry). One further refinement would be to let the rotation pivot on points other than the center.
