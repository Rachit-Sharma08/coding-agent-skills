# Camera tracker color

Version: DaVinci Resolve 20.3 Reference Manual. Context: Camera tracker.
[Chapter index](INDEX.md) / [Previous section](camera-tracker-3d-scene-transform.md) / [Next section](planar-tracker-node-what-the-planar-tracker-saves.md) / [Camera Tracker CTra](camera-tracker-track-tab.md)
<a id="source-color"></a> <a id="source-common-controls"></a> <a id="source-line-thickness"></a> <a id="source-offset"></a> <a id="source-options"></a> <a id="source-size"></a> <a id="source-the-camera-tracker-options-tab"></a> <a id="source-track-colors-locator-colors-export-colors"></a> <a id="source-understanding-camera-tracking"></a> <a id="source-wireframe"></a> <a id="source-workflow"></a>

### Color

Determines what color the ground plane takes on.

### Size

Governs the maximum size the ground plane may reach.

Subdivision Level Reports the polygon count making up the ground plane.

### Wireframe

Chooses whether the ground plane renders as a wireframe or a solid surface in the 3D view.

### Line Thickness

Controls the on-screen thickness of the lines drawn in the viewer.

### Offset

The ground plane’s center normally rests at the origin (0, 0, 0). You can apply this to nudge the ground plane higher or lower along the Y-axis.

Export Options Offers a checkbox list governing which items become nodes once you press the Export button. Your options here cover the following: Camera; Point Cloud; Ground Plane; Renderer; Lens Distortion; plus the camera’s Enable Image Plane. By way of the Animation menu you decide whether the camera or the point cloud gets animated. Pick the camera and the point cloud stays frozen in place while the camera is keyframed onto the live-action shot. Pick the point cloud and the reverse holds: the camera stays fixed while the whole point cloud is keyframed onto the live-action shot. Previous Export Clicking the Update Previous Export button refreshes the earlier exported nodes named here with whatever new data has been produced — that covers the camera path and attributes, the point cloud, and the renderer.

### Options

Through the Options tab you tailor the Camera Tracker’s onscreen controls, helping you make the most of whatever scene material is in front of you.

### The Camera Tracker Options tab

Trail Length Lays trail lines for the tracks over the viewer. How many frames ahead of and behind the current one are drawn comes down to this length value. Location Size This control resizes the point cloud locators within the 3D viewer. Each of Track Colors, Locator Colors, and Export Colors carries options to set its color to any of these: User Assigned, Solve Error, Take From Image, and White.

### Track Colors Locator Colors Export Colors

These cover the onscreen tracks shown in the 2D viewer, the point cloud locators shown in the 3D viewer, and the hues given to the locators exported inside the Point Cloud node.

Darken Image Lowers the image brightness in the viewers so the overlaid tracks stand out better, taking effect in both the 2D and the 3D viewers. Visibility Switches on or off which overlays appear in the 2D and 3D viewers. The available toggles are Tracker Markers and Trails; Reprojected Locators and Tracker Patterns; and a pair of Tooltips entries, one labeled “Tooltips in the 2D viewer” and the other “Tooltips in the 3D viewer.”

Colors Sets the color of the overlays.

- Selection Color: Controls the color of selected tracks/locators.
- Preview New Tracks Color: Sets the hue of the points that show in the viewer once the

Preview AutoTrack Locations option is switched on.

- Solve Error Gradient: Out of the box, a green-yellow-red gradient tints tracks and locators

so their solve error reads at a glance. You can adjust this gradient however you like. Reporting Sends an assortment of parameters and information out to the Console.

### Understanding Camera Tracking

On big productions, camera tracking — or 3D match moving — usually goes to specialists who know how to track and solve troublesome shots. Almost never can you tap a button or two and get a flawless result. Real success demands a grasp of the entire workflow and of what truly matters for landing a solid solved track. With hundreds of thousands of unknown variables to resolve, the Camera Tracker faces a tough job. The whole thing hinges on gathering quality tracking data that persists in the shot over a long stretch. Tracks that are false or poor will throw off the outcome. The pages here walk through clearing out false tracks along with other methods for reaching a good solve.

### Workflow

Arriving at a good solve is an iterative cycle: you Track, then Solve, apply your Refine Filters and Solve once more, run a Cleanup tracks pass followed by Solve, do a Cleanup from point cloud and Solve yet again, and Repeat the whole loop. At the start you will have many tracks, not all of them sound, so you have to filter and prune the unwanted ones until you are left with the strongest set. Once each round of cleanup finishes, hitting Solve should drive the solve error steadily downward. That figure has to drop below 1.0 to serve full HD content well, and it must go lower still at higher resolutions. Refining the tracks usually — though not always — yields a better solve. False Tracks A range of conditions spawn false tracks: objects moving through a shot, or glints and highlights bouncing off a car. Another flavor is the parallax error, where two objects lie at differing depths and their intersection ends up tracked. Such moiré effects can make a track drift. Spotting these False tracks and weeding them out is the single most important move in solving. Track Lengths A solid collection of long tracks is vital — the longer a track runs, the stronger the solve. Use the Bi‑Directional tracking option on the Tracker tab to push the start of tracks further back in time. The longer a track lasts and the more tracks that share overlapping time within a shot, the steadier and more precise the solve.

Seed Frames The solve relies on two seed frames. Its algorithm singles out a pair of frames separated as widely as possible in time while still holding the same tracks. This is precisely why long tracks weigh so heavily on which seed frames get chosen. Those two Seed frames act as the reference frames and ought to come from differing angles of one scene. The solve treats them as a master jumping-off point for fitting the remaining tracks across the sequence. The Solve tab offers an Auto Detect Seed Frames option, on by default and generally the smart pick — though letting it auto-detect can stretch the solve out. While you refine the Trackers and re-solve, switch the checkbox off and type the prior solve’s seed frames into the Seed 1 and Seed 2 sliders. You will find those seed frames listed in the Solve Summary near the top of the Inspector after the first solve. Refine Filters Once that first solve runs, every Tracker gains extra generated data — namely solve errors and tracking errors. Lean on the refine filters to thin out unwanted tracks, say by setting a minimum tracker length of eight frames. As you move each filter’s value, the Solve dialog reports how many tracks fall under that filter. Then Solve again. Onscreen Culling On the Options tab, dial the track to 20, which shows every track over the footage carrying a +-20 frame trail. As you scrub or play through, bad tracks become visible, can be selected right on screen, and removed with the Delete key. Catching tracks that go wrong this way calls for a practiced eye. Then Solve again. You may also open the exported scene in a 3D perspective viewer, where the point cloud appears. Orbit and pan the point cloud, then select and delete any points that fail to line up with the image and the scene space. Then Solve again. Keep cycling until the solve error sits below 1.0 ahead of exporting.

### Common Controls

Settings Tab You will find this same Inspector Settings tab repeated across the other Tracking nodes too. The shared controls get a full write-up just ahead, in the “The Common Controls” section.
