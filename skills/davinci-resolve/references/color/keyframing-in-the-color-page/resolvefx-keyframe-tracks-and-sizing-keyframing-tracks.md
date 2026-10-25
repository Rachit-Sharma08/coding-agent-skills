# Resolvefx keyframe tracks and sizing keyframing tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing in the color page.
[Chapter index](INDEX.md) / [Previous section](dynamic-keyframes-dynamics-and-static-keyframes-marks.md) / [Next section](deleting-keyframes-and-copying-keyframes.md)
<a id="source-auto-keyframing-selected-for-circular-window-on-node-1"></a> <a id="source-automatic-keyframing"></a> <a id="source-changing-dynamic-attributes"></a> <a id="source-changing-keyframe-values"></a> <a id="source-modifying-keyframes"></a> <a id="source-moving-keyframes"></a> <a id="source-navigating-among-keyframes"></a> <a id="source-resolvefx-keyframe-tracks"></a> <a id="source-the-ext-matte-nodes-freeform-isolation-track"></a> <a id="source-the-sizing-keyframing-tracks"></a>

### ResolveFX Keyframe Tracks

Within the Color page, the Color Page Keyframe Editor can display and edit keyframes for ResolveFX and OpenFX plugins in either of two ways:

- Plugins dropped onto a Corrector node turn up inside the nested list of keyframe tracks living under that node's top-level keyframe track.

The keyframe track belonging to a Resolve FX plugin placed on a Corrector node

- Plugins dropped in as standalone nodes turn up inside a fresh FX track of the Keyframe Editor. Every plugin added as its own separate node carries a separate FX track.

The keyframe track belonging to a Resolve FX plugin set up as a standalone node

### The Sizing Keyframing Tracks

Separately from the color controls, the Sizing keyframing tracks handle sizing transforms along with stereoscopic adjustments.

- Input Sizing: Controls the Input Sizing parameters found within the Sizing palette.
- Convergence: Controls the Convergence parameter in the Stereo 3D palette.
- Float Window: Governs the Floating Windows parameters for Left, Right, Top, and Bottom Position/Rotate/Softness.

- Auto Align: Governs, within the Stereo 3D palette, the Pitch and Yaw parameters.

TIP: Keyframing Output Sizing is possible only once you select Timeline mode over in the Node Editor.

### The Ext Matte Node's Freeform Isolation Track

When your node tree holds an External Matte, the EXT MATTE node surfaces a Freeform Isolation track inside the Keyframe Editor. That comes in handy for time offsets or for Sizing repositioning applied to the Ext Matte image.

### Automatic Keyframing

An Auto-Keyframing button sits on every track in the Keyframe Editor, switchable on or off. With auto-keyframing turned on for a given track, each tweak made to a parameter or control belonging to that keyframe track spawns a keyframe on its own. You can put this to work in two ways:

- Paired with a keyframing track, auto-keyframing makes setting up animated changes to particular adjustments inside a node a breeze. That beats dropping keyframes one at a time by hand.
- Alternatively, switching on auto-keyframing for the Corrector track turns it on across every keyframing track that node owns. In that scenario, keyframes drop automatically onto whichever keyframing track matches the parameters or controls you tweak.

### Auto-keyframing selected for Circular window on Node 1

While auto-keyframing is off, the tweaks you make revise existing keyframes instead. How that revision plays out hinges on where the playhead sits and on the keyframe types present in the Keyframe Editor. The next section covers more.

### Modifying Keyframes

After you begin laying down keyframes to animate a grade's changes, plenty of approaches exist for navigating and editing those keyframes to refine the effects further. This section walks through the various ways to move among, change, and delete keyframes.

### Navigating Among Keyframes

Many actions require parking the playhead squarely over the keyframe you mean to modify. You can always rely on the transport controls or the pointer to shift the playhead, but commands also exist for leaping straight to a particular keyframe. To move the playhead among a series of keyframes:

- Choose Playback > Next > Keyframe, bound to the right bracket key, or its counterpart Playback > Previous > Keyframe on the left bracket key.

### Moving Keyframes

When the timing of a keyframe run needs adjusting, you can relocate any keyframe and carry whatever values it holds along with it. To move a single keyframe using the onscreen interface:

- Drag any keyframe to a different spot with the pointer.
- Drag keyframes on a top-level Corrector or Sizing track to shift, all at once, every other keyframe sharing that frame within that corrector.

To move multiple keyframes at the same time: 1 If needed, open the keyframe track holding the keyframes you intend to move. 2 Draw a bounding box around the keyframes you want to move. The selected keyframes turn red to show they're chosen. 3 Drag any of the selected keyframes to slide them leftward or rightward.

### Changing Keyframe Values

Unlike a lot of other software, DaVinci Resolve permits altering keyframe values even while the playhead isn't sitting right on an existing keyframe. The behavior depends on where the playhead is relative to the keyframes present in the Keyframe Editor, and on which keyframe type you're working with.

- When the playhead sits left of, or right on, the first Dynamic keyframe: whichever Dynamic keyframe lies at or rightward of the playhead picks up the newly adjusted values.
- When the playhead sits left of, or right on, the last Dynamic keyframe: whichever Dynamic keyframe lies at or leftward of the playhead picks up the newly adjusted values.
- When the playhead falls between a pair of Dynamic keyframes: the Dynamic keyframe leftward of it absorbs the new values, leaving the one rightward unaffected.
- When the playhead falls between a pair of Static keyframes (marks): any tweak made there always lands on the keyframe leftward of the playhead. Everything from that keyframe up to the following one shifts together.

### Changing Dynamic Attributes

Out of the box, the move from one Dynamic keyframe to the next runs linear. Should you need to reshape how value interpolation speeds up between one Dynamic keyframe and the one after it, though, the dynamic attributes of that keyframe can be edited. Here's how to edit them: 1 In the Keyframe Editor, select a keyframe by clicking it. 2 Right-click the keyframe you selected, then choose Change Dynamic Attributes. 3 Once the Dynamic Attributes window opens, take either or both of these actions:

- Set a fresh outgoing acceleration curve via the Start slider, which shapes the interpolation happening on that keyframe's right.
- Set a fresh incoming acceleration curve via the End slider, which shapes the interpolation happening on that keyframe's left.

As you try out different acceleration curves, the display on the right updates with the resulting curve graph.

Changing the dissolve profile 4 Once the curve satisfies you, click OK. Mixing varied Start and End values lets you make animated adjustments "ease in" or "ease out" around a given keyframe, producing a softer or sharper transition. TIP: Each new keyframe's default dynamic profile start and end are configurable using the Dynamics Profile values, found under Project Settings within the General Options panel.
