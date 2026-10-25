# Face location and tracking and age shift

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Previous section](additional-grain-and-ai-face-age-transformer.md) / [Next section](eyes-and-nose.md)
<a id="source-age-shift"></a> <a id="source-ai-face-reshaper"></a> <a id="source-face-location"></a> <a id="source-face-location-and-tracking"></a> <a id="source-face-shape"></a> <a id="source-the-original-image"></a> <a id="source-tracking"></a>

### Face Location and Tracking

This set of tools pinpoints the face you mean to age and follows it across the clip.

- Face Location: Tells the tool where to hunt for the face being aged. Detected: Locate the face by tracking it through the effect’s own internal tracking tools. From Input Alpha: Locate the face by drawing on an alpha channel input fed from another node. Should you need it, there’s a choice to preview that alpha channel.
- Detect Faces in Frame: Press this button and the tool rings every recognizable face in the frame with a bounding box. Where several faces show up, click a box to settle on the one you want aged. The face box in play goes green, while the rest, left untouched, sit in red.
- Track Reverse: Runs the face box backward from where you are now to the very start of the clip.
- Track Reverse 1 Frame: Steps the face box one frame backward from where you are now.
- Find in Frame: Locks the face box onto a face in the present frame, which helps when tracking got broken off.
- Track Forward then Reverse: Drives the face box back to the clip’s start, then

ahead to its end, making certain it’s been tracked across the clip from end to end.

- Track Forward: Runs the face box forward from where you are now out to the end of the clip.
- Track Forward 1 Frame: Steps the face box one frame forward from where you are now.
- Show Overlay: Tick this box to flip the face box overlay on or off inside the viewer.
- Manual Adjustments: A keyframable attribute through which you can override the tracking data driving the

face position.

### Age Shift

This set of tools steers the AI aging parameters. Every value reads in human years.

- Subject’s Age: Set this slider to match how old the subject in the frame looks to you.
- Age Offset: Set this slider to however many years you’d like added onto or pulled off the subject. From there the Face Age tool ages the subject’s face up or down on its own.

NOTE: When the Subject’s Age field carries a fairly low number (say 30), pushing the Age Offset toward lower values eventually stops doing anything, since the model can only reach so far.

### AI Face Reshaper

With the Face Reshaper you can resize and reshape the various features of a subject’s face while holding the result temporally consistent right across the clip. A light hand suits the Face Reshaper best, leaning on small, understated tweaks. Evolution has left us acutely tuned to faces, so leaning on this toolset too hard sends the result tumbling into the uncanny valley in no time.

### The original image

The Face Shape operation shrinking the size of her mouth.

Running the Face Reshaper splits into two parts. Part one is pinpointing and tracking the face you mean to shape; part two is dialing in the actual shaping you want laid on.

### Tracking

- Detect Faces in Frame: Hit this button so the tool boxes each recognizable face in the frame inside a bounding box. When more than one face appears, click a box to pick the one you’d like reshaped. Whichever face box is active turns green, and the others, left alone, stay red.
- Track Reverse: Carries the face box backward from your current spot all the way to the clip’s opening.
- Track Reverse 1 Frame: Nudges the face box a single frame backward from your current spot.
- Find in Frame: Pins the face box to a face within the present frame, handy whenever tracking got cut off.
- Track Forward then Reverse: Sends the face box back to the clip’s opening, then

onward to its close, so that it ends up tracked over the clip’s full span.

- Track Forward: Carries the face box forward from your current spot out to the clip’s close.
- Track Forward 1 Frame: Nudges the face box a single frame forward from your current spot.
- Show Overlay: Mark this box to switch the face box overlay on or off within the viewer.

### Face Location

- Manual Adjustments: A keyframable attribute letting you override the tracking data behind the face position.
- Interpolate: Should tracking errors crop up, you can plant your own start and end points for the face’s movement and let the tool fill in the frames between on its own. For the start frame, move to a frame and tick this box. For the end frame, move to a frame, drag the face box onto the face’s spot, then clear this box.

### Face Shape

- Adjust Face: Ticking this box turns the Face Shape toolset on or off.
- Size : Scales the face’s overall size up or down.
- Width : Scales the face’s width up or down.
- Length : Scales the face’s length up or down.
- Cheek Position : Sets the cheek bones higher or lower on the face.
- Chin : Scales the chin’s size up or down.
- Jaw : Scales the jaw’s size up or down.
- Forehead : Scales the forehead’s size up or down.
