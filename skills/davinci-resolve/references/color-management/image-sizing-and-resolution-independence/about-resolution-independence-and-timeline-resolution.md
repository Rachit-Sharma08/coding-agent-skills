# About resolution independence and timeline resolution

Version: DaVinci Resolve 20.3 Reference Manual. Context: Image sizing and resolution independence.
[Chapter index](INDEX.md) / [Next section](fusion-page-resize-operations-are-not-and-image-scaling.md)
<a id="source-about-resolution-independence"></a> <a id="source-changing-the-timeline-resolution"></a> <a id="source-clip-resolution"></a> <a id="source-clip-source-resolution"></a> <a id="source-fusion-effects-and-resolution"></a> <a id="source-image-sizing-and-resolution-independence"></a> <a id="source-image-sizing-and-resolution-independence-part-1"></a> <a id="source-mixing-clip-resolutions"></a> <a id="source-operations-in-the-fusion-page-that-change-resolution"></a> <a id="source-pixel-aspect-ratio-par"></a> <a id="source-super-scale-high-quality-upscaling-studio-version-only"></a> <a id="source-the-davinci-resolve-sizing-pipeline"></a> <a id="source-timeline-resolution"></a> <a id="source-using-high-resolution-media-in-lower-resolution-projects"></a> <a id="source-you-can-use-separate-timelines-to-output-different-resolutions"></a> <a id="source-you-dont-need-separate-timelines-to-output-different-resolutions"></a>

### Image Sizing and Resolution Independence

DaVinci Resolve counts as a resolution-independent application. What that means is that no matter your source media's resolution, it can come out at whatever other resolution you please, and nearly every size-dependent effect across your project, text, grade windows, edit and input clip scaling, and the rest, scales to suit the new output resolution. It also means you may freely combine clips of any resolution, dropping 4K, HD, and SD clips into one timeline, each scaling to match the project resolution as needed. The resolution of your project can shift whenever, letting you work at one resolution and then deliver at another. That likewise makes it simple to put out several versions of a program at differing resolutions, say 4K, HD, and SD sizes of the same timeline. On top of that, most controls that transform clips, whether to push into a clip for creative reasons or to pan and scan media of one format so it sits better in another output format, are clever enough to keep referring back to the source resolution as they combine resizing operations to first shrink and then enlarge an image for whatever reason while you work across the Cut, Edit, Fusion, and Color pages. How the various sizing and transform controls in DaVinci Resolve relate to one another, and how they cooperate to manage clip and effect sizing intelligently as you work, is what this chapter covers.

### About Resolution Independence

If you read only one paragraph here, make it this one: Resolution Independence in DaVinci Resolve lets you add clips to a timeline in any blend of resolutions to suit whatever project resolution you've settled on, and lets you afterward output that timeline at as many other resolutions as you need to make multiple deliverables. When you do, every effect and transform readjusts itself automatically to fit the sizing of each new timeline resolution, and most transforms get calculated and processed at the full native resolution of the source media you've tied to that clip. Put briefly, this means you can produce multiple deliverables at multiple resolutions just by altering the timeline resolution, or by using a lower resolution setting on the Deliver page versus the timeline resolution when you set up a new render job, and every effect comes out the right size on its own.

### Timeline Resolution

Among your project's most fundamental settings is the timeline resolution, which defines its frame size. You find it in the Master Settings panel of the Project Settings, where you either pick a predefined resolution from the "Timeline resolution" drop-down menu or type a custom resolution into the X and Y fields beneath it.

The project-wide Timeline Resolution parameters, sitting in the Project Settings window's Master Settings panel

### Mixing Clip Resolutions

Media you use in a project needn't match the timeline resolution. Indeed, blending several resolutions inside one timeline is very common. Any clip that doesn't match the current resolution is resized automatically per the Image Scaling setting currently chosen (described below).

### Changing the Timeline Resolution

As noted earlier, the timeline resolution is yours to change whenever you wish. When you do, every Edit page transform scales accurately and automatically to suit the new resolution, and so does each Fusion clip effects output, each Color page Power Window, every Input and Output Sizing adjustment, each tracking path, each spatial keyframing value, plus any other resolution-dependent Resolve FX effect or transform operation in DaVinci Resolve.

