# Texture pop understanding advanced mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Texture pop studio version only.
[Chapter index](INDEX.md) / [Previous section](fast-noise-and-jpeg-damage-and-texture-pop.md) / [Texture Pop (Studio Version Only)](fast-noise-and-jpeg-damage-and-texture-pop.md)
<a id="source-details-controls"></a> <a id="source-mode-controls"></a> <a id="source-tonal-range-controls"></a> <a id="source-understanding-advanced-mode"></a>

### Understanding Advanced Mode

Advanced mode is where this effect gets genuinely interesting. To get a feel for what it does, drop every Details slider to -1.000, then bring each one up on its own to watch what sort of image detail comes back, and eventually gets boosted, as you carry each slider past 0.000. In the image below, every Details slider sits at -1, the heaviest smoothing each one allows, yielding an image stripped nearly bare of detail. In that example, a person plus the mechanical workings of a helicopter shot are smoothed out by parking each detail slider at -1.000. Notice that both results keep the broad sweep of color and contrast marking out each color region, but past the high-contrast edges every bit of textural detail has melted into a clean gradient.

(Left) A shot of a person rendered with every bit of detail smoothed off, (Right) A shot of machinery likewise smoothed flat of detail

Next, walking each Details slider back up to 0 or even +1 one at a time reveals precisely which kind of detail that slider governs. In the person example, the Tiny and Fine sliders touch nothing but the very smallest details, the hairs, lines, and skin pores. Over in the helicopter, you'll watch the small textures, tiny lines, and rivet details return.

(Left) That same shot of the person, now with the Tiny and Fine sliders lifted to feed gentle detail back in, (Right) The helicopter close-up after Tiny and Fine detail are restored to it Two sets of rules of thumb apply when you're considering the detail across a human face.

- Tiny, Fine, and Small controls govern an image's smallest details, the pores

(tiny), blemishes (fine), and wrinkles (small) typical of ordinary closeups. They also reach high-frequency edge detail such as individual strands of hair, foliage on a tree, or lettering on a printed page or a screen.

- Rough, Coarse, and Medium lean toward progressively smaller shadow contouring across faces, bodies, and objects.

Naturally, how granular a given type of image detail is comes down to whether the clip is a closeup or a long shot. With the camera nearer the subject you're adjusting, far finer details fall within reach. With the camera far off, even sizable details on the subject end up governed by the Tiny, Fine, and Small controls. So an adjustment you craft for a subject in a closeup will need reworking before it suits a long shot.

### Mode Controls

- Operating Mode: Lets you switch the plugin between its Simple and Advanced modes.
- Color Mode: Lets you switch between operating in RGB and in Luma/Chroma mode. Under RGB, one

shared set of parameters drives all three color channels together. Under Luma/Chroma mode, two separate control sets let you shape the luma and the chroma on their own.

- Output Mode: Lets you switch the output among the Final Result, Differences mode (which shows the effect diffed against the source image), and Difference Magnitude, which presents a high-contrast difference comparison.

### Details Controls

- Strength: Lets you drive the other Details sliders' effect harder or pull it back.
- Details: (Simple mode only) Softens or sharpens the image's midtone detail over a wider operating range.
- Rough/Coarse/Medium: (Advanced mode only) This trio of sliders acts on the image's progressively larger contours, seeming to work on its shadows and underlying structure.
- Small/Fine/Tiny: (Advanced mode only) This trio of sliders acts on the image's progressively smaller details and texture, reaching medium down to tiny details, lines, and specks.

### Tonal Range Controls

- Shadows: Lets you dial back the effect you've built up in the image's shadows, bounded by the Low Range parameter.
- Midtones: Lets you dial back the effect you've built up in the image's midtones, bounded by the Low and High Range parameters.
- Highlights: Lets you dial back the effect you've built up in the image's highlights, bounded by the High Range parameter.
- Low Range: Lets you pin the image value marking the handoff from Shadows to Midtones.
- High Range: Lets you pin the image value marking the handoff from Midtones

to Highlights.
