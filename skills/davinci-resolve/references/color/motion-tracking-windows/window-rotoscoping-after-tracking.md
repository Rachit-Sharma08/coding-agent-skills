# Rotoscoping window shapes after tracking and rotoscoping controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Motion tracking windows.
[Chapter index](INDEX.md) / [Previous section](dealing-with-occlusions-when-tracking-and-original-clip.md)
<a id="source-a-rotoscoping-workflow"></a> <a id="source-keyframes-appear-in-the-tracker-graph-ruler"></a> <a id="source-keyframing-in-frame-mode"></a> <a id="source-rotoscoping-controls"></a> <a id="source-rotoscoping-window-shapes-after-tracking"></a> <a id="source-viewing-a-windows-motion-path"></a>

### Rotoscoping Window Shapes After Tracking

As remarkable as the DaVinci Resolve trackers are at keeping a window glued to moving subjects or to elements inside a shot in motion, there will be no shortage of occasions where the finished track falls a little short. Say you're trying to isolate a person's face with a highly specific window, and that person rotates their head; the shape change that follows will almost surely demand animated tweaks to the window if you want to hold such a precise isolation.

Comparing before and after as a window tracks a turning head: the window falls slightly short of hugging the edge of the woman's face while her head rotates

Happily, the Frame mode of the Tracker palette makes it straightforward to animate the shape edits you apply to windows so they hug a moving subject more closely, work often called rotoscoping. By tracing a moving subject and laying down a run of automatically keyframed window tweaks wherever the subject shifts speed or direction, you can keep a window isolating a moving target with striking accuracy.

Employing Frame mode to rotoscope the window so it more closely hugs her facial edges and the line of her jaw On top of that, Frame mode can also fix sloppy tracks where the window strays off course thanks to fast or erratically moving features. For those cases, you have the choice of tracking the window by hand in Frame mode to match the feature's path, one frame after another. And finally, you needn't even have run a track at all to use the Tracker graph in Frame mode for keyframing animated window changes. As it happens, working the Tracker graph in Frame mode can at times beat using the Keyframe Editor in Auto Keyframe mode, depending on the task at hand.

### Rotoscoping Controls

Whether you're rotoscoping a shape comes down to the Clip/Frame buttons. In Clip mode: Whatever edits you apply to a window reshape it across the full length of that clip. To put it another way, you can track a window onto a moving feature, and in Clip mode any change to the window's size, rotation, position, or shape happens uniformly from that clip's start to its end. In Frame mode: An edit to a window automatically lays down a keyframe at the foot of the ruler in the Tracker graph. Two or more window edits in Frame mode yield automatically interpolated animation running from one keyframed window transformation to the next. You're free to switch back and forth between Clip and Frame modes as you edit a window. Even after keyframing a window's shape changes, you can flip on Clip mode and apply a blanket change to the window, enlarging it say, which enlarges the window equally at every keyframe.

### Keyframing in Frame Mode

After you've laid keyframes into the Tracker palette, several options exist for editing them. Ways to work with keyframes in the Tracker graph:

- To add a keyframe: In the top right corner of the Tracker graph, click the Add Keyframe icon. It looks much like the Keyframe icons sitting in the Edit page Inspector. It's handy when you want a keyframe on a frame where the window matches the subject nicely, ahead of advancing a few frames and reshaping the window onto the subject, which produces another keyframe.
- To move the playhead from one keyframe to another: In the top right corner of the Tracker graph, click the Previous Keyframe and Next Keyframe icons. They look much like the controls over in the Edit page Inspector.
- To delete a keyframe: With the playhead parked on the exact frame that holds the keyframe you want gone, open the Tracker option menu, and choose Delete Keyframe.

The graph's Previous Keyframe, New Keyframe, and Next Keyframe buttons sit in the Tracker graph

### A Rotoscoping Workflow

