# Video collage layout

Version: DaVinci Resolve 20.3 Reference Manual. Context: Video collage.
[Chapter index](INDEX.md) / [Previous section](video-collage-create-background.md) / [Next section](video-collage-tile-styling.md) / [Video Collage](video-collage.md)
<a id="source-custom-sizeshape"></a> <a id="source-layout"></a> <a id="source-manage-tiles"></a> <a id="source-margins-and-spacing"></a> <a id="source-mute-tiles"></a> <a id="source-resize-content"></a> <a id="source-synchronize-keyframing"></a>

### Layout

You’ll find these controls in Globals mode.

- Columns: Set how many vertical columns of tiles you want.
- Rows: Set how many horizontal rows of tiles you want.
- Stagger Horizontally: Builds an even offset from each row to the one after it, so every

row sits staggered against its neighbors.

- Stagger Vertically: Builds an even offset from each column to the one after it, so every

column sits staggered against its neighbors.

- Rounding: Curves the edges of each tile in the layout. At a value of 0.000 the edges stay

square. Raising rounding bends each tile’s corners more and more, and at a value of 1 the tile turns perfectly round.

### Margins and Spacing

You’ll find these controls in Globals mode.

- Left/Right Margins: Adjusts the gap between the frame edge and the left and right edges of the whole tile group. Pushing this parameter up steadily narrows every tile as they crowd toward the frame’s middle.
- Top/Bottom Margins: Adjusts the gap between the frame edge and the top and bottom edges of the whole tile group. Pushing this parameter up steadily shortens every tile as they crowd toward the frame’s middle.
- Horizontal and Vertical Offset: This pair of sliders lets you shove the whole tile group off-center in whatever way you please.
- Horizontal and Vertical Spacing: This pair of sliders widens or tightens the gap between tiles, leaving them broader or slimmer as a result.

### Synchronize Keyframing

You’ll find these controls in Globals mode. In essence they’re a built-in helper for shifting every Globals and Tiles parameter keyframe attached to the current effect — useful for those moments when intricate keyframing has produced an animated split-screen and you then have to change the length of the clip the effect rides on. Rather than making you surface each parameter’s keyframes in the Timeline to drag them, these controls slide every keyframe across all parameters forward or backward by a set number of frames in one move.

- Offset Frames: Lets you state how many frames forward to push all of this effect’s keyframes. Negative values carry the keyframes leftward.
- Apply Keyframing Offset: Carries out the offset.

### Manage Tiles

You’ll find these controls in Tiles mode.

- Active Tile: This menu pulls double duty. To begin, it fixes which tile shows the current clip — a point that matters later when you apply this effect to other superimposed clips you want working together in a layout. It also picks which tile you go on to refine with the Inspector’s Tile-based controls. Switch on the Open FX Overlay of the Timeline Viewer and each tile carries its own overlay, so a click on a tile in the Viewer makes it the Active Tile.
- Bring Tile Forward/Send Tile Back: This pair of buttons reorders the tiles listed in the Active Tile drop-down menu.
- Manual Tile Management: With this checkbox off (its default), altering the Columns and Rows parameters refreshes the Active Tile drop-down menu on its own, giving one tile per node of the resulting grid. Switch the checkbox on to Add and Delete tiles by hand, which opens the door to richer layouts with overlapping tiles and uneven spacing between them.

### Mute Tiles

You’ll find these controls in Tiles mode. One lone checkbox parameter, Mute Tile, switches the active tile’s visibility on and off. Being keyframable, this checkbox lets you animate various tiles into and out of view for different effects.

### Custom Size/Shape

You’ll find these controls in Tiles mode. They let you fine-tune layouts tile by tile and can also quickly animate a lone tile as it moves and resizes itself around the overall layout’s grid.

- Start/End Column and Row: These four controls do two things — shift a tile’s position by row and column number, or grow a tile so it covers several tile row or column positions (“spanning”). Before using them, first pick the tile you mean to adjust from the Active Tile drop-down menu. With your target tile active, drag the relevant sliders to produce either result, as laid out below.

To change Tile Position: Adjusted in tandem so the Start and End values match, they let you hand-place each tile within the grid your chosen rows and columns define. That’s especially handy when you want to swiftly keyframe animated position changes and hop a tile around the layout’s grid.

To make a tile span multiple positions: Giving the Start and End Row and/or Column parameters different values makes the currently active tile stretch over several grid positions in the layout, enlarging it so you can craft asymmetric mixes of bigger and smaller tiles. Keyframe these values too and you can readily animate a tile swelling to fill more grid positions, or contracting from several positions down to one. Decide how many rows/columns the tile should span, and in which directions. Note that spanning across multiple rows or columns that sit offset enlarges the resulting tile to cover the whole rectangular region marked out by the outer edges of both offset tiles.

- Custom Size/Shape: Ticking this checkbox switches on the rest of this group’s controls, letting you set individual scale and rounding for the selected active tile.
- Custom Scale: Lets you resize the active tile apart from the rest.
- Custom Rounding: Lets you reshape the rounding of the active tile apart from the rest.

### Resize Content

You’ll find these controls in Tiles mode. They let you resize the image fitted inside each tile so it reveals precisely what you intend.

- Pan/Tilt/Zoom: This trio of sliders moves and resizes the video layer shown within the active tile to fit it however you require.
- Edge Behavior: These settings govern how the video layer’s edges behave inside the tile.

Transparent: Whenever positioning runs past the video’s edge, that area goes transparent and reveals the Tile Color chosen in the Tile Styling options. Reflect: Whenever positioning runs past the video’s edge, the image mirrors back onto itself. Wrap: Whenever positioning runs past the video’s edge, the image repeats. Replicate: Whenever positioning runs past the video’s edge, a copy of that edge stretches to the control’s boundary, in effect packing the leftover space with the pixels found at the video clip’s extreme edges.

- Move With Tile: Sets how the image fits the tile whenever the tile’s size shifts because of other Video Collage effect parameters.

Position Only: The tile’s video content is sized through Pan and Tilt alone; Zoom is left out. Position and Scale: The tile’s video content is sized through Pan, Tilt, and Zoom.
