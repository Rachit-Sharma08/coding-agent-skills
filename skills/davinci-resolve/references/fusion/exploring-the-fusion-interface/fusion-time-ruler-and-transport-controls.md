# Time ruler and transport controls and time ruler controls in the Fusion page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](fusion-viewer-zoom-pan-and-node-loading.md) / [Next section](real-time-playback-not-guaranteed-and-frame-increment-options.md)
<a id="source-controlling-playback"></a> <a id="source-exploring-the-fusion-interface-part-2"></a> <a id="source-navigation-shortcuts"></a> <a id="source-render-range"></a> <a id="source-the-fusion-page-controls-for-playback"></a> <a id="source-the-playhead"></a> <a id="source-time-ruler-and-transport-controls"></a> <a id="source-time-ruler-controls-in-fusion-studio"></a> <a id="source-time-ruler-controls-in-the-fusion-page"></a> <a id="source-transport-controls-in-the-fusion-page"></a> <a id="source-zoom-and-scroll-bar"></a>

### Time Ruler and Transport Controls

Sitting just below the viewer area, the Time Ruler keys off the composition's overall duration. What it stands for hinges on the Fusion version you're running:

- For DaVinci Resolve users, the span shown in the Time Ruler range follows whatever is selected at the moment in the Edit or Cut page timeline.
- In Fusion Studio, the Time Ruler follows the Global Start and End values set under Fusion Studio Preferences > Defaults.

The transport controls beneath the Time Ruler bring together playback controls, audio monitoring, and number fields for the composition duration and playback range. Further controls switch on motion blur and proxy settings.

### Time Ruler Controls in the Fusion Page

With a single clip selected in the Edit or Cut page Timeline, the global range the Time Ruler displays reflects that clip's full source duration. The playhead can't travel past the global range. Those yellow lines, known as the render range, pin down the clip's current In and Out points and mark the only frames the Fusion page shows. Everything beyond that range makes up the unused head and tail handles of the source clip.

The Time Ruler laying out a clip's ranges in the Timeline through yellow marks (with the playhead in red) Should you have made a Fusion clip or a compound clip, the “working range” then mirrors that clip's whole duration.

The Time Ruler laying out a Fusion clip's ranges in the Timeline Render Range The render range fixes which frames the Fusion page shows and which feed interactive playback, disk caches, and previews. Frames lying past the default render range stay hidden on the Fusion page and go neither rendered nor played. You're free to alter the render range's length for preview and playback alone. Shortening or lengthening that range does nothing to trim the clip in the Edit or Cut page Timelines. To change the render range in the Time Ruler, do one of these:

- Keep the Command key held and drag a fresh range inside the Time Ruler.
- Drag either the starting or ending yellow line to shift where the range begins or ends.
- Right-click inside the Time Ruler and pick Set Render Range from the contextual menu.
- Type fresh ranges into the Range In and Out fields left of the transport controls.
- Drag a node out of the Node Editor onto the Time Ruler to match the range to that node's duration.

To send the render range back to the timeline clip's In and Out points, do one of these.

- Right-click inside the Time Ruler and pick Auto Render Range.
- Step back to the Edit or Cut page, then come back to the Fusion page.

### Time Ruler Controls in Fusion Studio

Sitting under the viewer area, the Time Ruler lays out two separate frame ranges: one spanning the whole composition, termed the global range, and another termed the render range, which dictates what gets rendered and what gets cached in memory for previews. The global start and end range fills the entire Time Ruler and sets a composition's total duration. The playhead can't be moved past the global range.

The Time Ruler showing a clip's ranges in the Timeline by way of yellow marks (the playhead rendered red) Global Start and End Range This range amounts to nothing more than the current composition's total duration. To change the global range, do one of these:

- To set the global range that every new composition starts with, macOS users choose Fusion Studio > Preferences, while on Windows or Linux you go to File > Preferences. Over in the Global and Default Settings panel, type a fresh range into the Global range fields.
- To set the Global range for the current composition, type a fresh range into the Global Start and End fields left of the transport controls.
- Dragging a node out of the Node Editor onto the Time Ruler automatically pins the Global and Render Range to the node's extent.

### Render Range

The render range sets which frames feed interactive playback, disk caches, and previews. Frames beyond the render range go neither rendered nor played, though you can still drag the playhead onto them to view those unused frames. When you want to preview or render a particular stretch of a composition, several ways exist to adjust the render range. To set the render range in the Time Ruler, do one of these:

- Keep the Command key held and drag a fresh range inside the Time Ruler.
- Right-click inside the Time Ruler and pick Set Render Range from the contextual menu to base the Render Range on the selected Node's duration.
- Type fresh ranges into the Range In and Out fields left of the transport controls.
- Drag a node out of the Node Editor onto the Time Ruler to match the range to that node's duration.

### The Playhead

A red playhead in the Time Ruler points to the frame you're currently viewing. Click anywhere in the Time Ruler and the playhead leaps to that frame; drag inside the Time Ruler and the playhead moves along within the available duration of the clip or composition.

### Zoom and Scroll Bar

A gray scroll bar with two handles lets you zoom into whatever range the Time Ruler shows, which helps when a very large Global range leaves the Render range as just a thin sliver in the Time Ruler. Dragging this bar's left or right handle zooms against the opposite handle, widening each displayed frame. After you've zoomed in, sliding the scroll bar left or right moves you across the composition. TIP: With the middle mouse button held down, a drag inside the Time Ruler scrolls the visible range.

### Transport Controls in the Fusion Page

On DaVinci Resolve's Fusion page, the Transport Controls gather buttons for driving playback plus time fields, those on the left for setting the render range and those on the right for the current time. The right-click menu holds extra controls.

### Controlling Playback

Beneath the Time Ruler on the Fusion page sit six transport controls. They run as follows: Composition First Frame and Play Reverse, then Stop, followed by Play Forward, and finally Composition Last Frame plus Loop.

### The Fusion page controls for playback

### Navigation Shortcuts

Plenty of the usual transport control keyboard shortcuts you already know carry over into Fusion, while a few answer to Fusion's own particular needs. To shift the playhead along the Time Ruler from the keyboard, do one of these:

- Spacebar: Switches forward playback on or off.
- JKL: The familiar JKL scheme works here too — press J to run backward, K to halt, and L to

play forward.

- Back Arrow: Steps backward by a single frame.
- Forward Arrow: Steps forward by a single frame.
- Shift-Back Arrow: Sends the playhead to the clip’s Global Start frame.
- Shift-Forward Arrow: Sends the playhead to the clip’s Global End frame.
- Command-Back Arrow: Jumps to the Render Range In point.
- Command-Forward Arrow: Jumps to the Render Range Out point.
