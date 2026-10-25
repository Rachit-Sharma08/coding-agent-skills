# Magic mask v2 tracking

Version: DaVinci Resolve 20.3 Reference Manual. Context: Magic mask v2 studio version only.
[Chapter index](INDEX.md) / [Next section](magic-mask-v2-and-magic-mask-v1-legacy-version.md)
<a id="source-click-list"></a> <a id="source-fixing-masks-with-the-paint-tool"></a> <a id="source-magic-mask"></a> <a id="source-magic-mask-part-1"></a> <a id="source-magic-mask-toolbar"></a> <a id="source-magic-mask-v2-studio-version-only"></a> <a id="source-the-controls-of-the-magic-mask-palette"></a> <a id="source-the-magic-mask-interface"></a> <a id="source-tracking"></a>

### Magic Mask

Driven by the DaVinci Neural Engine and steered by where the user clicks, the Magic Mask palette builds precise masks on its own so you can single out people or objects, whole or partial, before applying secondary tweaks in DaVinci Resolve. The pages that follow explain how the stroke and tracking controls inside this palette let you direct these capabilities.

### Magic Mask v2 (Studio Version Only)

The AI engine beneath Magic Mask was rebuilt from the ground up, both to streamline the interface and to deliver markedly stronger output than before; this revision carries the name Magic Mask v2. Beyond sharper recognition of patterns and shapes, the gains show up most in tricky tracking scenarios, such as something crossing in front of the masked subject or other depth-related complications. The user-facing controls in Magic Mask v2 largely match the earlier Magic Mask, apart from these additions:

- Person and Object are no longer split into distinct modes. Magic Mask v2 copes with both

on its own.

- You no longer have to draw Strokes; that step now gives way to merely making

Clicks on the object to make a selection.

- A straightforward paint tool now lets you brush extra regions into or out of the

mask on a frame by frame basis. Using the DaVinci AI Neural Engine, the Magic Mask palette automagically produces a mask that singles out one or more people or objects within the frame, taking its cue from user-applied clicks that flag the subject to be separated out. You can generate masks covering a whole object or person, or limited to particular features of someone (their face, hair, arms, shoes, etc.). The two example image types below appear with Highlight switched on in the Viewer. A red onionskin overlay reveals exactly what Magic Mask has selected.

(Left) Magic Mask separating skin tones alone, (Right) Magic Mask separating the apron alone. Notice that although the apron and shirt share nearly the same color, Magic Mask reads the apron's form to build the mask. Although a mask from Magic Mask is frequently solid enough to drive high-quality isolated adjustments on its own, it will not always come out flawless. When that happens, the Matte Finesse controls allow you to soften and loosen the mask as much as you need to clean up the boundary of a tough subject you are separating with the aid of a second mask-building approach, like a qualifier key or window. To touch up a single frame in a hurry, the paint tool also lets you bring regions of the mask in or out by hand. When you are singling out particular features of someone, you can also combine different things you are separating to assemble precisely the mask you need. Following the earlier example, you might pull the face together with bare skin on the torso and arms, building a mask for one overall skin tone adjustment that leaves out the subject's hair and clothing.

Clicks you place to flag the subject drive this entire procedure. A standard workflow has you placing positive clicks (shown in blue) on top of the person or feature you intend to separate. After that, where needed, you can add subtractive clicks (shown in red) over portions of the picture that are not the person or feature being separated, fixing whatever flaws turn up in the resulting mask.

Blue clicks flag a person or feature to separate, whereas red clicks flag elements that ought to stay out of the mask. Here we placed one positive click (blue) to single out the wood cutting board, plus three subtractive clicks (red) on nearby objects that were also roughly wood-toned (the wood serving dish and pepper grinder at left, and her arm), guaranteeing they would not slip into the mask. As a rule, both positive and subtractive clicks ought to sit on the part of the person or object you mean to bring into the mask. Should a particular click you placed not produce the mask result you wanted, you can reposition it by dragging rather than clicking afresh; clicks stay live and can be picked with the pointer to be moved or removed.

One blue click on her back accurately masks her whole body, arms and hair included. Observe that Magic Mask v2 properly tells her apart from her mirror reflection, even where the two overlap.

While you work, every click appears in the Click list, where you can select, enable/disable, delete, and otherwise handle the various clicks you place to steer automatic mask generation.

The Click list keeps a record of every click you have placed.

### Tracking

