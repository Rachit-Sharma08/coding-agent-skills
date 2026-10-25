# Tv and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Tv, Common controls.
[Chapter index](INDEX.md) / [Previous section](trails-and-tv.md) / [TV TV](trails-and-tv.md)
<a id="source-common-controls-1"></a> <a id="source-inspector"></a> <a id="source-noise-tab"></a> <a id="source-roll-bar-tab"></a> <a id="source-settings-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-common-effects-settings-tab"></a> <a id="source-the-tv-noise-tab"></a> <a id="source-the-tv-roll-bar-tab"></a>

### The TV Noise tab

### Noise Tab

The Noise tab is the second among three tabs for tailoring the analog TV distortion. This one shapes the picture's noise to mimic a feeble analog antenna signal. Power Push this slider's value past 0 to seed noise into the picture; the higher it climbs, the heavier the noise. Size Reach for this slider to blow the noise map up larger. Random Leave this thumbwheel control at 0 and the noise map holds still. Vary its value over time and the static shifts from one frame to the next.

### The TV Roll Bar tab

### Roll Bar Tab

The Roll Bar tab is the third among three tabs for tailoring the analog TV distortion. This one drives the bar's animation. Bar Strength With the default value of 0, nothing gets drawn. Raise it and the region the bar covers grows darker.

Bar Size Push this slider's value up to give the bar more height. Bar Offset Animate this control to scroll the bar across the screen.

### Common Controls

Settings Tab Since the Settings tab controls are shared by every Effect node, their write-ups sit in the “The Common Controls” section that comes next.

### The Common Controls

A number of identical controls turn up in the Inspector across all Effect nodes. The controls covered in this section are the ones Effect nodes hold in common.

### Inspector

### The Common Effects Settings tab

### Settings Tab

You'll find the Inspector's Settings tab on every tool within the Effects category, and the Settings controls show up even on third-party Effects-type plugin tools. They stay consistent and behave the same from tool to tool, though a handful of tools toss in one or two of their own options, which get covered here too. Blend The Blend control mixes between the tool's original image input and the tool's finished, altered output image. With the blend value at 0.0, the outgoing image matches the incoming one exactly, so the tool bypasses processing altogether and copies the input straight through to the output. Process When Blend Is 0.0 The tool still processes even with the input value at zero, which helps when the node is scripted to kick off some other task while the blend sits at 0.0. Red/Green/Blue/Alpha Channel Selector This quartet of buttons pins the tool's effect to particular color channels. Typically the filter kicks in once the tool has finished processing. Take a Blur tool with its red button switched off: the blur runs across the image first, after which the red channel from the original input is laid back over the result's red channel. A few exceptions exist, namely tools where switching off these channels makes the tool skip that channel's processing entirely. Such tools carry a matching set of RGBA buttons on their Controls tab, and in that case the buttons on the Settings and the Control tabs are one and the same. Apply Mask Inverted Switching on the Apply Mask Inverted option flips the tool's entire mask channel. That mask channel is the merged product of every mask wired into or produced within a node. Multiply by Mask Choose this option and the masked image's RGB values get multiplied by the mask channel's values, which turns every image pixel left out of the mask (that is, set to 0) black/transparent. Use Object/Use Material (Checkboxes) Certain 3D software can render to file formats carrying extra channels. The EXR file format in particular supports Object and Material ID channels, either of which can act as a mask for the effect. These checkboxes decide whether those channels get used when they're present, and the precise Material ID or Object ID involved is set with the next group of controls. Correct Edges This checkbox surfaces only while the Use Object or Use Material checkboxes are on. It flips between the methods for handling overlapping object edges in a multi-object image. Switched on, the Coverage and Background Color channels come into play to cleanly separate and refine the effect around an object's edge. Switched off (or with no Coverage or Background Color channels on hand), the mask edge can show aliasing. To dig further into coverage along with background channels, consult Chapter 78, “Understanding Image Channels,” within the DaVinci Resolve Reference Manual, or else Chapter 18 over in the Fusion Reference Manual.

Object ID/Material ID (Sliders) Reach for these sliders to pick which ID builds a mask out of an image's object or material channels. The Sample button works just like the Color Picker, letting you pluck IDs from the image shown in the view. That image or sequence has to have been rendered by a 3D software package with those channels baked in. Clipping Mode This option governs how the domain of definition rendering deals with edges. Clipping mode matters most once blur or softness enters the picture, since those may need samples drawn from parts of the image beyond the current domain.

- Frame: Frame is the default; it automatically points the node's domain of definition at the image's full frame, in effect disregarding the current domain of definition. Should the upstream DoD fall short of the frame, whatever remains of the frame counts as black/transparent.
- None: Pick None and no clipping of the source image takes place. Any data the node's effect needs that would ordinarily sit beyond the upstream DoD counts as black/transparent.

Use GPU The Use GPU menu carries three settings. Pick Disable and hardware-accelerated rendering on your computer's graphics card is switched off. Enabled puts the hardware to work. Auto draws on a capable GPU whenever one is on hand and drops back to software rendering when no capable GPU is around Motion Blur

- Motion Blur: This flips Motion Blur rendering on the tool on or off. With it switched on, the tool's predicted motion drives the motion blur a virtual camera's shutter would cause. With it switched off, no motion blur is generated.
- Quality: Quality fixes how many samples go into building the blur. A Quality setting of 2 has Fusion lay down two samples on each side of an object's real motion. Bigger values smooth the result but lengthen the render.
- Shutter Angle: Shutter Angle sets the angle of the virtual shutter that creates the motion blur effect. Wider angles pile on more blur but stretch the render times. A value of 360 matches a shutter held open for one whole frame's exposure. You can push past that, and higher values lend themselves to interesting effects.
- Center Bias: Center Bias shifts where the motion blur's center sits, opening the door to motion-trail effects.
- Sample Spread: Tweaking this control reweights each sample, which bears on how bright the samples come out.

Comments The Comments field lets you attach notes to a tool. Click into the blank field and type away. Once a note is on a tool, a tiny red square shows in the node's lower-left corner while the full tile is shown, or a tiny text-bubble icon appears at the right when the nodes are collapsed. To read the note inside the Node Editor, rest the mouse pointer on the node so the tooltip pops up. Scripts Every tool in Fusion offers three Scripting fields off the Settings tab. Each holds an edit box for entering scripts that fire while the tool renders. For fuller details on scripting nodes, turn to the Fusion scripting documentation.
