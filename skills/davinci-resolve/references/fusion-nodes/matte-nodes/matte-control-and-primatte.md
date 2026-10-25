# Matte control and primatte

Version: DaVinci Resolve 20.3 Reference Manual. Context: Matte control, Primatte.
[Chapter index](INDEX.md) / [Previous section](matte-control-controls.md) / [Next section](primatte-fine-tuning-tab.md) / [Continue Primatte Pri / Fine Tuning Tab / Selected Color](primatte-fine-tuning-tab-selected-color.md) / [Matte Control MAT](magic-mask-and-matte-control.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-inputs"></a> <a id="source-primatte-node-introduction"></a> <a id="source-primatte-pri"></a> <a id="source-spill-tab"></a> <a id="source-the-matte-control-spill-tab"></a> <a id="source-the-primatte-node"></a>

### The Matte Control Spill tab

### Spill Tab

Spill suppression in the Matte Control is managed by the Spill tab. Spill suppression is a flavor of color correction aimed at stripping the screen color out of the matte's fringe. Spill refers to the screen color passing through the alpha channel's semitransparent zones. With blue- or green-screen keying, this generally lets the background's color show up along the foreground subject's edges. Spill Color This menu picks the color that serves as the foundation for every spill suppression technique. Spill Suppression With this slider at 0, no spill suppression touches the image; raising it strengthens the spill method.

Spill Method This picks how aggressive the algorithm is that applies spill suppression to the image.

- None: Pick None whenever no spill suppression is needed.
- Rare: Strips away barely any of the spill color and is the gentlest of the methods.
- Medium: Performs best on green screens.
- Well Done: Performs best on blue screens.
- Burnt: Performs best on blue screen. Reserve this mode for especially difficult shots.

Fringe Gamma This control adjusts how bright the fringe or halo ringing the keyed image appears. Fringe Size This grows and shrinks the fringe or halo around the keyed image. Fringe Shape Fringe Shape nudges the fringe out toward the image's outer edge or draws it in toward the fringe's inner edge. A large Fringe Size value is when its effect reads most plainly. Cyan/Red, Magenta/Green, and Yellow/Blue Reach for these three controls to color correct the image's fringe. They help fix semitransparent pixels still carrying color from the original background so they match the new background.

### Common Controls

Settings Tab The Inspector's Settings tab is repeated across the other Matte nodes as well. The common controls it holds are laid out fully toward the end of this chapter within “The Common Controls” section.

### Primatte [Pri]

### The Primatte node

NOTE: Primatte is offered only within Fusion Studio.

### Primatte Node Introduction

Primatte is a sophisticated keying tool for Fusion Studio. Getting good mileage out of Primatte means grasping how it operates. By way of a set of selection buttons, Primatte sorts RGB pixels into one of four distinct zones.

Zone 1: The background image in full. Zone 2: The foreground image carrying spill suppression plus transparency. Zone 3: The foreground image carrying spill suppression alone. Zone 4: The foreground image in full. According to the variety of blue- or green-screen footage, you might discover the Delta Keyer or the Primatte keyer does a better job on a given keying task. Keying has no universal fix, and now and then pairing the two keyers turns out to be the strongest answer. NOTE: Licensing and distribution of Primatte are handled by IMAGICA Corp. of America, Los Angeles, CA, USA. The tool was created by IMAGICA Corp., Tokyo, Japan, which holds Primatte as a trademark.

### Inputs

Within the Node Editor the Primatte node carries six inputs. In contrast to every other Fusion tool, its principal orange input bears the name Foreground input, because it takes the green-screen or blue-screen image. On the Primatte node the green input acts as the background input; this optional input lets Primatte assemble the final merged composite. Foreground Input: The orange input takes a 2D image holding blue or green screen. Background Input: The green (optional) input takes a 2D image placed as the composite's background layer. With nothing connected, Primatte puts out the keyed foreground. Wiring an image into the background input switches on Primatte’s advanced edge blending options. Replacement Image: The magenta (optional) input takes a 2D image that feeds the color correction Primatte applies during spill suppression. Garbage Matte: A mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks goes into the gray garbage matte input. Wiring a mask here renders transparent any image areas falling inside the matte. That garbage matte feeds straight onto the image's alpha channel. Solid Matte: The white solid matte input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here renders fully opaque any image areas falling inside the matte. Effect Mask: The optional blue input anticipates a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps masks. Wiring a mask here confines the pixels at which keying happens. An effects mask gets applied to the tool once the tool has finished processing. NOTE: Wiring the background input while leaving the replacement image input unconnected makes the background image double as the replacement image surf spill suppression.

### Basic Node Setup

It's rare for one Primatte keyer alone to nail flawless results, since the majority of green- or blue-screen shots carry issues the keyer wasn't built to tackle. Keyers commonly lean on garbage mattes or solid mattes drawn with a Polygon or B-Spline node. A shot might also call for more than a single keyer before results are perfect. In the example below, the Primatte node has its blue-screen content wired to the orange input. Departing from other Fusion nodes, the foreground attaches to the orange input. What emerges is an image carrying alpha, which you can then feed into the foreground of a Merge node.

A Primatte node paired with a polygon matte acting as its garbage matte, then routed into the foreground of a Merge Primatte Tab View Mode The View Mode menu sits at the top of the Inspector. Its default choice presents the finished Composite result; switching it lets you inspect assorted intermediate stages of the keying process.
