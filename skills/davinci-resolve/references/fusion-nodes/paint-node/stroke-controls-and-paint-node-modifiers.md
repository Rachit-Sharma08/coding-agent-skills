# Stroke controls and paint node modifiers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Paint node.
[Chapter index](INDEX.md) / [Previous section](editing-options-toolbar-and-paint-controls-tab.md)
<a id="source-keyboard-shortcuts"></a> <a id="source-paint-node-modifiers"></a> <a id="source-stroke-controls"></a>

### Stroke Controls

The stroke controls hold parameters that adjust the whole stroke of paint along with governing it over time.

- Size: This control sets the brush size when the brush type is either Soft Brush or Circle. The brush diameter is drawn in the viewer as a little circle ringing the mouse pointer. The size can likewise be set on the fly within the viewer if you keep the Command or Ctrl key held down as you drag the mouse pointer.
- Spacing: The Spacing slider sets how far apart the dabs sit (the samples used to draw a continuous stroke along the underlying vector shape). Raising this value makes the stroke denser, while lowering it gives the stroke the look of a dotted line.
- Stroke Animation: The Stroke Animation menu supplies several ready-made animation effects you can apply to a paint stroke. This menu shows up only for vector strokes such as Stroke and Polyline Stroke.

All Frames: This default shows the stroke across every frame of the image wired into the orange background input of the Paint node. Limited Duration: This lasts for the number of frames the Duration slider specifies. Write On: With Write On chosen, an animation spline gets added to the paint stroke that exactly mirrors the timing of how the paint stroke was created. The stroke is written onto the image precisely as you drew it. To tweak the Write On effect's timing, head to the Spline Editor and use the Time Stretcher node to alter the animation spline's overall length. To smooth or hand-adjust the motion, try thinning out the points in the animation spline. Write Off: Write Off does the opposite of Write On, drawing the stroke from the end and moving backward toward the stroke's start. Write On Then Off: This menu option puts a Write On followed by a Write Off animation mode onto the stroke. Trail: Picking the Trail option from the menu animates the stroke's start and end points at the same time, offset from one another by the amount the Duration control specifies. What you get is a painted segment trailing along the path of the stroke. Just like the Write On and Write Off effects, it begins on the current frame as soon as the animation mode is chosen. The animation's timing can be hand-adjusted through the Spline or Keyframes Editors.

- Duration: In frames, Duration determines the length of each stroke. You'll see this control only with Multistroke and Clone Multistroke, or whenever Limited Duration is the chosen stroke animation mode. Its most frequent application is frame-by-frame rotoscoping across a scene.

In the Keyframes Editor, every Vector stroke placed on a scene holds a duration that's trimmable independently, stroke by stroke. Setting that duration to a value of 0.5 makes each stroke survive for only one field while the node tree runs in Fields mode.

- Write On and Write Off: Whenever Stroke Animation uses one of the Write On and Write Off methods, this range slider appears. Its range corresponds to where the stroke begins and ends. Pushing the Start value upward from 0.0 to 1.0 erases the stroke, while pushing the End value upward from 0.0 to 1.0 paints the stroke onto the screen. Animating this control can yield nice results. The best outcome comes from animating it automatically by way of the Write On and Write Off modes within the Stroke Animation menu.
- Make Editable: This button shows up only for Vector strokes. Clicking Make Editable converts the current stroke into a polyline spline so its shape can be adjusted or animated.

### Paint Node Modifiers

Each paint stroke you draw in the viewer brings an associated modifier stroke into being. Inside the Inspector's Modifiers tab, those modifier strokes show up as a roster of paint stroke operations. Every stroke you draw is open to being modified, deleted, or reordered by way of the modifier stack. NOTE: Because the MultiStroke tools are made for speed, they can house plenty of strokes internally without spawning an enormous list stack in the modifiers Each Paint modifier stroke holds Brush controls, Apply controls, and Stroke controls that match the ones in the main Controls tab of the Inspector.

### Keyboard Shortcuts

By way of keyboard shortcuts, you can switch painting styles and color without burrowing into menus. As you paint: a left-drag while you hold Command or Ctrl resizes the brush. Holding Option or Alt and clicking samples a color out in the viewer. As you clone: an Option-click or Alt-click fixes the clone source position, and strokes begin cloning from wherever that location is. Keeping O held briefly turns on a 50% transparent overlay of the clone source (you can adjust the % through the pref Tweaks.CloneOverlayBlend). A tap of P flips an opaque overlay of the clone source on and off. With the overlay visible: the clone source position shifts via the Arrow keys, plus you're free to drag crosshairs and tweak the angle control or size sliders. The clone source angle shifts with the Option + Left/Right or Alt + Left/Right Arrow keys. The clone source size shifts with the Option + Up/Down or Alt + Up/Down Arrow keys. Adding Shift + Command or Shift + Ctrl alongside any of these yields larger or smaller adjustments. The two square brackets, [ and ], shift the clone source Time Offset (a particular Clone Source node has to be assigned in the Source Node field for this). Copy Rect/Ellipse: constrain the shape by dragging the source out with Shift held. When one stroke alone is selected (this isn't offered on multi or polyline strokes): a press of X or Y flips that stroke. Paint Groups: a Command + drag or Ctrl + drag relocates a group's crosshair, leaving the group's own position untouched.
