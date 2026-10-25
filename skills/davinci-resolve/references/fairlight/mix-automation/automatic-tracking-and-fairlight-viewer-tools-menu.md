# Automatic tracking and Fairlight viewer tools menu

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mix automation.
[Chapter index](INDEX.md) / [Previous section](timeline-audio-keyframe-editing.md) / [Next section](recording-automation-for-multiple-tracks.md)
<a id="source-audio-tracker-object"></a> <a id="source-automatic-tracking"></a> <a id="source-automation-controls"></a> <a id="source-automation-toolbar-options"></a> <a id="source-fairlight-3926"></a> <a id="source-fairlight-viewer-tools-menu"></a> <a id="source-how-to-record-automation"></a> <a id="source-manual-tracker-object"></a> <a id="source-manual-tracking"></a> <a id="source-range-select-tool"></a> <a id="source-recording-mix-automation"></a> <a id="source-tracker-controls"></a> <a id="source-tracker-controls-manual-mode"></a>

### Automatic Tracking

Within Automatic Tracking mode, select a person or object on screen and DaVinci Resolve handles the related movement data over a chosen timeline range by itself, then produces the automation data. To switch on and work with Automatic Tracking: 1 Hit the Toggle Automation button found to the right of the transport controls.

Toggle Automation button 2 Open the Fairlight Viewer tools menu and select Show Tracker Controls.

### Fairlight Viewer Tools menu

The Tracker Controls show up along the lower edge of the Viewer, and an Auto Tracker Object appears on screen.

### Tracker controls

### Audio Tracker Object

You can also pick Show Tracker Coordinates, which gives an alpha-numerical readout of the tracker's current on-screen position.

Audio Tracker Object with Coordinates

3 Pick the target track you want to write panning automation onto, and use the I-Beam tool to mark the Timeline range you want the tracking to operate on.

### Range Select tool

NOTE: Unless a Timeline range is chosen, Auto-tracking won't run. 4 Within the Tracking Controls section, hit the Auto button to engage Auto Tracking. 5 According to whether the panning movement you're automating is horizontal or vertical, hit the Left-Right (L–R) or the Down-Up (D–U) button. TIP: Only while the Auto button is off does the Front-Back (F-B) button appear. 6 Over on the target track, hit the Automation dropdown in the Track Header, followed by Pan > L/R Pan or Pan > U/D Pan so it lines up with what you chose a step earlier. 7 Drag the Auto Tracker Object onto whichever on-screen object or person you mean to track. 8 Hit the Track button so the Auto-Tracking process begins. 9 Kick off playback to verify your audio track; it ought to trail the object or person you set for tracking. TIP: With a trickier track, perhaps a person whose distance from the camera keeps changing or who drifts out of frame, you might need to track in segments. When that happens, mark an area that tracked poorly, drag the tracker object into place, and re-track across the problem range to redo that stretch.

### Manual Tracking

Manual mode has you create keyframes off the Playhead position on the Timeline, with DaVinci Resolve smoothly vectoring between those keyframes exactly as it does for any other automation curve data. To switch on and work with Manual Tracking: 1 Hit the Toggle Automation button found to the right of the transport controls. 2 Choose the target track onto which your panning automation should be written. 3 Open the Video Viewer tools menu and select Show Tracker Controls. Those tracker controls appear along the Viewer's lower edge, with a Tracker Object showing on screen as a plain crosshair.

### Tracker Controls manual mode

### Manual Tracker Object

NOTE: The Tracker object won't show onscreen unless an audio track has been selected. You can also opt to Show Tracker Coordinates.

