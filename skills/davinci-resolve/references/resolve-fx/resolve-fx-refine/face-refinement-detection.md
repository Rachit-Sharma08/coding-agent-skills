# Face refinement face refinement filter detecting a performers face

Version: DaVinci Resolve 20.3 Reference Manual. Context: Face refinement studio version only.
[Chapter index](INDEX.md) / [Previous section](depth-map-and-face-refinement.md) / [Face Refinement (Studio Version Only)](depth-map-and-face-refinement.md) / [Next section](face-refinement-skin-texture.md)
<a id="source-adjusting-the-key-with-the-face-mask-active"></a> <a id="source-face-location"></a> <a id="source-main-controls-1"></a> <a id="source-resolve-fx-refine-part-2"></a> <a id="source-skin-isolation"></a> <a id="source-the-face-refinement-filter-detecting-a-performers-face"></a> <a id="source-the-tracking-controls-for-face-refinement"></a>

### The Face Refinement filter detecting a performer’s face

In most cases the basic tracking controls do a good enough job of tracking faces. In trickier situations, though — when the subject's head tilts away or something else in the frame blocks it — you might have to adjust the track by hand. Do that by jumping to the track's last reliable point and ticking the Interpolate (Keyframed) box. That drops keyframes automatically for the frame and turns the outlines blue to signal you're in manual mode. You can then move to the troublesome frames and click and drag to adjust the whole face by hand, or pick and adjust each separate feature as needed. As soon as you reach a point where automatic tracking holds up again, just clear the Interpolate box and hand it back to the automatic tracker.

Adjusting an eyebrow by hand in the Interpolate (Keyframed) mode With the face tracked, you're set to work. This plugin carves the tracked face into separate zones for the routine operations colorists frequently carry out — rapidly clearing blemishes, adjusting complexion hue and saturation in regionally fitting ways, reshaping lighting, sharpening worthwhile detail, and refining makeup. Since each adjustment conforms to the proportions of the detected and tracked face, your only task is making whatever adjustments you need, and DaVinci Resolve handles the rest.

### Main Controls

The top controls let you kick off the Face Refinement process.

### The tracking controls for Face Refinement

- Detect Faces in Frame: This button sets off the process of having the Face Refinement plugin's facial detection spot any faces in the frame. Be sure to land on a frame that plainly shows the face you mean to adjust. What can trip up the Detect Faces in Frame is a face that's upside-down, partly hidden, or lit oddly.

TIP: Pick a face box and it doubles as a selection box you can shift-click-drag. Doing so hunts the box for face points. On a tricky frame, nudging this around a bit often forces the detections to where you want them. When it lands, it's the quickest way to steer the Detect Faces in Frame toward a good result.

- Tracking Controls: Basic tracking controls for following facial features' motion across the clip Track Reverse: Pins down the face and tracks it backward across the clip. Track Reverse 1 Frame: Pins down the face and tracks it back 1 frame.

Find in Frame: Pins down the face in the current frame. Track Forward then Reverse: Pins down the face, then tracks it forward from the current spot and afterward in reverse from that spot. Track Forward 1 Frame: Pins down the face and tracks it ahead 1 frame. Track Forward: Pins down the face and tracks it forward across the clip.

- Show overlay: To wow your clients and judge how well Face Detection is tracking the face you're on, switch on this checkbox, which enables the wireframe tracking that reveals which facial details are being detected.

### Face Location

These controls let you set the effect's strength and also make manual tweaks to where the face and its features sit in the frame.

- Effect Strength: This slider sets the relative strength of the adjustments against the original image. 1.000 is full strength, while 0 shuts the effect off entirely.
- Interpolate (Keyframed): Ticking this box lets you hand-adjust the face and feature tracking in the Viewer and keyframes any changes for you. Click and drag in the Viewer to shift the whole face. Shift-click and drag to reframe the face. Click any single feature to adjust it, or any dot to relocate its position.

### Skin Isolation

These controls let you tweak the skin mask the plugin builds automatically so the effect stays confined to just the face of the person you're after.

### Adjusting the key with the face mask active

- Show mask: Ticking this checkbox displays the face mask as it's built, which is handy to watch while you fine-tune it.
- Skin Mask Source: Picks the origin for the skin mask. The default is DaVinci Resolve’s Internal Skin Model, though you may instead draw on the Input Alpha when you've keyed the skin tones in a separate node. None switches the mask off.
- Shadow Range: With this control you can grow or shrink the facial shadows the skin model has detected.
- Tint Range: With this control you can grow or shrink the tint range the skin model has detected.
- Temp Range: With this control you can grow or shrink the color temperature of the face picked up by

the skin model.

- Limit to Face Region: Switching on this checkbox lays down a circular garbage mask that tracks the

face so stray qualification of regions outside the face is removed.

- Region Size: Lets you tune the size of the face mask.
- Region Softness: Lets you tune the edge softness of the face mask.
- Flat Skin Areas Only: Ticking this box leaves the nose and eye-socket regions out of the

mask, so you operate only on the facial skin itself.

- Exclude Mouth: Ticking this box leaves the mouth region out of the mask, so you can

work only on the facial skin itself and not the lips.

- Denoise mask: With this slider you fill in spots of fine detail across the mask.
- Refine mask: With this slider you tweak the face mask to smooth over or close gaps in the key.
