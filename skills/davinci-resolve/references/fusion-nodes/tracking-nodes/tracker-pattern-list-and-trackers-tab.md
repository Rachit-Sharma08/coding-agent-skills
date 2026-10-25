# Tracker pattern list and trackers tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tracker.
[Chapter index](INDEX.md) / [Previous section](tracker-a-tracker-node-branched-from-the-node-tree.md) / [Tracker Tra](tracker-a-tracker-node-branched-from-the-node-tree.md) / [Next section](tracker-operation-tab.md)
<a id="source-inspector"></a> <a id="source-the-tracker-node-trackers-tab"></a> <a id="source-tracker-list"></a> <a id="source-tracker-pattern-display"></a> <a id="source-tracker-states"></a> <a id="source-trackers-tab"></a> <a id="source-tracking-nodes-part-5"></a>

### Inspector

### The Tracker node Trackers tab

### Trackers Tab

The Trackers tab holds the controls for making, placing, and launching tracking operations. Once a track is done, offset controls sharpen how the image lines up after the track. Track Buttons Four buttons kick off tracking, plus a middle button that halts a track already underway. These buttons can drive the current pattern forward or backward in time. Hovering the pointer over any button pops up a tooltip naming it. Here is how the buttons behave:

- Track Reverse: Pressing this sets every active tracker tracking from the end of the render range and working backward in time to the render range’s start.
- Track Reverse From Current Time: Pressing this sets every active tracker tracking from the current frame and working backward in time to the render range’s start.
- Stop Tracking: Pressing this, or hitting ESC, halts the tracking process at once. It’s only live while tracking is happening.
- Track Forward From Current Time: Pressing this sets every active tracker tracking from the current frame and working forward in time to the render range’s end.
- Track Forward: Pressing this sets every active tracker tracking from the first frame of the render range and working forward in time to the render range’s end.

Tracking Behavior Controls Every control here shapes how trackers cope with shifting patterns, how the resulting track path gets defined, and how many keyframes come out of it. Frames Per Path Point This slider sets how frequently the Tracker drops a keyframe onto the path. Its default of 1 lays a keyframe on the tracked path at each and every frame. Raising the figure makes the tracked path less precise. That can be useful when the track keeps returning unsteady results, but ordinarily you should leave this control at its default. TIP: With a field-rendered project, a value of 1 places a keyframe on every field. Because the Tracker is so precise, the field positions then introduce a faint up-and-down jitter. To get cleaner results tracking interlaced footage in Field mode, raise the Frames Per Path Point slider to 2, which yields a single keyframe per frame of your footage.

Adaptive Mode To assist with tricky tracks, Fusion can re-grab the tracked pattern whenever that’s needed. This menu picks the Adaptive tracking method.

- None: At None, the tracker hunts for the original pattern on each frame.
- Every Frame: At Every Frame, the tracker re-grabs the pattern on each frame. This lets

the Tracker absorb slow shifts in profile and lighting across time.

- Best Match: At Best Match, the tracker weighs the originally selected pattern against the pattern grabbed at each frame. Should the difference between the two exceed the threshold set by the Match Tolerance control, the tracker skips re-grabbing the pattern on that frame. This guards against Tracker drift brought on by fleeting artifacts crossing the pattern’s path (a shadow, for example).

Path Center This menu governs how the Tracker acts when a pattern is repositioned. It comes in especially handy once a pattern leaves the frame or alters so drastically that tracking it is no longer possible.

- Pattern Center: With Pattern Center chosen in the menu, the tracked path picks up from the center of the new path. That suits cases where you’re swapping out an existing path completely.
- Track Center (append): With Track Center (append) chosen in the menu, a new pattern’s tracked path is tacked onto the existing one. The fresh path is offset automatically by however much is required. You use this setting to introduce a new tracking pattern once the original drifts out of frame or gets hidden behind other objects. The trick works best when the new pattern sits near the original’s location, sparing you parallax or lens-distortion trouble.

### Tracker List

One Tracker node is able to track several patterns. Every tracker pattern made in the current Tracker node is administered through the Tracker List. Tracker List The Tracker List lists the names of all the trackers you’ve made.

- Each tracker pattern shows in the list by name beside a small checkbox. Clicking a tracker pattern’s name selects it.
- The controls beneath the list then shift to act on that tracker pattern alone. Click an already-selected tracker pattern once to rename it to something more descriptive.
- Clicking the checkbox toggles the tracker’s state.