Manual Tracker Object with Coordinates 4 Confirm the Auto button is switched off within the Tracking controls. That puts you in Manual Tracking mode. 5 Inside the Tracking Controls, hit the panning control of your choice, namely Left-Right (L–R), or alternatively FrontBack (F-B), or Down-Up (D–U). 6 Over on the target track, hit the Automation dropdown in the Track Header, then to mirror your earlier choice pick Pan > L/R Pan, or else Pan > F/B Pan, or Pan > U/D Pan. Should the Automation dropdown be hidden, you can increase the track height. 7 Bring the Playhead to whatever Timeline spot the automation should start at. 8 Lay down a keyframe at the video's current position by Option-clicking the Viewer wherever you'd like the sound sitting at that instant. A corresponding Automation node drops onto the automation line at the Playhead position. 9 For a further keyframe, shift the Playhead elsewhere along your timeline, then Option-click whichever on-screen person or object you're tracking. The Tracker Object leaps to that spot, a keyframe gets written, and a fresh Automation mode joins it at the Playhead position.

DaVinci Resolve vectors smoothly across the keyframes, just as it would with any other automation curve data. 10 Keep laying down keyframes at the spots you want by redoing the prior step. 11 For a "bounding keyframe" that pins a position so the automation line holds before shifting to a new one, Option-Shift-Click on a location. 12 Start playback to verify, and tweak your automation should it need it.

### Recording Mix Automation

Recording mix automation leans on plenty of the same techniques as drawing, only here you capture a performance by moving whichever controls need automating. It can prove flexible and creative as you "perform to picture" to land the outcome you want. As a first step, confirm Automation recording is switched on (refer to "Enabling and Viewing Automation" above), with one or more parameters set up for automation recording.

Clicking the Automation Controls button displays the Automation toolbar

### Automation Controls

Positioned to the right of the transport controls, the Automation Controls button lets you show and hide the Automation toolbar. The Automation toolbar carries buttons for each option available when you're getting ready to record automation in your mix.

### Automation toolbar options

The Automation toolbar shows the following options:

- Automation Modes: Governs how automation data gets recorded. Write: Records absolute changes to a control's position, overwriting whatever data sat there before. Trim: Records relative changes to a control's position, keeping the relative existing levels built up over time while raising or lowering those levels overall. This can be very useful when you're incrementally refining a mix.
- Touch Modes: Sets what occurs when an automatable control is moved during a mix. Off: No automation gets recorded. Latch: Automation begins recording once a control is moved and keeps recording after the control is released until the transport stops. Snap: Automation begins recording once a control is moved and then glides smoothly back to the prior level at the point of release, producing a seamless transition.

Where the glide transition finishes, automation is no longer recorded unless the control is moved once more while the transport plays. You can keep capturing further automation with Snap until the transport stops. You set the glide transition's duration, in milliseconds, under Preferences > User > Fairlight > Automation. Its default sits at 250 ms. Snap Latch: A blend of Snap and Latch modes, in which faders work in Snap while every other control works in Latch. This proves useful when you want dynamically changing fader levels through a mix pass while other controls "stick" when they're moved. It's particularly useful with Fairlight mix control surfaces, where faders and rotary controls can be altered at the same moment during a mix pass.

### FAIRLIGHT 3926

- On Stop: Determines what happens once you press Stop at an automation pass's end. Event: The most recent recorded automation value overwrites the earlier levels right up to where the next available recorded automation data (or event) begins on that track. Hold: Erases every previously recorded mixing entry following what you just laid down, so the last recorded level carries through the rest of that track. Return: That last recorded automation value gets interpolated, ramping back toward the track's previously recorded automation values.
- Enables: The buttons here let you toggle on or off the various controls you record automation for. Fader: covers track and bus volume. Mute: drives the mute button. Pan: handles all pan controls. EQ: takes in all EQ controls. Comp: targets only the Compressor controls inside the Dynamics window. Gate: targets only the Gate controls inside the Dynamics window. Lim: targets only the Limiter controls inside the Dynamics window. Sends: governs the Send controls over in the Sends window. Plugins: spans all Fairlight, VST, or Audio Unit (AU) plugins. Misc: reaches the Buss on/off, Insert, and Direct Out controls. Should a project be running the Fairlight legacy Fixed Bus configuration, automation of the fixed bus Main and Sub bus enables becomes available too.

### How to Record Automation

Two distinct approaches exist for setting up automation recording across levels, panning, EQ, Dynamics, and the other audio controls within the mixer.
