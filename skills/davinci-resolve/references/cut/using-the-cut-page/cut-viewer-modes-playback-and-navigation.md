# Viewer modes buttons and playing clips and navigating the timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the cut page.
[Chapter index](INDEX.md) / [Previous section](cut-page-interface-overview.md) / [Next section](audio-meter-showing-an-audio-signal-and-timeline.md)
<a id="source-audio-meter"></a> <a id="source-bypass-color-grades-and-fusion"></a> <a id="source-export-the-current-frame-from-the-viewer"></a> <a id="source-optimized-ui-layouts-for-vertical-editing"></a> <a id="source-playing-clips-and-navigating-the-timeline"></a> <a id="source-the-toolbar-at-the-bottom-of-the-viewer"></a> <a id="source-the-viewer-modes-buttons"></a> <a id="source-tools"></a>

### The Viewer modes buttons

Various actions enter the Different options automatically (left to right):

- Double-clicking any clip opens it into the Viewer as a Source Clip.
- A whole bin's worth of clips can be viewed via the Source Tape.
- Your edited program plays back in the Timeline.
- Every bit of your synced material shows together at once in the Multi Source viewer.

### Playing Clips and Navigating the Timeline

A handful of controls live along the bottom of the Viewer. With them you play through and otherwise move around clips and the Timeline in different ways. They're covered here from left to right.

### The toolbar at the bottom of the Viewer

- Tools button: Clicking the Tools button surfaces an assortment of controls: transform and crop, audio, speed effects, plus camera stabilization with lens correction, on top of dynamic zoom and compositing, each given fuller treatment later on.
- Voiceover: Reveals controls for recording voice over directly into the timeline.
- POI and Add POI: With these tools you select and adjust Points of Interest within Replay,

which has a manual of its own. For more on these tools, consult the "DaVinci Resolve Replay Editor Instruction Manual."

- Fast Review button: Made to help you get through a big pile of media in a hurry, clicking this button kicks off sped-up playback across the Source Tape or the Timeline, with the playback speed tied to how long each clip is. Long clips race by, while shorter ones play nearer to real time. That way you can take in a great deal of material very fast.
- Jog control: Click and drag inside the jog control to scrub through the Viewer's content with great precision.
- Transport controls: Clickable controls for driving playback of clips and the Timeline are formed by a bank of buttons: Previous Edit (Up Arrow) and Stop (Spacebar), then Play (Spacebar), followed by Next Edit (Down Arrow), with Loop Playback (Command-/) rounding it out. Each button has a keyboard shortcut to match.
- Mark In/Out: Clickable controls to set In and Out points respectively.
- Playhead timecode: A number field displays the timecode value at the playhead of a clip or the Timeline, giving you a numeric read on where you are.
- Skim Playhead: Footage can be skimmed in any viewer across the Media, Cut, Edit, Color, and Deliver pages by holding the C key and dragging the pointer back and forth within the viewer.

### Optimized UI Layouts for Vertical Editing

DaVinci Resolve supports optimized layouts for vertical timelines and projects. Load a vertical timeline or project and the UI shifts on its own to a layout tuned for vertical viewers across the Cut, Edit, and Color pages. Load a regular landscape timeline or project afterward and it flips back to the original layout automatically. Nothing further is required of you. This behavior is adjustable under Preferences > User > UI Settings > Use optimized UI layouts for vertical video. Clear that box to hold onto the normal horizontal layout even for vertical video timelines.

The UI now changes format to accommodate vertical video timelines automatically.

### Tools

Click the Tools button and out comes a toolbar for adding and editing clip effects right inside the Viewer, no Inspector needed. That toolbar puts forward an assortment of controls: transform plus crop, audio, speed effects, alongside camera stabilization with lens correction, and finally dynamic zoom plus compositing, all detailed further on. The Tools bar shown opened to the transform controls.

### Bypass Color Grades and Fusion

The Bypass Color Grades and Fusion Effects button/drop-down lets you switch off every grade and effect you may have laid down in the Color page and/or Fusion page so that playback runs better on low-power computers. Click the button (Shift-D) to turn grading and effects off or back on, or right-click it to reach a menu where you choose which things the button governs.

The Bypass Grades and Fusion button as it's right-clicked to surface its options

### Export The Current Frame from The Viewer

A still frame can now be exported from the Viewer across the Media, Cut, and Edit pages.

To Export a Still Frame from the Viewer: 1 With the Viewer's playback controls, navigate to whichever frame you'd like exported. 2 Pick File > Export > Current Frame as Still. 3 Within the File System viewer, type a name for the still frame. 4 Within the File System viewer, set the still frame's format. 5 Click the Export button.

### Audio Meter

Off to the right of the Viewer, an audio meter gives you a visual picture of the audio levels playing in the current clip or on the Timeline as you play through the Viewer, by way of animated vertical bars colored to show how loud things are:

- Green marks levels that are safe
- Yellow marks levels peaking right around the safe mark
- Red marks levels possibly peaking higher than they should,

at the risk of clipping the signal and bringing on distortion These animated bars act as a visual cue you can lean on to balance the volume of different clips pleasingly, and to keep from going past the loudest level you want and introducing clipping. Up top of the meters sits a speaker button for muting or unmuting audio playback.
