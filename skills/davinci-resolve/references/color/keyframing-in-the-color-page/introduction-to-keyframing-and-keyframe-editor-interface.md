# Introduction to keyframing and keyframe editor interface

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing in the color page.
[Chapter index](INDEX.md) / [Next section](dynamic-keyframes-dynamics-and-static-keyframes-marks.md)
<a id="source-allcolorsizing"></a> <a id="source-introduction-to-keyframing"></a> <a id="source-keyframing-in-the-color-page"></a> <a id="source-keyframing-in-the-color-page-part-1"></a> <a id="source-keyframing-methods"></a> <a id="source-the-keyframe-editor-interface"></a> <a id="source-the-keyframe-track-header"></a>

### Keyframing in the Color Page

A purpose-built Keyframe Editor lives on the Color page, sitting to the right of the palette area, and it lets you drive grading adjustments across frames over time. Since color work is a distinctly different job from cutting, this Keyframe Editor on the Color page behaves a bit unlike the Curve Editor you find over in the Edit page.

### Introduction to Keyframing

Call it keyframing, dynamics, or marks if you like; DaVinci Resolve gives you a way to smoothly interpolate color adjustment parameters through several methods, moving from one setting toward another. Say a clip drifts in exposure, for instance: you might roll a sequence of contrast tweaks with Dynamic keyframes so those exposure shifts feel less jarring.

The Keyframe Editor with dynamic keyframes animating the parameters of Node 2 Here's a second scenario: you're cutting a documentary, and one archival clip dropped into the middle of the Timeline is really six separate shots pulled from an eighties broadcast. Pressed for time, you can drop Static keyframes (marks) right at each shot's cut point, producing immediate single-frame jumps between the different tweaks applied to that clip's grade, so each shot inside the one clip gets its own treatment.

Round static keyframes dropped onto every parameter, letting shots that were combined into one clip each be tuned on their own Either way, the Keyframe Editor is where you build a run of keyframes that shift parameters from one value across to another. The pages ahead walk you through using the Keyframe Editor to construct these animated adjustments.

### The Keyframe Editor Interface

Every control you need to build and tweak keyframes for whichever clip is selected lives in the Keyframe Editor. When you want more room on a single-screen layout, just click its expand button (located at the top right of the Keyframe Editor) to widen it. With a pair of displays attached, the Color page's Dual Screen layout will park the Keyframe Editor on the second monitor and let it span that screen's full width, giving you a lot more workspace.

The Node Editor displayed wide, shoving every other palette over toward the left These are the pieces that make up the Keyframe Editor:

- Timeline Ruler: Reflects the record timecode of whichever clip is currently selected; drag inside the Timeline Ruler to reposition the playhead, while a timecode readout on the left reports the current frame.
- Keyframe track header: Every node in the active grade gets a matching keyframe track, Sizing carries its own keyframe track too, and the keyframing controls you'll manage are housed in the track header.

### The Keyframe track header

- Enable/Disable button: Toggling this round white button turns that track's matching node on or off.
- Lock button: Stops anything on that track's matching node from being altered. A lock icon marks any node you've locked. Locking and unlocking is also possible by right-clicking a node over in the Node Editor and picking Lock Node from the contextual menu.

Within the Color page's Keyframe Editor, Nodes 1 and 2 sit locked.

- Auto-Keyframe button: Flip this on so a Dynamic keyframe is generated automatically each time you tweak any parameter inside that node.
- Track disclosure triangle: Reveals separately keyframable parameter groups sitting below the primary keyframe track.
- Keyframe tracks: Sitting to the right of the track header, this is the area where keyframes that drive parameter changes get built and edited. At the very top, a "master keyframe track" surfaces every keyframe placed on any keyframe track in the Keyframe Editor, including ones on a keyframing track tucked away inside a track whose disclosure triangle is closed.
- Keyframes: A Dynamic keyframe shows up as a tiny diamond, whereas a Static keyframe shows up as a circle. Dissolves go with Dynamic keyframes, while Static keyframes (marks) take effect at once. Each grade ties back to the keyframe before it, possibly a default placed on the master clip's first frame. Click a keyframe to select it, or drag it elsewhere along the keyframe track to reposition.
- FX track: When Resolve FX or OFX plugins land in a grade as their own standalone node, they receive a dedicated track for building animated effects. That track's every parameter is keyframed through one combined keyframe track. Stack several plugins as separate nodes and each gets its own FX track.
- Sizing track: A wholly separate track exists for the Pan, Tilt, Zoom, Rotate, and Convergence (in Stereo 3D projects) parameter, meant for animating pan-and-scan moves.
- Track selection drop-down: A tinted bar marks the keyframing scope in effect right now: every track together, only the active correction node, or just the Sizing settings, governed by the Keyframe Timeline mode covered in the section that follows.

Normally the Keyframe Editor occupies the bottom-right third of the Color page. You can still stretch it out for more working room whenever a scene demands intricate keyframing. So, to grow or shrink the Keyframe Editor:

- Click the Expand/Collapse button up in the top right corner of the Keyframe Editor. The Keyframe Editor expands or contracts to match.

To zoom into and out of the keyframe tracks:

- Drag the Zoom slider to scale the Keyframe Editor in or out.
- Right-click on a keyframe track and pick Maximum Zoom to zoom in completely.
- Right-click on a keyframe track and pick Reset Zoom so the whole clip fits across the Keyframe Editor's available width.

### All/Color/Sizing

Arguably the single biggest keyframing control, the Keyframe Timeline mode changes which tracks receive keyframes when you trigger the Start Dynamic or Add Static Keyframe commands, whether off the keyboard or through your control panel's buttons. The command cycles through three modes:

- All: This is the default. It drops keyframes onto every track in the Keyframe Editor, keyframing all parameters across all nodes simultaneously, Sizing settings included. An orange bar shows up here, calling out the uppermost "master keyframe track."
- Color: Keyframes land only on whichever node is active in the Node Editor. A green bar appears here, marking the keyframe track that belongs to the currently selected node.
- Sizing: Keyframes go only to the Sizing track, which comes in handy while you keyframe "pan and scan" style transforms. A blue bar appears here, calling out the Sizing track.
- EXT MATTE: Shows up solely when an external matte node sits in the node tree. It lets you keyframe parameters specific to the external matte over in the Key palette.

While All is what's set by default, switching over to the Color or Sizing keyframing modes can pay off by sparing you a pile of pointless keyframes. Keyframing it all in one shot may be quick, yet those surplus keyframes can drag on you later, once you have to revisit nodes that never warranted keyframing to begin with. So, to swap the keyframing mode, take one of these routes:

- Select something from the Keyframe mode drop-down located up at the Keyframe Editor's top right.
- Select something from the Mark > Keyframe Timeline mode submenu.

TIP: This control serves a second purpose. The mode you pick also governs what gets carried over when you reach for the assorted grade management tools inside DaVinci Resolve. Choose Color, say, and a clip's color grade copies without its sizing tagging along. Choose Sizing, and the sizing copies free of the color grade.

For more information, refrer to "Copying Grades" see Chapter 142, "Grade Management."

### Keyframing Methods

DaVinci Resolve relies on two distinct keyframe types to produce automated changes. The way each type interpolates parameters is different.
