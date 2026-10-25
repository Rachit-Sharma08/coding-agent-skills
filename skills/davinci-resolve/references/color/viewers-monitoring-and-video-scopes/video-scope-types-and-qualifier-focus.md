# Display qualifier focus in video scope graphs and explanation of each video scope

Version: DaVinci Resolve 20.3 Reference Manual. Context: Viewers monitoring and video scopes.
[Chapter index](INDEX.md) / [Previous section](color-viewer-marker-overlays-and-navigation.md) / [Next section](parade-scope-display-options-and-options-in-the-parade-scope.md)
<a id="source-cie-chromaticity-scope"></a> <a id="source-customizing-the-video-scopes"></a> <a id="source-different-layout-options-in-the-scope-window"></a> <a id="source-display-qualifier-focus-in-video-scope-graphs"></a> <a id="source-explanation-of-each-video-scope"></a> <a id="source-histogram-rgbyrgb-parade-histogram"></a> <a id="source-panning-and-zooming-the-video-scopes"></a> <a id="source-parade"></a> <a id="source-the-histogram-scope-set-to-yrgb"></a> <a id="source-vectorscope"></a> <a id="source-waveform-monitor"></a>

### Display Qualifier Focus in Video Scope Graphs

The Display Qualifier Focus setting within the Video Scope option menu helps you work out which features of the video picture line up with which regions of the video scopes. With Display Qualifier Focus switched on, picking the Qualifier mode of the Viewer and sliding the eyedropper across the picture traces circles around the sampled pixels wherever they show up in the video scope graph that's currently on view. Where several video scopes are on view, each scope carries its own marking, particular to that scope, of where the sampled pixels lie.

Holding the eyedropper above a feature within the Viewer Those same pixels analyzed by region, surfacing across the stacked red, blue, and green waveforms of the Waveform scope.

### Explanation of Each Video Scope

Five video scopes are on offer, and each presents a separate breakdown of the video signal you're tweaking.

### Waveform Monitor

