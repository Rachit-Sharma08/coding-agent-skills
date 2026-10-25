# Playing flipbook previews and removing flipbook previews

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](viewer-divider-bar-and-zooming-and-panning-into-viewers.md) / [Next section](onscreen-controls-and-viewer-toolbars.md)
<a id="source-configurations"></a> <a id="source-flipbook-preview-render-settings"></a> <a id="source-frame-range"></a> <a id="source-network"></a> <a id="source-onscreen-controls"></a> <a id="source-playing-flipbook-previews"></a> <a id="source-removing-flipbook-previews"></a> <a id="source-settings"></a> <a id="source-shoot-on"></a> <a id="source-showing-and-hiding-onscreen-controls"></a> <a id="source-size"></a> <a id="source-the-angle-preview-control"></a> <a id="source-updating-a-preview"></a>

### Playing Flipbook Previews

Once the Flipbook Preview sits in a viewer, or is opened full-screen, both the mouse and the keyboard let you play it back or scrub through it. For mouse-driven Flipbook playback, here's the move:

- Double-click in the viewer to start playback.

For mouse-driven scrubbing through a Flipbook, here's the move:

- With the right mouse button held down, drag to the left or right and the frames scrub past.

For keyboard-driven Flipbook playback, take one of these routes:

- Press the Spacebar to start or stop playback.
- Hold Shift and press the Spacebar to play in reverse.

For keyboard-driven frame-by-frame scrubbing through a Flipbook, take one of these routes:

- Press the Left or Right Arrow keys to step to the previous or next frame.
- Hold Shift and press the Left or Right Arrow keys to leap back or ahead 10 frames.
- Press Command-Left Arrow to leap to the first frame.
- Press Command-Right Arrow to leap to the last frame.

TIP: These mouse and keyboard shortcuts function in full-screen mode too.

### Removing Flipbook Previews

Having built a Flipbook Preview, you'll want to know how to clear it out of RAM. To do away with a Flipbook you've created: Right-click inside a viewer that holds a Flipbook Preview, then pick Remove Preview.

### Flipbook Preview Render Settings

This section runs through every setting on offer for rendering Flipbook Previews into RAM.

### Settings

The Settings section of the Preview Render dialog carries three buttons that govern your Flipbook Preview's overall quality and look. Those buttons also weigh heavily on render times. HiQ: Switched on, this setting renders the preview at full image quality. To see how a node's final output would appear, you'd switch the HiQ setting on. While putting together a rough preview to test animation, you can spare yourself time by switching it off. MB: The MB here stands for Motion Blur. Switched on, this setting renders with motion blur in place wherever any node is set to produce motion blur. While building a rough preview where the motion blur on animated elements doesn't matter to you, you can spare yourself time by switching it off. Some: With Some switched on, only the nodes truly needed to produce the image of the node you're previewing get rendered.

### Size

Because RAM Flipbook Previews draw on RAM, it helps to know how many frames you can render into RAM before memory runs out. The Flipbook Preview dialog works out the memory currently free and shows how many frames will fit into RAM. Should your machine carry little RAM and you can't render the full range of frames you'd like, you can opt to drop the resolution to a setting that strikes the best quality/duration ratio for your preview.

### Network

Network rendering is on offer in Fusion Studio alone. For more on network rendering, turn to Chapter 66, "Rendering Using Saver Nodes," within the DaVinci Resolve Reference Manual or Chapter 4 of the Fusion Reference Manual.

### Shoot On

There are times you won't want every single frame rendered, but rather every second, third, or fourth frame, to trim render time and get feedback faster. The Step parameter lets you set the interval at which frames get rendered.

### Frame Range

This field starts out at the current Render Range In/Out set in the Time Ruler, fixing the first and last frames for rendering. You can adjust the range to render more frames or fewer.

### Configurations

Having built a preview configuration worth keeping, you can store it for later by clicking the Add button, naming it, and clicking OK.

### Updating a Preview

This option suits the hands-on, frame-by-frame business of rotoscoping and painting. On a preview in the viewer, right-click and pick Update from its contextual menu. While it's active, any frames you change on the previewed node refresh on their own within the preview's playback. That lets you hold the RAM in reserve for playback. You can leave it running on a loop or ping-pong while you carry on in another viewer.

### Onscreen Controls

When you're adjusting images, the Control Panel hands you very precise numerical values, yet now and then placing an element visually through onscreen controls gets you where you're headed with less fiddling.

### The Angle preview control

The viewers present onscreen controls for working the parameters of whichever node is currently selected. Crosshairs, angle indicators, polylines, and paint strokes count among the common onscreen controls. Each of these controls can be worked straight in the viewer with the mouse or keyboard. Which controls the viewers present hinges on which nodes are selected, not on the node shown in the viewer. As an instance, you can easily view a downstream blur while working the controls for a selected polygon mask or merge. With several nodes selected, the controls for every selected node show up all at once.

### Showing and Hiding Onscreen Controls

A viewer's onscreen controls can be tucked away so they don't get in the way of viewing the image. To flip the visibility of onscreen controls, do one of the following:

- Click a viewer's Option menu and pick Show Controls to flip the controls on or off.
- Right-click in a viewer and pick Options > Show Controls from the contextual menu.
- Select a viewer and press Command-K.
