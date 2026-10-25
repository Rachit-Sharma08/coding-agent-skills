# Object removal and pseudo color and rays

Version: DaVinci Resolve 20.3 Reference Manual. Context: Object removal, Pseudo color, Rays.
[Chapter index](INDEX.md) / [Previous section](hot-spot-and-object-removal.md) / [Next section](rays-and-shadow-and-trails.md) / [Object Removal ORm](hot-spot-and-object-removal.md)
<a id="source-analysis"></a> <a id="source-basic-node-setup-1"></a> <a id="source-clean-plate"></a> <a id="source-common-controls-1"></a> <a id="source-controls"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector-1"></a> <a id="source-pseudo-color-node-applied-to-an-image"></a> <a id="source-pseudo-color-node-introduction"></a> <a id="source-pseudo-color-pscl"></a> <a id="source-pseudo-color-rgba-controls"></a> <a id="source-rays-cir"></a> <a id="source-rays-node-introduction"></a> <a id="source-redgreenbluealpha-tabs"></a> <a id="source-render"></a> <a id="source-settings-tab"></a> <a id="source-the-pseudo-color-node"></a> <a id="source-the-rays-node"></a>

### Controls

The Object Removal controls give you a way to tune the parameters of the object analysis.

- Show Mask Overlay: Reveals the actual mask in play, tinted red, for the Object Removal.

### Analysis

- Scene Analysis: Clicking this button runs the analysis on the clip with the chosen parameters and swaps the object for a fitting background. Whenever you alter any parameter in this section, you’ll have to click it once more.
- Assume No Motion: When the camera stayed locked off during the shot while the object passed through, ticking this box makes the background analysis far simpler.
- Scene Mode: Offers several ways to analyze the scene, sharpening how the tool reads the motion of the region needing replacement so it can best work out how to fill the gap the removed object leaves.

Background: Analyzes the whole image apart from the object region. Boundary: Analyzes the boundary zone wrapping the object region. Object: Suited to analyzing an object that travels with the background, such as a sticker stuck on a window as the camera moves.

- Analysis Boundary: Sets how large the object’s boundary is for analysis.
- Show Scene Mask Overlay: Flips the scene mask overlay on or off so you can glimpse what sits

behind the mask.

### Render

- Search Range: Should you spot gray fringing on the object removal mask on certain frames as you play back the analyzed result, give the “Search Range” slider a try; it controls how many frames out from the current frame the Object Removal plugin looks for replacement image detail. With a Search Range of 20, for instance, it scans +/-20 frames either side of the current spot, 40 frames in all. The allowance of 10 frames means we look at every fourth frame. As a rule, the smallest range that still delivers an acceptable result is your best bet.
- Blend Mode: When the patch fills in fine but doesn’t sit well against the background, experiment with the Blend mode. Its default, Linear, is a straightforward cloning operation, yet Adaptive Blend is also on offer and can do better — except in cases where the replacement patch’s edges differ in color or brightness from the background.

### Clean Plate

- Clean Plate Source: Chooses where the clean plate comes from. The choices are Gray Image, which amounts to no source at all; Internal, which makes a “best guess” at building a background to fill the frame and blends that with frames it managed to fill; and External, which lets you wire your own plate into the pink input from another node.
- Build Clean Plate: Triggers construction of a fresh clean plate background according to the Clean Plate Source parameter you’ve set.
- Show Clean Plate: Ticking this box reveals the clean plate sitting behind the mask.

### Pseudo Color [PSCL]

### The Pseudo Color node

### Pseudo Color Node Introduction

The Pseudo Color node lets you generate shifts in an image’s color driven by waveforms that the node’s own controls create. You can produce these variances of the original image either static or animated.

### Inputs

The Pseudo Color node carries two Inputs: one image and one effects mask. Input: The orange input handles the main 2D image whose color gets altered. Effect Mask: The blue input takes a mask shape built from polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Hooking a mask up here keeps the pseudo color confined to the pixels lying inside the mask. The effects mask gets applied to the tool only after the tool has finished processing.

### Basic Node Setup

Since the Pseudo Color node can’t work on its own as a generator, it needs an image fed to its input from which to derive the color variations.

### Inspector

### Pseudo Color node applied to an image

### Pseudo Color RGBA controls

### Red/Green/Blue/Alpha Tabs

This node splits its controls across four matching tabs, one per RGBA color channel. Color Checkbox With this on, the Pseudo Color node acts on that color channel. Wrap With this on, waveform values that run past the permitted parameter limits fold back to the opposite extreme. High and Low Together, High and Low set the range within a given color channel that the node touches. Soft Edge This slider governs how soft the color transition’s edge is. Waveform This picks which waveform the generator builds. There are four to choose from: Sine, Triangle, Sawtooth, and Square. Frequency This sets the frequency of the chosen waveform, where larger values raise how many times the variances occur. Phase This shifts the waveform’s Phase, and animating it yields color-cycling effects. Mean This fixes the level of the selected waveform; raising it lifts the channel’s overall brightness up to its permitted ceiling. Amplitude Amplitude turns the waveform’s overall power up or down.

### Common Controls

### Settings Tab

Every Effect node carries the same Settings tab controls, which is why their write-ups live in the “The Common Controls” section wrapping up this chapter.

### Rays [CIR]

### The Rays node

### Rays Node Introduction

Rays is a reworked zoom blur effect that streams through an object outward from a point you designate.

### Inputs

The Rays node carries two inputs — an image one alongside an effects mask one. Input: The orange input handles the main 2D image that receives the rays. Effect Mask: The blue input takes a mask shape made from polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools. Wiring a mask in here holds the rays to the pixels inside the mask. This effects mask is applied to the tool after the tool has been processed.
