# Match move a tracker control in the match move filter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Match move studio version only.
[Chapter index](INDEX.md) / [Next section](match-move-and-surface-tracker.md)
<a id="source-a-match-move-workflow"></a> <a id="source-a-tracker-control-in-the-match-move-filter"></a> <a id="source-main-controls"></a> <a id="source-match-move-studio-version-only"></a> <a id="source-positioning"></a> <a id="source-resolve-fx-transform"></a> <a id="source-resolve-fx-transform-part-1"></a> <a id="source-the-display-options-group"></a> <a id="source-the-final-match-moved-composite"></a> <a id="source-the-manage-tracking-patches-group"></a> <a id="source-tracking-controls"></a>

### Resolve FX Transform

The plugins grouped here give you transform types — both keyframed and static — beyond what the Sizing palette or the Inspector's Clip Transform controls can offer.

### Match Move (Studio Version Only)

TIP: These days, match move tasks are handled far more capably on the Fusion page, where the relevant tools and techniques live. The Match Move filter works as a patch-style tracker, following a pattern area marked out by a tracker control. Apply the filter to a node and click any feature in the Viewer that you wish to follow, and you may add as many trackers as you want. The best candidates to track are sharply defined, high-contrast details with crisp angular edges. Every tracker control is made up of (a) a center point marking where the resulting motion path will be anchored, (b) a resizable inner box marking the image patch under track, (c) a resizable outer box marking the search region for that track, and (d) a patch window giving you a magnified close-up of the patch being followed. You resize patch windows, and reveal or conceal the remaining tracking controls, through the settings located in the Display Options section of the Match Move controls.

### A tracker control in the Match Move filter

Should a tracker control land somewhere by mistake, you can relocate it by dragging from anywhere inside the inner box, or remove it entirely by Option-clicking it. After it's down, resizing that tracker control determines how much picture detail gets factored into the analysis. Resizing is done by hovering the pointer over the inner box edge and dragging it smaller or larger. The plugin pulls out whatever amount of motion data the count of placed trackers permits:

- A single tracker follows position along the horizontal and vertical axes (pan and tilt).
- With two trackers or more, rotation is also followed.
- With four trackers or more, perspective is followed as well.
- Once you reach six trackers or more, the Match Move filter can on its own pick

from the whole set whichever tracker data is strongest, producing the most precise track achievable.

### A Match Move Workflow

What follows walks through the most basic end-to-end procedure for bringing in a foreground clip and compositing it, with a match move that tracks a background clip already sitting in the timeline. Use it for jobs like dropping a graphic onto the side of a building as a sign, or onto the screen of a phone. To match move: 1 Within the Media Pool of the Edit page, right-click whichever clip is to be match-moved onto a Timeline clip, then pick “Add as Matte For Color Page Clip” — this drops it into the Color page Node Editor of the clip currently selected, as a Timeline Matte. For now, that is the one and only way to match move and composite a foreground clip over a background clip while on the Color page. 2 Switch to the Color page, verify the destination background clip is selected, bring up the OpenFX library, and drag the Match Move plugin straight onto the link running from the tree's final node to the Output, dropping it in as its own independent FX node. Inserting the Match Move filter on its own as a standalone FX node 3 Right-click whichever corrector node you like in the node tree (here, Node 01), then from the contextual menu's Add Matte > Timeline Mattes submenu select the clip you brought in back at step 1, which surfaces that clip as an Ext. Matte node. Sever the link between the freshly created Ext. Matte node and whatever it connects to, then route its RGB output into the second input of the FX node instead.

Connecting the foreground image to the second input of the FX node

4 Select the FX node, confirm the OpenFX onscreen controls are turned on, decide whether tracking should kick off from the clip's first or last frames, and then click inside the Viewer to drop tracker controls onto the part of the image where the foreground image will be attached. For a perspective track, drop a minimum of four tracker patches onto regions you're confident won't be hidden by other elements in the frame. Pick angular, high-contrast features for best results, and do your best to keep the tracked features from leaving the frame or being covered by other things in it. While you drop tracking controls, each patch window takes on the tint of whichever channel DaVinci Resolve decides on its own will yield the strongest tracking outcome.

Dropping tracker controls onto the feature you intend to Match Move onto 5 (Optional) Where required, unwanted trackers can be removed by Option-clicking them. 6 With every tracker control now in place, the tracking analysis can begin. When the playhead sits at the clip's start, click Track Forward; otherwise click Track Backward. DaVinci Resolve then analyzes, on its own, every tracker control across the clip right through to its final frame.

Using the Tracking controls

