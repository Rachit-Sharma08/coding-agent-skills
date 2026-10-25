# Parade scope display options and options in the parade scope

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](video-scope-types-and-qualifier-focus.md) / [Next section](options-in-the-vectorscope-and-options-in-the-histogram-scope.md)
<a id="source-options-in-the-parade-scope"></a> <a id="source-options-in-the-waveform-scope"></a> <a id="source-parade-scope-display-options"></a> <a id="source-vectorscope-display-options"></a> <a id="source-viewers-monitoring-and-video-scopes-part-4"></a> <a id="source-waveform-scope-display-options"></a>

### Parade Scope Display Options

The Parade scope has the following options:

- RGB, YRGB, and YCbCr modes, which let you assess more channels than was possible before.
- A colorize checkbox lets you view graphs either in monochrome or in false-color (marking red,

green, and blue).

- An Extents checkbox draws an outline marking every graph excursion, to plainly reveal

all overshoots and undershoots within each waveform.

- The Parade slider turns that scope's graph brighter or dimmer. Brighter graphs make fine detail

easier to catch, yet harder to judge which stretches of the graph run stronger and weaker.

- The Graticule slider turns that scope's scale brighter or dimmer, rendering it more or less visible

(or distracting) against the graph.

- The Show Reference Levels checkbox lets you switch on adjustable Low and High

reference level markers by nudging the low and high sliders off their defaults. This proves especially handy for HDR grading where you're operating within a particular peak luminance threshold.

### Options in the Parade scope

### Options in the Waveform scope

### Waveform Scope Display Options

The Waveform scope has the following options:

- Y (luma) and CbCr (chrominance) modes that show you the genuine luma or chroma signals on their own, plus RGB that shows you nothing but an RGB analysis.
- In RGB mode, R, G, and B buttons each of which can be flipped on and off on its own to view whatever combination of graphs you want.
- A colorize checkbox lets you view overlaid graphs either in monochrome or in false-color (marking red, green, and blue). Where only the Y or C scopes are switched on, the distinct stretches of these graphs get drawn in color lifted from the image under analysis, which makes it easier to see which stretch of the scope graph maps to which stretch of the image.
- An Extents checkbox draws an outline marking every graph excursion, to plainly reveal all overshoots and undershoots within each waveform.
- The Waveform slider turns that scope's graph brighter or dimmer. Brighter graphs make fine detail easier to catch, yet harder to judge which stretches of the graph run stronger and weaker.
- The Graticule slider turns that scope's scale brighter or dimmer, rendering it more or less visible (or distracting) against the graph.
- The Show Reference Levels checkbox lets you switch on adjustable Low and High reference level markers by nudging the low and high sliders off their defaults. This proves especially handy for HDR grading where you're operating within a particular peak luminance threshold.

### Vectorscope Display Options

The Vectorscope has the following options:

- Choose ALL to analyze the image’s full tonal span as a Vectorscope graph, or to isolate only the shadows (Low), the mid-tones (Mid), or the highlights (High) of the image for a vectorscope graph analysis.
- A Colorize checkbox tints the various regions of these graphs using color sampled from the image under analysis, which makes spotting which scope-graph region maps to which image region far simpler. Leave colorize off and the graphs render in plain white.
- An Extents checkbox adds an outline tracing every graph excursion, so all overshoots and undershoots are shown to you without ambiguity.
- A Combine checkbox lets you view overlapping extents for the highlights, mid-tones, and shadows at once, layered atop each other.
- The Vectorscope slider raises or lowers the brightness of that scope’s graph. Brighter graphs reveal fine detail more readily, yet make it tougher to judge which portions of the graph are stronger or weaker.
- The Graticule slider raises or lowers the brightness of that scope’s scale, rendering it more or less prominent (or distracting) against the graph.
- Low Range and High Range sliders give you manual control over the thresholds that split shadows from mid-tones and highlights. The default for Low Range is 0.30, and the default for High Range is 0.70.
- Show 2X Zoom magnifies the vectorscope graph to 200%, which helps in reading fine detail and in pairing the vectorscope with charts.
- Show Skin Tone Indicator checkbox places a line at the classic Inphase angle, handy as a rough reference for typical skin tone hue.
- Show Graticule checkbox toggles the visibility of both the circular degree markings around the outer rim and the cross hairs marking the vectorscope’s center.