Once you have placed one or more clicks to direct the analysis, the tracking controls inside this palette let you motion track those clicks so they trail the subject across that shot. When several clicks exist, all of them track together, and each click automatically rides along with whatever image detail sits right around it, so no setup is required. You merely place one or more clicks and then hit the track forward or backward button. As a click tracks, the overall tracking bar indicates which frames have already been tracked (tracked frames show blue).

Controls let you track every mask analysis click forward and backward across the shot. After you have added the clicks needed to single out the subject and motion tracked them to ride with the shot's movement, a mask is generated live and automatically for every frame of the shot. This matters because any edit you make, whether adding, removing, or hand-moving clicks, reshapes the resulting mask on the fly.

### Fixing Masks with the Paint Tool

Now and then the Magic Mask can drift during tracking and pull in something you did not want, or leave out something you did. A basic paint tool sits in the toolbar for patching gaps in the mask or stripping masked areas back out. Because the paint tool runs frame by frame, it does not track along with the mask. It works well for clearing brief mask glitches, but for anything beyond a handful of frames you are better off returning to the add and subtract tools to rework your mask.

The Add/Subtract Paint Stroke tools and the Brush Size control With the plus and minus paint tools you can place strokes onto, or pull strokes off of, the mask as needed, and the paint brush size tool lets you enlarge or reduce the brush that draws those strokes.

(Left) On this frame, Magic Mask mistakenly pulled the silver rings on her fingers into the mask. Across most of the track it did not, so only a handful of frames need correcting. (Right) Choosing the Subtract Paint Stroke tool (green circle) and tuning its size, we gently paint a gap in the mask across her rings.

The final frame, with the rings correctly excluded from the mask

### The Magic Mask Interface

Three groups of controls make up the Magic Mask palette: the Toolbar, the Click list, and the Mask Finesse panel. The Magic Mask palette starts out blank when you first open it, with a prompt telling you to click inside the Viewer to build a mask.

### The controls of the Magic Mask palette

### Magic Mask Toolbar

Most of the palette's interactive controls live in a toolbar across the top of the Magic Mask palette.

- Tracking Controls: These controls let you track all available clicks so they trail camera or subject motion within the frame. Reading left to right, they are:

Go To Reference Frame: Moves the playhead to the frame where you first placed the clicks. Go To First Frame of Tracked Area: Sends the playhead to the earliest tracked frame of a tracked range, readying you to track backward when untracked frames remain at the clip's start. Track One Frame Reverse: Steps one frame back and halts. Handy when you are tracking frame by frame to follow the progress of an especially intricate piece of motion. Should anything fail, you can return to the last frame where the click tracked the subject cleanly and drag the click to a stronger spot with the pointer so it follows correctly. If you must, advance one frame at a time, dragging the click to a better position whenever it loses the feature you are using it to single out. Track Reverse: Tracks nonstop from the current frame right back to the clip's start. Stop Tracking: Pauses the track whenever the track misbehaves and you need to adjust it. Track Forward and Reverse: Runs from the present frame through to the close of the clip, then loops back to the original tracking point and runs backward to the clip's opening. Track Forward: Tracks without pause from the present frame straight through to the clip's close. Track One Frame Forward: Advances one frame and halts. Handy when you are tracking frame by frame to follow the progress of an especially intricate piece of motion. If you must, advance one frame at a time, dragging the click to a better position whenever it loses the feature you are using it to single out. Go To Last Frame of Tracked Area: Sends the playhead to the final tracked frame of a tracked range, readying you to track forward when untracked frames remain at the clip's end.

- Click tools: A pair of tools on the right let you decide whether your clicks flag the feature you want to single out or flag things that are not the feature so you can trim away unwanted spread in the resulting mask. The plus eyedropper brings an area into the mask; the minus eyedropper takes an area out of the mask.
- Paint tools: These three paint tools handle fast touchup on a mask frame by frame. The plus paint brush adds to the mask, while the minus paint brush takes away from the mask. The paint brush size control lets you alter the brush size.
- Invert Mask: A button flips the resulting mask for cases where you want this palette's feature analysis to single out everything other than the feature or features being analyzed.
- Mask Overlay: Switches on an onion-skinned overlay so you can see which parts of the image are masked and which are not, letting you keep refining the result by adding, moving, or deleting clicks. The separated portion of the mask is shaded translucent red.

### Click List

After you begin placing clicks to flag features for mask generation, they show up in this Click list.

- Click list header: Sitting at the left of the Click list, the header carries controls for choosing and removing individual clicks.
- Click timeline area: A Timeline ruler indicates the length of the clip you are currently masking. The Overall Track shows how many frames of each click have been tracked. A small colored mark (blue or red) sits on each click track to indicate where the reference frame falls.
