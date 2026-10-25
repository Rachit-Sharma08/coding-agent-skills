# Creating a custom voice for the speech generator and speech generator vs voice convert

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Previous section](ai-intellisearch-and-setting-up-intellisearch.md) / [Next section](depth-map-and-lens-properties.md)
<a id="source-ai-cinefocus"></a> <a id="source-aperture-mode"></a> <a id="source-creating-a-custom-voice-for-the-speech-generator"></a> <a id="source-depth-mode"></a> <a id="source-focus"></a> <a id="source-focus-mode"></a> <a id="source-result"></a> <a id="source-speech-generator-vs-voice-convert"></a>

### Creating a Custom Voice for the Speech Generator

Crafting a custom voice for the Speech Generator is easy. All it takes is an audio file of the person speaking for roughly twenty seconds, captured as a clean, high-fidelity signal. After that, just bring the file into the Speech Generator via the Custom setting in the Voice Model dropdown menu. Pointers for capturing the best voice sample:

- A 10-20 second recording is all it takes. Indeed, anything longer gets trimmed back to its first 20 seconds for Speech Generator analysis.
- See to it that the voice recording stays clean, carrying good levels and little noise.
- Aim to keep your pacing steady, with no long gaps and no swings in volume or emotion if an

even result is what you’re after.

- Stuck on what to record? Give the “Harvard Sentences” a read aloud for twenty

seconds or thereabouts. They’re built to be phonetically balanced for the frequency of the English language.

- Experiment to see what works.

IMPORTANT: Be sure you’ve secured permission before using a real person’s voice, and that the creative voice talent is being paid fairly!

### Speech Generator vs. Voice Convert

Though their overall effect is alike, the input powering the two AI speech tools differs greatly. Speech Generator spins up a fresh audio file and performance out of written text, whereas Voice Convert takes an existing audio file and aims to match the tonality and performance of that exact clip, only with a different voice. On top of that, Speech Generator’s voices can be built from nothing more than a short snippet of audio, so it’s quick to deploy, while Voice Convert needs a longer source file and analysis time to build a voice model.

### AI CineFocus

CineFocus lets you build your own custom virtual lens that mimics realistic defocus and bokeh effects. It makes phone camera footage look as though it were shot on a real cinematic lens, or it can hand you added post-production control over professionally captured footage from any camera you like. The complete lens-build toolset teams up with an AI-generated Depth Map to construct a working depth model out of a 2D image, then wraps it in an easy-to-use graphical interface on the viewer. Switch on the Open FX overlay in the viewer and a split-prism icon becomes your pointer. As long as your shot came in entirely crisp, say off a phone camera, a single click on a region in the viewer “focuses” the lens onto that subject, while the remaining CineFocus parameters dictate what gets thrown out of focus, where, and in what manner.

The original phone footage, with everything in sharp detail.

The same image, with the focal point changed to the wall.

The same image, this time with the focal point moved onto the temple The effect runs left to right through the four mode tabs along the top of the inspector.

### Depth Mode

Press this button to bring up the depth map view and switch on the Depth Map toolset. Brighter objects sit “closer” to the camera, grey areas land in the mid-field, and darker areas fall into the distance. This view reveals what the AI judges to be nearer or farther from the camera, and it can be reshaped with the Depth Map controls below.

The CineFocus Depth Map view. Brighter areas are “closer” in depth.

### Focus Mode

Press this button to bring up the focus mode view and switch on the focus controls. The colored areas sit in focus, whereas grayer areas get defocused. While the OpenFX overlay is on, a click focuses an area in the viewer, and you can also click-drag the split prism icon to mark out a range of focus. From there the CineFocus controls act on the defocused (gray) parts of the image.

The CineFocus Focus view; the greyed-out areas fall out of focus. The split prism icon lets you click areas in the viewer to bring them into focus.

### Aperture Mode

Press this button to bring up Aperture mode. This view depicts the inner physics of the virtual CineFocus lens. It lets you visually sculpt your lens properties as you move the sliders. Along the diagram’s upper edge it traces the light path fanning out from the foreground that sits “in front” of the focal point (over on the left), passing through the focal point (that narrow middle), and on to the background “behind” the focal point (over on the right). Below the light path sit Bokeh “slices” drawn from the range above that let you see the Bokeh’s shape and size at a fixed distance.

The CineFocus Aperture view. Showing the virtual lens characteristics.

### Result

Press this button to view the CineFocus tool’s final outcome and tweak any parameter in the effect further.

### Focus

With this toolset you reshape the virtual lens’s focus parameters. Reaching for the Focus mode view above can show you these tools’ results in finer detail.

- Bokeh Quality: Enhanced scales quality off the source resolution, yielding finer detail though it can drag at a high aperture size. Better turns out softer bokeh while running more efficiently. “Faster” ramps up the optimizations alongside frame resolution.
- Aperture Size: Move this slider to alter the virtual aperture. Higher values pile more blur onto the image’s out-of-focus areas.
- Focus Distance: Set this to fix the virtual lens’s focal point, working off the data from the depth map. This virtual lens can’t focus in units of meters or feet; instead it’s a percentage value keyed to the Depth Map. Keyframing and animating this value lets you “pull focus” between one distance and the next.
- Depth of Field: Depth of Field (”DoF“ in photography) gauges the range of depths counted as in-focus. Within CineFocus this can be stretched artificially to hold a subject perfectly in focus without your having to dial down the strength of the near/far defocus”.
- Track Focus to Point: Tick this box so focus trails a point you set in the FX Overlay over in the viewer. The FX Tracker can then take that point and track focus across the whole clip.
- No Foreground Blur: Tick this box to strip the blur off the foreground, keeping it sharp. That makes it simpler to be sure a foreground subject stays in focus when that’s the aim, and the option can also lift performance.
- Focus Peaking: Tick this box to switch on focus peaking lines that flag the parts of the frame that are in focus. This echoes the same function real cameras carry.
- Boost Highlights: Raise the brightness of the highlights. It steers the balance of dark and bright regions where they’re blurred together. This can help brighten bokeh set against dark backgrounds, and it can broadly tune the result depending on your color management
