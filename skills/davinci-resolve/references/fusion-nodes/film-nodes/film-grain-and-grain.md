# Film grain and grain

Version: DaVinci Resolve 20.3 Reference Manual. Context: Film grain, Grain.
[Chapter index](INDEX.md) / [Previous section](cineon-log-input.md) / [Next section](grain-and-light-trim-and-remove-noise-and-common-controls.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab-1"></a> <a id="source-controls-tab-2"></a> <a id="source-examples"></a> <a id="source-film-grain-controls"></a> <a id="source-film-grain-fgr"></a> <a id="source-film-grain-node-adding-grain-back-before-output"></a> <a id="source-film-grain-node-introduction"></a> <a id="source-grain-controls"></a> <a id="source-grain-grn"></a> <a id="source-grain-node-introduction"></a> <a id="source-grain-spread-controls"></a> <a id="source-input-1"></a> <a id="source-input-2"></a> <a id="source-inspector-1"></a> <a id="source-log-processing-on"></a> <a id="source-processing-examples"></a> <a id="source-spread-tab"></a> <a id="source-the-film-grain-node"></a> <a id="source-the-grain-node"></a>

### Film Grain [FGr]

### The Film Grain node

### Film Grain Node Introduction

The Film Grain node lays synthesized film grain over an image. A common workflow, when a composite mixes film-shot and digital elements, is to strip the grain away during the compositing work and then add it back onto the finished composite. Doing so sells the illusion that every element was captured in one take on a shared film stock. NOTE: While it is the more precise tool, the Film Grain node is not a drop-in replacement for the legacy Grain node, which stays available so older compositions can still load and render; even so, the Film Grain node is the better pick in nearly every situation.

### Input

Two inputs sit on the Film Grain node: one takes the image and one takes the effects mask. Input: Route the primary 2D image that should receive grain into the orange input. Effect Mask: The blue input expects a mask shape, drawn from polylines, plain primitive shapes, paint strokes, or bitmaps brought over from other tools. Hooking a mask here keeps the grain inside only the pixels the mask spans. Note that the tool finishes its processing before the effects mask is layered on.

### Basic Node Setup

You will usually drop the Film Grain node ahead of a MediaOut node in DaVinci Resolve, or ahead of a Saver node in Fusion Studio. Because source footage frequently has its grain stripped for cleaner keys and compositing, reintroducing film grain just before output makes the final composite read as more believable.

### Film Grain node adding grain back before output

### Inspector

### Film Grain controls

### Controls Tab

Every parameter that shapes how the film grain looks lives in the Controls tab. Complexity The Complexity value sets how many grain “layers” are stacked onto the image. At a complexity of 1, the node figures and applies a lone grain layer. Raise complexity to 4 and it works out four independent grain layers, then blends their averaged result into the final image. Pushing complexity higher yields richer-looking output that avoids the obvious repetition you can often spot in grain generated digitally. Alpha Multiply Turning on the Alpha Multiply checkbox makes the Film Grain node scale its output by the Alpha channel of the source image. You need this for post-multiplied images, so that grain stays clear of any region where the Alpha equals 0.0 (transparent). NOTE: Because there is no way to know a semitransparent pixel's final value until it has been merged with its background, hold off on applying log-processed grain to those elements until the compositing is done. That timing keeps the grain's strength correct. Log Processing With this checkbox on (the default), the grain's intensity is mapped onto the image nonlinearly so it tracks the grain signature of typical film. Put simply, grain intensity climbs exponentially as you move from black up to white. Switch the checkbox off and the grain lands evenly, no matter how bright the pixel underneath happens to be. A defining trait of real film grain is that its look shifts dramatically with exposure: the blacks carry almost no grain, while both the quantity and the spread of grain grow as a pixel's exposure rises. Within a film negative, the image's deepest shadows read as fully opaque, hiding the grain there; as the negative grows clearer, more of the grain surfaces in the outcome. Chemical differences

in how the R, G, B, layers each react to light give every color component of the film its own grain signature, and ordinarily the blue channel shows the heaviest grain. For that reason, the Log Processing checkbox is one of the Film Grain node's key controls: leave it on when you are matching film, and turn it off for images that call for a more linear grain response. With it switched on, the result closely echoes what you would get by placing a Linear to Log conversion before the old Grain node and a Log to Linear conversion right after it. Seed Any Fusion node whose output depends on randomness exposes a Seed slider together with a Reseed button. Feed two nodes matching seed values and they yield identical random results. Press the Reseed button to draw a fresh seed at random, or move the slider to dial one in by hand. Time Lock Switching on Time Lock prevents the random seed from spawning fresh grain frame after frame. Monochrome While the Monochrome checkbox is on (the default), grain hits the image's red, green, and blue channels in equal measure. Clear it and you gain per-channel command over the grain's Size, Strength, and Roughness. Lock Size X/Y Clear the Lock Size X/Y checkbox so you can size the grain independently along the X- and Y-axis. Size Grain size is measured against a single pixel's size, which means altering the image resolution leaves the grain's relative look untouched. At the default grain size of 1.0, each grain kernel spans about 2 pixels. Strength Grain shows up as a departure from a pixel's original color, and the greater the grain's strength, the larger that possible swing away from the starting pixel value. Take a pixel whose original value is p run through a Grain node where complexity = 1 size = 1; roughness = 0; log processing = off; the output works out to p +/- strength. Put differently, a pixel valued at 0.5 paired with a grain strength of 0.02 might land anywhere from 0.48 to 0.52. As before, that simplifies things a bit, all the more so once complexity climbs past 1. Switching on the Log Processing checkbox additionally reshapes that swing so the blacks vary less and the whites vary more. NOTE: To picture how grain acts on an image, the more mathematically minded might imagine a sine wave in which each lobe spans 1 pixel while the Grain Size sits at 1.0. The Grain Size then governs that sine wave's frequency and the Grain Strength its amplitude. This too is a bit of a simplification. Roughness Dragging the Roughness slider introduces low-frequency variation, suggesting that the grain clumps together. Set roughness to 0 and you will see the grain hold a very uniform luminance variation right across the image. Crank roughness up to 1.0 and notice the “cellular” unevenness appear in that luminance variation.

Offset Use the Offset control to align grain intensity down in the deep blacks; it shifts the values first, and only then is the grain's intensity (strength) worked out. With an offset of 0.1, for example, a pixel sitting at 0.1 picks up grain as though it were really at 0.2.

### Common Controls

Settings Tab The same Settings tab controls turn up on all Film nodes; for that reason their write-ups sit together in the chapter-ending “The Common Controls” section.

### Processing Examples

### Log Processing On

Out of the box, the blacks and the whites of the image each pick up their own distinct amounts of Grain Log Processing Off

With Log processing switched off, the Grain spreads uniformly over the whole image, just as pictured here

### Grain [Grn]

### The Grain node

### Grain Node Introduction

Compared with the newer, more faithful Film Grain node, the Grain node gives you a legacy approach to emulating film grain. It remains in the toolset purely so that older compositions can keep loading and rendering, yet for nearly any task the Film Grain node is the wiser choice.

### Input

The Grain node exposes two Inputs, one meant for the 2D image and one for the effects mask. Input: Send the primary 2D image that is to be grained into the orange input. Effect Mask: A mask shape feeds the blue input, and you can build that shape from polylines, ordinary primitive shapes, paint strokes, or bitmaps carried over from other tools. Attaching a mask at this point confines the grain to just the mask's pixels. The tool processes itself first, and the effects mask is then applied afterward.

### Basic Node Setup

Typically the Grain node goes ahead of a MediaOut node within DaVinci Resolve, or ahead of a Saver node within Fusion Studio. Its job is to restore grain that was taken out earlier in the composite.

A Grain node reinstating grain for a more believable composite Inspector

### Grain controls

### Controls Tab

All the settings that govern the grain's look are gathered in the Controls tab. Power This slider sets how strong the grain is; raising it makes the grain more visible and pronounced. RGB Difference Independent Red, Green, and Blue sliders let you tune the effect's strength channel by channel. Grain Softness This slider governs how blurry or fuzzy the grain reads, with lower values rendering it sharper and coarser. Grain Size This slider sets how large the grain particles are, and bigger numbers enlarge the grain. Grain Spacing This slider sets the grain's density, or how much grain falls in a given area; raise it and the grain looks more spread apart. Aspect Ratio This slider tweaks the grain's aspect so it can line up with anamorphic images. Alpha-Multiply Tick this checkbox to multiply the image by the Alpha, wiping any grain effect out of the black regions.

### Grain Spread controls

### Spread Tab

By means of separate curves for the red, green, and blue channels, the Spread tab regulates how much grain appears across each channel's tonal range. RGB Checkboxes Ticking the red, green, and blue checkboxes switches on each channel's own curve, giving you control over the grain level in that channel. Following typical film behavior, the blue channel would carry more grain than the red, and the green channel the least of all. A right-click inside the spline area brings up a contextual menu whose options relate to editing spline curves.

If you want fuller detail on the LUT Editor’s controls, turn to Chapter 107, “LUT Nodes,” within the DaVinci Resolve Reference Manual, or to Chapter 47 of the Fusion Reference Manual. In and Out With this control you edit curve points directly by entering their In/Out point values.

### Examples

Default Spread Left at its default, the grain falls uniformly over the whole image, just as pictured here. Real film, though, frequently carries differing grain amounts through the blacks, mids, and whites. Bell-Shaped Spread A bell curve usually makes a solid jumping-off point for grain that looks more lifelike. What you see here is an uneven distribution with the grain set to different levels in the red, green, and blue channels. Across both of these examples, the grain's power has been pushed higher than normal so the effect reads more clearly.