### You Can Use Separate Timelines to Output Different Resolutions

From DaVinci Resolve 16 on, you may create separate timelines carrying individual Format (Input Scaling included), Monitoring, and Output Sizing settings for cases where you must set up multiple timelines to make multiple deliverables with different resolutions, pixel aspect ratios, frame rates, monitoring choices, or output scaling options than the overall project, "Mismatched Resolution Files" settings among them. For more information, see Chapter 34, "Creating and Working with Timelines."

### You Don't Need Separate Timelines to Output Different Resolutions

Thanks to the way DaVinci Resolve operates, separate timelines aren't required when all you want is to output the same timeline at several resolutions. You can instead concentrate on mastering one timeline, which you then output to as many other resolutions as you need. As an example, from one lone timeline in a project sitting at 4096x2160 (4K DCI) resolution, you can readily turn out UHD and HD deliverables, plus center-cut SD and center-cut Instagram sized ones, in any format you require, just by altering the Resolution drop-down on the Deliver page Render Settings before you set up a render job. DaVinci Resolve handles the rest.

Within the Render Settings panel, the Deliver page drop-down menu sets which resolution the current timeline is output at

### Using High Resolution Media in Lower Resolution Projects

Every group of transform and sizing parameters and settings that resizes clips is merged intelligently, so that a clip's full source media resolution always serves as the source for any transform. Take, for example, using 8K media inside a 1920x1080 project where you need to enlarge a clip with the Input Sizing palette's Zoom parameter to 200%; the image scales relative to the source's native 8K resolution, and the outcome is fit into the current timeline resolution. That automatically secures top quality for any image transform you make, as long as you don't zoom past any given clip's native resolution.

The same holds when, say, you shrink a clip on the Edit page with the Edit Sizing controls only to re-enlarge that clip on the Color page with the Input Sizing controls. Here DaVinci Resolve is clever enough to do the arithmetic that folds together project resolution along with the Edit Sizing and Input Sizing controls, so a single transform lands on that clip's native source resolution and yields the finest-quality outcome. NOTE: Applying Fusion effects to any clip alters this, as the discussion later in this chapter explains.

### Clip Source Resolution

In DaVinci Resolve, clip resolution is determined by the combination of Pixel Aspect Ratio and Resolution.

### Pixel Aspect Ratio (PAR)

The Timeline Format settings, located in the Master Settings of the Project Settings, let you set a Pixel Aspect Ratio for the project on top of the frame size. This defaults to Square Pixel, which suits high definition projects and most digital media. There are, though, options as well for 16:9 anamorphic, 4:3 standard definition, or Cinemascope. Which ones show up depends on the timeline resolution you've chosen. Beyond that, each clip carries its own adjustable PAR settings in the clip attributes, for when you're blending several media types within one project. If, for instance, you're mixing SD clips that have non-square pixels with HD clips that have square pixels, you can gather every SD clip in the Media Pool and give them the correct non-square pixel ratio PAR setting, whether NTSC or PAL. For more, see Chapter 22, "Modifying Clips and Clip Attributes."

### Clip Resolution

Normally a clip's resolution rests entirely on whatever resolution was set when the media got shot, or rendered out of a compositing, VFX, or 3D package. After a piece of media is made, its native resolution is locked, and to keep that clip's sharpness ideal, you must make sure any resizing transform you apply zooms in by no more than 10-20% beyond the native resolution (if that much), since otherwise the image visibly softens. Even so, DaVinci Resolve supplies advanced Super Scale image processing within every video and image clip's Clip Attributes, letting you resize clips past their native resolution while the apparent sharpness of a clip still inside its native resolution is preserved. It's an illusion, but a convincing one.

### The DaVinci Resolve Sizing Pipeline

The various sizing controls DaVinci Resolve makes available, and how they work in concert, are the subject of this section.

### "Super Scale" High Quality Upscaling (Studio Version Only)