### Tracker States

- Enabled (black checkbox): A pattern that’s enabled re-tracks on every launch of the track. Other nodes can use its path data, and that data is open to Stabilization and Corner Positioning.
- Suspended (white circle): A Suspended pattern won’t re-track when the track launches. Its data is locked so it can’t change further. The path’s data still serves other nodes and remains open to advanced Tracking modes such as Stabilization and Corner Positioning.
- Disabled (clear): A Disabled pattern lays down no path when tracking launches, and its data reaches neither other nodes nor advanced Tracking operations such as Stabilization and Corner Positioning.

Three tracking patterns, top to bottom: enabled, suspended, and disabled

Add/Delete Tracker These buttons let you add or remove IntelliTrack or Point trackers from your Tracker List. Show This menu chooses which controls appear among the Tracker node controls. It has no bearing on how the tracker runs; it only governs the lower half of the Inspector interface.

- Selected Tracker Details: With Selected Tracker Details picked, the controls on view apply solely to whichever tracker is currently selected. You’ll get the Pattern window plus the Offset sliders.
- All Trackers: With All Trackers picked, the pattern window for every added tracking pattern shows at once beneath the Tracker List.

Left Pattern Display The pattern display holds two image windows set side by side along with a row of status bars. The left window presents the pattern you first selected, while the right one gives a live view of the current pattern as the track moves along. Whenever the onscreen controls shift during tracking, the leftmost window refreshes to reflect the pattern. As the pattern travels, the vertical bars just to the right of the image report how clear and contrasty each image channel is. Whichever channel or channels read clearest are picked for tracking. Those channels carry a gray background in their representative vertical bar. You can stick with the automatic tracking or overrule it and name the channel yourself by clicking the button under the channel you want tracked.

### Tracker pattern display

Ordinarily, the pattern display shows the channel that’s selected. When that channel is blue, what appears is a grayscale rendering of the pattern’s blue channel. The image is shown in color only after you switch on the Full Color button. To change this, click the Show Full Color button under the pattern display rather than the Show Selected Channel button. TIP: Since Fusion automatically chases the highest-contrast channel, you could wind up tracking a channel that’s noisy yet high in contrast. It’s always wise, before you track, to zoom into your footage and inspect the RGB channels one at a time. Right Pattern Display The right-hand pattern display reflects the actual pattern grabbed for tracking. It stays black until you’ve tracked the selected pattern at least once. During tracking the display springs to life, showing the pattern Fusion grabs frame after frame. As the track runs, each frame’s pattern stacks up into a Flipbook that you can replay in the pattern window afterward using the transport controls along the bottom of the window.

As the track proceeds, the vertical bar right beside the pattern conveys how sure Fusion is that the current pattern lines up with the one you first selected. A green bar signals strong confidence that the current pattern matches the original, a yellow bar signals weaker certainty, and a red bar signals severe doubt. Once tracking finishes, the pattern display presents a little Flipbook of that pattern’s track to help you spot frames where the track went wrong. Tracker Sizes Beyond the onscreen controls, every tracker comes with sizing parameters for adjusting the pattern and search box.

- Pattern Width and Height: These controls let you set the selected tracker pattern’s width and height by hand. You can also size the tracker pattern in the viewer, which is the usual approach, though tiny adjustments often go more smoothly with the precision these manual controls offer.
- Search Width and Height: The search area dictates how far Fusion scans the image from frame to frame to re-grab the pattern while tracking. Just as with Pattern Width and Height, you can size the search area in the viewer, but you might prefer to make small adjustments by hand with these controls.

Tracked Center Where the tracker's center sits is reported by this positional control. To strip a path you tracked earlier off a tracker pattern, right-click this parameter and pick Remove Path out of the contextual menu. X and Y Offset For objects that don't hand you a well-defined or dependable pattern, the Offset controls help you build a track anyway. What the Offset controls do is let you track something nearby in place of the intended object. Lean on these Offsets to nudge the path into the position you want, all while the tracker pattern rectangle stays parked over the real tracking spot. The Offset is adjustable right in the viewer too, by switching on the Offsets button found in the viewer toolbar.

Up at the viewer's top left, the tracker offset icon serves to shift the tracking pattern away from the object you're aiming at.
