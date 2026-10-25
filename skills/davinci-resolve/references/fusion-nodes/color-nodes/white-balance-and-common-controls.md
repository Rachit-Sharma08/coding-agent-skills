# White balance and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: White balance, Common controls.
[Chapter index](INDEX.md) / [Previous section](white-balance-inputs.md) / [White Balance WB](set-canvas-color-and-white-balance.md)
<a id="source-balance-tab"></a> <a id="source-basic-node-setup"></a> <a id="source-color-settings-inspector"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-motion-blur"></a> <a id="source-ranges-tab"></a> <a id="source-settings-tab"></a> <a id="source-settings-tab-1"></a> <a id="source-the-common-controls"></a> <a id="source-white-balance-controls"></a> <a id="source-white-balance-range-tab"></a> <a id="source-white-balance-temperature-controls"></a>

### Basic Node Setup

As with plenty of 2D image-processing nodes, the White Balance node takes in a 2D image, such as the MediaIn1 pictured beneath. Its output carries the node tree onward, wiring into either another 2D imageprocessing node or a Merge node.

### Inspector

A White Balance node sitting on a MediaIn1 node

### White Balance controls

### Balance Tab

Space Reach for this menu to pick the source image’s color space whenever you know it. Naming it can tighten the correction, since the node then folds the color space’s natural gamma into what it does. When the image’s color space is a mystery, just leave this menu on its default. Method Two methods drive the White Balance node: a Custom method or a color Temperature method.

- Custom: The Custom method asks you to pick a scene pixel that ought to have come out pure gray. From that, the node figures the color correction needed to drag the pixel back to genuine gray. Run that correction with no effect mask wired in and the LockBlack/Mid/White checkbox on, and the node white balances the whole shot.
- Temperature: The color Temperature method asks you to state the shot’s real color temperature.

Lock Black/Mid/White Ticking this checkbox binds the Black, Midtones, and White points as a unit, so the whole image shifts by the same amount. Clear it and you get separate controls for white balancing each range on its own. The effect lands the same way regardless of which method is active. Black/Mid/White Reference These controls surface only with the Custom method chosen. Their job is picking a color off a pixel in the source image. The White Balance node then corrects the image until that chosen color turns into whatever sits in the Result Color Picker beneath, gray as a rule. Aim for a color that was meant to read pure gray yet, for whatever reason, didn’t come out truly gray. Clear the Lock Black/Mid/White checkbox and you can name a separate reference per color range. For the black and white references, for instance, hunt for pixels that aren’t clipped across any color channel. Up high, a workable case is a light-pink pixel reading 255, 240, 240. That pixel is saturated/clipped in the red even though the color isn’t white. Down low, a really dark blue-gray pixel might sit at 0, 2, 10. It too clips in red, yet it isn’t black. Neither one makes a sound reference pixel, because too little headroom would be left for the White Balance node. Black/Mid/White Result These controls show up only with the Custom method active. They set the color the node leans on to balance the reference color, defaulting as a rule to pure, midrange gray. Clear the Lock Black/Mid/White checkbox and a separate result can be set per color range. Temperature Reference With the Method menu on Temperature, the Temperature reference control fixes the source image’s color temperature. Clear the Lock Black/ Mid/White checkbox and a separate reference can be set per color range.

### White Balance Temperature controls

Temperature Result Lean on this control to dial the image’s target color temperature. Clear the Lock Black/Mid/White checkbox and a separate result can be set per color range.

Use Gamma Ticking this checkbox decides whether, while correcting, the node factors in the image’s gamma, drawing on the default gamma of whatever color space the Space menu at the tab’s top holds.

### Ranges Tab

Through the Ranges tab you can tailor which pixels in the image the node counts as shadows, as midtones, and as highlights.

### White Balance range tab

Spline Display You set the ranges by working the spline handles. Four spline points exist, each carrying a single Bézier handle. The pair of handles up top mark where the shadow and highlight ranges begin, while the pair down low mark where the range ends. Falloff is governed through the Bézier handles. There are no dedicated controls for the midtones range, since it’s simply taken to be the gap sitting between the shadow and highlight ranges. With the X and Y text controls under the Spline display you can key in exact positions for whichever Bézier point or handle is selected. Preset Simple/Smooth Ranges These two buttons snap the spline ranges back to either Smooth (default) or Simple (linear) settings.

### Settings Tab

Other Color nodes carry this same Settings tab in the Inspector. The “The Common Controls” section at this chapter’s close lays out these shared controls thoroughly.

### The Common Controls

Across the Inspector, the nodes that perform Color adjustment operations hold several matching controls. What this section covers are the controls shared among color nodes.

### Inspector

### Color Settings Inspector

### Settings Tab

