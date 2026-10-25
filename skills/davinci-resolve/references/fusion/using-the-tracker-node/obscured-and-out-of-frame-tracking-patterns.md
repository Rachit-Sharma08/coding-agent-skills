# Dealing with obscured patterns and dealing with patterns that leave the frame

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](best-match-tracking.md) / [Next section](simple-match-moving-and-corner-positioning-operations.md)
<a id="source-dealing-with-obscured-patterns"></a> <a id="source-dealing-with-patterns-that-leave-the-frame"></a> <a id="source-edges"></a> <a id="source-match-move-settings"></a> <a id="source-merge"></a> <a id="source-positionrotationscaling"></a> <a id="source-setting-up-tracker-offsets"></a> <a id="source-smoothing-motion"></a> <a id="source-stabilization-using-the-tracker-match-move-mode"></a> <a id="source-stabilizing-with-the-tracker-node"></a> <a id="source-the-match-move-settings"></a> <a id="source-the-track-center-append-mode-pop-up-menu"></a> <a id="source-the-tracker-offset-controls-in-the-inspector"></a> <a id="source-using-the-tracker-node-for-match-moving"></a>

### Dealing with Obscured Patterns

It frequently happens that a perfectly good pattern is briefly hidden (occluded) or kept from tracking— say, while following a car that slips behind a telephone pole. When that occurs, split the render range into two segments: one running up to the point where the pattern vanishes and another picking up once it reappears. Once each segment has been tracked on its own, the Tracker fills in the gap automatically, interpolating from where the first ends to where the second begins. Should you need to revise the resulting motion path to allow for any non-linear movement happening between the two tracked segments, click the track path to bring up a Node toolbar whose controls let you adjust this path’s control points. As one example, you might pick Insert and Modify mode to add points within the untracked span, compensating for nonlinear motion in the pattern being tracked.

The viewer’s Node toolbar holding tools for editing tracker paths

### Dealing with Patterns That Leave the Frame

You have two choices once a tracker exits the frame. Should the pattern come back into view, handle it as you would an obscured pattern. If it never returns, or hand-tracking parts of the movement is unappealing, reach for the Track Center (Append) mode to pick a fresh pattern.

### The Track Center (Append) mode pop-up menu

With Track Center (Append) mode, you choose a fresh pattern that keeps adding keyframes onto the path you already have. The system works out the offset between the prior pattern and the replacement on its own, yielding a single unbroken path. Here is the procedure for the Track Center (Append) mode: 1 Once the pattern can no longer be tracked for whatever reason, halt the analysis and park the playhead on the final frame that tracked cleanly. 2 In the Inspector, open the Path Center pop-up menu and pick Track Center (Append). 3 At this point, drag the Pattern selector onto a fresh pattern that can be tracked going forward. 4 Resume tracking from the present frame.

When you pick a pattern to append onto an existing path, the strongest results come from one that sits near the prior pattern and at the same apparent depth within the frame. As the new pattern moves farther off, it becomes increasingly likely that shifts in perspective and axial rotation will undermine how accurately the track resolves.

### Setting Up Tracker Offsets

Frequently you simply can’t track the very thing you intend to attach an effect to. Suppose the sole pattern that supports an accurate track is a button on an actor’s sleeve, yet the effect calls for the person’s hand to glow. Getting the glow’s effect mask to sit centered on the actor’s hand means you must turn to the Tracker Offset control.

### The Tracker Offset controls in the Inspector

With the X and Y Offset controls you can build either fixed or animated positional offsets measured against the actual pattern center of the Tracker. In the viewer, a dashed line drawn from the pattern center out to the offset location marks where that offset sits. The offset can likewise be tweaked in the viewer by means of the Tracker Offset button. Pressing it lets you move the path around while the Tracker pattern stays put.

Within the viewer’s Node toolbar sits the Tracker Offset tool; here a track of the orange dot is shifted over to sit at the ray gun’s center After an offset is established for a pattern, other positional controls can be wired to the Tracker’s Offset menu through the Connect To > Tracker: Offset Position option found in the control’s contextual menu. The path produced during the track stays anchored to the pattern’s center.

