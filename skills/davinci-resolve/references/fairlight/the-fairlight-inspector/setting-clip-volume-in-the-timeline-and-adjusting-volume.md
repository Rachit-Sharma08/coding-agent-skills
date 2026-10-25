# Setting clip volume in the timeline and adjusting volume

Version: DaVinci Resolve 20.3 Reference Manual. Context: The Fairlight inspector.
[Chapter index](INDEX.md) / [Previous section](paste-and-remove-attributes.md)
<a id="source-adding-and-adjusting-volume-keyframes"></a> <a id="source-adjusting-volume"></a> <a id="source-normalizing-audio-levels"></a> <a id="source-paste-and-remove-attributes-for-clips-and-tracks"></a> <a id="source-setting-clip-volume-in-the-timeline"></a> <a id="source-the-paste-attributes-dialog-in-the-fairlight-page"></a>

### Setting Clip Volume in the Timeline

Every audio clip carries its own Volume level — and where audio is linked across multiple tracks, that level belongs to the audio item as a whole. As a result, a clip holding several channels uses one shared Volume setting. A handful of straightforward methods let you change these levels.

### Adjusting Volume

In the Timeline, every audio clip (or item) shows a Volume overlay; drag it upward or downward with the pointer to set that clip’s gain. The position of this overlay tracks the Volume parameter found in the Inspector.

Dragging a Volume overlay to adjust the clip level Beyond that overlay, each audio clip has an Audio Curve Editor button tucked into its lower right-hand corner. Clicking it brings up a Curve Editor dedicated to audio, where keyframing covers pan and the settings of any audio filters on the clip in addition to volume. NOTE: Choosing Show Clip Gain Line from the Fairlight menu displays each clip’s gain right in the Timeline — a quick way to survey how the gains of every clip compare.

Turn on the Clip Info display to surface clip information for all of the Timeline’s clips.

### Adding and Adjusting Volume Keyframes

Placing and tweaking individual keyframes is a quick, effective route to evening out the relative levels of your clips and to repairing dynamic level issues that affect a single clip. The procedures below apply whenever you edit an audio parameter curve by hand.

Ways to reshape the Volume curve with the pointer:

- To adjust any curve segment: For a clip carrying no keyframes, hover the pointer anywhere along its segment; otherwise place it between a pair of keyframes, right on the segment you intend to move. As soon as the move cursor appears, drag upward to raise the Volume or downward to lower it.
- To adjust a section of level in a clip: Highlight the stretch you want to change with the Edit Selection tool. With the Clip Gain line visible, raise or lower it to the level you want; keyframes appear on their own at each edge of the adjusted region.
- To add keyframes to the level curve: With the Option key held, click the curve wherever you want a keyframe placed at that frame. At least two keyframes are required before an automated Volume change takes effect. Holding the Option and Command key together lets you delete any keyframe.
- To adjust a keyframe in any direction: Hover over a keyframe until the four-way cursor shows, then drag vertically to alter the Volume or horizontally to shift its timing.
- To adjust a keyframe in only one direction: Hover over a keyframe until the four-way cursor shows, then drag toward the single axis you intend to change — vertically to set the clip’s volume at that frame, or horizontally to relocate the keyframe to another moment in time. As soon as the drag commits to one axis, the keyframe stays locked to that axis until you let go.
- To select one or more keyframes: A single click on any keyframe selects it.
- To select multiple discontiguous keyframes: Command-click each keyframe you want, regardless of whether they sit side by side.
- To select multiple contiguous keyframes: Click the first keyframe in the run, then shift-click the last one; every keyframe in between is selected as well.

NOTE: While you change the gain on clips, the tooltips report the current gain level and update live, showing the size of the change as the keyframe travels.

### Normalizing Audio Levels

The Normalize Audio Levels command drives the level of timeline clips toward a target you specify, and it lets you pick which method should examine the levels of each audio clip so it knows how to normalize that clip’s volume. Among the choices are several loudness normalization algorithms tied to the various international standards; these help match the perceived overall loudness across a group of clips no matter how the transient levels move within any one clip. Peak normalization is available too, offering both Sample Peak and True Peak. The loudness-based methods judge an audio signal by how loud a listener perceives it, and that yields a more faithful automatic balance between the levels of different clips, irrespective of the transient peaks that come and go across them. For the maximum “true peak,” the target peak meter has shifted to the BS.1774 standard, so it can now register “inter-sample peaks” instead of reading only the peak found at each waveform sample. You may still pick Sample Peak, the older approach that reports the genuine peak of the samples held in a media file.

Whatever the Normalize Audio Volume command alters is purely the volume; it leaves dynamics untouched, so once it runs, the loudest portions of every selected clip line up with each other at the target level. You will find this command on the Fairlight page as well. To normalize one or several selected timeline clips: 1 Right-click any of the chosen clips and pick Normalize Audio Levels. The Normalize Audio Level dialog appears.

Shown here on the Fairlight page, the Normalize Dialog. 2 Pick the Normalization Mode you intend to apply. Your options span a range of standardized loudness measurement algorithms, plus Sample Peak and True Peak. 3 Set, in dBFS, the reference level you want the peak volume of the chosen clips to reach. 4 Decide how the level should be handled across several selected clips: with Set Level on Relative, every selected clip is handled as though it were a single clip, so the loudest peak found anywhere in the selection sets the adjustment and each clip’s volume shifts by that same amount. That suits a run of clips — a dialog recording, say — whose levels already agree and that you want normalized as a group. With Set Level on Independent, each clip’s own peak level drives its adjustment, so every selected clip moves by an amount unique to it. What comes out can be a spread of widely differing volume shifts whose purpose is to bring the peak levels of all the clips into agreement. That works well when, for instance, you need to even out an assortment of sound effects whose opening levels are far apart. For more on loudness normalization, see Chapter 182, “Audio Meters and Audio Monitoring.”

### Paste and Remove Attributes for Clips and Tracks

On the Fairlight page you get Paste Attributes and Remove Attributes commands, which copy and reset audio parameters and effects much as their counterparts do over on the Edit page.

### The Paste Attributes dialog in the Fairlight page

Three categories of attribute are offered in the Paste Attributes dialog box. Volume applies the copied attributes to the clip. Plugins applies any plugin attributes to it. Equalizer brings over EQ data taken from a different clip. You may transfer just one of these or every one at once. The Remove Attributes dialog box presents the same three categories, this time for clearing them from a clip. With the Volume box turned on, every Clip Gain keyframe is stripped from the clip.
