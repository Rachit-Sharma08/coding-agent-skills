# Snapping to guide lines and proxy handling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](source-clip-and-viewer-showing-source-clip.md) / [Next section](clip-status-scene-detection-and-edit-ranges.md)
<a id="source-bypass-color-grades-and-fusion"></a> <a id="source-enhanced-viewer"></a> <a id="source-full-screen-viewer"></a> <a id="source-playing-clips-and-navigating-the-timeline-in-the-viewer"></a> <a id="source-proxy-handling"></a> <a id="source-scrolling-through-the-timeline"></a> <a id="source-snapping-to-guide-lines"></a> <a id="source-the-enhanced-viewer-in-the-cut-page"></a> <a id="source-the-full-screen-viewer-icon"></a> <a id="source-the-project-settings-quick-menu"></a> <a id="source-the-toolbar-at-the-bottom-of-the-viewer"></a> <a id="source-timeline-resolution"></a>

### Snapping to Guide Lines

By default, when you move the clip inside the frame using the Transform Viewer controls, whenever the image edge nears a Guide line it will snap the image edge to it automatically, turning the Guide line purple to let you know it's exactly placed. If you'd like to switch this behavior off, just hold the option key down while moving the image in the viewer to bypass the snapping.

The Guide lines shift to purple once the image's edge snaps onto that location

### Proxy Handling

You can flip between using your original source media and the proxy media for playback on the Cut page via the Proxy Handling icon in the Viewer, choosing one of the following options: Disable All Proxies: This option turns proxies off entirely and forces original media playback only. Where the original media isn't available, the clip is swapped for a Media Offline graphic. Prefer Proxies: This option uses proxy files for playback, and where there's no proxy file for a clip, the original media gets used automatically instead. Prefer Camera Originals: This option uses the original media files for playback, and where there's no original media file for a clip, the proxy media gets used automatically instead. The Proxy Handling icon in the Cut page Viewer lets you pick how you'd like to use proxy files.

### Timeline Resolution

This drop-down menu, at the top-right of the Viewer, lets you quickly pick which resolution to work at. A Custom option lets you open the Timeline Settings panel to choose your own options. For more about the Timeline Settings, see Chapter 6, "Project Settings."

### The Project Settings quick menu

### Bypass Color Grades and Fusion

With the Bypass Color Grades and Fusion Effects button/drop-down you can turn off every grade and effect applied on the Color page and/or Fusion page, lifting playback performance on low power computers. Click the button (Shift-D) to switch grading and effects off or back on, or right‑click it to reach a menu where you choose which things the button governs.

The Bypass Grades and Fusion button, captured mid right-click to reveal its options

### Playing Clips and Navigating the Timeline in the Viewer

Several controls run along the Viewer's base. They give you various ways to play through and otherwise move around clips and the Timeline. What follows describes the controls left to right.

### The toolbar at the bottom of the Viewer

- Tools button: The Tools button brings up an assortment of controls; among them are transform and crop, audio, speed effects, then camera stabilization plus lens correction, dynamic zoom, and compositing as well, all detailed more fully later in this chapter.
- POI and Add POI: These tools handle selecting and modifying Points of Interest in Replay, which gets its own manual. For further detail on them, consult the "DaVinci Resolve Replay Editor Instruction Manual."
- Fast Review button: Built to help you watch through a big media collection in a hurry, a click on this button kicks off accelerated playback over the Source Tape or the Timeline, the playback speed scaling with how long each clip you're running through is. Lengthy clips race by, while shorter ones run nearer real time. This lets you take in a great deal of material very fast.
- Jog control: Clicking then dragging inside the jog control lets you scrub very precisely across the Viewer's content.
- Transport controls: A cluster of buttons supply clickable control over playback of source clips and the Timeline, whichever one the Viewer happens to show; every button has its own matching keyboard shortcut. Among them are Previous Edit (Up Arrow), then Stop (Spacebar), Play (Spacebar) too, plus Next Edit (Down Arrow), along with Loop Playback (Command /).
- Mark In/Out: Clickable controls for setting In and Out points respectively.
- Playhead timecode: A number field shows the timecode value sitting at the playhead of a clip or of the Timeline, handing you a numeric reference for your position. The Cut page also has its own dedicated timecode entry mode.

DaVinci Resolve can be told you intend a timecode action in three ways, regardless of how the numeric keypad keys are mapped within the Keyboard Customization preferences.

- Select Playback > Goto > Timecode (=) and enter your timecode value.
- Hit the "+" or "-" keys, then type your timecode value to shift the current position

ahead or back by that amount.

- Click the Viewer's Timeline Timecode display, then type your timecode value.
- Skim Playhead: You can skim footage in any viewer across the Media, Cut, Edit, Color, and Deliver pages by holding the C key down and scrubbing the pointer back and forth in the viewer.

### Full Screen Viewer

Up in the Cut page's upper right is a Full Screen Viewer icon; clicking it turns on Full Screen view. Hit Escape to return to your usual view mode.

### The Full Screen Viewer icon

### Enhanced Viewer

On the Cut page the Enhanced Viewer offers an alternative. This larger viewer claims the screen's upper half, with the timeline area left where it is. Pressing Option-F toggles the Enhanced Viewer.

### The Enhanced Viewer in the Cut page

### Scrolling Through the Timeline

The Cut page keeps the playhead fixed. While you play, shuttle, or jog through your program, the Timeline's clips flow past the playhead right to left during forward play, or left to right during backward play. The upshot is that for playback, editing, or trimming, you carry the frame you'd like to see over to the playhead, instead of carrying the playhead over to the frame (the way you do on the Edit page).

To scroll or scrub through the Timeline, do one of the following:

- Have the Viewer display the Timeline, then reach for any transport or playback controls or keyboard shortcuts to shuttle the Timeline's clips back and forth, the playhead flagging the current frame.
- Drop the pointer inside the Upper Timeline's Timeline Ruler, then drag left or right to scrub across your whole program.
- Drop the pointer inside the Timeline Ruler of the larger Timeline Editor underneath, then drag left or right to scrub around the area close to the current frame.
- The navigation tools Playback > Previous / Next > Clip (Up Arrow/Down Arrow) or

Marker (Shift - Up Arrow/Shift - Down Arrow) serve to move around the Cut page Timelines.

TIP: Whenever you have to analyze the video in the Viewer, DaVinci Resolve's complete set of scopes can be reached on the Cut page by selecting Workspace > Video Scopes > On (Shift‑Command-W).