7 (Optional) When a tracked patch gets covered by something, or the feature being tracked starts to drift past the frame edge, that tracker control can wander off and ultimately shut itself down. Should that occur, resuming the track is remarkably simple: a) Press the Track Forward (or Track Backward) button once more to halt the analysis. b) Roll the playhead back to the final frame holding good tracking data, then click the inner box of each tracker control that misbehaved to confirm it's active (a visible patch window tells you it's on), and click “Clear tracking forward” or “Clear tracking backward” as appropriate to wipe the bad tracking data. Once that's done, click the inner box of each errant tracker to switch it off again, so it stops trying to track wrongly (a hidden patch window tells you it's off). c) At this point, drop extra trackers onto other features of that same surface to stand in for the trackers you had to disable.

Dropping additional tracking controls to make up for those that shut themselves down on leaving the frame or being hidden by other moving elements in the picture d) Click “Track forward” again to pick the track back up, and DaVinci Resolve will draw on those extra features as it carries on the analysis. e) Once the analysis wraps up, switch the trackers you'd disabled back on. Every active tracker feeds data into the match move across whatever frame ranges hold valid tracking data for it. 8 After DaVinci Resolve wraps up its analysis, roll the playhead back to the track's first frame and pick Positioning from the “Show controls for” pop-up menu. That carries you into the following stage of the Match Moving process.

Choosing the Positioning controls

9 A grid shows up across the Viewer. This is the positioning canvas, which lets you corner-pin the region where the foreground image you wired up in step 3 gets composited and tracked. Dragging its corners both corner-pins and resizes it, while dragging the center repositions it.

Resizing the canvas to fit the foreground image into the background 10 With the grid placed, scrub forward and backward to confirm it tracks accurately and holds up visually once things move. 11 In the “Show controls for” pop-up menu, pick Compositing so the compositing controls appear. 12 Switch the Output pop-up menu over to “Composite” in order to render out the finished match-moved composite. As needed, the Composite Type and Plate Cropping controls let you set how the foreground image blends against the background and let you trim away unwanted edge portions of the image.

### The final match moved composite

With that, the match move is complete.

### Main Controls

Through the “Show controls for” pop-up menu you select among four control pages that walk you through the match moving workflow. The Output pop-up menu sets what gets output, offering Disabled, Positioning Reference, and Composite.

### Tracking Controls

The Tracking Controls oversee the opening stage of match moving, and this control page supplies all you require to set up, run, and fine-tune multi-patch motion tracks.

Controls revealed once Main Controls is switched to Tracking Controls The Tracking Controls group The main controls for kicking off tracking. They comprise the tracking buttons, which run tracks either automatically via the outer Track Forward or Track Backward buttons or by hand via the inner Track Next or Track Previous buttons. Pausing a track is handled by the middle button. The Next Track End and Previous Track End buttons jump you to earlier and later tracked spans of frames; whenever gaps exist in your tracking data, these controls hop you between separate stretches of continuous tracking data. A pair of checkboxes determines whether Zoom and/or Rotation gets tracked and analyzed. You have to set these before tracking starts.

### The Manage Tracking Patches group

Up top, two buttons govern which tracking patches are switched on to feed the overall match moving result and which are switched off. Activate None and Deactivate All flip every patch on or off in a single action.

Clear Past and Clear Future wipe out faulty tracking data either ahead of or behind the playhead's present position, applying to enabled tracker controls. Delete Tracking removes the tracking data only at the current frame, again for enabled tracker controls. Refresh Tracks renews a tracker control's patch whenever the tracked feature shifts enough in shape, color, or lighting to disrupt the track. Pick one or more trackers and click Place New Patch in Track to refresh the tracked feature at that frame.

### The Display Options group

Use this group to toggle whether various onscreen controls appear. Its checkboxes cover Show Trackers; Show Center, meaning the red center point of the track; Show Paths, meaning the motion paths that were tracked; and Show Active Patches. A slider sets the dimensions of each patch window. Show Comp Result reveals the composited foreground layer over the background layer.

### Positioning

The Positioning controls handle the second phase of the match moving process. They give you all you need to transform the foreground image so it sits against the background, through repositioning, corner-pinning, and resizing.

Controls revealed once Main Controls is switched to Positioning Canvas Options The Canvas Controls pop-up menu toggles you into corner-pin controls, in which dragging each of the four corners performs corner-pinning, dragging the center moves the grid, and dragging the top, bottom, or sides scales it vertically or horizontally. A Reset Corners button returns the grid to full screen, handy when you want to abandon the current attempt and start fresh.