Stacks waveform readouts — whether of the Y (luma/luminance) channel, the CBCR (the color difference channels of Y'CBCR), or the RGB (red, green, and blue) channels — atop one another so their alignment is visible to you.

The Waveform scope showing Y' (luma) only, with colorization and extents enabled. What the Y option hands you is a genuine Luma scope on which Colorize can be switched on to surface false color, letting you see where the colors of the Viewer image land within the video scope graph.

Where the RGB scopes are concerned, what the relative heights of the red, green, and blue graphs convey matches exactly the account given further down for the Parade scope, and once color is switched on those red, green, and blue graphs each pick up a tint of the color they stand for. That makes it simple to spot where all three graphs line up, by hunting for the places where stretches of the waveform monitor read as white, which results from the red, green, and blue graphs lining up and combining their color.

### Parade

The Parade scope lays out separate waveforms beside one another that gauge the strength of individual video signal components. You can configure the Parade scope to gauge RGB, YRGB, and Y'CBCR. By presenting the intensity of the luma, red, green, and blue channels side by side, the Parade scope makes spotting and weighing imbalances possible through a comparison of the relative heights of the RGB graphs across three zones — the highlights, found at the top of the R, G, and B graphs; the shadows, down at the bottom of the R, G, and B graphs; and the midtones, sitting in the middle of the R, G, and B graphs — all so you can pin down color casts and carry out scene-by-scene correction. With the YRGB channels viewed together, the foot of all graphs flags the black point of the picture, while the crest of all graphs flags the white point. From there it follows that the gap between the foot and crest of all graphs flags the overall contrast ratio of the picture under your assessment. Tall parade graphs flag a wide contrast ratio, whereas short parade graphs flag a narrow contrast ratio.

The Parade scope showing YRGB waveforms, with colorization and extents enabled

### Vectorscope

Gauges the full sweep of hue and saturation present within a picture. The readings are taken against a centered graticule, which you can switch on, overlaid upon the scope to supply a reference through crosshairs. A traditional vectorscope ships with DaVinci Resolve, its graph mimicking a trace-drawn one, where 75 percent color bar targets mark the angle of every primary and secondary color around the graph's rim, alongside an optional skin tone reference graticule (also called the In-phase reference). The Vectorscope can have Colorize switched on to surface false color, which lets you see where the colors of the Viewer image fall within the video scope graph. The more saturated colors in the frame push those stretches of the graph further out toward the rim, while the less saturated ones cling nearer the vectorscope's center, which stands for 0 saturation. By gauging how many stretches of the vectorscope graph jut out at varying angles, you can tell how

many hues sit in the picture, while the precise angle of each stretch of the graph reveals which hues those are. On top of that, by gauging how neatly the middle of the vectorscope graph centers itself against the crosshairs, you can sense whether a color imbalance is present in the picture. Should the vectorscope graph sit off-center, whichever direction it tilts toward signals that a color cast (tint) is present in the picture.

The Vectorscope displayed at 2x mode, its highlights, mid-tones, and shadows extents merged together

### Histogram (RGB/YRGB parade histogram)

Presents a statistical breakdown of how many pixels of each color channel sit at each percentage of tonality, charted along a digital scale running from 0 percent (black) up to 100 percent (white). Setting the left, middle, and right portions of the Y, R, G, and B graphs (Y being optional) against one another lets you gauge the color balance across the shadows, midtones, and highlights of the picture.

### The Histogram scope set to YRGB

Viewed together, the left edge of all graphs flags the black point of the picture, while the right edge of all graphs flags the white point. From there it follows that the gap between the left and right edges of all graphs flags the overall contrast ratio of the picture under your assessment. Wide histogram graphs flag a wide contrast ratio, whereas narrow histogram graphs flag a narrow contrast ratio.

### CIE Chromaticity Scope

DaVinci Resolve carries CIE 1931 xy and CIE 1976 uv scopes, which let you view the current image analysis as a graph laid over a triangle standing for the tristimulus values of the color gamut you're operating within, together with a marker for the current white point. A label names the gamut presently chosen, with the exact coordinates of these Red, Green, and Blue values plus the White point, while the broad "horseshoe" outline stands for the whole range of visible light, the lot of it charted upon an xy graph. The white point generally rests atop a curve tracing the center of the shape. That curve marks the black body locus, along which the assorted color temperatures of a picture's white point line up, running from orange-ish warm toward blue-ish cool. This black body locus corresponds to the color temperatures yielded by heating carbon up through successive temperatures. You've also got the choice of displaying a second gamut triangle, for occasions where you'd like to set the current analysis against two distinct gamuts. That can prove handy when your deliverables span several gamuts and you want to see which stretches of the video signal stay safe across all gamuts and which stretches push past the smaller of the pair. When you do so, a label goes on each of the two gamuts, while off to the side you'll find listed, for both gamuts, the coordinates of the Red, Green, and Blue values.

The CIE 1931 xy scope showing both P3 and Rec. 709 gamuts. Seen one way, the Chromaticity scope counts as a 3D scope, yet it's rendered as though you were peering down at the top of a 3D form that charts every color value in a picture across X, Y, Z space, while you can only make out the 2D outline tracing the broadest stretches of that form drawn upon an X, Y plot. Truly the graph accounts for each individual value that a 3D plot of the image data contains, yet the triangle marks nothing more than the broadest "slice" of the current gamut and of this 3D form across the mid-tones. The upshot is that, although the Chromaticity scope's graph hands you a rough sense of whether the current picture sits within gamut against your delivery spec, it's neither exact nor foolproof, since a portion of the image data might land inside this wide triangle yet still overshoot the demanded gamut somewhere else, up in the highlights at the top or down in the shadows near the bottom of the 3D form you're peering down upon. Conversely, should any portion of the graph reach beyond the edges of the gamut triangle, that unmistakably marks a gamut violation. An extra gamut triangle can be added within the scope settings so you can set the color space you're working in against another color space, for reference. Anyone with even passing exposure to color grading ideas will recognize the traditional CIE 1931 horseshoe graph, which charts the slice of the spectrum the human eye can perceive per studies carried out in the late 1920s (later studies have borne out this analysis). The optional CIE

1976 uv graph rests on a revised color space (CIELUV) that the International Commission on Illumination (CIE) put forward in a bid to draw a more perceptually uniform graph of color. Where the CIE 1931 analysis visually overstates certain stretches of a color graph, the CIE 1976 graph renders every stretch of a color graph roughly in proportion to the rest. On the whole, neither analysis ranks as more "correct" than its counterpart; it comes down simply to which you'd rather look at.

The CIE 1976 scope showing both P3 and Rec. 709 gamuts

### Panning and Zooming the Video Scopes

Should you wish to inspect any stretch of a video scope's graph more closely, here's what you can do: To zoom into a graph: Keep the Option key held while you spin the scroll control. To pan around a graph: Drag with the middle pointer button held down.

### Customizing the Video Scopes

Having opened the video scopes, you've got a range of ways to tailor how the scopes look and to surface extra onscreen graticule detail that helps you measure whatever you're after. Ways to tailor the Scopes window:

- To resize the Scopes window: Grab its lower right-hand corner and drag to set the Scopes window to whatever size suits you.
- To set how many scopes show simultaneously: Within the upper right-hand corner of the Scopes window, click one of the buttons to lay the video scopes out in 1, 2, 4, or 9 up arrangements. You can equally set how many scopes show at the same time by choosing Workspace > Video Scopes > 1-Up, 2-Up, or 4-Up.
- To reassign which scope sits in which pane: At the upper left corner of each scope's pane, click the Name drop-down and pick a different scope. If it suits you, you can spin up more than one of any kind of video scope within multi-scope layouts, for occasions where you'd like to view variations on one scope type carrying different settings.

To give an example, you might choose to surface three Vectorscopes, each set to a separate tonal range, so you can view Vectorscope analyses of Low (shadows), Mid (midtones), and High (highlights) all at once.

### Different layout options in the Scope window

Once it's open, you can resize the Scopes window as big or small as you need, dropping it on a secondary display should you want it bigger still. To tailor each video scope's display options: 1 Click the Option button sitting to the right of the Scope drop-down menu to surface the current scope's Custom Controls window.

Clicking to open the current scope's custom controls 2 Tweak any of the controls on offer to shape the look of that particular scope. 3 Click anywhere beyond the Custom Controls window to dismiss it.
