# Clip mode vs track mode and audio tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: The Fairlight inspector.
[Chapter index](INDEX.md) / [Next section](inspector-speed-change-and-parametric-eq.md)
<a id="source-clip-mode"></a> <a id="source-clip-mode-vs-track-mode"></a> <a id="source-common-controls"></a> <a id="source-dialogue-leveler-controls-in-the-inspector"></a> <a id="source-pan"></a> <a id="source-pan-control-in-the-inspector"></a> <a id="source-pitch"></a> <a id="source-pitch-control-in-the-inspector"></a> <a id="source-speed-change"></a> <a id="source-the-audio-tab"></a> <a id="source-the-fairlight-inspector"></a> <a id="source-the-fairlight-inspector-part-1"></a> <a id="source-voice-isolation-control-in-the-inspector"></a> <a id="source-volume-control-in-the-inspector"></a>

### The Fairlight Inspector

Every clip in the Timeline and Media Pool, plus each audio track or bus, carries settings and properties you can tweak, animate, and edit from the Fairlight Inspector. With it, jobs become straightforward, like aligning the levels or EQ across several clips while keeping the track level free for your full mix, or tuning levels and audio effect parameters on tracks and busses. Keep in mind that clip-based effects are not the same as real-time track and bus effects, since they touch only single clips sitting on the Timeline or in the Media Pool instead of every clip on a track. The pages that follow explain how to operate these controls inside the Fairlight Inspector.

### Clip Mode vs. Track Mode

To clear up any doubt over whether your parameter changes in the Audio tab land on an audio clip or a track, the Inspector carries a Clip Mode and a Track Mode button. (Left) the Clip mode (circled); (Right) the Track mode (circled)

- Pick an audio clip in the Media Pool or on the Timeline and the Clip Mode button lights up, with that clip’s name shown at the top of the Inspector just right of the Track Mode button. Should you pick a Media Pool clip, the words “Media Pool “ precede the clip name up top in the Inspector. Pick a timeline clip and only its name shows.

Up top in the Inspector, the words “Media Pool “ sit ahead of the clip name

- Click the Track Mode button while a Timeline clip is chosen and any edits you then make in the Audio tab go to that clip’s matching Mixer channel, with the clip name up top in the Inspector swapping over to the track name.
- Clicking a track header likewise flips on track mode. Either way, the clip name shown up top in the Inspector becomes the track name.

### Common Controls

Pick an audio clip, an audio track, or a bus channel strip in the Mixer and the Audio and Effects panels reveal a set of shared audio-specific parameters and controls.

Closed and open Inspector group controls in the Fairlight page

Among these controls are:

- Enable button: Sitting to the left of a parameter group’s name, this toggle lets you switch off then back on every parameter in that group together. Orange signals that track is on; gray means off.
- Parameter group title bar: A double-click on any parameter group’s title bar collapses or opens it. Better still, Option-double-clicking one group’s title bar collapses or opens all parameter groups together.
- Keyframe and Next/Previous Keyframe buttons: With this button you place or remove keyframes at the playhead position across every parameter in the group. An orange highlight means a keyframe sits at the playhead’s current spot; dark gray means none does. The left and right arrow buttons hop the playhead between keyframes for more tweaking.
- Reset button: Returns all parameters in that group to their default settings.

TIP: For “granular” moves on the virtual sliders, hold the Option or Shift key as you click into the numerical value field and drag it left or right.

### The Audio Tab

### Clip Mode

While you handle audio clips (Clip mode) on the Audio Timeline or in the Media Pool, the Audio tab supplies the controls and audio effects covered below. NOTE: You cannot edit parameters in the Inspector for audio clips that live on locked tracks.

To read more about locking audio tracks, turn to Chapter 175, “Editing Basics in the Fairlight Page.” Volume The Volume control is what sets the gain of a given clip.

### Volume control in the Inspector

### Pan

Use this control to pan a chosen clip. Although most professional mixes keep panning to the beefier panner in the Fairlight page Mixer, this basic clip-level Pan control helps picture editors in the Edit page whip up simple panning effects to support a craft edit. Drag the slider to pan audio from left to right. By default this control rests centered at 0.

### Pan control in the Inspector

Voice Isolation (Studio Version Only) Switch this control on and Voice Isolation is applied.

### Voice Isolation control in the Inspector

To read more about Voice Isolation, turn to Chapter 181, “Fairlight FX.” Dialogue Leveler Every audio clip on the Timeline or in the Media Pool carries Dialogue Leveler controls for applying that effect to the clip.

### Dialogue Leveler controls in the Inspector

To read more about Dialogue Leveler, turn to Chapter 181, “Fairlight FX.”

### Pitch

With the Pitch control you shift a clip’s pitch while its speed stays put. A pair of sliders adjusts clip pitch in Semi Tones (coarse moves, a twelfth of an octave) and Cents (fine moves, 100th of a semi tone).

### Pitch control in the Inspector

### Speed Change

Use the Speed Change control to alter how fast the clip runs. It offers the choice of letting the clip’s pitch track the new speed change or holding onto the original speed’s pitch.
