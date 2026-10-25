# Audio keyframes on the timeline and adding and deleting individual keyframes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mix automation.
[Chapter index](INDEX.md) / [Previous section](creating-mix-automation-and-why-use-track-automation.md) / [Next section](automatic-tracking-and-fairlight-viewer-tools-menu.md)
<a id="source-adding-and-deleting-individual-keyframes"></a> <a id="source-adjusting-a-selected-range"></a> <a id="source-adjusting-the-automation-line"></a> <a id="source-adjusting-the-entire-line"></a> <a id="source-audio-panning-to-video-1"></a> <a id="source-automating-switched-controls"></a> <a id="source-before-and-after-cut-or-deletion"></a> <a id="source-drawing-automation-with-the-pencil-tool"></a> <a id="source-editing-mix-automation-curves"></a> <a id="source-mute-automation-showing-on-and-off-states"></a> <a id="source-select-all-automation-to-adjust-the-entire-line"></a> <a id="source-trimming-a-selected-range-of-the-automation-curve"></a> <a id="source-trimming-automation-from-unity-in-the-mixer"></a> <a id="source-using-edit-operations"></a> <a id="source-working-with-audio-keyframes-on-the-timeline"></a>

### Working with Audio Keyframes on the Timeline

To draw automated changes to any audio control:

- Turn on the Automation button to display Automation View across all audio tracks.
- On the track(s) where automation should be created, choose, within the Automation type dropdown menu in the track header, the parameter you'd like to automate.
- Focus Mode's Multi tool lets you draw automation via the up/down arrow cursor (for shaping a broad curve), insert or delete keyframes individually using modifier keys, generate varied curves according to where each keyframe sits, mark and remove a span of keyframes, and beyond.

### Adding and Deleting Individual Keyframes

Handling keyframes on the automation line is almost the same as working with clip gain.

- To add a keyframe: Hold the option key and a plus sign appears. Click to drop a keyframe onto the automation line.
- To remove a keyframe: Hold Command-option and a minus sign appears. Click on the keyframe to delete it.

For more information see Chapter 176, "The Fairlight Inspector."

TIP: You can rapidly switch between Clips View and Automation View with the keyboard shortcut F4. This can be reassigned via the DaVinci Resolve > Keyboard Customization dialog.

### Editing Mix Automation Curves

### Using Edit Operations

The usual editing operations—cut, copy, paste, delete, and nudge—all work on automation keyframe data. When automation data gets cut or deleted, the value at each end of the selection is held. Nudging proves quite handy for fine-tuning where automation events sit.

### Before and after cut or deletion

### Adjusting the Automation Line

Once one or more keyframes sit on the automation line, the resulting curve for the whole track can be adjusted. Individual keyframes can be moved up or down using the same techniques as adjusting clip gain; the entire line can be adjusted, or just a selection can be affected. Adjust the last keyframe on a line carrying multiple keyframe points and the line will shift from that point onward to the level you newly set.

Adjusting an individual keyframe changes the line from that point onwards.

### Adjusting the Entire Line

To adjust the entire line:

- With automation view on, click anywhere inside the track, and select every bit of automation data on the curve by choosing Command-A.
- Bring the cursor near the line and the dual arrow cursor appears, letting the level of the whole line be adjusted.

### Select all automation to adjust the entire line

### Adjusting a Selected Range

Adjustments can be confined to only a specific portion of the automation curve. This is useful for those times you'd like to apply "snapshot" changes to one particular scene. To adjust only a selected range:

- Use the Focus Mode Select tool (I-beam cursor) to mark the range you want to affect.
- Bring the mouse near any part of the line, and the up/down arrow cursor appears.
- Trim the line up or down. A tooltip surfaces showing the current value plus a delta from the original value, so any change in a control's value is visible.
- At the edges of the selection, "bounding keyframes" get created automatically, so the level at the selection's border is held.

### Trimming a selected range of the automation curve

TIP: Hold the Shift key while adjusting levels to keep precision. When you're adjusting fader levels this gives .1 dB accuracy, even while working with small track heights.

### Drawing Automation with the Pencil Tool

Automation keyframes can be drawn freely with the Pencil tool:

- Pick the Pencil tool in the Automation toolbar, or while in Focus mode, hold Option-Shift to switch over to the Pencil tool temporarily.
- Click the mouse and drag to draw keyframes in either direction.

### Automating Switched Controls

Some automation parameters are switched (that is, they hold only fixed states). Mutes (on or off) are an example of this control type. When you're adjusting switched automation, keyframes can only sit at the bottom end of the Automation view or the top.

### Mute automation showing on and off states

### Trimming Automation from Unity in the Mixer

In the Fairlight mixer, Trim mode lets you trim automation from unity (Fader at 0) by working through the steps that follow: 1 Within the Automation toolbar, switch the Automation mode over to Trim. The Automation toolbar - Trim mode 2 Choose one Touch mode out of Latch, Snap, or Snap Latch. 3 Hit the Automation Arm button on whatever mixer channel or tracks need trimming. On the armed mixer channels the faders go yellow and snap down to zero, while the dB Indicator sitting above each armed fader reads Δ0.0dB. TIP: Either Command-Option click the Automation Arm button to trim automation across every track, or Option-click that button to trim automation for whichever set of tracks or mixer channels you've highlighted. Mixer faders set to trim utomation from unity 4 Start playback and shift the fader above or beneath Δ0.0dB. That trims the automation curve, with the dB indicator displaying the trim figure as a plus or minus (+/-) value. Where you've chosen Snap mode, the fader heads back to Δ0.0dB according to the Glide time set in Preference > User > Fairlight > Automation.

### Audio Panning to Video

Audio Panning to Video taps DaVinci Resolve's cutting-edge object-tracking engine to help you rapidly produce precision panning automation from how people and objects move in the Fairlight Viewer. Audio Panning to Video provides Automatic and Manual modes of operation.
