# Custom tool neighborhood filter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom tool.
[Chapter index](INDEX.md) / [Previous section](custom-tool-expression-operators.md) / [Next section](fields-fields-node-introduction.md) / [Custom Tool CT](custom-tool-value-variables-n1-n8-p1x-p4x-p1y-p4y-s1-s4.md)
<a id="source-common-controls-2"></a> <a id="source-filtering"></a>

### Filtering

This second example of ours reproduces what a 3 x 3 Custom Filter node does once it is set to average the current pixel alongside the eight pixels ringing it. To reproduce that through a Custom Tool node, drop a Custom Tool node onto the node tree, then key the following expressions into the Setup tab. (Keep the node unconnected so it holds off any updating until we are good and ready.)

```text
s1: 1.0/w1
s2: 1.0/h1
```

This pair of expressions gets worked out as each frame begins. S1 splits 1.0 by the frame’s present width, while S2 splits 1.0 by its height. Out of that comes a floating-point value between 0.0 and 1.0 standing for the span from the current pixel over to the next pixel along each axis.

Now key the following expression into the Channel tab’s first text control (r).

```text
(getr1w(x-s1, y-s2) + getr1w(x, y-s2) + getr1w(x+s1, y-s2) + getr1w(x+s1, y) + getr1w(x-s1, y) + r1 +getr1w(x-s1, y+s2) + getr1w(x, y+s2) + getr1w(x+s1, y+s2)) / 9
```

What this expression does is sum the current pixel and its eight neighbors, calling the `getr1w()` function eight times and handing it values measured against the current position. Take note that we named the pixels through x+s1, y+s2, in place of x+1, y+1. Because Fusion names pixels as floating-point values between 0.0 and 1.0, that is the very reason we built the expressions placed into the Setup tab. Had x+1, y+1 gone in instead, the expression would have kept sampling that one same pixel again and again. (The function we leaned on wraps the pixel position around the image whenever the offset values stray out of range.) With the red channel settled, now turn to the following expressions for the green, blue, and alpha channels.

```text
(getg1w(x-s1, y-s2) + getg1w(x, y-s2) + getg1w(x+s1, y-s2) + getg1w(x+s1, y) + getg1w(x-s1, y) + g1 +getg1w(x-s1, y+s2) + getg1w(x, y+s2) + getg1w(x+s1, y+s2)) / 9
(getb1w(x-s1, y-s2) + getb1w(x, y-s2) + getb1w(x+s1, y-s2) + getb1w(x+s1, y) + getb1w(x-s1, y) + b1 +getb1w(x-s1, y+s2) + getb1w(x, y+s2) + getb1w(x+s1, y+s2)) / 9
(geta1w(x-s1, y-s2) + geta1w(x, y-s2) + geta1w(x+s1, y-s2) + geta1w(x+s1, y) + geta1w(x-s1, y) + a1 + geta1w(x-s1, y+s2) + geta1w(x, y+s2) + geta1w(x+s1, y+s2)) / 9
```

Now the moment has come to look over the results. Drop in a Background node set to a solid color, then shift that color to a pure red. Drop in a hard-edged Rectangular effects mask and wire it to the expression you have just built. By way of contrast, drop in a Custom Filter node and mirror the settings from the image shown above. Run a pipe into this node from the background, then look over the results. Flip back and forth between the Custom Tool node and the Custom Filter, zoomed in tight on the effects mask’s top corners. Granted, the Custom Filter node renders far quicker than the Custom Tool node we put together, yet the real edge of the Custom Tool node lies in its flexibility. As one case, you might take an image wired into input 2 and let it steer the neighborhood average applied to input one, swapping every instance of getr1w, getg1w, and getb1w throughout the expression for getr2w, getg2w, and getb2w, all while leaving the r1, g1, and b1s untouched. That is but a single case; what the Custom Tool node can do knows no bounds.

### Common Controls

Settings Tab Here again the Inspector’s Settings tab is mirrored across the rest of the miscellaneous nodes. Every one of these shared controls is laid out at length where the chapter ends, inside the “The Common Controls” section.
