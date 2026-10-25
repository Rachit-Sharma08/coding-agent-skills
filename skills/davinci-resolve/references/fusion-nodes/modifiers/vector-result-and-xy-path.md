# Vector result and xy path

Version: DaVinci Resolve 20.3 Reference Manual. Context: Vector result, Xy path.
[Chapter index](INDEX.md) / [Previous section](shake-and-track-and-vector-result.md) / [Vector Result](shake-and-track-and-vector-result.md)
<a id="source-controls-tab-4"></a> <a id="source-example-2"></a> <a id="source-inspector-4"></a> <a id="source-inspector-5"></a> <a id="source-the-vector-result-modifier-controls-tab"></a> <a id="source-xy-path"></a> <a id="source-xy-path-modifier-controls"></a>

### Inspector

### The Vector Result modifier Controls tab

### Controls Tab

Origin This control marks the position the vector's distance and angle values spring from. Distance This slider control fixes how far the vector reaches from the origin. Angle This thumbwheel control fixes the vector's angle relative to the origin. Image Aspect This slider control mainly exists to offset image aspect differences. For a square image of 500 x 500 the Image Aspect value would be 1, whereas a rectangular image of 500 x 1000 would call for an Image Aspect value of 2. This value defaults to what the current Frame Format preferences supply via width/height. You may have to alter this control to fit the current image.

### Example

- Create a 100-frame comp.
- Build a plain node tree out of a black background plus a Text node foreground

connected to a Merge.

- Enter some text in the Text node.
- Select the Merge node.
- Inside the viewer, right-click the Merge's Center control and pick Modify With >

Vector Result. That drops a crosshair onscreen control governing the Vector distance and angle. This onscreen control corresponds to the Distance and Angle controls displayed in the Modifiers tab.

- Within the Modifiers tab of the Inspector, drag the Distance control so the text moves away from the Vector origin.
- Drag the Angle thumbwheel so the text swings around the Vector origin.
- Unlike adjusting a pivot point, here the text itself does no rotating.
- Those points accept animation and may be wired to other controls.
- Over in the Inspector, right-click the Origin control and pick a path so a motion path

modifier joins the Origin control.

- Confirm the current frame reads frame 0 (zero), then either use the Origin controls in the

Inspector or drag the Vector Origin crosshair down to the screen's bottom-left corner.

- On the Vector Angle thumbwheel, click the Keyframe button so this control animates.
- Set the Angle thumbwheel to a value of 10.
- Move to frame 100 and click the screen's top-left corner to shift the

Vector Origin crosshair.

- Set the Vector Angle thumbwheel to a value of 1000.
- Play the comp to see the results.

That sends the text orbiting around the path you've just made.

### XY Path

The XY Path type relies on two separate splines, one for position along the X-axis and one for position along the Y-axis. To animate a coordinate control via an XY path, right-click the control and pick Modify With > XY Path from the contextual menu. On first look, XY paths behave like Displacement paths. To lay out the path, switch frames and place the control where it belongs on that frame, then switch frames once more and shift the control to its next spot. Fusion fills in the interpolation between the points for you. The distinction is that the onscreen path receives no keyframes. The X and Y channel splines turn up inside the Spline Editor. Whatever changes you make to the control's values get keyframed on those splines. The upside of the XY path is how simple it makes working with motion along one individual axis.

### Inspector

### XY Path modifier controls

X Y Z Values These mirror the animated control's position through X, Y, and Z values. Center The path's actual center. This too can be modified and animated to shift the whole path about. Size The path's size. Again, this permits later modification of the animation. Angle The path's angle. Again, this permits later modification of the animation. Heading Offset Should another control (a mask's Angle, for example) be wired to the path's heading, this control lets you add to or subtract from the computed angle. Plot Path in View Switches on or off whether the actual path shows in the views. Switching Default Paths You can swap the Default Path type to XY path (when that's your preferred animation type). Open the Default category within the Global Preferences and find the Point With drop-down menu. Switch it from its current value to XY Path. The next time Animate gets chosen from a Coordinate control's contextual menu, an XY path serves in place of a Displacement path.
