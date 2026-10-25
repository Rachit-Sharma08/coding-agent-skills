# Custom poly and expression

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom poly, Expression.
[Chapter index](INDEX.md) / [Previous section](calculation-coordinate-spline-and-poly-modifiers.md) / [Next section](expression-modifier-formula-names-and-descriptions.md) / [Continue Expression / Expression Syntax Formulas](expression-modifier-formula-names-and-descriptions.md) / [Custom Poly](calculation-coordinate-spline-and-poly-modifiers.md)
<a id="source-config-tab"></a> <a id="source-config-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-expression"></a> <a id="source-expressions-modifier-controls"></a> <a id="source-inspector-3"></a> <a id="source-name-for-number-or-point-x"></a> <a id="source-number-out-tab"></a> <a id="source-point-out-tab"></a> <a id="source-polyline-tab"></a> <a id="source-the-custom-poly-polyline-tab"></a> <a id="source-the-expressions-modifier-config-tab"></a> <a id="source-the-number-out-tab"></a> <a id="source-the-point-out-tab"></a>

### The Custom Poly Polyline tab

### Polyline Tab

The polyline tab lays out the controls for wiring up and reshaping the polyline. Connect Source Polyline here Lets you wire other polylines into the modifier. Show View Controls This checkbox flips the polyline controls' visibility in the viewer on or off. Number of Points You can set how many output points there are, which governs how finely the polyline is custom-subdivided. A value of zero falls back on the count of original source points.

Poly Expression X/Y The fields where you type the mathematical expressions. For instance, px*(1-n1)+n1*get2x(disp) and py*(1-n1)+ n1*get2y(disp). It draws on most of the same expression variables as the Expression modifier covered below (that is, n1..n9, p1x..p9x, p1y..p9y, math functions, and so on), and tacks on these:

- px,py giving the current point on the source polygon
- disp giving how far the point sits along the polyline (0.0 marks the start, 1.0 the end)
- index giving the current point’s index (counted from zero)
- num giving the count of output points
- getx(disp), gety(disp) for pulling values from any spot on the polyline
- getx_at(disp, time), gety_at(disp, time) for pulling values from polylines at other times
- In the same vein, get2x/y(), get3x/y(), get2x/y_at(), get3x/y_at() cover the second and third source polys

### Config Tab

The config tab lets you choose how many Points and Numbers the modifier displays (up to 9) and hand them custom names to keep things organized.

### Expression

An expression is a variable or a mathematical calculation placed on a parameter in lieu of a plain numeric value. You can attach an expression to any parameter in Fusion, or you can attach the Expression modifier, which appends several tabs to the modifier Inspector. Putting this modifier on a parameter grants the ability to drive that parameter off any number of controls, whether positional or value-based. It is exceptionally flexible next to the more limited Calculation or Offset modifiers, yet it cannot reach values from frames other than the present time. The Expression modifier takes nine value inputs and nine position inputs, which feed a user-defined mathematical expression that outputs a value. To attach it to a parameter, right-click the parameter in the Inspector and pick Modify With > Expression from the contextual menu. What kind of value the Expression returns hinges entirely on the control it is modifying. Against a value control (a slider, say), the Expression in the Number Out tab is evaluated to form the result. Against a positional control (such as Center), the Point Out tab drives the result. The controls for the Expression modifier sit in the Inspector's Modifiers tab and are described below.

### Inspector

### Expressions modifier controls

### Controls Tab

This tab hands you nine number controls and nine point controls. Within an expression, the number controls' values are addressed as n1 through n9. Each point control's X-coordinate is addressed as p1x through p9x, and its Y-coordinate as p1y through p9y. You can set these values by hand, wire them to other parameters, animate them, and even wire them to other Expressions or Calculations.

### Number Out Tab

Here you type mathematical formulas that pull on the Controls tab's Number In and Point In values. Whatever they output drives the control the Expression was placed on. The syntax for this field is covered below.

### The Number Out tab

### Point Out Tab

This tab's two text boxes run mathematical formulas that tap the Number In and Point In values from the Controls tab. The resulting value drives the control the Expression was placed on. The Expression in the upper text box computes the X-axis value, while the lower text box computes the Y-axis control. The syntax for this field is covered below.

### The Point Out tab

### Config Tab

A solid expression gets reused time and again. Because of that, giving each parameter or control a more telling name and tucking away the unused ones can pay off. The Expressions modifier's Config Tab lets you tailor both the visibility and the name of every one of the nine point and number controls.

### The Expressions modifier Config tab

Random Seed The Random Seed control fixes the starting number that the Rand() function uses. The rand(x, y) function yields a random value between X and Y, generating a fresh one each frame. So long as this Random Seed slider stays put, the values generated at frame x never change. Move the Seed slider to a new value to draw a different value at that frame. Show Number or Point X These checkbox controls number eighteen in all, one per each of the nine Number and nine Point inputs. Tick a checkbox to bring the control for Number x or Point x into the Controls tab.

### Name for Number or Point X

These edit controls also number eighteen, one per each of the nine Number and nine Point inputs. Enter a fresh name for the input into this edit control to relabel that Input in the Controls tab.
