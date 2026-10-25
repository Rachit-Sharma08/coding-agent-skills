# Script and script preferences

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](email-notification-and-server-settings.md) / [Next section](timeline-preferences-and-filter-filter-to-use.md)
<a id="source-login"></a> <a id="source-lut-view-options"></a> <a id="source-options"></a> <a id="source-python-version"></a> <a id="source-script"></a> <a id="source-spline-editor"></a> <a id="source-spline-editor-options"></a> <a id="source-splines"></a> <a id="source-the-script-preferences"></a> <a id="source-the-spine-editor-preferences"></a> <a id="source-the-splines-preferences"></a> <a id="source-timeline"></a>

### Script

The Scripting preferences carry a field for the passwords used to run scripts from the command line, plus the applications to call on when editing scripts.

### The Script preferences

### Login

Running scripts beyond the Fusion application comes with three login options.

- No Login Required to Execute Script: Switched on, scripts launched from the command line — or scripts that try to drive remote copies of Fusion — can run without logging in to the workstation.
- Specify Custom Login: With a username and password set, Fusion turns away incoming external script commands (those from FusionScript, say) until the Script logs in to the workstation first. This bears only on scripts launched from the command line, or scripts that try to drive remote copies of Fusion. Scripts launched from within the interface need no login no matter how this is set. For more information, see the Scripting documentation.
- Use Windows Login Validation: When you run Fusion on Windows, switching this on checks the user name and password (also known as credentials) against the operating system before the script runs.

### Options

- Script Editor: Reach for this preference to pick an external editor for scripts. It comes into play when you choose Scripts > Edit.

### Python Version

- A pair of options sit here for picking which version of Python you intend to use for your scripts.

### Spline Editor

The Spline Editor preferences let you dial in various spline options covering Autosnap behavior, handles, markers, and beyond. This touches only splines shown in the Spline Editor, not splines made in the viewer with the polygon tool or paths.

### The Spine Editor preferences

### Spline Editor Options

These settings steer how splines behave in the Spline Editor, along with how the graph area looks.

- Independent Handles: Switch this on and the In or Out direction handle on freshly made key frames can move on its own, leaving the other untouched. You’ll also find this option through the Options submenu when right-clicking in the Spline Editor graph.
- Follow Active: The Spline Editor centers on whichever tool is currently active. You’ll also find this option through the Options submenu when right-clicking in the Spline Editor graph.
- Show Key Markers: Small colored triangles appear along the top of the Spline Editor Time Ruler to mark key frames on active splines. Each triangle’s color matches its spline’s color. You’ll also find this option through the Show submenu when right-clicking in the Spline Editor graph.
- Show Tips: Switches the display of tooltips on or off. You’ll also find this option through the Show submenu when right-clicking in the Spline Editor graph.
- Autosnap Points: As you move points in the Spline Editor, they’ll either snap to the fields or frames or stay free to move. You’ll also find this option through the Options submenu when right-clicking in the Spline Editor graph.
- Guides: As you move points in the Spline Editor, they’ll snap to guides too. You’ll also find this option through the Options submenu when right-clicking in the Spline Editor graph.
- Autosnap Guides: As you move or create guides, they’ll either snap to the fields or frames or stay free to move. You’ll also find this option through the Options submenu when right-clicking in the Spline Editor graph.
- Autoscale: Holds the Spline Editor scales steady as the graph’s editable spline content changes. This scale is likewise reachable through the Options submenu when right-clicking in the Spline Editor graph.
- Scroll: Scrolls both horizontally and vertically to bring all, or nearly all, of the spline points into view. You’ll also find this option through the Scale submenu when right-clicking in the Spline Editor graph.
- Fit: Zooms so every point fits within the spline graph, where needed. You’ll also find this option through the Scale submenu when right-clicking in the Spline Editor graph.

### LUT View Options

These settings let you steer how the LUT view is shown.

- Independent Handles: Switch this on and the In or Out direction handle on freshly made key frames can move on its own, leaving the other untouched.
- Show Key Markers: Small colored triangles appear along the top of the Spline Editor Time Ruler to mark key frames on active splines. Each triangle’s color matches its spline’s color.
- Show Tips: Switches the display of tooltips on or off.

### Splines

You’ll find options for handling and smoothing animation splines, tracker path defaults, and rotoscoping over in the Splines preferences.

### The Splines preferences

- Autosmooth: Smooths any freshly made points or key frames automatically on whichever splines are picked in this section. You can opt to auto-smooth animation splines, B-Splines, polyline matte shapes, LUTs, paths, and meshes.
- B-Spline Modifier Degree: This setting fixes how strongly the line segments sway the resulting curvature when B-Splines drive animation. Cubic B-Splines trace a segment through two control points between the anchor points, while Quadratic B-Splines trace a segment through one control point between the anchor points.
- B-Spline Polyline Degree: This setting works like the one above but applies to B-Splines used for masks.
- Tracker Path Points Visibility: This setting fixes how visible the control points on tracker paths are. You can show them, hide them, or have them appear when your cursor hovers over the path, which is the default behavior.
- Tracker Path: By default the tracker makes Bézier-style spline paths. Two further options in this setting let you pick B-Spline or XY Spline paths instead.
- Polyline Edit Mode on Done: This setting fixes what state the Polyline tool lands in once you finish drawing a polyline. It can be set either to adjust the spline’s existing control points or to adjust and add new control points to the spline.
- Onion Skinning: The Onion Skinning settings fix how many frames show while you rotoscope, letting you preview and compare a span of frames. You can also set whether the preview draws frames only from before the current frame, after the current frame, or split across the two.

### Timeline

The Timeline preferences are where you build and edit Keyframes Editor/Spline Editor filters and set the default options for the Keyframes Editor.
