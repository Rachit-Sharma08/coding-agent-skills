# Depth map and difference keyer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Depth map, Difference keyer.
[Chapter index](INDEX.md) / [Previous section](delta-keyer-node-introduction-and-depth-map.md) / [Next section](difference-keyer-and-luma-keyer.md) / [Depth Map DMp](delta-keyer-node-introduction-and-depth-map.md)
<a id="source-basic-node-setup-1"></a> <a id="source-common-controls-1"></a> <a id="source-controls-tab"></a> <a id="source-difference-keyer-dfk"></a> <a id="source-difference-keyer-node-introduction"></a> <a id="source-inputs-1"></a> <a id="source-the-depth-map-controls-tab"></a> <a id="source-the-difference-keyer-node"></a>

### The Depth Map Controls tab

### Controls Tab

Every parameter for dialing in the quality of the finished matte lives on the Depth Map's Controls tab.

- Mode: Depth Map leans hard on computation. Its quality setting offers a Faster mode that keeps responses to your tweaks snappy, whereas the default Better mode delivers top quality and is best switched on once you've stopped adjusting.
- Depth Map Preview: This box starts out checked, showing the present Depth Map so you can make tweaks. Uncheck it and the resulting Alpha becomes available for grading over on other nodes.
- Invert: Tick this and the Depth Map flips, trading its transparent and opaque regions.

Resulting Map Adjustment Use these controls to dictate how the Depth Map's contrast gets tuned.

- Adjust Map Levels: Left off (the default), all scaling is suspended so you can work the Depth Map's full range. Switch it on and the option pins the Depth Map's levels to 0 and 1. That previews what becomes of the Depth Map once it serves as an Alpha channel, where the values are forever clamped to 0 and 1. Ticking this box also lights up the tools beneath it.
- Far Limit: This one tunes the Depth Map's black levels.
- Near Limit: This one tunes the Depth Map's white levels.
- Gamma: This one shifts the in-between depth values brighter or darker relative to

the fixed black and white levels. Isolate Specific Depth With these controls you can travel forward and back through the scene by depth, picking out one depth band to adjust.

- Isolation: This checkbox flips the depth isolation tools on or off.
- Target Depth: This picks the exact depth to single out. 1 lands fully in the foreground, whereas

0 lands fully in the background.

- Tolerance: Fixes how far on each side of the Target Depth gets folded into the Depth Map.
- Softness: This eases a gentle ramp-in and ramp-out at the edges of the chosen band for a more

natural selection. Map Finesse These controls reshape the finished Depth Map's Alpha channel so it suits grading.

- Post Processing: This toggles the Map Finesse tools on or off.
- Post-Filter: This blends the map onto the image's smooth zones and edges. Its job is to

keep later grading effects from visibly drifting within the region.

- Contract/Expand: This dilates or erodes the whole shape along its edges, handy for fine

tuning where the map's affected and unaffected regions meet.

- Blur: This eases the map's boundary so it folds more seamlessly into the

resulting image.

### Common Controls

Settings Tab This Inspector Settings tab shows up again on the other Matte nodes too. The shared controls it holds are spelled out fully where the chapter ends, in the "The Common Controls" section.

### Difference Keyer [DFK]

### The Difference Keyer node

### Difference Keyer Node Introduction

Difference keying works by deriving a matte from the gap between two images. It draws on a pair of inputs: one that shows the subject sitting in front of the background, and one that shows the background by itself. Plausible as that sounds up front, small shifts in camera placement between the two shots normally make clean results hard to achieve. Picture the hopeless task of keying smoke against a brick wall while handing it a clean plate of that same brick wall as the difference input. Some of the wall's texture never quite disappears with this approach. So a Difference Keyer tends instead to deliver a rough matte that you marry to other nodes for a finer one.

### Inputs

Over in the Node Editor, the Difference Keyer node offers four inputs. Background: This orange background input takes a 2D image showing the set alone, minus your subject. Foreground: The green foreground input takes a 2D image of the shot with your subject present in the frame. Garbage Matte: The gray garbage matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and the image regions inside that matte turn transparent. Solid Matte: The white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here and the image regions inside that matte turn fully opaque. Effect Mask: The optional blue input looks for a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wire a mask here to pin down which pixels the difference matte covers. That effects mask reaches the tool only after the tool has finished processing.

### Basic Node Setup

Lacking footage shot against a blue or green screen, you can slot the Difference Keyer in as one link among many in a chain that lifts an object off its background. In the example here, MediaIn1 supplies the main subject and a clean background plate without the subject fills the Background. A B-Spline reins in the area the Difference Keyer has to wrestle with during extraction. What comes out is a matte that assists the key without fully cracking it.

A Difference Keyer fed two inputs: one showing the subject over a background, the other showing that background by itself Inspector