Every tool in the Color category carries this Settings tab in the Inspector. Even third-party color-type plugin tools turn up with the Settings controls. The controls hold steady and behave the same from tool to tool, though a tool here and there tacks on an option or two of its own, covered here as well. Blend Use the Blend control to mix the tool’s original image input against the tool’s final reworked output image. At a blend value of 0.0, the image leaving matches the image arriving. As a rule that makes the tool bypass processing altogether, piping the input straight through to the output.

Process When Blend Is 0.0 Here the tool still runs even with the input value at zero. That earns its keep when this node’s processing is scripted to fire off some other task while the node’s own value rests at 0.0. Red/Green/Blue/Alpha Channel Selector This quartet of buttons pens the tool’s effect into the color channels you name. Typically that filtering follows after the tool has run. Take a blur tool: clear its red button and the blur still strikes the whole image first, after which the red channel from the original input is laid back over the red channel of the output. A few cases break the pattern — there, clearing a channel makes the tool skip that channel’s processing outright. Such tools usually carry a matching set of RGBA buttons over on the tool’s Controls tab, and when so, the buttons on the Settings tab and the Controls tab do the same thing. Apply Mask Inverted Switch on Apply Mask Inverted and the tool’s entire mask channel flips. That mask channel is what you’re left with after combining every mask either wired into or generated within a node. Multiply by Mask Pick this option and the masked image’s RGB values get multiplied against the mask channel’s values. Every pixel left out of the mask (that is, set to 0) thereby turns black/ transparent. Use Object/Use Material (Checkboxes) Certain 3D software can render to file formats that carry extra channels. The EXR file format in particular holds Object and Material ID channels, usable as a mask for the effect. These checkboxes settle whether those channels get used when present. Which exact Material ID or Object ID is hit gets picked through the next batch of controls. Correct Edges This checkbox turns up only once the Use Object or Use Material checkboxes are on. It switches the approach for handling where object edges overlap in a multi-object image. With it on, the Coverage and Background Color channels go toward separating and sharpening the effect around the object’s edge. Leave it off (or have no Coverage or Background Color channels on hand) and aliasing can creep in along the mask’s edge. Want more on the Coverage and Background Color channels? You’ll find it under Chapter 78, “Understanding Image Channels,” over in the DaVinci Resolve Reference Manual, while the Fusion Reference Manual covers the same ground in its Chapter 18. Object ID/Material ID (Sliders) These sliders pick which ID builds a mask out of an image’s object or material channels. Work the Sample button just as you would the Color Picker, grabbing IDs straight off the image shown in the viewer. The image or sequence has to have been rendered from a 3D software package with those channels baked in.

Clipping Mode This option governs how edges get treated during domain of definition rendering. It chiefly matters for nodes such as Blur, which may need samples drawn from parts of the image beyond the current domain.

- Frame: The default here is Frame, which on its own pegs the node’s domain of definition to the image’s full frame, effectively brushing aside the current domain of definition. Should the upstream DoD come in smaller than the frame, whatever frame area is left over reads as black/transparent.
- Domain: Switch this to Domain and the upstream domain of definition is honored as the node’s effect runs. That can bring on unwanted clipping wherever the node reaches for a large filter.
- None: Switch this to None and no clipping of the source image happens whatsoever. So any data the node’s effect needs that would ordinarily fall outside the upstream DoD reads as black/transparent.

Use GPU Three choices live on the Use GPU menu. Pick Disable to shut off hardware-accelerated rendering on your computer’s graphics card. Enabled puts the hardware to work. Auto taps a capable GPU whenever one’s around and drops to software rendering when none is.

### Motion Blur

- Motion Blur: Switches Motion Blur rendering on the tool on or off. Switched on, the tool reads its predicted motion to build the motion blur a virtual camera’s shutter would throw. Switched off, no motion blur arises.
- Quality: Sets how many samples go into building the blur. At a quality setting of 2, Fusion places two samples on each side of an object’s real motion. Bigger values smooth the outcome but stretch render time.
- Shutter Angle: Drives the angle of the virtual shutter behind the motion-blur effect. Wider angles pile on blur but lengthen render times. Set it to 360 and the shutter sits open across one full frame exposure. You can climb past that, which opens room for some interesting effects.
- Center Bias: Slides where the center of the motion blur falls. That makes motion-trail effects possible.
- Sample Spread: Tuning this control shifts how much weight each sample holds, which in turn changes the samples’ brightness.

Comments Use the Comments field to pin notes onto a tool. Click into the field and type away. Once a tool carries a note, a small red square shows in the node’s lower-left corner while its full tile is on screen, or a small text-bubble icon turns up off to the right when the nodes are collapsed. To read that note within the Node Editor, rest the mouse pointer over the node so the tooltip surfaces. Scripts From the Settings tab, every Fusion tool offers three Scripting fields. Each holds an edit box where you slot scripts that run as the tool renders. For fuller detail on scripting nodes, please turn to the Fusion scripting documentation.
