# Auto align and color match buttons and options for auto processing

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](stereoscopic-palette-clip-adjustments.md) / [Next section](floating-window-controls-and-animating-floating-windows.md)
<a id="source-auto-align-and-color-match-buttons"></a> <a id="source-auto-processcolor-matching"></a> <a id="source-auto-processstereo-alignment"></a> <a id="source-floating-windows"></a> <a id="source-monitoring-controls-for-stereo-3d"></a> <a id="source-options-for-auto-processing"></a> <a id="source-stereo-3d-monitoring-controls"></a> <a id="source-stereo-3d-output-options"></a>

### Auto align and color match buttons

### Options for Auto Processing

The frame used to automatically analyze and process stereo clips is selectable through the Alignment and Matching controls in the Stereo 3D palette option menu. Pick Auto Process > First or Middle, whichever suits your media best.

### Auto Process—Stereo Alignment

If the stereoscopic effect is to read without giving viewers headaches, both eyes absolutely must be aligned. Adjusting this by hand is fiddly, but the software can analyze it for you automatically. You can run stereo 3D alignment on a single clip, or pick a range of clips to align them all at once. Two choices exist, and the right one depends on the kind of geometry problem you’re trying to fix.

- Transform Alignment: Examines the image and applies vertical and rotational tweaks to register the left- and right-eye images as tightly as it can.
- Vertical Skew: Examines the images and applies a vertical-only tweak to register the left- and right-eye images.

To align one or more clips automatically: 1 In the Thumbnail timeline of the Color page, highlight one or several stereo clips. 2 Decide which frame of each clip drives the analysis: open the Stereo 3D palette, click the Option menu, and pick Auto Process > First or Auto Process > Middle. 3 Click whichever of the Stereo Alignment buttons you want. The left button handles Automatic Transform; the right button handles Automatic Vertical Skew. Should you have picked several clips, the Stereo Alignment window opens and a progress bar reports how much time is left for the job.

### Auto Process—Color Matching

Owing to differences among stereo 3D rig designs, the color and contrast of one eye’s media sometimes fails to line up precisely with the other eye. DaVinci Resolve offers two commands that match two eyes together fast and automatically.

- Stereo Color Match (Primary Controls): Leans on the Lift/Gamma/Gain controls to bring one eye into line with the other. The outcome is an easily tweaked, simple adjustment that occasionally falls short of what Custom Curves can do.
- Stereo Color Match (Custom Curves): Leans on the Custom Curves to build a multipoint adjustment matching one eye to the other. The outcome tends to be more capable on difficult shots.
- Stereo Color Match (Dense Color Match): Runs a pixel-by-pixel, frame-by-frame color match of remarkable accuracy. The operation is heavy on the processor, so when batch processing lots of clips or matching lengthy clips, budget enough time. Since this match is so exact, it’s advisable to apply Dense Color Match only after running one of the stereo alignment commands.

TIP: For optimal output, run automatic color matching inside its own dedicated node, kept apart from your other corrections. The behavior of stereo 3D color match shifts depending on whether one half of the stereo 3D pair already carries a grade. The walkthrough below shows how to match a left- and right-eye pair before applying any hand adjustments at all. To match a pair of left- and right-eye clips automatically: 1 In the Thumbnail timeline of the Color page, highlight one or several clips. 2 Open the Stereo 3D palette and click any of the three Color Match controls. The Color Matching window opens, and a progress bar reports how much time remains for the job. You can likewise use automatic color matching to align an ungraded clip with a paired clip that’s already graded. That works solely for grades made up of one or more primary corrections; secondary corrections won’t auto-match. To auto-match an ungraded clip against an already-graded paired stereo clip: 1 To suspend stereo grade linking temporarily:

- Open the Stereo 3D palette, and turn off the Ripple Link button.
- Right-click the Thumbnail timeline, and choose Stereo 3D > Ripple Link > Solo.

2 Apply a primary adjustment to some clip in the left-eye timeline so as to build a basic base grade. At this point the left-eye clip carries a grade while the right-eye clip carries none. 3 Do one of the following to switch eyes:

- In the Stereo 3D palette, click Right.
- Right-click the Thumbnail timeline again, and choose Stereo 3D > Switch Eye.

This routine succeeds only if you run the Stereo Color Match commands on the ungraded half of a left- and right-eye stereo pair so as to align it with the graded half. 4 To make the match, do this: in the Stereo 3D palette, click any of the three color match controls. The two clips ought to line up with each other very closely.

### Stereo 3D Monitoring Controls

