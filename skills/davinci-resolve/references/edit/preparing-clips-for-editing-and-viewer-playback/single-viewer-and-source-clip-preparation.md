# Single viewer mode and opening clips into the source viewer to prepare for editing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preparing clips for editing and viewer playback.
[Chapter index](INDEX.md) / [Previous section](media-pool-browsing-and-selection.md) / [Next section](special-playback-viewer-guides-and-snapping.md)
<a id="source-j-k-l-press-j-repeatedly"></a> <a id="source-opening-clips-into-the-source-viewer-to-prepare-for-editing"></a> <a id="source-plays-100-backward"></a> <a id="source-plays-100-forward"></a> <a id="source-press-and-hold-kl"></a> <a id="source-press-l-repeatedly"></a> <a id="source-shift-j-shift-l-shift-k-press-and-hold-kj"></a> <a id="source-simple-keyboard-shortcuts-for-playback-and-navigation"></a> <a id="source-single-viewer-mode"></a> <a id="source-stops-playback"></a> <a id="source-using-jkl-to-control-playback"></a> <a id="source-viewer-transport-controls"></a>

### Single Viewer mode

While Single Viewer mode is on, your current pick in the Media Pool or Timeline drives which controls show up in the Viewer, so you can accomplish nearly all the same tasks you would with both viewers open at once.

### Opening Clips Into the Source Viewer to Prepare for Editing

After settling on which clips belong in your program, send them to the Source Viewer for a fuller look. The behavior here hinges on the Source Viewer’s Live Media Preview setting. To skim a Media Pool metadata or thumbnail and watch clips in the Source Viewer via Live Media Preview: 1 Switch on Live Media Preview (if it isn’t already) from the Source Viewer option menu by choosing Live Media Preview. 2 With the Media Pool showing in Metadata or Thumbnail mode, hover the pointer over a clip; after a brief pause its thumbnail begins to skim, and the portion you’re scrubbing shows up in the Source Viewer. Then do one of these: a) While you skim inside the thumbnail, the playhead in the thumbnail stays tied to the one on the Viewer’s jog bar, and as you skim you can drop markers and set In and Out points b) Keeping the pointer parked over that clip, drive the JKL keyboard shortcuts to play it through, adding markers and setting In and Out points however you wish 3 Because skimming waits a beat to kick in, you can dart the pointer off that clip and back to the Source Viewer without triggering any other clip. Switching Live Media Preview off returns you to the more deliberate, conventional ways of loading clips into the Source Viewer.

To send a clip to the Source Viewer with the mouse: Double-click any clip in the Media Pool, or one in its Filmstrip, and it opens into the Source Viewer. To bring the bin’s previous or next clip into the Source Viewer: 1 Click within the Source Viewer so it holds focus. 2 Tap the Up Arrow key to step back to the prior clip in the bin that’s open and load it into the Source Viewer. 3 Tap the Down Arrow key to advance to the following clip in that same bin and load it into the Source Viewer. To send a clip to the Source Viewer with the keyboard: 1 If needed, press Command-1 to land on the Bin list, then use the Up and Down arrows to pick a folder and reveal its contents. The Right Arrow key opens folders and exposes any nested ones within, while the Left Arrow key collapses folders and hides what they nest. 2 Press Command-2 to jump to the Media Pool browser, and shift the highlight from clip to clip across the Media Pool — up, down, left, and right — with the Arrow keys. 3 With your target clip highlighted, press Return to open it into the Source Viewer. To send a timeline to the Source Viewer: Drag a timeline and drop it onto the Source Viewer, ready either to gang it against the existing Timeline or to cut it, whole or partway using In and Out points, into the Timeline currently open. Monitoring with an External Video Display As you work on the Edit page, what shows on a connected external video display is governed either by the present Media Pool selection or by which portion of the Edit page interface holds focus. For instance, selecting a clip in the Media Pool so it appears in the Filmstrip sends that clip out to video. Opening it next into the Source Viewer routes the Source Viewer’s contents to video instead. Switch over to the Timeline Viewer and your timeline becomes the video output.

### Viewer Transport Controls

Two Viewers sit on the Edit page. While cutting, the Viewer on the left should be set to source video or source audio so it presents the source clip for whatever edit you’re building. On the right sits the Timeline Viewer, displaying the frame under the playhead’s current Timeline position. Between the Source and Timeline Viewers, you can assemble a broad range of edits. Transport controls run beneath each Viewer.

The transport controls at the bottom of the Source Viewer

