# Eyes and nose

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Previous section](face-location-and-tracking-and-age-shift.md) / [Next section](remove-motion-blur-dialog-overview.md)
<a id="source-after-blemish-removal"></a> <a id="source-ai-blemish-removal"></a> <a id="source-ai-motion-deblur"></a> <a id="source-ai-slate-finder-and-ai-slate-id"></a> <a id="source-ai-ultrasharpen"></a> <a id="source-eyebrows"></a> <a id="source-eyes"></a> <a id="source-mouth"></a> <a id="source-nose"></a> <a id="source-the-original-footage"></a>

### Eyes

- Adjust Eyes Separately: Ticking this box breaks the toolset into left and right eyes handled on their own.
- Adjust Eyes: Ticking this box turns the Eyes toolset on or off.
- Size: Scales the eyes’ overall size up or down.
- Height: Scales how wide open the eyes sit.
- Separation: Sets how far apart the eyes are.
- Position: Shifts the eyes higher or lower on the face.
- Angle: Sets the tilt angle of the eyes.
- Eyebag: Shifts where the bags beneath the eyes sit.

### Nose

- Adjust Nose: Ticking this box turns the Nose toolset on or off.
- Size: Scales the nose’s overall size up or down.
- Width: Scales the nose’s width up or down.
- Height: Scales the nose’s vertical height on the face up or down, rather than how far it juts

out from the face.

### Mouth

- Adjust Mouth: Ticking this box turns the Mouth toolset on or off.
- Size: Scales the mouth’s overall size up or down.
- Position: Shifts the mouth higher or lower on the face.
- Width: Sets how wide the mouth is.
- Smile: Bends the angle of the mouth toward a smile or a frown.

### Eyebrows

- Adjust Eyebrows Separately: Ticking this box opens up a separate left / right Eyebrow toolset.
- Adjust Eyebrows: Ticking this box turns the Eyebrow toolset on or off.
- Position: Slides the brow higher or lower along the face.
- Separation: Sets how far apart the eyebrows are.
- Thickness: Scales the eyebrows’ thickness up or down.
- Tilt : Sets the angle of the eyebrows.

### AI Blemish Removal

Blemish Removal is an AI powered tool aimed at clearing facial and skin blemishes such as acne, scars, and other imperfections. As the resolution of video cameras climbs, a face in close-up can blow up even the faintest skin flaw into a glaring distraction. This is a dead-simple skin-smoothing tool, and your actors will love you for it.

- Strength: Sets how much Blemish Removal is applied.

### The original footage

### After Blemish Removal

NOTE: Faces deliberately dirtied (think a firefighter with soot across their face) can throw Blemish Removal off.

### AI Slate Finder and AI Slate ID

Slate Finder leans on AI to spot slates (clapper boards) on its own and flag where they sit across your clips, the clapper close point included. Slate ID reads off the Scene, Take, Angle, Shoot Day and whatever else is written on the slate, then hands you choices for filling in a clip’s metadata. Being an AI based operation, Slate Finder and Slate ID first need an AI model pulled down from the Extras Download Manager. To work through slates, in the Media Page pick the clip or clips bearing the slates you’re after, then rightclick one of them and choose AI Tools > Analyze for Slate. Alternatively, switch on Analyze for Slate inside the AI Clip Analysis tool, whose icon sits up top of the Media Pool.

Slate Finder has pinned down the frames the slate turns up in and tagged them with a yellow duration marker. NOTE: At this beta stage, Slate Finder and Slate ID remain works in progress, so not every function may be fully there yet.

### AI UltraSharpen

UltraSharpen is built to deliver exceptionally high-quality sharpening across moving video images. Because UltraSharpen is an AI tool, it sharpens selectively, hitting only the spots it judges need it rather than blanketing the whole image. Put plainly, a shot that’s a touch soft or out of focus may well be salvageable through UltraSharpen. It can likewise lift the resolution of low resolution footage in a smart way.

The subject in this frame is slightly out of focus

The subject with UltraSharpen — see how detail climbs across the face and hair while the background is left alone. The tool couldn’t be simpler, carrying just one control. Sharpen Amount: Dial in how much sharpening lands on the image.

### AI Motion DeBlur

Motion DeBlur is an AI tool built expressly to clear away the usual motion blur artifacts, softness in a clip among them. The payoff is crisper, sharper-focused images out of footage captured at slow shutter speeds. Being an AI based operation, Motion DeBlur first needs an AI model pulled down from the Extras Download Manager. Motion DeBlur renders fresh media clips onto your workstation and drops them into your Media Pool, leaving the original footage in place.

The original footage with motion blur.

The crisper footage after the Motion DeBlur operation.

To run Motion DeBlur on a clip: 1 In the media pool, pick one or more clips. 2 Right-click one of them and choose AI Tools > Remove Motion Blur 3 Set the file name, codec, and mode within the Remove Motion Blur dialog 4 Hit Render. NOTE: Motion DeBlur leans hard on your resources, and analysis can run as long as 60 seconds for every second of footage.