Sending both eyes to a stereo 3D display requires clicking the Vision: Mono or Stereo button and then picking a display mode from the Out pop-up menu.

### Monitoring controls for Stereo 3D

- Vision: A button toggles between Stereo — where both eyes can appear in the Viewer and feed video output across many formats — and Mono, where just one eye reaches the Viewer and your video output interface.
- Out: A pop-up menu offering various stereo viewing methods for previewing stereo 3D signals different ways. By default it also links to the Internal Video Scope options of the Viewer display. Each stereo 3D viewing mode is described thoroughly in the upcoming “Stereo 3D Output Options” section.
- Link button: While active, the Viewer and internal video scopes share the Out pop-up menu’s stereo 3D viewing choice. While inactive, you can set different stereo 3D viewing options for the Viewer and for the internal video scopes.
- Viewer: Lets you pick a stereo 3D viewing method for the Viewer.
- WFM: Lets you pick a stereo 3D viewing method for the internal video scopes.
- Cbd Size: Should any stereo 3D viewing option be set to Checkerboard, this parameter turns

active, allowing you to specify, in pixels, how big the checkerboard boxes are. On certain Blackmagic I/O devices, dual 4:2:2 Y’CbCr stereoscopic video streams are sent across HD-SDI once you switch on the ”Use left and right eye SDI output” checkbox within the Master Settings panel of the Project Settings. Depending on what your stereo-capable display supports, you can pick either Side-by-Side or Line-by-Line output to feed it.

### Stereo 3D Output Options

On top of that, the Viewer and video scopes can be configured to present both “eyes” in any of several modes.

- Side by Side: Places both images alongside each other. Each eye gets anamorphically squeezed so the pair fits the same resolution as the GUI viewer.
- Top and Bottom: Stacks both images one above the other. Each eye gets vertically squeezed so the pair fits the same resolution as the GUI viewer.
- Line by Line (Even/Odd): An interlaced mode in which the eyes alternate line by line. How thick those lines look in the Viewer scales with your zoom level.
- Checkerboard: Shows both eyes through an alternating checkerboard pattern. It’s a great mode for spotting picture regions where color or geometry differs between the two eyes.
- Anaglyph (B/W): Both eyes are desaturated and overlaid via Red/Cyan anaglyph to expose the disparity between them across different parts of the picture. Divergence in the left eye reads red, divergence in the right eye reads cyan. Areas where the eyes align show up grayscale. Anaglyph modes help judge geometric differences between the eyes and pinpoint the point of convergence (where the eyes register most precisely) that sets a picture region at the screen plane. The red/cyan coding also reveals which way the parallax runs. For any one feature, a disparity in which red sits to the right while cyan sits to the left marks positive parallax (projecting backward, away from the audience). The reverse — red on the left, cyan on the right — marks negative parallax (projecting forward, toward the audience).
- Anaglyph (Color): Like Anaglyph (B/W), except areas that align closely keep full color. As it happens, both anaglyph modes can be viewed on regular displays through old-school red/cyan anaglyph glasses, which permits stereo 3D monitoring even on displays that aren’t stereo 3D-capable.
- Difference: Overlays grayscale renditions of both eyes through the difference composite mode. Corresponding left/right-eye pixels in perfect register render black, while pixels that disagree render white. This mode is exceptionally handy for judging geometric differences between the eyes and locating the point of convergence, free of the color distraction the anaglyph modes carry.

NOTE: In the Viewer, only the eye belonging to the timeline you currently have selected is shown. That said, it works together with one checkbox — “Use Dual Outputs on SDI” — found under Master Settings within Project Settings; turning that on routes each eye to its own HD-SDI output on your Blackmagic I/O card.

The Viewer set to display an anaglyph stereo image in color

### Floating Windows

Floating Windows exist to fix “Window violations,” cases where picture elements carrying negative parallax — the ones projecting forward off the screen plane toward the audience — get clipped by the frame edge. When that happens, the mismatch between what the left and right eyes are shown produces a visual paradox viewers find hard to resolve. To be precise: once a forward-projecting element gets clipped by the frame’s left or right edge, one eye perceives something its partner never does. A fast-moving subject may make this a non-issue, but if the clipped (or occluded) element hangs around onscreen, it troubles viewers and collapses the stereo 3D illusion. Here stereopsis (the viewer’s binocular vision) supplies one depth cue at the same time that occlusion supplies an entirely contradictory one.

The remedy is to apply Floating Windows that crop the clipped object out of the eye on the side where it’s cut off, removing the slice of the stereo image hidden from the other eye that’s causing the trouble.
