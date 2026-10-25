# Adjustment clips and paste attributes

Version: DaVinci Resolve 20.3 Reference Manual. Context: Effects overview.
[Chapter index](INDEX.md) / [Previous section](effects-inspector-controls-and-adding-filters-to-video-clips.md)
<a id="source-adjustment-clips"></a> <a id="source-keyframe-options-for-pasting-keyframed-attributes"></a> <a id="source-option-to-ripple-the-timeline-for-pasting-speed-effects"></a> <a id="source-paste-attributes"></a> <a id="source-remove-attributes"></a> <a id="source-the-paste-attributes-window"></a> <a id="source-the-remove-attributes-window"></a>

### Adjustment Clips

You can likewise put all manner of effects onto multiple Timeline clips using Adjustment clips, found in the Effects bin of the Toolbox in the Effects Library. Whenever an Adjustment Clip is stacked over one or more Timeline clips, whatever filters or additional effects you place on that Adjustment clip propagate down to each clip below. The kinds of effects you can apply with Adjustment clips include:

- Resolve FX and Open FX plugins
- Inspector parameters including Composite, Transform, Cropping, and Dynamic Zoom
- Fusion page effects
- Color page grading and sizing

Adjustment clips offer a quick and readily revisable means of applying one or more effects and grades across a span of clips. Adjustment clips that struggle to play back in real time can be rendered to cache, the same as any ordinary video clip. Adjustment Clips can be named through the Inspector. To stash an Adjustment clip, simply drag it from the Timeline into the Media Pool. From there you can manage the Adjustment clip the same as any other media type.

An Adjustment clip casting the vignette of a Prism Blur Resolve FX down onto a pair of clips below

### Paste Attributes

The Paste Attributes command lets you copy and paste video and audio attributes, along with color corrections, from a single clip onto several clips. It is a quick route to spreading video and audio tweaks and effects out of one clip onto numerous others throughout the Timeline. To copy attributes: 1 Pick a clip whose attributes you wish to push to other clips, then hit Command-C. 2 Pick one or more further clips as the paste destinations. 3 Go to Edit > Paste Attributes (Option-V), or right-click any of those selected clips and pick Paste Attributes from the contextual menu. 4 Once the Paste Attributes window opens, tick the checkbox for each attribute you intend to paste, then hit Apply when finished.

### The Paste Attributes window

The Paste Attributes window presents at the top the clip you are copying from and the clip(s) you are pasting onto, and supplies checkboxes for choosing which attributes to paste.

### Keyframe Options for Pasting Keyframed Attributes

A pop-up menu underneath lets you pick how any keyframes belonging to the attributes being pasted should be applied; the choices are Maintain Timing or Stretch to Fit.

### Option to Ripple the Timeline for Pasting Speed Effects

While using Paste Attributes to copy speed effects between clips, the Ripple Sequence checkbox lets you decide whether or not the pasted speed effect ripples the Timeline.

### Remove Attributes

Specific attributes can also be cleared from one or more clips through a window that mirrors the opposite of the Paste Attributes window.

### The Remove Attributes window

To remove attributes: 1 Pick one or more clips carrying effects you wish to strip away. 2 Go to Edit > Remove Attributes, or right-click any of those selected clips and pick Remove Attributes from the contextual menu. 3 Once the Remove Attributes window opens, the checkboxes for removable effects become active, so switch on whichever attributes you want gone. 4 (Optional) Should one of the attributes being stripped be a retime effect, the Ripple Sequence checkbox lets you decide whether the Timeline ripples as a consequence. 5 Hit Apply when finished.