The walkthrough below shows how a window can rotoscope an onscreen feature you want isolated. As it goes, it explains preparing a window for rotoscoping by means of the Tracker palette, plus a handful of practices that keep your rotoscoping work quick. To rotoscope, or hand-track, a window with automatic keyframing: 1 Build a window around the feature you mean to adjust, and let the tracker carry it along with the subject's motion. Where the window fails to trace the subject's contours as tightly as you need, you can begin keyframing its shape manually atop whatever tracking you've already performed to rotoscope your subject. 2 With the Tracker palette open, click Frame to switch the tracking mode.

Clicking the Frame button to start keyframing the shape The best Frame mode tracking technique is to either start on the last frame you tracked successfully and proceed forward, or start on the first frame you tracked successfully and proceed backward. That approach extracts the maximum from the automatic keyframing and the between-keyframe interpolation, animating the window you're reshaping cleanly. 3 With the playhead resting on whichever frame (first or last) shows the window fitting your isolated subject, you may click the Add Keyframe button in the upper right corner of the Tracker graph, or jog any control point a pixel or two, in order to set a keyframe there.

Clicking the Add Keyframe icon in the Tracker graph Placing a keyframe at the final frame where the window tracks the subject's motion well ensures any later animated changes interpolate forward from that frame, instead of from earlier frames that need no edits.

Adjusting the window in Frame mode adds a keyframe Throughout Frame mode, the edits you make to the window automatically spawn a keyframe in the Tracker palette, showing up at the foot of the Tracker graph's timeline.

### Keyframes appear in the Tracker graph ruler

It's often crucial to drop a keyframe on the final frame where a window matches the subject you're isolating well, so as to confine window animation between that frame and the next keyframed transformation, rather than letting it animate by accident from the clip's opening, or from an adjacent keyframe in the Tracker graph. 4 Then, advance the playhead to the next frame where the window needs adjusting to better suit the moving subject, and tune the window's position, its control points, or both, isolating the subject however necessary.

Readjusting the window in Frame mode to follow the subject’s motion

The result is a second keyframe placed into the Tracker graph ruler. A pair of keyframes producing rotoscoped animation atop whatever motion tracking is in effect 5 Once your opening pair of keyframes is down, drag the playhead to and fro between them to judge how well the window's animation interpolates automatically to track the subject you're isolating. If the window isn't following your subject's motion closely enough, take the playhead to the frame where the window strays the worst and make a further tweak to fix the shape. That spawns yet another keyframe.

One of the frames sitting between your two rotoscoped keyframes that calls for more adjustment

After adjusting the in-between frame

6 Having finished tweaking between your opening two keyframes, push the playhead onward and lay down keyframes as needed so the window tracks your subject's motion. As a rule, hunt for the frames where your subject's motion begins, ends, accelerates, decelerates, or shifts direction. While you work, aim to use the smallest number of keyframes that still yields smooth motion between them. Cramming too many keyframed tweaks too tightly together for a smoothly moving subject risks introducing jerky motion if you're not watchful. Conversely, with an erratically moving subject you might be forced to add more keyframes, perhaps frame by frame, to land the look you're after.

TIP: When you're isolating a subject whose shape is intricate and that moves a great deal, think about using several simple overlapping shapes to track and rotoscope it rather than one complicated shape, which makes the job easier. 7 After you've wrapped up rotoscoping the window, make a point of clicking the Clip button to return to Clip mode, so that you can trim the window's shape across every keyframe you just laid down, if needed. This also keeps you from inadvertently piling on more keyframes if you go select other shapes.

This approach takes a touch more effort than relying on the Tracker alone, but it lets you swiftly fine-tune a window's animation so it clings more snugly to a moving subject whenever you need a tweak aimed at that subject by itself. The same approach also works for nudging particular motion path points partway through an otherwise good track to seat them better, or for adding keyframes at the head or tail of a track where the subject leaves frame but the window stays put.

### Viewing a Window’s Motion Path

To display the motion path for whichever window you're tracking, choose Show Track from the Tracker Option menu.