Sitting right below the transport controls is a jog bar that lets you drag the playhead by hand with the pointer. The entire span of the Source Viewer’s jog bar maps to a clip’s whole length, whereas the entire span of the Timeline Viewer’s jog bar maps to the whole length of the current timeline. Each playhead’s present spot is reported in the timecode field tucked into the upper right-hand corner of its viewer. Off to the left of the other transport controls, a standalone jog control (&lt;o&gt;) offers a slower way to creep through lengthy clips or a long timeline. Dragging it left and right steps through a clip or the Timeline one frame per move. Below the jog bar you’ll find the transport controls. Within the Source Viewer they cover Jump to the First Frame, then Play Reverse, Stop, and Play Forward, plus Jump to the Last Frame. Within the Timeline Viewer the lineup shifts to move to the Previous Edit, then Play Reverse, Stop, and Play Forward, plus move to the Next Edit. Looping during playback is handled by a loop control.

### Simple Keyboard Shortcuts for Playback and Navigation

A whole assortment of keyboard shortcuts exists just for moving around clips and timelines and steering playback.

- Spacebar: The Spacebar both kicks off and halts playback.
- Skim Playhead: Footage can be skimmed in any viewer across the Media, Cut, Edit, Color, and Deliver

pages by keeping the C key down and dragging the pointer to and fro inside the viewer.

- Play Again: Hitting Option-L restarts playback at once from the playhead’s starting point without

a stop, handy when you want to quickly hear the opening of whatever you’re reviewing again.

- Step One Frame Forward/Step One Frame Back: A press of the Left Arrow or Right Arrow nudges the

playhead a single frame either direction, while Shift-Left Arrow and Shift-Right Arrow jump it in one-second steps.

- Step One Second Forward/Step One Second Reverse: A press of Shift-Left Arrow or Shift-Right Arrow moves the playhead one second backward or forward.
- Next Edit/Previous Edit: Up Arrow drops the playhead on the previous edit and selects that edit point, whereas Down Arrow drops it on the next edit and selects that edit point.
- First Frame/Last Frame of the Current Clip: The Semicolon key sends the playhead to the opening frame of whichever clip it crosses, while the Apostrophe key sends it to that clip’s closing frame.
- Previous Keyframe/Next Keyframe: When keyframes are shown in the Timeline, Shift-Semicolon hops the playhead to the prior keyframe on the left, and Shift-Apostrophe hops it to the next keyframe over on the right.
- Previous Marker/Next Marker: Where markers exist in the Timeline Ruler or inside Timeline clips, Shift-Up Arrow and Shift-Down Arrow carry the playhead left and right between consecutive markers.
- Previous Gap/Next Gap: When Timeline tracks with Auto Select enabled hold gaps between clips, Option-Command-Semicolon and Option-Command-Apostrophe walk the playhead left and right from gap to gap.
- Timeline Start/Timeline End: The Home key parks the playhead on the opening frame within the Source or Timeline Viewer, while the End key sends it to that viewer’s closing frame instead. Go to
- In Point/Go to Out Point: Shift-I jumps the playhead to the In point marked in either the Viewer or the Timeline. Shift-O jumps it to the Out point.

TIP: Within the Editing panel of the User Preferences window, the “Always highlight current clip in the media pool” option controls whether your current Timeline selection is echoed back in the Media Pool.

### Using JKL to Control Playback

Shared across countless editing programs, the JKL keyboard shortcuts rank among the handiest playback and editing controls seasoned editors rely on. What follows lays out the many ways these three keys let you run through clips and timelines while you work.

### J K L Press J repeatedly

### Press L repeatedly

### Shift-J Shift-L Shift-K Press and hold K+J

### Press and hold K+L

Holding K as you tap J Holding K as you tap L Command-J alongside Command-L

### Plays 100% backward

### Stops playback

### Plays 100% forward

Each additional press of J ramps the reverse speed up, giving you a spread of fast-reverse rates Each additional press of L ramps the forward speed up, giving you a spread of fast-forward rates Runs fast in reverse Runs forward at speed Play Slow at 1/2, 1/4 or 1/8 speeds Reverses in slow motion (audio plays back in slow motion too) Runs forward in slow motion (audio is pitch-corrected on macOS) Steps the playhead back by one frame Steps the playhead ahead by one frame Keeping Command held as you work the J and L shortcuts lets you dynamically stretch or trim the chosen edit points or clips at 100 percent speed or quicker, governed by whether the Selection or Trim tool is active. To learn more about dynamic trimming, consult Chapter 44, “Trimming.”

Whenever the JKL commands drive playback above or below real-time speed, a speed indicator shows up just right of the Viewer’s frames-per-second readout.

Above the Viewer, a speed indicator reports playback running at 4x speed Once all the various JKL playback techniques become second nature, they’ll likely turn into one of your primary means of driving the playhead around in DaVinci Resolve.
