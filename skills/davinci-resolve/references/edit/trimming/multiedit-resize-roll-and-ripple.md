# Resizing and rolling multiple edit points and rippling multiple edit points

Version: DaVinci Resolve 20.3 Reference Manual. Context: Trimming.
[Chapter index](INDEX.md) / [Previous section](ripple-trim-and-sync-lock.md) / [Next section](dynamic-trimming-or-jkl-trimming-overview.md)
<a id="source-asymmetric-trimming"></a> <a id="source-dragging-to-slip-multiple-selected-clips-at-once"></a> <a id="source-dynamic-jkl-trimming"></a> <a id="source-keyboard-trimming-during-looped-playback"></a> <a id="source-quick-trimming"></a> <a id="source-resizing-and-rolling-multiple-edit-points"></a> <a id="source-rippling-multiple-edit-points"></a> <a id="source-sliding-multiple-clips"></a> <a id="source-slipping-multiple-clips"></a>

### Resizing and Rolling Multiple Edit Points

Multiple edit selections can be resized or rolled in one go. Doing so lets you adjust the edit points of several superimposed clips all at once. Trimming multiple edit points essentially "gangs" them together so every selected edit shifts as a single unit.

- To resize a number of clips together, grab the left (outgoing) or right (incoming) side of each edit point that needs changing, then drag those edit points using the Selection tool to resize them as a group.
- To roll several clips at once, select every edit point you need to change right at the center, so both the incoming and outgoing halves of each edit point are chosen, then drag those edit points with either the Selection or Trim tools to roll them all together.

NOTE: You cannot combine ripple and roll operations at the same time.

### Rippling Multiple Edit Points

You can also pick multiple incoming or outgoing edit points either on superimposed video tracks, or on a single video track, so as to ripple them all in one go. A good illustration of wanting to ripple several clips on a single track is when you have an end credit sequence built from 14 text generators and wish to compress that whole run by a particular figure. You can see this very case below. As you ripple trim several edits sharing one track, how many frames come off in any single trim depends on which method you pick for the trimming.

- Should you drag in the Timeline with the Trim tool, you can choose to ripple the entire batch of edits by some arbitrary duration, perhaps trimming or extending the whole batch by eight frames. When you do, DaVinci Resolve runs your multi-selection trim one edit at a time, shaving a single frame off each selected edit moving left to right as you trim, continuing until either you stop the operation or each selected edit has lost one frame, whereupon DaVinci Resolve begins removing the second frame from each selected edit left to right, then the third, and onward, until your trimming ceases. Going about it this way, the mouse lets you fit any quantity of clips into any duration you choose.
- Alternatively, you can choose to ripple every selected edit by the same fixed amount, say stripping three frames off each of the selected edits all in one move. For that, keep the Command key held as you drag selected edits with the Trim tool, or rely on Dynamic JKL trimming, or trim by typing relative timecode values, or reach for the nudge keys (Period and Comma).

To ripple trim several edits sharing one track: 1 Click the Trim tool, then drag out a bounding box across the Timeline to grab all 14 edits. 2 Hit the U key to highlight the incoming side of each selected edit. 3 Reach for whichever trimming method you like to ripple the run shorter or longer. Dragging via the Trim tool permits trimming by an arbitrary frame count, whereas keeping Command held as you drag with the Trim tool, typing timecode to trim, pressing the Comma and Period nudge keys, or invoking Dynamic JKL trimming each trims every selected edit by an equal frame count.

(Before) Choosing 14 incoming credits edit points, (after) Trimming the whole batch in one move

(Before) Choosing several incoming edit points and (after) Trimming the entire group together

### Asymmetric Trimming

Asymmetric resize or ripple trimming can be performed on multiple clips too, allowing one selection per track on as many tracks as you need. To trim two or more clips asymmetrically, select an outgoing edit point on one track, then Command-click an incoming edit on another track.

Choosing opposing outgoing video and incoming audio edit points while getting set to carry out an asymmetric ripple trim To grab the outgoing video edit on one clip together with the incoming audio edit on the next clip while preparing a split edit, you can Option-click the outgoing video edit so linked selection is suspended, then Command-click the incoming audio edit, adding that one on its own into the selection. After that, dragging, nudging, or trimming with timecode sends each chosen edit point in the reverse direction.

Dragging with the Trim tool to run an asymmetric ripple trim that forms a split edit DaVinci Resolve permits asymmetric trims on multiple edits within the same video and/or audio track. Two compelling reasons exist for doing so: Grab the outgoing half of an edit point (its left side), then Command-click to independently grab the incoming half of that very same edit point (its right side). This produces no roll edit; instead it lets you either reach for the Selection tool to pull both edit points away from one another and open a gap, or reach for the Trim tool to ripple the edit's two sides, trimming both clips down while at the same time tightening up the Timeline.

Before and After ripple trimming an edit's incoming and outgoing halves together to cut down both clips' duration in a single move You can likewise grab a clip's In and Out points in the Timeline together and reach for the Trim tool to ripple that clip's head and tail toward the middle, trimming it down while holding the central content intact, and tightening up the Timeline as you go.

