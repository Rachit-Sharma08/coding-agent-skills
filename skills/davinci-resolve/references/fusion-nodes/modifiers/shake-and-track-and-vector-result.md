# Shake and track and vector result

Version: DaVinci Resolve 20.3 Reference Manual. Context: Shake, Track, Vector result.
[Chapter index](INDEX.md) / [Previous section](perturb-and-probe-and-publish-and-resolve-parameter-and-shake.md) / [Next section](vector-result-and-xy-path.md) / [Shake](perturb-and-probe-and-publish-and-resolve-parameter-and-shake.md)
<a id="source-controls-tab-3"></a> <a id="source-example"></a> <a id="source-example-1"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-the-shake-modifier-controls-tab"></a> <a id="source-the-tracker-modifier"></a> <a id="source-track"></a> <a id="source-tracker-modifier-vs-tracker-node"></a> <a id="source-vector-result"></a>

### Inspector

### The Shake modifier Controls tab

### Controls Tab

Random Seed The Random Seed control holds the value that seeds the random number generator. Hand it the same seed and a random number generator always turns out the same results. Swap the seed whenever the randomizer's results don't satisfy. Smoothness This control smooths the overall randomness of the Shake. A higher value renders the motion smoother. A value of zero yields wholly random results, with no smoothing applied at all. Lock X/Y This checkbox unlocks the X- and Y-axis, exposing independent slider controls per axis.

Minimum and Maximum This control fixes the shake's overall strength. The low values stand for the lowest value the randomizer can produce, and the high values stand for the highest. To make a Shake that sends a center crosshair anywhere across the image, put the Minimum at 0.0 and the Maximum at 1.0. To pen the motion into a smaller shake at the image's bottom-right corner, put the Minimum at 0.70 and the Maximum at 0.90.

### Example

- Create a new comp, and then add and view a Text node.
- Type some text in the Text node.
- Inside the viewer, right-click atop the text's Center control and pick Modify With >

Shake Position.

- Over in the Inspector, open the Modifiers tab and dial the smoothing to 5.0.
- Set the Minimum to 0.1 and the Maximum to 0.9.

That layers some chaotic movement onto the text. We can shift this over time, though Move to frame 0 and, inside the Inspector, click the Keyframe button alongside the Minimum together with the Maximum controls.

- Head to frame 0 and, within the Inspector, click the Keyframe button sitting beside both the Minimum and the Maximum controls.
- Head to frame 90 and reset the Minimum to 0.45 along with the Maximum to 0.55.
- View the results.

Now the text kicks off flying all across the screen and draws in toward the screen's center as the comp runs.

### Track

While a standalone Tracker node exists, a Tracker modifier can also be used to attach a tracker straight onto a parameter. To apply the Tracker modifier, head into the viewer and right-click the Center control belonging to any transform, text, mask, or similarly positionable element. Out of the contextual menu, pick Object x Center > Modify With > Tracker. Then settle on one of three options:

- Tracker Position: Tracks a point from the source.
- Steady Position: Stabilizes based on a single point in the source.
- Unsteady Position: Adds original motion back after stabilizing.

That places a modifier in the Inspector carrying a set of controls nearly the same as those in the Tracker node itself.

### Inspector

### The Tracker modifier

For a thorough rundown of this node, turn to Chapter 119, "Tracking Nodes," within the DaVinci Resolve Reference Manual; the Fusion Reference Manual covers it in Chapter 59.

### Tracker Modifier vs. Tracker Node

Here's how a Tracker modifier and a Tracker node differ:

- The Tracker modifier can only track a single pattern.
- The Tracker modifier emits just one value, leaving it unsuited to intricate stabilization or match-moving work.
- For the modifier, the default source image is the node directly upstream of the one holding the modifier (so, when adding a Tracker modifier onto a Glow node fed by a Loader, the Tracker Source input defaults to the Loader's output). Point the Tracker modifier at a different source image by typing in the node's name. Or else, drag the source node out of the Node Editor into the Text Box control.

### Example

Suppose you have to track an actor's eyes so an otherworldly, alien glow can be laid over the eyes.

- Select the Loader node.
- Add a Glow node.
- Put an Ellipse mask onto the Glow, shaped to match one of the eyes.
- Right-click that mask's center, then choose Modify With > Tracker > Position.

Because the track rides on the mask, the tracker treats the glow as its tracking image. That could spell trouble, since the glow may heavily obscure the eye. A cleaner source is the Loader feeding the glow.

- Drag the Loader into the modifier Inspector's Track Source field.
- Track the actor's eye.
- Perform the same steps on the other eye.

### Vector Result

The Vector Result modifier serves to offset positional controls, crosshairs among them, by distance and angle. These can be static or animated values. You apply it by right-clicking a control and picking Modify With > Vector.
