# Node editor and color page timeline

Version: DaVinci Resolve 20.3 Reference Manual. Context: Introduction to DaVinci resolve.
[Chapter index](INDEX.md) / [Previous section](work-area-and-viewers.md) / [Next section](toolbar-and-buttons-in-the-fairlight-page-toolbar.md)
<a id="source-about-audio-monitoring-and-audio-input"></a> <a id="source-audio-layering-in-a-mono-audio-track"></a> <a id="source-center-palette-selection-buttons"></a> <a id="source-center-palettes"></a> <a id="source-fairlight-page"></a> <a id="source-introduction-to-davinci-resolve-part-3"></a> <a id="source-keyframe-editor"></a> <a id="source-keyframe-editor-displaying-dynamic-grade-changes"></a> <a id="source-left-palette-selection-buttons-in-the-top-bar"></a> <a id="source-left-palettes"></a> <a id="source-node-editor-1"></a> <a id="source-the-audio-timeline"></a> <a id="source-the-audio-timeline-1"></a> <a id="source-the-color-page-timeline"></a> <a id="source-the-fairlight-page"></a>

### Node Editor

The Node Editor is where you string together one or more individual corrections (nodes) to build multi-correction grades (shown as node trees). It's a potent approach to assembling grades, because varied combinations of nodes let you produce different corrections and very particular adjustments by reordering operations, blending keys, or shifting the layer order of separate adjustments. For more on the Node Editor, refer to Chapter 143, “Node Editing Basics.”

Use the Node Editor to lay out the signal flow that processes your grade Timeline Over in the Color page, the Timeline reflects the contents of the Edit page Timeline, yet it takes on a different appearance tuned to what a colorist needs. The content is the same, though, and any change made to the Timeline in the Edit page shows up at once in the Color page as you flip between them. The Color page Timeline offers a handful of ways to move through the clips in your project and to keep tabs on what's been done to which clips.

### The Color page Timeline

Three parts divide the Timeline, each presenting different information and supplying different controls. Across the top, a Timeline Ruler lets you scrub the playhead over many clips and can be zoomed out far enough to display every clip in your whole program. Below it, the MiniTimeline (which you can open or close with a button at the right of the palette bar) presents a compact rendition of the Edit page Timeline in which each clip runs as long as its real duration. At the foot of the Timeline sits the Thumbnail timeline, where a single frame stands in for each clip. The clip currently selected is ringed in orange, and above and below each thumbnail you'll find details like its source timecode, the clip number together with the track number, the version name, plus indicators for grading, for tracking, for flagging, and the like.

### Left Palettes

A row of palettes at the lower left of the Color page opens up the various sets of grading tools, used chiefly for working on color, contrast, and raw media format settings. You open each individual palette by clicking its matching icon across the top of the Palette panel.

### Left palette selection buttons in the top bar

The palettes on offer are the Camera Raw palette (for metadata tweaks on raw media formats), the Color Match palette (which produces grades on its own by reading on-camera color charts), the Color Wheels (graphical balance controls along with master wheels or sliders that tune YRGB Lift/Gamma/Gain), HDR Grade for advanced High Dynamic Range grading, the RGB Mixer (which blends color channels into one another), plus the Motion Effects palette, whose controls handle noise reduction and synthetic motion blur.

### Center Palettes

When you're at 1920x1080 resolution or above, a second group of palettes is laid out at the lower center of the Color page. These palettes cover broad functionality, and the changes you make with them can be paired with those made through the Color palettes.

### Center palette selection buttons

NOTE: When the resolution drops, the Left and Center palettes get combined so the DaVinci Resolve interface squeezes into a tighter footprint. Among the eight Center palettes you'll find these: Curves palette, Color Warper palette, Qualifiers palette, Windows palette, Tracker palette, Magic Mask palette, Blur palette, Key palette, Sizing palette, along with the Stereoscopic 3D palette.

### Keyframe Editor

The Keyframe Editor gives you an interface for animating Color, Sizing, and Stereo Format adjustments across time. Each node sitting in the Node Editor corresponds to its own track over in the Keyframe Editor, so you're able to animate the adjustments of every node independently.

### Keyframe Editor displaying dynamic grade changes

Beyond that, each node's track can be expanded to expose parameter groups, so you can animate portions of an individual node's functions separately from other functions inside the same node.

### The Fairlight Page

When you're in single monitor mode, the Fairlight page offers an optimized view of your project's audio tracks, complete with an expanded mixer and bespoke monitoring controls that make it easy to assess and tune your program's levels and craft a smooth, balanced mix.

### Fairlight page

### About Audio Monitoring and Audio Input

The audio processing across DaVinci Resolve, on the Fairlight page as well as audio processing through Fairlight FX plugins, works identically on every platform DaVinci Resolve runs on, namely macOS, Windows, and Linux. DaVinci Resolve handles audio monitoring through:

- The audio coming from a supported Blackmagic Design I/O device, for instance an UltraStudio or a Decklink.
- The on-board audio of your macOS, Windows, or Linux workstation.
- Any interface that is Core Audio compatible, Windows compatible, or compatible with Advanced Linux Sound

Architecture (ALSA)-supported third-party audio interface.

- The Fairlight Audio Accelerator, MADI Upgrade, and Fairlight Audio Interface. DaVinci Resolve handles audio input through the embedded audio carried on an incoming SDI video feed when capturing live A/V source, by way of system audio and also through the Fairlight Audio Accelerator, MADI Upgrade, and Fairlight Audio Interface.

### The Audio Timeline

At the core of the Fairlight page, the Audio Timeline presents the channels and tracks of whichever timeline is selected in a manner unlike the Edit page, relying on a one-channel-per-track layout tuned for mixing and sweetening audio. The Audio page Timeline can't be closed.

### The Audio Timeline

### Audio layering in a mono audio track

The Fairlight page of DaVinci Resolve handles several audio tracks, and any given audio track can hold several lanes. The clips edited into the Timeline turn up within each track, with each clip's recorded channels filling as many lanes as that clip offers. Along the left of every track is a header region containing a set of controls. The Fairlight page parts ways with the Edit page Timeline in one more distinctive way, in that it supports audio layering. Audio layering is a specialized audio editing mode letting you stack several audio clips in one track, where whichever audio clip sits on top decides which audio plays. In effect, when audio layering is on, stacked audio clips behave like stacked video clips all set to 100% opacity, the topmost clips hiding (or muting) those below.

Switching on Track Layers frees up room to edit additional audio within each track

Audio layering proves enormously handy whenever you're stitching fragments of several takes into one VO, audio vocal track, or dramatic performance, because their stacked order in the track lets you decide which fragments win out, all while the remaining takes stay tucked underneath should you need them down the road. TIP: Track Layering can be used on the Edit page as well.
