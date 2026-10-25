# Magic mask v1 legacy version the magic mask interface

Version: DaVinci Resolve 20.3 Reference Manual. Context: Magic mask v1 legacy version.
[Chapter index](INDEX.md) / [Previous section](magic-mask-v2-and-magic-mask-v1-legacy-version.md) / [Next section](magic-mask-v1-legacy-version-stroke-list.md) / [Magic Mask v1 (Legacy Version)](magic-mask-v2-and-magic-mask-v1-legacy-version.md)
<a id="source-magic-mask-part-2"></a> <a id="source-the-magic-mask-interface-1"></a>

### The Magic Mask Interface


Three groups of controls make up the Magic Mask palette: the Toolbar, the Stroke list, and the Mask Finesse panel. The very first time you open the Magic Mask palette it sits empty, prompting you to draw a stroke in the Viewer so a mask can be built.

The Magic Mask palette's controls shown while in Object mode Magic Mask Toolbar Most of the palette's interactive controls reside in a toolbar running along the top of the Magic Mask palette.

- Object Mode: Clicking this icon switches the Magic Mask tool to Object mode, meant for isolating subjects that aren't people.
- Person Mode: Clicking this icon switches the Magic Mask tool to Person mode, meant for isolating people along with portions of people. Over on the left, a tab control sets which kind of mask gets built, offering two options:

Person: Builds a mask that isolates whatever portion of a person the shot's framing leaves visible. Features: Builds a mask that isolates only a single area, such as someone's face, hair, or arms. While in Features mode, you may also fold several specific features together into one mask.

- Tracking Controls: The controls here let you track every available stroke so it follows camera or subject movement across the frame. Reading from left to right, they are:

Go To Reference Frame: Jumps the playhead to the frame where you first drew the strokes. Go To First Frame of Tracked Area: Jumps the playhead to the earliest tracked frame within a tracked range, setting you up to track backward when untracked frames remain at the clip's start. Track One Frame Backwards: Steps a single frame backward, then halts. This helps when you are tracking one frame at a time to watch how a tricky stretch of motion unfolds. Should anything go awry, return to the last frame where the stroke still tracked the subject cleanly, then drag the stroke with the pointer to a better spot so it locks back onto the subject. If you must, advance one frame at a time, nudging the stroke into a better position each time it loses the feature you mean to isolate. Track All Frames Backwards: Runs continuously from the present frame right back to the clip's start.

Stop Tracking: Halts the track whenever it runs into trouble and you need to make a change. Track Forwards and Backwards: Runs from the current frame through to the clip's end, then comes back to the original tracking point and runs backward to the clip's start. Track All Frames Forwards: Runs continuously from the present frame straight to the clip's end. Track One Frame Forwards: Advances a single frame, then halts. Handy when you are tracking one frame at a time to follow how an especially complicated stretch of motion plays out. As needed, move one frame at a time, sliding the stroke to a better position each time it drops the feature you are using it to isolate. Go To Last Frame of Tracked Area: Jumps the playhead to the final tracked frame within a tracked range, getting you ready to track forward when untracked frames sit at the clip's end.

- Stroke tools: A pair of tools on the right decides whether your strokes mark the feature you intend to isolate or mark what isn't the feature, the latter to trim unwanted overflow out of the finished mask. The plus eyedropper grows the mask by an area; the minus eyedropper trims an area away.
- Invert Mask: This button flips the finished mask, useful when you want the palette's feature analysis to isolate everything other than the feature or features it analyzed.
- Mask Overlay: Switches on an onion-skinned overlay so you can see which parts of the image fall inside the mask and which don't, letting you keep refining by adding, repositioning, or removing strokes. The isolated region of the mask carries a translucent red tint.