Before and After ripple trimming a clip's In and Out points simultaneously, cutting it down by stripping heads and tails while the central action stays put

In essence, you can apply almost any combination of edit selections you require to trim multiple clips at once within the same track, across several tracks, whatever you need to do to save time. On top of that, asymmetric trimming works in either Selection or Trim mode, whether to open and close gaps or to slide edit points over one another to form split edits.

### Slipping Multiple Clips

Any number of selected clips can be slipped simultaneously (provided they have handles) across any mix of tracks: select the clips you wish to slip, then choose the Trim tool, and drag their name bars or use the Comma and Period keys to nudge the selection.

### Dragging to slip multiple selected clips at once

### Sliding Multiple Clips

You can select as many clips as you'd like to set up a slide operation. Select multiple contiguous clips and they slide together as a single unit.

(Before) Picking four clips for a slide, (After) Every one of the four dragged rightward with the mouse

### Keyboard Trimming During Looped Playback

If you favor precision trimming through the Nudge commands, one excellent approach is turning on looped playback so that the Play Around command (Forward Slash) keeps circling around the edit point under your trim while you nudge a frame or five at a time to refine the cut. To trim while looping: 1 Bring the playhead near the edit point that needs trimming, and press V to grab it. 2 Press the U to decide which half of the edit to grab so you can ripple or roll it, and/or Option-U to settle whether the trim covers video+audio, video alone, or audio alone. 3 Press Command-Forward Slash (/) to switch looped playback on. 4 Press Forward Slash (/) to play around whatever is currently selected. With looping active, playback runs on until you halt it. The Edit panel of the User Preferences is where Pre-roll and post-roll get adjusted. 5 While looped playback runs, press the Comma (,) and Period (.) keys to shift the selection back or ahead one frame, or Shift-Comma and Shift-Period to move it in 5-frame steps. Should you do this while looped playback is in its post-roll, the loop replays instantly from the top, so no time is wasted in seeing the result. 6 Once finished, press the Spacebar or K key to halt playback. TIP: Holding down the Shift key as you nudge for a "fast nudge" gives you a duration that's customizable through the Editing panel of the User Preferences. Five frames is the default, yet you can dial it to whatever value you prefer.

### Dynamic JKL Trimming

One of the more interactive trimming capabilities in DaVinci Resolve lets you dynamically resize, ripple, roll, slip, slide, or move chosen edit points and clips through the JKL transport control keyboard shortcuts. What that buys you is the ability to set up an appropriate Timeline selection (edit points for resizing, rippling, or rolling, or clips for slipping or sliding) and then trim it as playback runs, all while you keep an ear on the audio and an eye on the video. The advantage of trimming as the chosen clip or edit point plays back is that it lets you become emotionally caught up in what's on screen, and also feel a clip's timing as it runs, both of which sharpen your sense of precisely how a given cut needs trimming. As you dynamically trim, you see the very same two-up or four-up display, the very same Timeline overlays, and the very same live-updating Timeline that appear when the Trim tool is driven by the mouse. The sole difference is that the trimming happens while your program plays.

There are two methods of doing dynamic trimming:

- Quick Trim: Pick one or more edit points or clips and trim them right away by pressing Command-J or Command-L for a backward or forward trim. It's a speedy route to dynamic trimming, with the caveat that backward and forward trims happen only at 100 percent speed or above.
- Turning on Dynamic mode: When you need finer control, tap the W key to engage Dynamic mode (or pick Trim > Dynamic Trim Mode), which drops you into a dedicated mode in which the JKL shortcuts trim nothing but the active selection, no matter what that is. This mode further offers extra options for steering which slice of the selection, where multiple selection trims are involved, gets monitored during audio/video playback.

TIP: With nothing selected while you sit in Dynamic Trim mode, JKL just runs through the Timeline as it normally would.

### Quick Trimming

When time is short and you can land the trim you're after at real-time or quicker playback, then keeping the Command key held as you use the J or L keyboard shortcuts lets you dynamically trim whatever is selected in the Timeline, complete with audio/video playback. For dynamic trims via Command-J or Command-L:

- To dynamically roll an edit: From either Selection or Trim mode, grab the center of one or more edit points, then keep Command pressed as you tap J or L to drive the selection around.
- To dynamically ripple an edit: Switch to Trim mode, grab the outgoing or incoming half of one or more edit points, then keep Command pressed and tap J or L to drive the selection.
- To dynamically resize an edit: Switch to Selection mode, grab the outgoing or incoming half of one or more edit points, with Command held while J or L nudges the selection along.
- To dynamically move a clip: Switch to Selection mode, grab one or more clips, with Command held as J or L carries the selection back and forth.
- To dynamically slip or slide a clip: Switch to Trim mode, grab one or more clips to slip, or a lone clip to slide, press S to flip between Slip or Slide modes, then with Command held use J or L to run either the slip or the slide.

When trimming several selections, you decide which edit point to monitor across the whole trim by parking the playhead on one of the chosen edit points. TIP: Once a "quick trim" is finished and you'd like to watch how that edit plays, hit the Forward Slash key (/) to play around the current selection and rapidly preview that stretch of the Timeline.
