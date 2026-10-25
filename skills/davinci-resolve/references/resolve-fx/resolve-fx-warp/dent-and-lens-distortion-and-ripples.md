# Dent and lens distortion and ripples

Version: DaVinci Resolve 20.3 Reference Manual. Context: Dent, Lens distortion studio version only, Ripples.
[Chapter index](INDEX.md) / [Next section](vortex-and-warper.md)
<a id="source-dent"></a> <a id="source-lens-distortion-studio-version-only"></a> <a id="source-main-controls"></a> <a id="source-resolve-fx-warp"></a> <a id="source-resolve-fx-warp-1"></a> <a id="source-ripple-controls"></a> <a id="source-ripples"></a>

### Resolve FX Warp

This group of filters distorts the picture along several axes to produce procedural or hand-shaped warps, a number of which can animate on their own. The Warper plugin offers a point-driven, free‑form Warp tool.

### Dent

A distortion that produces assorted styles of round bulging and creasing.

- DentType: Pick among six distinct styles of “dent” distortion. Available are Type 1, Type 2, Type 3, Sine, Cosine, and Black Hole.
- X and Y: These position sliders shift where the warp is centered.
- Size: Use this to set the warp's diameter.
- Strength: Sets both how far and which direction the warp goes; pushing this beneath zero “pulls”

the picture inward toward the effect's middle, whereas pushing it past zero “pushes” the picture out so it bulges following whichever DentType you’ve picked.

- Edge Behavior: This removes blanking produced by negative distortion, filling the black regions through one of several modes you choose; choices are Black (takes no action, keeping the blanking), Reflect, Wrap-Around, and Replicate.

### Lens Distortion (Studio Version Only)

Applies either convex or concave lens distortion so the picture bulges either out or in, mimicking a cheaply built lens. The same filter works correctively too, offsetting footage that shows barrel distortion. On top of that, you can dial the distortion amount separately per color channel, producing a chromatic aberration look by leaning on the curvature of the distortion you’re introducing for greater realism.

- Red, Green, and Blue Distortion: By default these sliders move together because of the Gang checkbox. While ganged, dragging them leftward (negative values) deepens “fisheye” distortion, and dragging them rightward (positive values) yields a reversed “fisheye” that curves the picture inward instead of out. Switching Gang off lets each of the Red, Green, and Blue Distortion sliders hold its own value, adding a more faithful chromatic aberration to the picture.
- Fine Adjustment: Ticking this checkbox narrows the operating range of the distortion sliders considerably, allowing finer control.
- X and Y Position: Use these sliders to relocate where the distortion effect is centered.
- Edge Behavior: The choices in this pop-up clear away blanking that negative

distortion causes, populating black regions through one of several user-chosen modes; the choices are Black (takes no action, keeping the blanking), Reflect, Wrap-Around, and Replicate. TIP: When a clip holds a heavy distortion effect that pushes blanking onto the frame edges, you'll have to resize it with the Zoom control, which sits inside the Node Sizing mode within the Sizing palette. Both Edit and Input sizing confine their zoom to the picture inside the boundary blanking has created.

### Ripples

A distortion that produces assorted styles of ripples.

### Main Controls

These settings determine the ripple style along with the quality of any optional ripple shine you'd like.

- Ripple Shape: Pick from Circular, Square, Horizontal, Vertical, Exponential, Star, and Radial ripples.
- Wave Shape: Pick from Sinusoidal, Triangular, Fresnel In, Fresnel Out, and Natural waves.

A group of Shine parameters lets you lay a simulated shine over the top of these ripples.

- Shine: This checkbox switches the shine on or off.
- Shine Direction: Adds a light shine along the ripple crests. Performs best when shine strength is kept low.
- Vertical Shine Height: Sets how thick the highlights along the ripples appear.
- Shine Size: Sets how long the highlights along the ripples run.
- Shine Strength: Governs the shine's overall look.
- Animate: When ticked, this checkbox exposes a Speed slider that controls the pace at which the

ripple effect auto-animates the phase of whatever ripple effect is currently set, with no keyframes required.

### Ripple Controls

A distinct group of Ripple parameters lets you activate as many as five ripples laid over one another.

- Enable Ripple: A keyframable checkbox that switches an individual ripple on or off.
- X and Y Position: Relocates where each group of ripples is centered.
- Amplitude: Sets the “height” this effect gives each ripple.
- Frequency: Sets the number of ripples being generated.
- Decay: Sets the ripple effect's falloff, with ripples slowly fading out as they

approach the decay point.

- Phase: Sets the ripple effect's phase against the central origin point. When you

want a quick way to animate a ripple, keyframing the Phase parameter reproduces the same result the Animate checkbox above gives you.
