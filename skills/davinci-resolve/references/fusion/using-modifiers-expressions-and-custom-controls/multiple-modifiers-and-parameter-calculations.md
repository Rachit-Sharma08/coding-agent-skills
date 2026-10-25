# Adding and inserting multiple modifiers and performing calculations in parameter fields

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using modifiers expressions and custom controls.
[Chapter index](INDEX.md) / [Previous section](contextual-menu-for-parameters-in-the-inspector-and-modifiers.md) / [Next section](expression-and-pick-whipping-to-create-an-expression.md)
<a id="source-a-simpleexpression-using-the-sine-and-time-functions"></a> <a id="source-adding-and-inserting-multiple-modifiers"></a> <a id="source-description"></a> <a id="source-expression-time-merge1blend"></a> <a id="source-performing-calculations-in-parameter-fields"></a> <a id="source-using-simpleexpressions"></a>

### Adding and Inserting Multiple Modifiers

In the same way nodes do in the Node Editor, modifiers can be wired together and branched off one another. Take the Calculation modifier: it emits a number yet carries two Number parameters, and either of those can itself receive a modifier. Should you need to slot a modifier in between an existing one and the parameter it modifies, reach for the Insert submenu found in that parameter’s contextual menu.

Available Modifiers in Fusion:

- Anim Curves: Brings in an animation curves modifier with which you can reshape an animation’s timing, scaling, and acceleration on the fly.
- Bézier Spline: Drops a Bézier spline into the Spline Editor so the chosen parameter can be animated.
- B-Spline Spline: Drops a B-Spline spline into the Spline Editor so the chosen parameter can be animated.
- Calculation: Forges an indirect link, carrying a mathematical expression, between a pair of parameters.
- CoordTransform Position: Works out where a given object currently sits in 3D, even once several 3D transforms have shuffled that object along the node tree hierarchy.
- Cubic Spline: Drops a Cubic spline into the Spline Editor so the chosen parameter can be animated.
- Expression: Lets you feed a parameter a variable or a math calculation in place of a plain numeric value. Controls for the Expression modifier live in the Modifiers tab, where there is more room and more parameters at hand than the SimpleExpression
- From Image: Reads color samples off an image along a line you define, then builds a gradient out of those samples.
- Gradient Color Modifier: Builds a gradient of your own design and lays it across a stated time range to animate a value.
- KeyStretcher: Stretches keyframes within a Fusion Title template when that template is trimmed on the Edit page or Cut page timeline.
- MIDI Extractor: Drives a parameter’s value from the data held inside a MIDI file.
- Natural Cubic Spline: Drops a Natural Cubic spline into the Spline Editor so the chosen parameter can be animated.
- Offset (Angle, Distance, Position): These three Offset modifiers serve to introduce variances, or offsets, between a pair of positional values. Attach this modifier to a size parameter, for example, and an object’s size can be driven by the gap between two onscreen controls (position and offset).
- Path: Yields a pair of splines that steer an object’s animation: an onscreen motion path (spacial) plus a Time spline shown in the Spline Editor (temporal).
- Perturb: Produces smooth, continuously shifting random animation on a chosen parameter.
- Probe: Auto-animates a parameter by reading the color or luminosity of a particular pixel, or a rectangular patch, of an image.
- Publish: Linking two un-animated parameters starts with the Publish modifier publishing a parameter. From there, other parameters can reach the Connect To submenu and tie themselves to the published one.
- Resolve Parameter: Lets you alter how long a Fusion transition template runs straight from the Edit page Timeline. Rather than keyframing the transition, you apply the Resolve Parameter Modifier to any animated parameter.
- Shake: Much like Perturb, Shake puts out smooth, continuously shifting random animation on a chosen parameter.
- Track: Pins a single-point tracker onto the chosen parameter. That tracker can then follow an object across the screen to animate the parameter. It is faster and more direct than the usual Tracker node, though less flexible, since the tracker amounts to just one point and serves only the parameter it is attached to.
- Vector Result: Akin to the Offset modifier, Vector Result offsets position parameters by way of origin, distance, and angle controls in order to form a vector. That vector is then available to drive any other parameter.
- XY Path: Yields an X and a Y spline in the Spline Editor for animating an object’s position..

For fuller detail on every modifier Fusion offers, turn to Chapter 124, “Modifiers,” in the DaVinci Resolve Reference Manual, along with Chapter 64 in the Fusion Reference Manual.

### Performing Calculations in Parameter Fields

Straightforward math equations can be typed right into a number field to work out the value you are after. Enter 2.0 + 4.0 into most number fields, for instance, and you land on a value of 6.0. That comes in handy whenever you want one parameter to equal the total of two others, or some fraction of the screen resolution.

### Using SimpleExpressions

A Simple Expression is a distinct kind of script that can sit right beside the parameter it governs. They earn their keep for working out modest calculations, wiring up one-way parameter links, or doing both together. To create a SimpleExpression, type an equals sign straight into the parameter’s number field and then press Return.

Typing an equals sign brings up the SimpleExpression field together with its Pick Whip control A blank field opens beneath the parameter, while a yellow marker shows up off to the left. Meanwhile the parameter’s present value gets dropped into the number field. With Simple Expressions you can write a math formula that drives a parameter’s value, or even bind two separate parameters together. It comes in handy whenever an animation is too hard — or simply impossible — to build through keyframing. To make an object pulse, for one, apply the sine and time functions to a Size parameter. Divide the time function to ease the pulsing down; multiply it to quicken the beat.

### A SimpleExpression using the sine and time functions

Within the SimpleExpression text box you may write single-line Lua scripts that lean on a bit of Fusion-specific shorthand. A handful of Simple Expressions, shown with their syntax, follow:

### Expression time Merge1.Blend

Merge1:GetValue("Blend", time-5)

### Description

This hands back the current frame number. This hands back the value of a separate input, Blend, taken from a separate node, Merge1. This hands back another input’s value as well, only sampled at a different frame — here, the point five frames earlier than the current one.
