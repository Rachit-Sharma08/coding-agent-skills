# Chroma keyer chroma key tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Chroma keyer.
[Chapter index](INDEX.md) / [Previous section](alpha-divide-and-alpha-multiply-and-chroma-keyer.md) / [Next section](chroma-keyer-and-delta-keyer-node-introduction.md) / [Chroma Keyer CKy](alpha-divide-and-alpha-multiply-and-chroma-keyer.md)
<a id="source-chroma-key-tab"></a> <a id="source-clean-plate"></a> <a id="source-clean-plate-node-introduction"></a> <a id="source-common-controls"></a> <a id="source-fusion-2459"></a> <a id="source-how-to-create-a-clean-plate"></a> <a id="source-image-tab"></a> <a id="source-inputs-3"></a> <a id="source-inspector-2"></a> <a id="source-matte-tab"></a> <a id="source-the-chroma-key-image-tab"></a> <a id="source-the-chroma-key-matte-tab"></a> <a id="source-the-chroma-key-tab"></a> <a id="source-the-clean-plate-node"></a>

### Inspector

### The Chroma Key tab

### Chroma Key Tab

Use the Chroma Key tab to make the first color pick for keying. Key Type The Key Type menu sets which selection method drives the matte creation.

- Chroma: The Chroma method builds a matte off the RGB values of the chosen color range.
- Color: The Color method builds a matte off the hue of the chosen color range.

Color Range You make colors transparent by selecting the Chroma Keyer node in the node tree, then dragging a selection over the colors in the viewer. The range controls refresh on their own to mirror your current color pick. Although you can nudge the range sliders a little, picking colors in the displays is usually all it takes. Lock Color Picking Switch this checkbox on and color picking from the viewer is turned off, guarding against accidental additions to the range. Turning it on once you've made the matte's color pick is wise. Every other control in the node stays editable. Soft Range This control eases the chosen color range outward, pulling extra colors into the matte. Reset Color Ranges Click this button to reset the Chroma Keyer's range controls and drop every color pick. All the remaining sliders and controls keep their values.

### The Chroma Key Image tab

### Image Tab

Mostly the Image tab deals with stripping spill color off the foreground subject. Spill happens when light carrying the color you're removing bounces onto the foreground subject. Spill Color This menu picks the color serving as the foundation for every spill suppression technique. Spill Suppression This slider sets how much spill suppression hits the foreground subject. At a setting of 0, no spill suppression applies. Spill Method This menu picks the strength of the algorithm that applies spill suppression to the image.

- None: Pick None when there's no spill suppression to do.
- Rare: This takes off very little of the spill color and is the gentlest method of all.
- Medium: This performs best on green screens.
- Well Done: This performs best on blue screens.
- Burnt: This performs best on blue. Reserve this mode for the most troublesome shots. You'll most likely

need to add heavy color correction after the key to recover, say, your skin tones. Fringe Gamma This control tunes the brightness of the fringe or halo ringing the keyed image. Fringe Size This grows and shrinks the fringe or halo around the keyed image. Fringe Shape Fringe Shape pushes the fringe toward the image's outer edge or toward the fringe's inner edge. The effect shows most clearly while the Fringe Size slider sits at a large value. Cyan/Red, Magenta/Green, and Yellow/Blue Reach for these three controls to color correct the image's fringe. They help fix semitransparent pixels that still hold color from the old background so it matches the new one.

### The Chroma Key Matte tab

### Matte Tab

Through the Matte tab you refine the resulting matte's softness, its density, and how well it fits overall. Filter This control picks the filtering algorithm applied when blur hits the matte.

- Box: The fastest method, though quality drops. Box suits small amounts of blur best.
- Bartlett: Also called a Pyramid filter, Bartlett strikes a fine balance between speed

and quality.

- Multi-box: Choose this filter and the Num Passes slider shows up, letting you govern the

quality. At 1 and 2 passes, results match Box and Bartlett in turn. From 4 passes upward, results usually rival Gaussian, in less time and with no edge “ringing.”

- Gaussian: Built on a genuine Gaussian approximation, the Gaussian filter delivers excellent results, albeit a touch slower than the others. Now and then it yields an extremely slight edge “ringing” on floating-point pixels.

Blur Matte Blur softens the matte's edge according to the Filter menu setting. A value of zero gives a sharp, cutout-style hard edge. Higher values pile more blur onto the matte. Clipping Mode This option sets how edges get handled during domain of definition rendering. It matters a great deal when blurring the matte, which may need samples from parts of the image beyond the current domain.

