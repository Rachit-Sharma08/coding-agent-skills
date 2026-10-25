# Wipe and user transitions

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using transitions.
[Chapter index](INDEX.md) / [Previous section](motion-and-shape.md) / [Next section](burn-away-transition-and-adjust-timing.md)
<a id="source-fusion-transitions"></a> <a id="source-resolve-fx-transitions"></a> <a id="source-user-transitions"></a> <a id="source-wipe"></a>

### Wipe

Wipe transitions aim to keep motion flowing unbroken from one clip to the next. They pull this off by lining up the broad movement and heading of the subjects as the outgoing clip gives way to the incoming one.

- Band Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers. Reverse, a checkbox, swaps the transition’s direction. Preset offers a pick from these presets:
- Horizontal
- Vertical
- Horizontal Bilinear
- Vertical Bilinear
- Center Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Angle dictates the wipe’s angle as it spreads outward from the screen’s middle. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers. Reverse, a checkbox, swaps the transition’s direction.
- Clock Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Angle dictates the wipe’s opening angle as it rotates about the screen’s center. The Clockwise checkbox fixes which way the clock wipe turns. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers. Reverse, a checkbox, swaps the transition’s direction.
- Edge Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Angle dictates the wipe’s angle as it travels over the screen. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers.
- Radial Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers. Reverse, a checkbox, swaps the transition’s direction.
- Spiral Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers. Reverse, a checkbox, swaps the transition’s direction.
- Venetian Blind Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Repeat dictates how many “blinds” show up inside the wipe effect. Angle dictates the angle of this multi-wipe effect. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers.
- X Wipe: Color decides the border’s shade, should one be present. Border, given in pixels, governs how wide that border runs; set it to 0 and none appears. Feather, once its checkbox is ticked, leans on the Border slider to set how softly the transition’s edge feathers. Reverse, a checkbox, swaps the transition’s direction.

### User Transitions

Whatever transition presets you’ve built yourself live under the User category. They alone among the transitions are the ones you’re allowed to delete.

### Fusion Transitions

Within the Transitions panel, the Fusion Transitions section gathers Fusion effects that have been turned into reusable transitions. A Fusion Transition behaves like any other transition. After being cut into the Timeline, it can be edited just as any other transition is, and selecting it surfaces adjustable parameters in the Inspector so you can shape its effect to suit you. Fusion Transitions, though, go far further in how much you can customize them. Just right-click a Fusion Transition and pick Open in Fusion Page to reveal every Fusion node behind that transition’s effect, which lets you rebuild it into whatever you require. Head back to the Edit page and that transition saves itself. What’s more, anyone comfortable building effects in Fusion can author their own Transitions by crafting Fusion Macros and dropping them into the Effects Library, where they then turn up in the Effects Library’s Fusion Transitions section. For guidance on doing this, turn to Chapter 68, “Node Groups, Macros, and Fusion Templates,”

- Brightness Flash: Pushes brightness upward while crossing from one clip to the other. Brightness governs the flash’s luminance level. Saturation governs the flash’s saturation.
- Camera Shake: Shakes the frames, splitting the color channels apart, as its transition. Shake Speed governs how quick the shaking runs. Shake Strength governs how big the shakes get. Contrast, Brightness and Saturation each drive their own parameter on the transition.
- Circles: Crosses from one frame to the next by way of concentric circles. Circle Color sets the transition’s color. Red, Green, Blue, and Alpha govern how strong each channel is relative to the rest. Circle Thickness lets you tune how wide the circles are.
- Crash Zoom: Fires off two quick zoom-ins on the clips as its transition.
- Cross Dissolve: Dissolves from one clip to another. Reach for this as the base Fusion transition whenever you mean

to build a custom transition of your own in Fusion.

- Drop Warp: Conjures a virtual water drop to carry the move between the two clips. Warp Scale tunes

how much the drop warps the image.

- Fall and Bounce: As its transition, the trailing clip drops into frame and bounces. Fall Angle

steers the direction it falls in from.

- Film Strip: Zooms a moving virtual film strip as its transition between the two clips. Color sets the film base’s color. Red, Green, Blue, and Alpha govern how strong each channel is relative to the rest.
- Flip 3D: Carries out a plain rotation between the two faces of a plane as its transition.
- Foreground Wipe: Sends a zoomed-in column wiping over the frame as its transition. Invert

Wipe flips the wipe’s direction. Shadow Softness governs the column’s “depth.” Border Width governs how wide the column is.

- Glitch: Breaks the image up digitally as its transition. It works best across very brief spans of a handful of frames.
- Noise Dissolve: Puts Fusion’s FastNoise tool to work as a transition. As many as 6 versions of this transition can be stored. Mix governs how far the dissolve has progressed across the frame. Type governs which direction the noise spreads out from. Softness governs how feathered the border between the two clips is. Animation governs how fast the noise shifts. Border lets you lay a colored border along the edge where the noise meets between the two clips.
- Paint On: Lays down virtual paintbrush strokes as its transition. Shadow Blend governs the strokes’ “depth.” This one serves best across longer spans.
- Pan (Down, Left, Right, Up): Sets mirrored images moving as its transition. Which way the motion runs follows from the particular transition you select.
- Rotate: Blends a counterclockwise 180 degree rotation with a dissolve to form its transition.
- Rotate 90: Blends a counterclockwise 90 degree rotation with a dissolve to form its transition.
- Round and Down: Spins counterclockwise about a central pivot as it dissolves from one clip to the other.
- Slice Push: Builds its transition from several columns that slide out and shove across the two clips. Slices governs the column count. Angle lets you fix the columns’ angle. Shadow fixes the strength of the columns’ drop shadow. Shadow Softness governs how far that drop shadow spreads. Shadow Offset governs the shadow’s angle.
- Slide (Down, Left, Right, Up): Runs a mirrored slide whichever way is indicated. The Curve control lets you pick among these animation curve options:
- Linear
- Easing
- Custom
- Tunnel of Light: Runs a glowing transition in which the first clip is drawn into a single point, after which the second clip blooms outward from that very point. Contrast lets you set how much contrast the light rays carry. Glow Gain governs the glow’s brightness. Glow Size governs how much glow there is. Glow Red, Green, and Blue let you recolor the glow.
- Warp: Runs a warping transition, like water swirling down a drain, between the two clips.
- Zoom In: Runs a transition that zooms in while blending the two clips into one. Zoom Scale

governs the zoom’s strength (a negative figure zooms out rather than in). Zoom Center lets you fix the point the zoom centers on. The Curve control lets you pick among these animation curve options:

- Linear
- Easing
- Custom
- Zoom In and Out: Runs a transition blending a zoom-in on the first clip with a zoom-out on the second. Zoom Scale governs the zoom’s strength. Zoom Center lets you fix the point the zoom centers on.

### Resolve FX Transitions

Resolve FX Transitions are dressed-up graphical transitions that lean on the processor harder than the ordinary wipes and dissolves do.
