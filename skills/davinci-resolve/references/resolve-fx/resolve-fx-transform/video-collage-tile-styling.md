# Video collage tile styling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Video collage.
[Chapter index](INDEX.md) / [Previous section](video-collage-layout.md) / [Video Collage](video-collage.md) / [Next section](video-collage-easing-blur.md)
<a id="source-drop-shadow"></a> <a id="source-resolve-fx-transform-part-4"></a> <a id="source-tile-animation"></a> <a id="source-tile-styling"></a>

### Tile Styling

You’ll find these controls in Tiles mode. They let you add a colored border and set the opacity of every tile or only the one that’s currently active. These parameters can be animated.

- Apply to All Tiles: When ticked, whatever you change in the Tile Styling parameters carries across to all tiles in the Video Collage, no matter which tile is active at the moment.
- Tile Border: This slider sets the width of the tile’s border. Its values run from -0.250 to 0.250, with negative numbers growing the border inward into the tile and positive numbers growing it outward.
- Tile Color: Lets you pick the tile’s background and border color.
- Tile Opacity: This slider alters the transparency of the tile itself and leaves the video clip

inside it untouched. The values run from 0.000 (fully transparent) to 1.000 (fully opaque).

### Drop Shadow

You’ll find these controls in Tiles mode. They let you add and shape a drop shadow on either all tiles or just the active one. These parameters can be animated.

- Apply to All Tiles: When ticked, whatever you change in the Drop Shadow parameters carries across to all tiles in the Video Collage, no matter which tile is active at the moment.
- Strength: This slider governs the drop shadow’s transparency. The values run from 0.000 (fully transparent) to 1.000 (fully opaque).
- Color: Lets you pick the Drop Shadow’s color.
- Drop Angle: Lets you fix the angle from which the shadow falls. The slider covers a full 360

degrees of travel, from -180.0 to 180.0.

- Drop Distance: Lets you fix how far the shadow sits from its source tile. The

values run from 0.000 to 0.200.

- Expand: This slider governs how far the shadow spreads out from its origin. The values run

from 0.900 to 1.250.

- Blur: Lets you govern how much the Drop Shadow diffuses. The values run from

  0.000 (no blur) to 1.000.

### Tile Animation

You’ll find these controls in Tiles mode. They make short work of building simple intro/outro animations that usher all or some tiles onscreen and drive all or some tiles offscreen in assorted ways. The Animate drop-down menu decides whether the animation runs automatically or is built by hand with keyframes.

- Apply to All Tiles: When turned on, any animation you configure lands on every tile in the layout at the same time.
- Animate: Through this drop-down menu you pick between hand-keyframing intro or outdo animations and having tiles introduced or concluded automatically. The options are:

Manually Keyframe: Here you keyframe the four progress sliders below yourself to produce animated Intro and Outro animations. Intro Only: Animation is generated automatically to usher each tile onscreen per the animation types you tick from four checkboxes below. The choices — Fly, Shrink, Rotate, and Fade — combine freely. A Duration slider turns up so you can set the Intro’s length. Outro Only: Animation is generated automatically to drive each tile offscreen per the animation types you tick from four checkboxes below. The choices — Fly, Shrink, Rotate, and Fade — combine freely. A Duration slider turns up so you can set the Outro’s length. Intro & Outro: Animation is generated automatically to usher each tile onscreen and then drive it offscreen, per the animation types you tick from four checkboxes below. The choices — Fly, Shrink, Rotate, and Fade — combine freely. A Duration slider turns up so you can set how long the Intro and Outro last.

- Fly Animation: Lets you choose the direction tiles fly in from and fly out toward.
- Shrink Animation: Lets you choose a way of shrinking out or in as the Fly Progress

slider animates.

- Fly Progress: (manual key framing only) A slider that, once animated, flies a tile into

or out of the frame. At a value of 0.000 the tile rests in its default grid position. At a value of 1.000 the tile sits completely off screen.

- Shrink Progress: (manual key framing only) When animated, this slider scales a tile anywhere from nothing up to its present size. At a value of 0.000 the tile sits at its largest state. At a value of 1.000 the tile collapses to nothing.
- Rotate Progress: (manual key framing only) When animated, this slider sends a tile flying into or away from the frame. At a value of 0.000 the tile rests in its default grid position. At a value of 1.000 the tile sits completely off screen.
- Fade Progress: (manual key framing only) When animated, this slider sends a tile flying into or away from the frame. At a value of 0.000 the tile rests in its default grid position. At a value of 1.000 the tile sits completely off screen.
