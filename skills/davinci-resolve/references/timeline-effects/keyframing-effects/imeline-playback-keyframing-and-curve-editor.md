# Keyframe directly in the timeline during playback and keyframe and curve editor

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing effects.
[Chapter index](INDEX.md) / [Previous section](video-inspector-keyframes-and-motion-paths.md) / [Next section](keyframe-editor-and-timeline-tray.md)
<a id="source-keyframe-and-curve-editor"></a> <a id="source-keyframe-directly-in-the-timeline-during-playback"></a> <a id="source-organizing-the-keyframe-editor"></a> <a id="source-the-keyframe-editor"></a> <a id="source-to-show-only-specific-tracks"></a> <a id="source-to-show-only-tracks-that-already-have-keyframes"></a> <a id="source-to-show-only-video-related-tracks"></a> <a id="source-to-show-or-hide-tracks-by-parameter-group"></a> <a id="source-to-undock-and-resize-the-keyframe-editor"></a>

### Keyframe Directly in the Timeline During Playback

You can drop keyframes straight onto clips in the Timeline as playback runs. Keyboard shortcuts let you add and remove a clip’s keyframes, and DaVinci Resolve does its best to read the clip’s context and set the right keyframe. With this approach you can rapidly and accurately lay down retime and audio gain Keyframes during playback, then return later to work the points you marked. To Add a Keyframe to a Clip in the Timeline:

- Play the clip on the Timeline, and as the playhead crosses the frame of the clip where the keyframe belongs.
- Choose Mark > Add Keyframe (Command-[).

To Delete a Keyframe in a Clip in the Timeline:

- Pick the keyframe or keyframes you intend to remove from the clip.
- Choose Mark > Delete Keyframe (Option-]).

Although dropping a keyframe onto a timeline clip is a single keypress, how does DaVinci Resolve figure out which exact parameter, among all the choices in the inspector, you meant to keyframe? In short, the keyframes are now context aware: the keyframable attribute (Zoom, Position, Volume, etc.) that DaVinci Resolve picks rests mainly on the last thing you worked with, or otherwise on the one used most often. DaVinci Resolve’s keyframe selection hierarchy walks the keyframable options from the top downward; whenever no keyframe fits the context of the topmost entry, it moves on to the next entry below, and so forth. The DaVinci Resolve Keyframe Selection Order:

- The Retime Controls (if already active)
- The active effect curve in the Keyframe Editor (if already open)
- The last Inspector control that was manipulated
- Audio Gain

As an illustration, suppose you had earlier tweaked the Zoom parameter on a clip, then dropped a fresh keyframe onto it by pressing Option-[ ; it would skip past the Retime Controls and the Effect Curves (if those were closed in the inspector) and lay down a new Zoom keyframe, since that was the last tool you touched. By the same token, adding a keyframe to a plain clip on a timeline that has no modifications gives you an Audio Gain Keyframe. Should you want richer keyframing, or should DaVinci Resolve misread the context, you can fall back on the Keyframe Editor.

### Keyframe and Curve Editor

DaVinci Resolve’s Keyframe and Curve Editors exist to hand you precise control over intricate animations too detailed for the Inspector. You can reach the Keyframe and Curve Editor from both the Cut and Edit pages as a panel of its own. Just click the Keyframes tab in the upper left to bring it up. The Keyframe Editor appears by default, presenting every keyframable parameter from the Video Inspector alongside any keyframes already placed there. Clicking the Curve icon in the upper left carries you over to the Curve Editor.

### The Keyframe Editor

Within the Timeline, the Keyframe Editor is the strongest means of laying out all of a clip’s keyframes and fine-tuning their timing and interpolation.

The Keyframe Editor showing all the video attributes found in the Inspector For each parameter that can be keyframed on the chosen clip, the Keyframe Editor lays out one keyframe track. At first glance this resembles a long list of fiddly items to track (no pun intended), yet it does hand you a solid survey of everything animatable on your clip. That said, the Keyframe Editor offers several tools for clearing away needless clutter so you can zero in on just the parameters you care to animate. These keyframe tracks let you edit keyframes against the real clip durations in the Timeline.

Keyframe Tracks: Transform serves as the track group (revealed via the disclosure triangle), with Zoom and Position XY being tracks nested in it. An outline and white fill mark the selected keyframes. The tracks are likewise sorted by parameter category. As an example, every Transform, Cropping, and Speed parameter is wrapped inside group tracks. Had you keyframed the Zoom and Position parameters, those keyframes would also surface inside one keyframe track named Transform, while Crop Left and Crop Right changes would land on a separate group keyframe track named Cropping. Shifting a keyframe on a group track moves the keyframes sitting at that same spot across all of its contained parameters together. Every group keyframe track carries a disclosure arrow letting you reveal or conceal each separate parameter inside that group. As an example, clicking the Transform keyframe track’s disclosure arrow exposes the Zoom and Position tracks, so you can work their individual keyframes.

### Organizing the Keyframe Editor

Keyframing on its own is a reasonably simple business, but the sheer count of keyframable attributes can be daunting, so unless you intend to animate something fiendishly complex, you are likely better off narrowing the Keyframe Editor’s interface down to only what you require.

### To show or hide tracks by parameter group

- Click the little disclosure triangle beside the group track’s name. As an example, if you only meant to keyframe parameters within the Transform group (Zoom, Position, etc.), you could shut the disclosure triangles in the Cropping and Speed groups to tuck away the surplus tracks.
- Click the 3-dot option menu at the right of the parameters column, and pick Expand All Parameters to throw open every group track and reveal its enclosed parameters.
- Click the 3-dot option menu at the right of the parameters column, and pick Collapse All Parameters to shut all group tracks.

### To show only tracks that already have keyframes

- Click the 3-dot option menu at the right of the parameters column, and pick Display Parameters with Keyframes. This reveals only those tracks already holding at least one keyframe, plus their enclosing group tracks.

### To show only Video related tracks

- Click the 3-dot option menu at the right of the parameters column, and pick Display All Video Parameters. This conceals any keyframe tracks driving audio-related functions from the Audio Inspector.

### To show only specific tracks

- Click the 3-dot option menu at the right of the parameters column, and pick Display Selected Parameters. Then you can tick checkboxes for Video and Audio. Clicking those reveals a further set of checkboxes letting you pin down exactly which tracks to show.

### To undock and resize the Keyframe Editor

- Click the undock icon in the Keyframe Editor to pop it out as a standalone window. From there you can resize the window to grow the Keyframe Editor to whatever dimensions you need.
