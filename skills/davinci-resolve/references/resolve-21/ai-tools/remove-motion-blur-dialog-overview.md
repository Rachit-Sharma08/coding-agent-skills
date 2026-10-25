# Remove motion blur dialog overview

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Previous section](eyes-and-nose.md)
<a id="source-the-remove-motion-blur-dialog"></a>

### The Remove Motion Blur Dialog

Within the Remove Motion Blur dialog you can set these parameters:

- File Name: Where you name the file for the new DeBlurred media clip.
- Format: Pick the video format the new DeBlurred media clip takes.
- Codec: Pick the video codec the new DeBlurred media clip takes.
- Type: Pick the video codec type the new DeBlurred media clip takes.
- Mode: Decide how much blur to strip from the clip — standard or extreme, hinging on how much motion blur you began with.
- User selected mark in and out: Tick this box and only the media sitting between the clip’s set In and Out points renders, which keeps render times in check. Clear it and the whole clip renders.
- Render at source resolution: Tick this box and the new DeBlurred media clip renders at its source resolution. Clear it and it renders at the timeline resolution instead.
- Use more GPU memory for higher quality: Tick this box to throw more GPU ram at the operation, buying higher quality results.

A few pointers for getting more out of Motion DeBlur:

- The model usually copes well with mild motion blur that comes from slow camera panning.
- Clips carrying obvious camera shake can land fine too, as long as the main subject stays in view across every frame. Footage that keeps the subject close to the frame’s center for the whole clip especially tends to fare better. Minor shifts in framing are fine and can still turn out good results.

As an instance, capturing a city scene while strolling slowly or standing put with a bit of handheld wobble can do the trick.

- Clips holding at least a few sharp frames tend to deblur more strongly. A video might, for example, blur briefly during a step or a movement while its other frames stay reasonably clear.
- Bumping up the frame rate can help in tougher cases, though motion blur that’s extremely severe may still sit past what the model can manage.
- Steer clear of very fast camera movement, above all when the subject tears across the frame — say, corner to corner inside a handful of seconds.
