# Adjusting clips using the stereo 3D palette and stereoscopic 3D palette

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](grading-mastered-stereoscopic-media-from-tape.md) / [Next section](stereo-auto-alignment-and-color-match.md)
<a id="source-adjusting-clips-using-the-stereo-3d-palette"></a> <a id="source-automatic-image-processing-for-stereo-3d"></a> <a id="source-batch-grade-management-for-stereo-3d-projects"></a> <a id="source-protecting-stereo-adjustments-when-copying-grades"></a> <a id="source-sizing-repositioning-in-stereo-3d"></a> <a id="source-stereo-3d-geometry-controls"></a> <a id="source-stereo-eye-selection"></a> <a id="source-stereoscopic-3d-geometry-controls"></a> <a id="source-stereoscopic-3d-palette"></a> <a id="source-swap-and-copy-controls"></a> <a id="source-swap-and-copy-grades-between-eyes"></a> <a id="source-using-ripple-link-when-grading-stereo-3d-clips"></a>

### Adjusting Clips Using the Stereo 3D Palette

After you have built or imported a timeline flagged as stereoscopic 3D, grading can begin. By default the Edit and Color pages show the left eye, but a right-click on the Timeline followed by Stereo 3D Mode lets you switch to the opposite eye. The usual approach for colorists is to grade a single eye first — generally the left — and then ripple those grades across to the second eye, making distinct tweaks per eye whenever camera mismatches need correcting. DaVinci Resolve can handle that rippling for you automatically. Once stereo 3D media is configured, the Stereo 3D palette becomes available on the Color page. Every control you need for stereoscopic work lives in this palette. Among its functions: picking which eye to grade, dialing in convergence, swapping and copying both grades and media across paired left- and right-eye clips, automatically matching the color and geometry of those paired clips, configuring stereo 3D monitoring, and managing floating windows.

### Stereoscopic 3D palette

This palette will only open if your project already holds stereo 3D clips. To learn how to configure a stereo 3D project, consult the “Creating Stereo 3D Clips From Separate Files” section of this chapter.

### Stereo Eye Selection

The usual approach for colorists is to grade a single eye first — generally the left — and then ripple those grades across to the second eye, making distinct tweaks per eye whenever camera mismatches need correcting. Within the Stereo 3D palette, the first three buttons govern which eye you grade as you work and whether each clip’s grade ripples through to its opposite-eye counterpart. Each time you flip eyes, the 3D badge sitting above a clip’s thumbnail shifts color (blue meaning right, red meaning left) and the thumbnails redraw to reflect that eye’s media.

The Left eye is master and ganged with the Right Left button: Shows the left-eye image along with its grade. Ripple Link button: While active (orange), every grade change you apply to the eye that’s currently selected is mirrored automatically onto its opposite eye. While inactive (gray), any grade applied to the selected eye stays independent. Right button: Shows the right-eye image along with its grade. Another way to set which eye you view and grade is to right-click a clip’s thumbnail and pick Stereo 3D > Switch Eye, or to use View > Switch Eye To > Left Eye or Right Eye.

### Using Ripple Link When Grading Stereo 3D Clips

Switching Ripple Link off pauses the rippling, which is handy when you need to tweak a single eye’s grade on its own to bring the two into closer agreement. After the two clips line up, flip it back on and automatic grade rippling resumes. Because stereo 3D grade rippling always works relatively, any differences already present between the left- and right-eye grades stay intact. Indeed, adding or deleting nodes on one eye automatically mirrors that same node addition or deletion on its paired clip, no matter whether Ripple Linked is on or off. IMPORTANT: No matter the state of Ripple Link, any local versions you create for one stereo 3D-identified clip are automatically made available to the paired timeline.

### Stereo 3D Geometry Controls

The following set of parameters governs the geometry of stereo 3D clips. The Pan, Tilt, and Zoom controls exist here for convenience and just echo the identical parameters in the Transform palette’s Input mode, only tailored to the geometry of the left- and right-eye media. The three parameters found nowhere but the Stereo 3D palette are Convergence, Pitch, and Yaw.

### Stereoscopic 3D Geometry controls

