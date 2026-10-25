# Speed effect controls in the timeline and retiming an entire clip

Version: DaVinci Resolve 20.3 Reference Manual. Context: Speed effects.
[Chapter index](INDEX.md) / [Previous section](speed-effects-and-retiming-and-speed-effects-and-audio.md) / [Next section](speed-processing-and-optical-flow-quality.md)
<a id="source-closing-retime-controls"></a> <a id="source-creating-variable-speed-effects-using-the-retime-controls"></a> <a id="source-reading-clip-speed-arrows"></a> <a id="source-retiming-an-entire-clip"></a> <a id="source-rippling-or-overwriting-the-timeline-when-using-retime"></a> <a id="source-the-speed-effect-controls-in-the-timeline"></a> <a id="source-using-retime-curves"></a>

### The Speed effect controls in the Timeline

### Retiming an Entire Clip

Using the Retiming effect at its most basic means changing the playback speed of the whole clip, which in turn ripples everything in the Timeline lying to the right of the retimed clip as its length grows from stretching or compressing it. To retime a clip by dragging: Bring the pointer over to either end — left or right — of the Speed Change name bar atop the clip, and once it becomes a Retime cursor, drag that side to stretch or squeeze the clip into its new timing. To retime by an exact amount: 1 With a clip selected, press Command-R. 2 Click the pop-up that sits beside the speed percentage text along the bottom of the clip. 3 Do one of the following:

- Pick a fresh playback speed out of the Change Speed submenu.
- Pick reverse segment so the clip runs backward. Reverse speed appears in the Retime

control track as arrows that point left rather than right. To send a clip back to its original speed: Click the pop-up beside the speed percentage text along the bottom of the clip and pick Reset to 100%.

### Rippling or Overwriting the Timeline When Using Retime

Whether the clips lying to the right in the Timeline ripple to absorb the duration change brought on by the speed adjustments you make with the Retime controls comes down to which tool is active: the Selection tool/mode leaves the Timeline unrippled, while the Trim tool/mode makes it ripple.

### Reading Clip Speed Arrows

As you retime a clip, the Clip Speed pop-up menu reports the present speed of the whole clip. The arrows along the Retime control track, meanwhile, convey playback speed and direction. Drop clip speed under 100% and the Retime control track displays yellow playback triangles set farther apart. Push it above 100% and the track instead shows blue triangles packed closer together. Right at 100% normal speed, the track presents blue triangles evenly spaced, whereas blue arrows pointing left signal reverse playback. Here three clips each carry a different speed; reading left to right, the yellow arrows mark 100% speed, then slow motion, then fast forward.

### Creating Variable Speed Effects Using the Retime Controls

The Retime controls also let you drop freeze frames into the middle of a clip and craft other bespoke variable speed effects by means of speed points. Among the extra variable speed choices are rewind and speed ramp effects, which lay down speed points on their own to produce preset results. To freeze a frame at one specific instant: 1 With the Retime controls on display, bring the playhead to the frame within that clip you want frozen. The classic use is an effect where a character in motion abruptly halts on a chosen frame. 2 Open the Clip Speed pop-up menu (the one beside the speed percentage text along the bottom of the clip) and pick Freeze Frame. A pair of new speed points joins the clip, marking out a span over which it stays frozen on that frame. The vertical red bars in the Retime control track make this visible. Beyond the second speed point, the clip picks up playback from the very next frame onward.

3 Drag the second speed point either way to set how long the freeze frame lasts. The upshot is that the clip runs normally until the first speed point, holds on that frame through to the second speed point, and then carries on. To create variable-speed effects: 1 With the Retime controls showing, bring the playhead to the frame where you want the clip’s speed to shift, and pick Add Speed Point out of the Clip Speed pop-up menu. 2 Advance the playhead to the next frame where the clip speed should change again, and drop in another speed point. At least two speed points are required before any speed effect takes shape. 3 To change the speed of the clip segment falling between those two speed points, do one of the following:

- With the pointer, drag the top handle of the second speed point rightward to slow that segment’s playback, or leftward to quicken it, all within that one segment. The move either trims or extends the clip and, depending on whether the Selection or Trim mode is active, either overwrites or ripples the neighboring clips.
- Again with the pointer, you can drag any speed point’s bottom handle to broaden the stretch of clip running at that specific speed. That action shifts frames from before and after the segment being adjusted so all the speed segments keep the same speed, and it too trims or extends the clip, though by a different margin.
- Through the Clip Speed pop-up menu, select a new speed for the segment from the Change Speed pop-up menu. Any segment can also be made to run backward by selecting Reverse Segment.

4 To wipe out a speed point and drop that clip’s speed segment from the effect, pick Clear Speed Point from any Clip Speed pop-up menu, which removes whichever speed point sits to its left. While you’re building variable-speed effects, the arrows along the Retime control track help you stay oriented, and each segment’s speed pop-up reveals the real numeric speed. The shift in speed from one segment to the next is eased automatically, giving a smooth handoff between speeds.

