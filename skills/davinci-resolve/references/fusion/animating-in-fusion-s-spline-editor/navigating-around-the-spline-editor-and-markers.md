# Navigating around the spline editor and markers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating in Fusion s spline editor.
[Chapter index](INDEX.md) / [Previous section](animating-in-fusions-spline-editor-and-spline-editor-overview.md) / [Next section](displaying-marker-with-the-timeline-and-autosnap.md)
<a id="source-markers"></a> <a id="source-navigating-around-the-spline-editor"></a> <a id="source-using-the-marker-list"></a> <a id="source-working-with-markers"></a>

### Navigating Around the Spline Editor

Often enough you’ll need to zoom and pan about the graph area so the splines you mean to work on stay in view. By and large, scaling and panning the Spline Editor behaves just as it does throughout the navigable corners of the Fusion interface. Even so, the Spline Editor brings a handful of its own functions for governing your view by the height, width, and selection of several animation splines. The plainest navigation tools to reach for are the scale sliders and buttons up in the top left of the Spline Editor panel.

For moving about the graph you have the Zoom Height slider, the Zoom Width slider, the Fit button, and the Zoom to Rectangle button To scale and pan with the sliders and buttons: The Zoom Height and Zoom Width sliders resize the graph area’s height and width. The Fit button tries to rescale the view so that every active spline fits inside the graph. The Zoom to Rectangle button (Command-R) lets you draw a bounding box over the patch of graph you’d like centered and scaled. To scale by the axis labels: Rest the mouse pointer on whichever ruler, horizontal-axis or vertical-axis, then drag to resize the graph along that axis alone. The scaling centers on wherever the pointer first sat on the ruler.

Dragging within the Time Ruler scales the graph horizontally To scale and pan via the mouse and/or keyboard:

- With the Spline Editor active, tap the + and - keys on your keyboard to zoom the graph in and out.
- You can likewise zoom onto a particular control point by holding the Command key and rolling the middle mouse wheel. Wherever the mouse pointer rests sets the area that magnifies.
- Rest the mouse pointer over the graph, then hold the middle mouse button down. While that middle button stays pressed, a single left-button click zooms in and a single right-button click zooms out.

To pan the graph area:

- Drag leftward or rightward with the middle mouse button, or lean on the scroll bar along the graph’s bottom and right edges.

Using the Graph contextual menu to navigate: The Spline Editor contextual menu opens up several more ways to move about the graph area.

- Choose Scale > Scale to Fit (Command-F) to tuck every active spline into the graph area.
- Choose Scale > Scale to Rectangle (Command-R) to drag a bounding box around the patch of graph

you’d like centered and scaled. The result matches clicking the Zoom to Rectangle button.

- Choose Scale > Default to return the graph area’s scaling to its default values.
- Choose Scale > Zoom In/Zoom Out to scale the graph area. It carries out the same job as

tapping the + and - keys on the keyboard.

- Choose Scale > Auto Fit to have the graph rescale on the fly to hold every spline as you show splines

and hide them. Change the scaling while Auto-Fit is on and the graph area scrolls along as the comp plays so all the keyframes stay in view.

- Choose Scale > Auto Scroll to make the graph area scroll whenever, during playback, the splines drift past the graph horizontally.
- Choose Scale > Manual to switch off every automatic effort to keep splines shown in the graph.
- Choose Options > Fit Times to scale the X-axis on its own so the selected spline fits. Every visible spline counts toward this, not the freshly selected one alone. Leave this option off and bringing up a new spline won’t alter the horizontal scale.
- Choose Options > Fit Values to scale the Y-axis on its own so the selected spline fits. Every visible spline counts toward this, not the freshly selected one alone. Leave this option off and bringing up a new spline won’t alter the vertical scale.

### Markers

Markers serve to flag frames that matter within a project. One might point to a frame where a ray gun fires a beam in the scene, the instant somebody steps through a portal in the image, or any other notable event in the composite. A marker dropped onto the Timeline on the Cut, Edit, Fairlight, or Color page turns up in the Fusion page’s Keyframes Editor and Spline Editor. Markers can be placed from the Keyframes Editor or the Spline Editor as well, whether you’re in Fusion Studio or on the Fusion page. They line up along the top of the Spline Editor’s horizontal-axis Time Ruler. Drawn as small blue shapes, each, once selected, sends a line straight down through the graph. NOTE: Markers fastened to clips on the Cut, Edit, Color, or Fairlight pages Timeline stay invisible in Fusion’s Spline Editor.

Markers left unselected sit along the top as blue shapes, while a selected one casts a vertical line down through the graph

### Working with Markers

A marker draws the eye to one particular frame inside a comp. Markers can be named, shown in a list, and edited. Once they’re in place, you can readily hop the playhead from one to the next, reposition them, or remove them entirely. To create a marker:

- Right-click within the horizontal axis Time Ruler and pick Add Marker.

A right-click in the horizontal time axis is how markers get added To delete a marker, do one of the following:

- Drag the marker upward, clear of the Spline Editor panel.
- Right-click the marker, then pick Delete Marker from the menu.
- Pick the marker, then press Delete or Backspace on the keyboard.
- Within the Marker List, pick a guide from the list and click the Del button.

To shift a marker onto a new frame, do one of the following:

- Drag the marker handle along the time axis.
- Right-click in the marker area and pick Options > Enable Marker Grab, then drag the marker’s vertical line to reposition the guide.

To send the Playhead to a marker:

- Right-click a marker and pick Set Current Time To [Frame number].

### Using the Marker List

The Marker List rounds up every marker in the present comp. It can present markers from the Keyframes Editor, from the Spline Editor, or from both panels at once. Click a guide’s frame number or name and the current time jumps to that marker’s frame. Being a floating window, the Marker List can stay open, letting you dash between different markers as you work in the Spline Editor. To show the Marker List:

- Right-click within the horizontal axis and pick Show Marker List, or press Shift-G.

Any markers already in the comp turn up in the Marker List on their own, no matter whether they came from the Keyframes Editor, the Spline Editor, or another page in DaVinci Resolve. Markers can also be added straight from the Marker List, which helps when several need adding and their timing is roughly known to you. Adding a guide from there runs thus: 1 In the Marker List window, click the Add button. 2 Type a frame number into the Time field. 3 Press Tab or click the Close button to shut the Marker List. To name a marker, do one of the following:

- Within the Marker List, double-click the Name column, just right of the frame number, and type a name for the marker.
- Right-click a marker in the horizontal axis and pick Rename Marker. In the dialog that opens, type a name for the marker.
