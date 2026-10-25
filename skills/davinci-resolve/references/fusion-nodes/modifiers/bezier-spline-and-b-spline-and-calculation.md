# Bezier spline and b spline and calculation

Version: DaVinci Resolve 20.3 Reference Manual. Context: Bezier spline, B spline, Calculation.
[Chapter index](INDEX.md) / [Previous section](anim-curves-and-bezier-spline.md) / [Next section](calculation-coordinate-spline-and-poly-modifiers.md) / [Bézier Spline](anim-curves-and-bezier-spline.md)
<a id="source-b-spline"></a> <a id="source-b-spline-editor"></a> <a id="source-calc-tab"></a> <a id="source-calculation"></a> <a id="source-calculation-calc-tab"></a> <a id="source-calculation-time-tab"></a> <a id="source-inspector"></a> <a id="source-spline-ease-inout-modifier"></a> <a id="source-time-tab"></a> <a id="source-usage-1"></a>

### Spline Ease In/Out modifier

### B-Spline

Standing in as an alternative to the Bézier Spline, B-spline is yet another of Fusion's animation modifiers and is usually put onto numerical values rather than point values. You apply it by right-clicking a parameter and picking Modify With > B-Spline.

### Usage

### B-Spline Editor

- This animation spline modifier comes with no real Controls tab. The Spline Editor shows the B-spline, though, and that is where you control it. Observe that even though the second keyframe's actual value is 0, the resulting spline reads 0.33, an outcome of the B-spline's distinctive smoothing and weighting algorithms.
- To change the weight, click a control point to select it, hold the W key, and slide the mouse left and right to ease or raise the tension. The same works on several selected control points at once.

### Calculation

Calculations serve to forge indirect links between parameters. A Calculation runs a mathematical expression over two operands, each of which may be wired to another parameter or entered by hand. On top of that, through the Time tab's Time offsets and Scale controls, the Calculation control can reach a parameter's values at moments other than the present time. Its most frequent use is tying two parameters together when one's value range or scope does not suit the other. NOTE: The Expression modifier is, in essence, a more flexible take on the Calculation modifier, bar one thing. Shaping the operands' timing is far simpler in the Calculation modifier than it is with an Expression.

### Inspector

### Calculation Calc tab

### Calc Tab

The Calc tab carries two dials for the wired-in parameter and the value that gets mathematically blended with it. The Operator menu decides how the Second Operand value blends with the parameter's value. First and Second Operand These sliders either hook into published or animated parameters or get hand-set to the values the calculation needs. Operator Pick from the mathematical operations this menu lists to set how the two operands combine. Click the drop-down arrow to open the menu, which holds these options:

- Add
- Subtract (First - Second)
- Multiply
- Divide (First / Second)
- Divide (Second / First)
- Subtract (Second - First)
- Minimum
- Maximum
- Average
- First only

### Time Tab

The Time tab lets you alter the timing of the Calculation modifier. Its controls either retime how fast the effect runs or shift it in time.

### Calculation Time tab

First and Second Operand Time Scale These sliders scale the frame number and hand back the operands' values at the scaled frame number. At a value of 1 the operand's value comes back from frame x while the composition sits on frame x. As an illustration, if the first operand is animated from a value of 1 to 50 across frame 0 to 10, then a scale of 0.5 makes the calculation hand back a value of 25 at frame 10 (in effect halving the animation's speed as far as the calculation is concerned).

First Operand and Second Operand Time Offset These sliders hand back the operand's value at the Time Offset you specify. A value of 10 fetches the operand's value 10 frames ahead in time, while -10 fetches it 10 frames behind. A practical example appears below.
