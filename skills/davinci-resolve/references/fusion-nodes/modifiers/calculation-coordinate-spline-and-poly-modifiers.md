# Calculation and coordtransform position and cubic spline and custom poly

Version: DaVinci Resolve 20.3 Reference Manual. Context: Calculation, Coordtransform position, Cubic spline, Custom poly.
[Chapter index](INDEX.md) / [Previous section](bezier-spline-and-b-spline-and-calculation.md) / [Next section](custom-poly-and-expression.md) / [Calculation](bezier-spline-and-b-spline-and-calculation.md)
<a id="source-controls-tab"></a> <a id="source-controls-tab-1"></a> <a id="source-coordtransform-position"></a> <a id="source-cubic-spline"></a> <a id="source-cubic-spline-editor"></a> <a id="source-custom-poly"></a> <a id="source-example"></a> <a id="source-inspector-1"></a> <a id="source-inspector-2"></a> <a id="source-selecting-the-custom-poly-modifier"></a> <a id="source-the-coordinate-transform-modifier-controls-tab"></a> <a id="source-the-custom-poly-controls-tab"></a> <a id="source-usage-2"></a>

### Example

The example here leans on a calculation to blur a Text node by an amount that runs inverse to the text's size.

- Start a new composition running from frame 0 to frame 100.
- On frame 0, drop a Text+ node into the composition.
- Type in a little text and set the size to 0.05
- Click the Keyframe button just right of the Size slider to lay down a keyframe.
- Jump to frame 100 and set the Size value to 0.50.
- Wire a Blur node after the Text+ node.
- Bring the Blur node up in one of the viewers.

Making the blur weaken as the text grows cannot be done with plain “pick whip”-style parameter linking. You cannot simply wire the controls together, since the Text Size control's values are climbing rather than shrinking.

- Right-click the Blur Size and pick Modify With > Calculation from the contextual menu.

That puts a Calculation modifier on the Blur node. Up top in the Inspector, a fresh set of controls turns up in the Modifiers tab whenever the Blur node is selected.

- Up top in the Inspector, open the Modifiers tab (F11).
- Right-click the First Operand slider and pick Connect To > Text 1 > Size from the

contextual menu. The Blur Size is now tied to the Text Size parameter, but the link is not much use yet. The Blur Size control caps at a maximum value of 0.5, barely registering as a blur.

- Switch the Operator drop-down to Multiply.
- Push the Second Operand slider to 100.
- The first operand is now multiplied by 100, and working the dial yields a far

blurrier blur.

- Move to the modifier's Time tab and set the First Operand Time Scale to -1.0.

Ordinarily the first operand takes the value of whatever control it links to from the same frame as the present time. So at frame 10 the first operand matches the Text size at frame 10. Setting this to -1 makes the value get read one frame back in time each time the composition's current time steps forward by 1 frame. That, however, means the Calculation would be reading the Text size's value at frame -10 while we sit at frame 10 in the composition.

- To put that right, set the First Operand Time Offset slider to 100.
- Head back to the Tools tab up top in the Inspector and hit Play (Spacebar) to observe how

the Blur Size's value tracks the Text Size's value.

### CoordTransform Position

Owing to how hierarchical 3D is in Fusion, an object's starting position in a 3D scene frequently no longer reflects where it currently sits. Take an image plane that begins at a position of 1, 2, 1, only to be scaled, offset, and rotated by other tools further down the node tree, winding up at an absolute location of 10, 20, 5. That can muddy any attempt to wire an object further down the composition straight to the position of an object upstream. The Coordinate Transform modifier can be dropped onto any set of the XYZ coordinate controls to work out a given object's present position at whatever point in the scene hierarchy. To add one, right-click the numeric input on any node and pick Modify With > CoordTransform Position from the contextual menu.

### Inspector

### The Coordinate Transform modifier Controls tab

### Controls Tab

The Controls tab carries two fields, one for the target and one for the scene input. The target holds the node bearing the original coordinates, while the scene input holds the scene with the new coordinates. Target Object This control wires to the 3D tool that yields the original coordinates due to be transformed. To make that connection, pull its node out of the Node Editor and onto the text edit control, or else right-click that control to choose the tool from the contextual menu. You may also type the tool's name straight into the control. SubID The SubID slider lets you zero in on a single sub-element of certain geometry types, such as one character made by a Text 3D tool or a particular copy spawned by a Duplicate 3D tool. Scene Input This control ought to wire to the 3D tool that outputs the scene holding the object at its new location. To set that up, drop a tool tile out of the Node Editor onto the text edit control, or instead right-click that control to choose an object from the Connect To pop-up menu.

### Cubic Spline

The Cubic Spline is one more of Fusion's animation modifiers, ordinarily put onto numerical values rather than point values. You apply it by right-clicking a numerical control and picking Modify With > Natural Cubic Spline.

### Usage

As an animation spline, this modifier offers no real Controls tab. Its effect can still be viewed and shaped within the Spline Editor, though.

### Cubic Spline Editor

### Custom Poly

The Custom Poly modifier attaches to Polygon masks or paths. Working much like the Custom and pCustom tools, it lets you shift the polyline's existing points around or swap them out wholesale for a fresh set. Its expressions run for every point on the output polygon. To apply it, right-click the “Right-click here for shape animation” text at the foot of the Polygon controls and pick Insert > Custom Poly from the contextual menu.

### Selecting the Custom Poly modifier

### Inspector

### The Custom Poly Controls tab

### Controls Tab

The Custom Poly Controls tab becomes reachable once you open the modifiers tab on the Polygon's inspector. It offers a single point input plus number variables for use in animating the expressions. By default that is one point and four numbers, though both can grow to a maximum of nine. You add further points and numbers from the Config tab.
