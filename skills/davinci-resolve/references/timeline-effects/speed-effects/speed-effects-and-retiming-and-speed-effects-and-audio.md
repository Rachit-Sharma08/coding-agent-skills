# Speed effects and retiming and speed effects and audio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Speed effects.
[Chapter index](INDEX.md) / [Next section](timeline-speed-controls-and-whole-clip-retiming.md)
<a id="source-clip-retiming-controls"></a> <a id="source-creating-freeze-frames"></a> <a id="source-creating-simple-linear-speed-effects"></a> <a id="source-speed-change-controls-in-the-video-inspector"></a> <a id="source-speed-effect-parameters-shown-in-the-speed-dialog"></a> <a id="source-speed-effects"></a> <a id="source-speed-effects-1"></a> <a id="source-speed-effects-and-audio"></a> <a id="source-speed-effects-and-retiming"></a> <a id="source-the-speed-change-controls-in-the-video-inspector"></a>

### Speed Effects

Whether you bring in linear and nonlinear speed changes from other software or build these effects yourself, the aim is to quicken or slow the clips in your programs. DaVinci Resolve offers a full suite of controls for making such effects by way of dedicated Retime controls, curves, and particular edit types. After an effect exists, DaVinci Resolve further gives you several methods of processing it so that playback comes out as smooth as it can possibly be.

### Speed Effects and Retiming

The term speed effects covers any effect that quickens, slows, or in some other way alters how fast clips play back in the Timeline. DaVinci Resolve gives you four fundamental routes to producing speed effects.

- Importing speed effects: DaVinci Resolve can pull linear speed effects out of imported EDL, AAF, and XML projects, plus nonlinear ones out of XML and AAF project files. Wherever such effects exist, DaVinci Resolve runs the clips at whatever speed has been specified. Your own speed effects can likewise be built with controls on the Edit page. Two avenues exist for adjusting a clip’s speed: the Change Speed dialog and the Retiming effect in the Timeline.
- Creating speed effects using Fit to Fill edits: A clip’s speed can also be altered in the Timeline by editing it with the Fit to Fill command, which retimes the clip so it spans whatever arbitrary duration you decide on in the Timeline. To read more about working with Fit to Fill, turn to Chapter 39, “Threeand FourPoint Editing.”
- Creating freeze frames: The freeze frame command lets you convert a whole clip into a freeze frame of whichever frame the playhead happens to cross.
- Creating simple linear speed effects: Straightforward fast or slow-motion effects can be made either through the Change Clip Speed command or by dragging the left and right handles of the Retime controls in the Timeline. This section walks through both approaches.
- Creating variable speed effects: For far more intricate variable speed effects, where a single clip quickens and slows several times by varying degrees, turn to either the Retime controls or one of the two available speed curves. These techniques get coverage later in this section as well.

### Speed Effects and Audio

Every technique DaVinci Resolve provides for making linear speed effects — among them the Retime controls, the Fit to Fill edit, and the Change Clip Speed command — retimes a clip’s audio alongside its video, doing so without pitch correction on Linux and Windows but with pitch correction on Mac OS X (Yosemite and above). Audio paired with variable speed effects, on the other hand, gets muted.

### Creating Freeze Frames

Several routes lead to a freeze frame, but the quickest is to park the playhead on the frame you’d like frozen, then choose Clip > Freeze Frame or press Shift-R. The whole clip turns into a freeze frame of the frame the playhead was sitting on. To undo the freeze frame effect, you can either select the clip and strip the speed effect away through the Remove Attributes dialog, or just open the Change Clip Speed dialog and clear the Freeze Frame checkbox.

### Creating Simple Linear Speed Effects

When your only goal is to play a clip in slow motion, run it faster, reverse it, or freeze a frame, a simple speed effect applied through either the browser or the Change Speed dialog does the job. To change a clip’s speed, do one of the following:

- With a clip selected, choose Clip > Change Clip Speed and work the controls in the Edit Speed Change dialog.
- Right-click a clip in the Timeline, pick Change Clip Speed, and operate the controls in the Edit Speed Change dialog.
- The speed of several selected clips can be altered all at once by way of either the Inspector or the Change Clip Speed dialog box.

The options offered by Change Clip Speed operations are:

- Change Clip Speed parameters: Resets the chosen clip’s speed by any percentage, frame rate, or duration you prefer.
- Ripple Sequence checkbox: Tick this checkbox if you’d like the upcoming speed change to ripple the Timeline, shoving every clip after the current one along to make room for the clip’s altered size.

### Speed effect parameters shown in the Speed dialog

- Reverse Speed checkbox: Ticking this box flips the present speed to a negative figure, sending the clip’s motion into reverse.
- Freeze Frame checkbox: Turns the whole clip into a freeze frame of whatever frame the playhead currently rests on.
- Pitch Correction checkbox: Tick this box and pitch correction runs on the clip’s attached audio, so that even as the audio’s length shifts to match the picture speed it keeps sounding natural. Keep in mind that pitch correction across large speed adjustments may not sound as pleasing as it does on small ones.
- Maintain Timing/Stretch to fit radio buttons: Picking Maintain Timing keeps every keyframe in the clip pinned where it began, whereas picking Stretch Keyframes squeezes or stretches all Composite, Transform, and Cropping keyframes by the same percentage as the clip throughout a speed change.

### Speed Change Controls in the Video Inspector

A clip’s speed can equally be tweaked right within the Video Inspector’s Speed Change controls. One advantage of this route is that it works on both the Cut and Edit pages.

- Direction: Picks the clip’s intended motion — forward, backward, or freeze frame.
- Speed %: Moving this slider shifts the clip’s motion on a percentage basis.

This value can be keyframed.

- Frames Per Second: Moving this slider alters the clip’s motion by raising or lowering how many frames per second it plays back at. This value can be keyframed.
- Duration: Decide outright how long the clip should run by entering a specific duration here using HH:MM:SS:FF format. Resolve then automatically tunes the clip’s speed so every frame plays within exactly that span of time.
- Ripple Sequence checkbox: Tick this checkbox when you want the upcoming speed change to ripple the Timeline, shoving every clip after the current one along to accommodate the clip’s revised size.
- Pitch Correction checkbox: Tick this box and pitch correction is applied to the clip’s attached audio, so even though the audio’s length shifts to match the picture speed it still sounds natural. Bear in mind that, across large speed adjustments, pitch correction can sound less convincing than it does on small ones.

### The Speed Change controls in the Video Inspector

### Clip Retiming Controls

A further way to change clip speed in the Timeline is by applying the Retime effect. This style of retiming hands you a handy control overlay for tuning clip speed right in the Timeline, and it also supplies the controls you need to build variable-speed effects. To bring up the Retime controls on a clip:

- With a clip selected, choose Clip > Retime Controls (Command-R).
- Right-click a clip and pick Retime Clip out of the contextual menu.

The Retime controls then sit over that clip in the Timeline. They comprise a Retime control track stretching across the top of the clip, its arrows signaling playback speed and direction (the default blue right-facing arrows mean normal 100% playback), together with a Clip Speed pop-up menu centered at the clip’s bottom that also reports the clip’s present speed.
