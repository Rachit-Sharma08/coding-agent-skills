# Anim curves and bezier spline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Anim curves, Bezier spline.
[Chapter index](INDEX.md) / [Next section](bezier-spline-and-b-spline-and-calculation.md)
<a id="source-anim-curves"></a> <a id="source-bézier-spline"></a> <a id="source-bézier-spline-editor"></a> <a id="source-bézier-spline-modifier-menu"></a> <a id="source-curve-shape-controls"></a> <a id="source-ease-inout"></a> <a id="source-modifiers"></a> <a id="source-modifiers-part-1"></a> <a id="source-modifiers-right-click-menu"></a> <a id="source-scaling"></a> <a id="source-the-inspector-for-the-anim-curves-modifier"></a> <a id="source-timing"></a> <a id="source-usage"></a> <a id="source-using-the-anim-curves-modifier-with-paths"></a>

### Modifiers

This chapter runs through which modifiers Fusion makes available.

A modifier extends the regular parameter set a node shows in the Inspector; their very purpose, in fact, is to drive other parameters. Some are as plain as a motion path or a link between two parameters. Others, though, can run to intricate expressions, procedural functions, external data, third-party plugins, or scripted Fuses. To attach a modifier, right-click over a parameter in the Inspector and pick one from the menu. As another route, right-click a control out in the viewer. Not every modifier shows in the right-click menu for every parameter, and some apply only to certain parameter types. NOTE: Text3D and Text+ carry their own text-specific modifiers, addressed in those nodes' sections.

### Modifiers right-click menu

### Anim Curves

The Animation Curves modifier (Anim Curves) lets you reshape an animation's timing, values, and acceleration on the fly, even when you opt to alter a comp's duration. Leaning on it makes stretching or squishing animations, smoothing motion, lending things a bounce, or mirroring animation curves vastly easier, sparing you the headache of hand-tweaking splines.

### The Inspector for the Anim Curves modifier

As you build Fusion templates for DaVinci Resolve's Edit and Cut page, the Anim Curves modifier lets the keyframed animation you set up in Fusion stretch and squish as it should whenever the transition, title, or effect's duration shifts on the Edit and Cut page Timelines.

### Curve Shape Controls

The Anim Curves modifier's controls live in the modifier's own Inspector tab. The Curve Shape controls dictate the animation curve's acceleration or shape.

- Source: This drop-down offers three options keyed to how the comp was spawned from DaVinci Resolve's Edit page. Transition: Chosen automatically whenever the comp springs from an Edit page transition effect. Should the transition's duration be revised on the Edit page, the animation's timing revises along with it. Duration: Reach for this when the comp comes from a clip on the Edit page. The animation timing refreshes if trimming alters the clip's duration. Custom: Brings up an Input dial for steering the timing by hand.
- Input: This dial surfaces only while Source sits on Custom. Its job is to alter the input keyframe value.
- Curve: The Curve drop-down picks which interpolation method runs between keyframes. There are three choices: linear, easing, or custom. Linear: The default Linear interpolation method holds a steady, even acceleration from keyframe to keyframe. Easing: Brings up interpolation menus for the curve's start (In) as well as its end (Out). Custom: Opens a mini Spline Editor for shaping the interpolation across the animation from start to finish.
- Mirror: Runs the animation forward and, on hitting the end, walks it back to its opening value. This doubles the speed of the initial animation, since the comp's back half is spent on the reverse run.
- Invert: Turns the animation curve upside down so the values open high and close low.

### Scaling

The Scale parameters reshape the animation values through relative adjustments.

- Scale: This figure is a multiplier laid over the keyframes' values. Where the Scale value is 2 and a keyframe holds a value of 0, it stays 0. Where the Scale value is 2 and a keyframe holds a value of 10, the outcome is as though the keyframe were set to 20. Picture it as the animation's closing value. The best moment to set it is while you have the comp's final frame in view.
- Offset: The offset gets added onto the keyframe values and can be pictured as the animation's opening value. The best moment to set it is while you have the comp's first frame in view.
- Clip Low: Keeps the output value from ever falling under 0.0.
- Clip High: Keeps the output value from ever climbing past 1.0.

### Timing

The Timing parameters tune the animation's timing through relative values.