### Stabilizing with the Tracker Node

A Tracker node switched to Match Move in the Operations tab can perform several jobs. The obvious one is transferring the background clip’s motion onto the foreground clip. That said, Match Move also serves to stabilize footage, either stripping motion from the scene entirely or smoothing out movement that is already there. Below are a few typical stabilization scenarios that the Tracker handles in Match Move.

- Footage meant to hold still is marred by vibration or unwanted motion.
- A clip that calls for a fluid camera move is instead afflicted by jarring.

The Tracker Operation tab Match Move set to BG Only for stabilization

### Stabilization Using the Tracker Match Move Mode

When you stabilize motion, all apparent movement is erased from the image. The shift between one frame and the next is computed, then the frame’s contents are transformed so the picture returns to a reference position. That position might be the sequence’s opening or closing frame, or any frame you single out by hand. A lone pattern is enough for stabilization to fix position, whereas correcting rotation or scaling inside the image takes at least two patterns. With the Operation menu on Match Move, selecting BG only in the Merge operation menu stabilizes the background (yellow input) clip. The Operation tab surfaces only those controls that pertain to stabilization. A handful of stabilization controls stay accessible throughout, gathered beneath the Match Move Settings disclosure button. They remain on hand at all times because a tracker always publishes its Steady and Unsteady positions, which keeps them available for other controls to connect to even when the Tracker isn’t set to match moving.

### The Match Move settings

### Merge

Which input connection receives the Tracking data is decided by the Merge menu. To stabilize an image so that all motion is gone, or merely to smooth it, the Merge button has to be on BG Only.

### Edges

Once stabilization is applied, the Edges menu sets whether image borders that slide past the visible frame get cropped, duplicated, or wrapped. Wrapped edges often suit certain match-moving approaches, though they are seldom what you want when stabilizing for any other reason. For fuller detail on these controls, consult Chapter 119 (“Tracking Nodes”) of the DaVinci Resolve Reference Manual, or alternatively Chapter 59 within the Fusion Reference Manual.

### Position/Rotation/Scaling

The Position, Rotation, and Scaling checkboxes let you pick which facets of the motion get corrected.

### Match Move Settings

Among the Match Move settings you’ll find Pivot and Reference. Pivot Type The stabilization’s Pivot Type feeds the math that figures out the rotation axis and the scaling. It defaults to the averaged centers of all the patterns, but you can switch it to a single tracker’s position or to a spot you choose by hand. Reference The Reference controls decide whether the picture is stabilized against the sequence’s first frame, its last frame, or a frame you pick yourself. Wherever the tracked patterns stray from this reference, the image is transformed back toward this ideal frame. A handy rule of thumb: to strip every bit of motion from a clip, put the Merge mode on BG Only, set Pivot Type to Tracker Average or Selected Tracker, and leave the Reference control on Start, End, or Select Time.

### Smoothing Motion

Faced with footage whose camera motion is jittery or jerky, you often want to keep the original camera move while shedding only the erratic part, rather than wiping out movement altogether. That is exactly what the Start & End reference option is built for. Rather than locking onto a reference frame, it simplifies the tracked path. Each pattern’s position is assessed at the path’s beginning and end together with the points in between. What emerges is smooth motion standing in for the previous unsteady move.

The Reference Intermediate Points slider appears once Start & End is chosen, making it possible to smooth the motion To hold onto some of the original camera move’s curvature, raise the value of the Reference Intermediate Points slider that surfaces under the Start & End reference mode. When you track to produce smooth camera motion, confirm that the Start & End reference mode is on and that the Merge mode is set to BG Only. Leaving the Pivot Type control on Tracker Average is the recommended choice.

### Using the Tracker Node for Match Moving

The chapter opened with a basic match moving example, yet this part fills in extra particulars you might not have realized. Some cases where match moving applies are:

- A motionless CG element has to be convincingly dropped into a moving shot.
- A pair of sequences carrying unlike motion have to be combined into one.

Certain clips have to be stabilized first so that material from a different source can be placed into the shot. Once that element or effect is composited in, you take the stabilization back out so the shot reads naturally once more.
