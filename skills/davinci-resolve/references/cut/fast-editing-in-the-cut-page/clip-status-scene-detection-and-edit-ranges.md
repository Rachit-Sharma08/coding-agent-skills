# Clip status scene detection and edit ranges

Version: DaVinci Resolve 20.3 Reference Manual. Context: Fast editing in the cut page.
[Chapter index](INDEX.md) / [Previous section](snapping-to-guide-lines-and-proxy-handling.md) / [Next section](setting-in-and-out-points-using-the-pointer.md)
<a id="source-display-clip-names-and-status-in-the-timeline"></a> <a id="source-scene-cut-detection-in-the-cut-timeline-studio-version-only"></a> <a id="source-setting-in-and-out-points"></a> <a id="source-setting-in-and-out-points-using-the-keyboard"></a> <a id="source-the-boring-detector"></a> <a id="source-the-boring-detectors-analyze-timeline-edits-window"></a>

### Display Clip Names and Status in the Timeline

Should you want, clip names and clip status icons can appear directly atop your Timeline clips, making them easier to identify. To Display Clip Names for Clips in the Cut Timeline:

- Click on the Timeline Options icon.
- Select Display Clip Names from the drop-down menu.

To Display Clip Status Icons for Clips in the Cut Timeline:

- Click on the Timeline Options icon.
- Select Display Clip Status from the drop-down menu.

### Scene Cut Detection in the Cut Timeline (Studio Version Only)

The Scene Cut functionality can be put to work directly within a Cut timeline. It comes in handy where you've brought in video files of an already finished program and want it automatically chopped back into individual clips. For further detail on using Scene Cut Detection, consult Chapter 23, "Using Scene Detection." To run Scene Cut Detection on a Cut Page Timeline: 1 Pick the video clips on the Timeline you'd like split back into multiple cuts. 2 Pick the Timeline Actions icon and choose Detect Scene Cuts off the drop-down menu.

### The Boring Detector

A live analysis of how long each of your Timeline clips runs is what the Boring Detector performs, then it flags stretches too long or too short that might want your attention. To reach it, click the Timeline Options icon and pick Boring Detector. Clicking the icon a second time toggles it off. The Boring Detector icon alongside the Timeline displaying its results Analyze Timeline Edits CUT You adjust the Boring Detector's parameters within its Analyze Timeline Edits window.

- Boring Clips: Adjusting this slider sets the minimum number of seconds a clip's duration must reach before being flagged as too long. Clips exceeding this length are highlighted in light gray on the Upper Timeline.
- Jump Cuts: Dragging this slider fixes the most frames a clip's duration may carry before it gets flagged as too short. Clips falling below this length show up in red on the Upper Timeline. Set it to 2 frames and it can automatically surface accidental "flash frames" for you.
- Cancel: Closes the window while leaving the Boring Detector's analysis untouched.
- Analyze: Kicks off the live analysis of your timeline against the criteria you picked above.

Being persistent, the Boring Detecter carries on working as you go on editing on the Cut page. A further click on the Boring Detector icon turns it off.

### The Boring Detector's Analyze Timeline Edits window

### Setting In and Out Points

As a rule, source media stretches well beyond the actual clips you'll put into a program, so being able to mark off the range of media you'd like edited into the Timeline matters. You do this by laying In and Out points, whether in the Media Pool under Thumbnail or Filmstrip mode, or in the Viewer under Source Clip or the Source Tape.

### Setting In and Out Points Using the Keyboard

As you scrub a thumbnail or filmstrip within the Media Pool, hit the I (In) or O (Out) keys to mark off a range of media. Those edit points appear laid over the clip's thumbnail area, and over the Viewer's scroll area too whenever the clip is mirrored there. Marking off a range of media in the Media Pool with In and Out points (in white) As you scrub or shuttle media within the Viewer under Source Clip or the Source Tape, or run through your program with the Viewer set to Timeline mode, hit the I (In) or O (Out) keys to mark off a range of media. Marking off a range of media in the Viewer with In and Out points As you scrub or shuttle the Timeline while dragging the ruler left and right, hit the I (In) or O (Out) keys to mark off a range for incoming edit operations. That range gets indicated across both the upper and lower regions of the Timeline.

Marking off a range of the Timeline for editing operations with In and Out points