- Time Scale: Stretches or compresses the animation so it plays faster or slower. At 1.0 the animation spans the comp's duration (barring any customization you have done with the Modifier's other controls).
- Time Offset: This value holds the animation back by a fraction of its full duration. At 0.0 there is no delay. At 0.5 the animation's start is pushed to the midpoint of the comp's duration.

Using the Anim Curves Modifier to Create a Custom Transition To get a feel for using the Anim Curves modifier on a transition, let's build a simple scaling dissolve. 1 Drop a standard cross dissolve into the Edit page Timeline. 2 Right-click the transition and pick Convert to Fusion Cross Dissolve. 3 Right-click the transition once more and pick Open in Fusion page. 4 Attach a Transform node to MediaIn1 and to MediaIn2. 5 Click the Transform node tied to MediaIn2. 6 In the Inspector, right-click the Size control and pick Modify With > Anim Curves from the contextual menu. Putting this modifier on the Size control makes the slider animate from 0 to 1 across the Cross Dissolve's duration. 7 Click the Transform node tied to MediaIn1. 8 In the Inspector, right-click the Size control and pick Modify With > Anim Curves from the contextual menu. 9 Up top in the Inspector, open the Modifier tab and press the Invert button. Inverting the animation curves drives MediaIn1 to scale the opposite way from MediaIn2. 10 In the Modifiers tab, switch the Curve drop-down to Easing and try out the various ease-in ease-out curve types from the In/Out drop-downs. After you turn this node tree into a Macro and save it as a Transition template, you can drop it into the Edit page Timeline. Alter the transition duration on the Edit page and the animation timing adjusts to suit.

### Using the Anim Curves Modifier with Paths

To grasp how to pair the Anim Curves modifier with a Path modifier, let's suppose you want text that drops from the top of the frame and bounces once it hits the bottom. 1 In Fusion, lay down two keyframes that send text from the top of the frame down to the bottom. A Path modifier is created automatically. 2 In the Inspector's Modifier tab, right-click the Displacement parameter and pick Insert > Anim Curves. The animation is normalized against the comp's duration. 3 Set the Source menu to Duration, given that this is no transition and we are leaving the duration untouched. 4 From the Curve menu pick Easing, then for the Out menu pick Bounce. 5 Run the animation to watch the Bounce animation. 6 To land the bounce halfway down the frame, set the Scale to .05. 7 To double the animation's speed, type 2.0 into the Time Scale parameter. Once this node tree is turned into a macro and stored as a Title template, dropping it into the Edit page Timeline becomes possible. Change the title's duration on the Edit page and the animation timing falls into line. TIP: To see the resulting animation curve in the Spline Editor, click the parameter name in the Spline Editor's header. The spline refreshes as you work the controls.

### Bézier Spline

The Bézier Spline counts among Fusion's animation modifiers and usually goes onto numerical values rather than point values. It attaches automatically when you keyframe a parameter, or any time you right-click a number field and pick Animate.

### Bézier Spline modifier menu

### Usage

To bring the Bézier Spline into the Spline Editor, right-click a number field and pick BezierSpline. Because it is the go-to pick for animation splines, it is pulled out of the Modify With menu so you can reach it faster. Picking BezierSpline from the menu plants a keyframe at the present spot and shows a Bézier Spline in the Spline Editor.

### Bézier Spline Editor

Setting it apart from most modifiers, this one carries no real Controls tab in the Inspector. The Spline Editor does present the Bézier Spline, though, and that is where you work it. The Bézier Spline hands you per-point control over each control point's smoothness by way of Bézier handles. That smoothness can be applied in several ways:

- To smooth the control points, select them and hit Shift-S. The handles then let you refine the smoothness further.
- To make the control points linear, select them and hit Shift-L. These same actions are available through the contextual menu too.
- Choose the control point(s), right-click, and pick Smooth or Linear. That menu also lets you smooth a spline via a convolution analysis known as a Savitzky-Golay filter. Choose the control point(s), right-click, and pick Smooth Points -Y Dialog.

### Ease In/Out

Classic Ease In/Out can likewise be adjusted through the number field virtual sliders in the Spline Editor. Choose the control points you wish to adjust, right-click, and pick Ease In/Out... from the contextual menu. Then steer the Ease In/Out by the numbers using the number field virtual sliders.