Speed controls arranged to ramp across three distinct playback speeds; the spacing of the arrows conveys the timing Two further command sets exist for building preset speed effects that draw on multiple speed points.

To add a rewind effect: With a clip’s Retime controls showing, open any Clip Speed pop-up menu and pick a preset percentage out of the Rewind submenu. Two more speed points get appended past the rightmost speed point of the current segment, which makes that segment play in fast reverse at the chosen percentage and then run through a second time from its start.

Speed effect controls shown before and after a “rewind” effect is built To build a speed ramp: With a clip’s Retime controls on display, open any Clip Speed pop-up menu and pick one of the two entries in the Speed Ramp submenu, swapping the current speed effect for a run of five speed segments beginning at 10% and climbing in steps to 30%, 50%, 70%, and finally 90%. After it’s built, you can drag the speed points to tailor the effect to whatever durations you need.

Speed effect controls arranged to build a gradual ramp running from 0 up to 100 percent playback speed

### Closing Retime Controls

Once your Retime effect is complete, you can dismiss the Retime controls so the clip looks normal once more. Dismissing them changes nothing about the clip’s timing; it merely keeps you from accidentally nudging the clip’s speed with the mouse. To close the Retime controls in the Timeline:

- Click the X button up in the top left-hand corner of the Retime control box.
- Press the escape key.
- Pick the retimed clip, then either go to Clip > Retime Controls or hit Command-R.

Whenever a retimed clip has its Retime controls hidden, a Retime badge shows up just left of that clip’s name in the Timeline. The Retime controls can be reopened any time you need to make further changes.

The Speed Effect badge that shows a clip is being retimed To bring the Retime controls back in the Timeline: pick the retimed clip, then either go to Clip > Retime Controls or hit Command-R. Once a clip has been retimed with the Retime effect, that clip’s Retime Process parameter in the Inspector lets you set how its retiming is handled — through the low quality Nearest option, through Frame Blending, or through Optical Flow.

### Using Retime Curves

Optionally, curves can also retime clips, working either alongside the Retime controls or on their own. You might, for instance, lean on the simpler retiming controls first to lay down the broad speed effect you want, then bring in one of the available Retime Curves to fine-tune things by dragging Bezier curve handles that shape the handoff from one speed to another; alternatively, you could open either Retime Curve up front and build your speed effect from nothing by adding and tweaking control points and curve segments. Whatever your preferred approach, every speed curve’s control points line up 1:1 with the speed points shown in the Retime controls, and edits to a curve segment are echoed by speed point shifts in the Retime controls whenever both are open together. The practical payoff is that, when assembling complex variable retiming effects, it’s simple to grab whichever control most readily dials in the quality of speed you’re after.

With their handles, the Retime Curves let you shape the handoff between one speed and the next On top of that, two varieties of Retime curve are available for maximum flexibility. The better pick hinges on which you find more comfortable and on which more readily handles the kind of motion you intend to create:

- The Retime Frame curve presents a diagonal line standing in for a time graph. It’s the same sort of curve seen across many other post-production tools, where the vertical axis stands for each frame of that clip’s source media and the horizontal axis stands for each frame of playback in the Timeline. On the default diagonal graph, each frame of source media maps one-to-one with each frame of timeline playback, which equals 100% speed. Adding control points, though, changes how source frames map onto the Timeline. Take any two control points on the Retime Frame curve: as long as the left one of a curve segment sits lower than the right one, motion runs forward, with longer shallow segments yielding slower motion and steeper shorter segments yielding faster motion in the clip.

A diagonal Retime Frame curve (green) holding two segments: a long shallow one on the left producing slow motion and a short steep one on the right producing fast motion

- Should a curve segment’s left control point sit higher than its right one, the motion flips and that segment runs backward.

A Retime Frame curve (green) whose inverted curve produces reverse motion

- The Retime Speed curve presents a flat line standing for 100% speed. Speed changes when you add pairs of control points and drag each segment up or down — and it’s the segments you drag, not the control points themselves. Lifting a curve segment shortens it and quickens that stretch of the clip, while dropping a segment lengthens it and slows that stretch. As you work each curve segment, a tooltip reveals the precise speed percentage it stands for. Bear in mind that reverse motion can’t be made with the Retime Speed curve; for that you must fall back on either the Retime controls or the Retime Frame curve covered above.

A Retime Speed curve (blue) where raising the line between two keyframes boosts the speed, while the flat line along the 0 axis on either side marks normal 100% speed. Ways to handle speed curves: To bring up a clip’s speed curves within the Timeline: 1. Pick a clip in the Timeline and choose the Keyframes tab at the top of the interface. 2. Click the Keyframe Curves icon, which opens the Curve Editor for that clip. 3. Pick Retime Speed and Retime Frame out of the parameter list, after which you can edit them just like any other curve — adding, moving, and deleting control points.