When you need upscaling of better quality than the standard Resize Filters can manage, you can now turn on one of the "Super Scale" options, either in the Inspector or within the Clip Attributes window's Video panel, for a selected clip or several. Unlike the many scaling options across the Edit, Fusion, or Color pages, Super Scale really does lift the processed clip's source resolution, so that clip then carries more pixels than it did and grows more processor-intensive to handle than it was, unless you optimize the clip (which bakes the Super Scale effect into the optimized media) or cache it somehow.

Super Scale options shown within the Clip Attributes' Video panel The Super Scale dropdown menu offers 2-3-4x and 2-3-4x Enhanced, along with Sharpness and Noise Reduction options for tuning the scaled result's quality. Most Super Scale parameters come in fixed Low, Medium, or High increments, but the Enhanced modes let you apply them in variable amounts. Picking one of these options lets DaVinci Resolve bring advanced algorithms to bear on how image detail reads when you enlarge clips substantially, the way you might when cutting SD archival media into a UHD timeline, or when a clip has to be enlarged past its native resolution for a closeup. Depending on the source media you're handling, you may find that setting Sharpness to Medium gives a fairly subtle result that's tough to spot, while setting Sharpness to high should be noticeably more agreeable, though it also sharpens grain and noise in the image to an undesirable degree at the default settings. While raising Noise Reduction eases that, it likewise erodes the gains you made by raising Sharpness. In such cases, it's worth trying to keep Sharpness at Low or Medium so Super Scale sharpens every aspect of a clip, then using the Color page's Noise Reduction tools (with their extra capacity for fine-tuning) to cut the unwanted noise. TIP: Super Scale, useful as it is, taxes the processor, so be aware that switching it on will probably block real-time playback. One workaround is to make Optimized Media for any clip on which you've switched Super Scale on, given that Optimized Media "bakes in" the Super Scale effect. A second tack is to assemble a string-out of every piece of source media you'll need to enlarge at high quality, switch Super Scale on for all of them, and then render that timeline as separate clips while enabling the "Render at source resolution" and "Filename uses > Source Name" options.

### Fusion Effects and Resolution

Every bit of image processing the Fusion page performs happens ahead of effects applied by the Edit page, the lone exception being the Lens Correction effect. As for sizing and image resolution, whether the Fusion page affects resolution hinges on the way you use it. Fusion Effects Inherit the Source Resolution of a Clip Open a Timeline clip on the Fusion page and the Fusion page takes on that clip's full source resolution, whatever the Timeline resolution happens to be. Verify this by glancing at the resolution listed above the Viewer's upper-right corner. Thus, as long as you apply no operation that drops image resolution (covered later), sizing adjustments made afterward on other pages point at the same resolution the source clip has.

Above the Viewer's upper-right corner, circled in red, you can see the currently selected clip's available resolution and bit depth Fusion Clips Inherit the Timeline Resolution Combine several Timeline clips into a Fusion clip and the Fusion page takes on the timeline resolution, no matter the clip's source resolution. The image then goes out to the Edit page at this timeline resolution, and each subsequent sizing adjustment occurs against the timeline resolution, paying no heed to the source clip's original resolution.

The available resolution and bit depth of a clip converted into a Fusion Clip, now sitting at the timeline resolution of 1920x1080

### Operations in the Fusion Page That Change Resolution

Do nothing to change a clip's size on the Fusion page and its resolution holds, so you effectively send that clip's source resolution to the Edit page. Should you Merge the image with a second clip wired to the background carrying a different resolution, however, or reach for a Crop or Resize node to push the image resolution up or down, the fresh resolution then travels to the Cut and Edit pages as that clip's effective source resolution. Put briefly, within DaVinci Resolve's image processing pipeline the Fusion page hands the Edit page whatever resolution your composition's final node emits, treating that as the clip's effective resolution. Fusion Page Transform Operations Are Resolution Independent On the Fusion page, several Transform nodes operate in a resolution-independent fashion against the source clip's resolution. What this gives you is that shrinking an image to 20% with one Transform node and then bringing it back to 100% with a second Transform node leaves you an image carrying all the resolution and sharpness of the input image.
