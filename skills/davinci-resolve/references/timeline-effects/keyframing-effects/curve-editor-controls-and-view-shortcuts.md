# Curve editor controls and set a keyboard shortcut to switch between curve and keyframe views

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing effects.
[Chapter index](INDEX.md) / [Previous section](curve-editor-open-in-the-timeline-and-curve-editor.md) / [Next section](keyframable-open-fx-and-resolve-fx-overview.md)
<a id="source-curve-editor-controls"></a> <a id="source-set-a-keyboard-shortcut-to-switch-between-curve-and-keyframe-views"></a>

### Curve Editor Controls

Running left to right, the Curve Editor controls begin with Curves Editor, Keyframe Editor, Parameters, Selection, and Hand; next come Add Keyframe, Linear, Ease in, Ease out, plus Ease in and Out; then Detail Zoom, Full Extend Zoom, Zoom Slider, Expand, and finally Option Menu.

Parameters: A click on this icon reveals or hides the parameter names.

Curves Editor: A click on this icon brings up the Curves Editor.

Keyframe Editor: A click on this icon brings up the Keyframe Editor. Pointer Mode: Drops you back into the usual mode, where pointing and clicking on items selects them. Hand Mode: Lets you grab and drag your way around the Curve Editor while zoomed in — handy when an animation is dense and intricate. Add Keyframes: Converts the pointer into an Add Keyframe tool, so a click on any curve in the Curve Editor drops a keyframe there. Show Handle: Flips the Bezier handle controls on or off.

Linear: Makes the curve travel straight from one keyframe to the next.

Ease In: Makes the curve build up gradually away from the starting keyframe.

Ease In and Out: Makes the curve build up gradually away from the starting keyframe and likewise build up gradually as it approaches the ending keyframe. Ease Out: Makes the curve build up gradually as it approaches the ending keyframe.

Detail Zoom: Zooms the Keyframe Editor inward, centered on the playhead.

Full Extend Zoom: Zooms the Keyframe Editor outward so the whole clip’s range is in view.

Zoom Slider: Lets you dial in a zoom level of your own for the Keyframe Editor

Zoom Height Slider: With Auto Zoom Graph Height switched off, this slider sets the Curve Editor’s height.

Expand: Pops the Keyframe and Curves Editor out into its own resizable window. Parameters: Brings up a checkbox for switching the visibility of individual curves. On top of that, should you have attached a keyframable Open FX or Resolve FX to the clip, those parameters can be chosen here.

Option Menu:

- Display Time Ruler in Seconds: Presents the time ruler using HH:MM:SS:FF timecode notation

drawn from the timeline.

- Display Time Ruler in Frames: Presents the time ruler as a frame count measured from the

timeline’s beginning.

- Enable Snapping: Once switched on in the Curve Editor, this locks keyframe control points

onto the playhead’s position.

- Show Curve Tooltips: Once switched on in the Curve Editor, hovering the pointer over a curve

surfaces that curve’s track name and value at that spot.

- Show Handles: Once switched on, the handles for every point along a curve appear and

become live.

- Auto Zoom Graph Height: When With this setting enabled (default) the curve editor’s height

shifts on its own according to the values of the keyframes currently in play. Switch it off and the graph-height zoom kicks in, governed in range by a horizontal slider, while a vertical window slider lets you scroll the full graph height from top all the way to bottom. That comes in handy when several keyframed parameters share the graph and their ranges differ by orders of magnitude.

### Set a Keyboard Shortcut to Switch Between Curve and Keyframe Views

When you’re reaching for the keyframes and curves a lot, a keyboard shortcut can flip you back and forth between the curve and keyframe views. 1 Head to DaVinci Resolve > Keyboard Customization. 2 Under Commands, pick All Commands. 3 Enter “toggle keyframe” into the search box. 4 Bind a keyboard shortcut to Toggle Keyframe/Curve for the Cut Page, Edit Page, or Keyframe Editor.