Convergence: Tunes the disparity between left and right eyes so as to set the point of convergence (POC) — the area of the picture where left- and right-eye features line up exactly. Where required, you can animate Convergence by way of the Stereo Format parameter group located within the Sizing track of the Keyframe Editor. To work with convergence in pixel units, open the Stereo 3D palette option menu and switch on “Show convergence in pixels.” Where features sit exactly atop one another in both the right- and left-eye clips, parallax is zero, placing that feature’s depth right at the screen plane. Where matching features diverge across the left- and righteye clips, parallax grows increasingly positive and the features read as receding from the audience. Where matching features are both divergent and reversed across the left- and right-eye clips, parallax grows increasingly negative and the features read as advancing toward the audience past the screen plane. Linked Zoom button: While active (white), both left- and right-eye clips zoom together each time Convergence changes, so neither eye ever stops filling the screen. While inactive (gray), Convergence changes let blanking creep in along the opposing left and right edges of each eye’s clip. Pitch: Tips the image about the frame’s horizontal center plane. Yaw: Tips the image about the frame’s vertical center plane.

### Sizing Repositioning in Stereo 3D

Most of the time you’ll reposition stereo 3D clips while Ripple Link is on, though now and then you may need to hand-adjust one specific eye with Ripple Link off. Just like color work, Sizing changes performed with Ripple Link off apply only to the clip in the current Timeline. With Ripple Link on, every Sizing change copies automatically to the equivalently numbered shot in the partner stereo 3D timeline. WARNING: Avoid the Rotate parameter when transforming stereo 3D clips. From a geometric standpoint, rotation skews a stereo clip pair the wrong way and destroys the “side by side” convergence required for the stereoscopic illusion to hold.

### Protecting Stereo Adjustments When Copying Grades

Every grade version keeps its own stereo adjustments saved alongside the Sizing settings. So that convergence and alignment data isn’t accidentally clobbered while copying grades between clips, you can right-click inside the Gallery and enable any of these options:

- Copy Grade: Preserve Convergence
- Copy Grade: Preserve Floating Windows
- Copy Grade: Preserve Auto Align

With these on, you can replace a clip’s grade while leaving particular Stereo 3D parameters untouched. TIP: In the DaVinci Resolve image processing pipeline, Stereo 3D and Sizing settings get applied ahead of any node-based corrections.

### Swap and Copy Controls

A further group of controls along the right edge of the Stereo 3D palette handles swapping and copying grades plus swapping clips, for cases where you must reverse whatever has been applied across a left- and right-eye clip pair.

### Swap and Copy grades between eyes

- Swap Grade: Trades the grades sitting on the left- and right-eye clips.
- Swap Shot: A checkbox that, once enabled, switches the actual media used by two

corresponding left- and right-eye clips. Handy when a stereo 3D clip’s eyes got labeled incorrectly and you’d like to swap the clips without having to rebuild both EDLs.

- Copy Right to Left: Applies the right-clip grade onto its matching left-eye clip.
- Copy Left to Right: Applies the left-clip grade onto its matching right-eye clip.

### Batch Grade Management for Stereo 3D Projects

A further group of batch-processing commands handy for stereoscopic grading shows up when you right-click one or more chosen clips in the Thumbnail timeline:

- Stereo 3D Batch Copy: Duplicates every grade from the left-eye clips onto the right-eye clips.
- Stereo 3D Batch Sync: Carries grades from one eye to the other strictly when the two node graphs

share an identical node count. That safeguard stops you from inadvertently clobbering a bespoke grade whose node layout was built specifically to reconcile two eyes on a troublesome shot. Within the Stereo submenu of the Timeline contextual menu you’ll also find these commands: Copy Grade, Swap Grade, Swap Shots, Ripple Link, plus Switch Eye.

### Automatic Image Processing for Stereo 3D

On stereoscopic shoots it’s typical for small geometry and color divergences to creep into the captured footage. To ease the burden of grading stereo 3D media, DaVinci Resolve supplies a group of auto-adjustment controls along the right side of the Stereo 3D palette that hands you a starting point for matching left- and right-eye clips.