- Frame: The default, Frame, automatically sets the node's domain of definition to span the image's full frame, in effect disregarding the current domain of definition. Where the upstream DoD is smaller than the frame, the leftover frame area counts as black/transparent.
- Domain: Set this option to Domain to honor the upstream domain of definition while applying the node's effect. That can cause unwanted clipping wherever the node uses a large filter.
- None: Set this option to None and no source image clipping happens at all. So any data the node's effect needs that would ordinarily fall outside the upstream DoD counts as black/transparent.

### FUSION 2459

Contract/Expand This slider trims or enlarges the matte's semitransparent areas. Values over 0.0 enlarge the matte; values under 0.0 trim it. You'd usually pair this control with the Matte Blur to soften a matte's hard edge and cut fringing. Because it touches only semitransparent areas, it does nothing to a matte's hard edge. Gamma Matte Gamma lifts or drops the matte's values across the semitransparent areas. Higher values push the gray areas toward opaque, lower ones push them toward transparent. Fully black or white regions of the matte are left alone. Because it touches only semitransparent areas, it does nothing to a matte's hard edge. Threshold This range slider fixes the lower threshold via the left handle and the upper threshold via the right handle. Anything under the lower threshold setting goes black or transparent in the matte. Anything over the upper threshold setting goes white or opaque in the matte. Everything inside the range keeps its relative transparency. This control often serves to knock out salt and pepper noise in the matte. Restore Fringe This brings back the matte's edge around the keyed subject. Keying often clips out the subject's edge where there's hair. Restore Fringe returns that edge while keeping the matte solid. Invert Matte Tick this checkbox and the keyer's alpha channel flips, so every transparent area turns opaque and every opaque area turns transparent. Solid Matte Solid Mattes are mask nodes or images wired into the node's solid matte input. The solid matte goes straight onto the image's alpha channel. As a rule, solid mattes hold out keying in areas meant to stay opaque, like someone with blue eyes against a blue screen. Turning on Invert flips the solid matte ahead of it being combined with the source alpha. Garbage Matte The garbage mattes are themselves mask nodes or images wired into the node's garbage matte input. The garbage matte goes straight onto the image's alpha channel. As a rule, garbage mattes strip out unwanted bits that can't be keyed, such as microphones and booms. They also serve to fill in areas holding the keyed color that you'd rather keep. You can't mix garbage mattes of differing modes inside a single tool. A Matte Control node frequently follows a Keyer node to add a garbage matte whose effect opposes the matte applied at the keyer. Turning on Invert flips the garbage matte before it's combined with the source alpha. Post-Multiply Image Pick this option so the keyer multiplies the image's color channels against the alpha channel it builds for the image. This option is generally enabled and on by default.

Clear this checkbox and the image no longer counts as premultiplied when you merge it with other images. Reach for the Merge node's Subtractive option rather than the Additive one. For further detail about these Merge node settings, consult the DaVinci Resolve Reference Manual, Chapter 95, "Composite Nodes," or else the Fusion Reference Manual at Chapter 35.

### Common Controls

Settings Tab Other matte nodes carry a copy of the Inspector's Settings tab as well. The chapter's closing “The Common Controls” section walks through these shared controls thoroughly.

### Clean Plate

### The Clean Plate node

### Clean Plate Node Introduction

A pre-keying node, the Clean Plate tool builds an image of the green or blue color screen so as to even out lighting differences. Later the Clean Plate's output feeds the Clean Plate input on the Delta Keyer, so the Delta Keyer can key fine detail without choking or clipping the matte.

### How to Create a Clean Plate

Making a clean plate works the reverse of making a key. Keying has you removing the green or blue color, whereas making a clean plate has you preserving as much of the blue- or green-screen as you can. Box-selecting stretches of the screen color in the viewer leaves you with an image of the green/blue screen. Everything outside the blue or green screen reads as a transparent cutout.

With the selection in hand, the Erode control widens the pre-matte, clearing away stray small pixels of non-green/blue screen near the edges. Growing the pre-matte then plugs the holes until you've got a solid blue or green image.

### Inputs

Inside the Node Editor the Clean Plate node carries three inputs. Input: The orange input takes a 2D image holding the green or blue screen. Garbage Matte: The white garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and any image areas inside the matte get left out of the clean plate. For a clean plate, garbage mattes ought to cover whatever lies outside the blue or green screen. Effect Mask: The optional blue input anticipates a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines where the clean plate is generated to certain pixels. An effects mask gets applied to the tool once the tool has been processed.
