# Curves palette and colorslice palette

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the color page.
[Chapter index](INDEX.md) / [Previous section](media-pool-and-node-editor.md) / [Next section](clip-details-window-and-customizing-the-color-page.md)
<a id="source-blur-palette"></a> <a id="source-clip-details"></a> <a id="source-clip-info"></a> <a id="source-clips-proxy-clip-cache-ref-transform-ref-mode"></a> <a id="source-color-warper-palette"></a> <a id="source-colorslice-palette"></a> <a id="source-convergence-stereo-grade-stereo-display"></a> <a id="source-curves-palette"></a> <a id="source-dual-monitor-layout"></a> <a id="source-file-name"></a> <a id="source-info-palette-displaying-clip-info-and-system-status"></a> <a id="source-key-palette"></a> <a id="source-keyframe-editor-video-scopes-and-information"></a> <a id="source-magic-matte-palette"></a> <a id="source-qualifier-palette"></a> <a id="source-reel-name-start-tc-end-tc-duration-frames"></a> <a id="source-sizing-palette"></a> <a id="source-stereoscopic-3d-palette"></a> <a id="source-system-info"></a> <a id="source-the-color-page-in-dual-screen-mode"></a> <a id="source-the-info-palette-and-clip-information"></a> <a id="source-tracker-palette"></a> <a id="source-version-frame-rate-source-res-codec"></a> <a id="source-window-palette"></a> <a id="source-wipe-style"></a>

### Curves palette

### ColorSlice palette

### Color Warper palette

### Qualifier palette

### Window palette

### Tracker palette

### Magic Matte palette

### Blur palette

### Key palette

### Sizing palette

### Stereoscopic 3D palette

### Keyframe Editor, Video Scopes, and Information

The bottom right of the Color page can be flipped among one of three things:

The trio of controls that bring up the Keyframe Editor, the video scopes, or the Information palette Keyframe Editor: Hands you an interface for animating Color, Sizing, and Stereo Format adjustments across time. Every node in the Node Editor lines up with a track in the Keyframe Editor, so each node’s adjustments can be animated separately. Beyond that, a node’s track opens up to reveal parameter groups, letting you animate subsets of one node’s functions independently of that node’s other functions. For more on keyframing, consult Chapter 148, “Keyframing in the Color Page.” Video scopes: Gives you a docked spot in which a single video scope can be surfaced at a time for reference while you work. The video scopes can also be “undocked” into a stand-alone window capable of showing four different scopes at once. More on the video scopes comes later in this chapter. Information: Offers a means of viewing clip and system information as you work.

### Dual-Monitor Layout

The Color page offers a dual monitor layout that hands the primary monitor as much room as possible for the Viewer, Node Editor, and Control palettes, while the secondary monitor simultaneously displays a Gallery, Lightbox, Keyframe Editor, Metadata Editor, and Video Scope panel. A dual-screen layout’s second screen can be resized but not rearranged. Even on a single ultra-wide monitor you can adopt the dual-monitor layout, and DaVinci Resolve scales the interface as if a pair of ordinary monitors stood next to each other. To enter dual-screen mode: Choose Workspace > Dual Screen > On.

### The Color page in dual screen mode

To swap which UI elements land on which monitors: Choose Workspace > Primary Display > (Monitor Name), which flips the contents of the two monitors while in dual screen mode.

### The Info Palette and Clip Information

The Info palette stays hidden by default. Click the Info palette button at the far right of the toolbar to reveal it. It carries two tabs that show different information, and it holds no user-editable controls.

### Info palette displaying Clip Info and System Status

### Clip Info

The first tab reports on whichever clip is currently selected in the Timeline. None of this is editable; it’s provided for reference, and it includes:

### File Name

### Reel Name Start T/C End T/C Duration Frames

The disk file name of the media. Where the current clip is a Multicam clip, this instead shows whichever angle is selected. That clip’s reel name, provided one is being read correctly. The first frame’s source timecode value within the clip. The last frame’s source timecode value within the clip. How long the clip runs, expressed in timecode. How long the clip runs, expressed in frames.

### Version Frame Rate Source Res Codec

Which remote or local version the clip uses. The frame rate the clip runs at. The source clip’s native resolution. Which codec or format the source clip uses.

### System Info

The second tab reports on the operational modes DaVinci Resolve is currently running in. It’s meant to convey the state of the various DaVinci Resolve features that can be turned on, turned off, or cycled through different options. This information includes:

### Clips Proxy Clip Cache Ref Transform Ref Mode

### Wipe Style

### Convergence Stereo Grade Stereo Display

How many clips the Timeline holds in total. Whether Proxy mode is on (On or Off). Where the Clip Cache mode stands (Off, All, Dissolves, User, User & D). Where Reference Still reposition stands. Where the Reference mode stands (Gallery, Timeline, Offline). Whichever Wipe Style is chosen for split screens (Wipe-H, Wipe-V, Wipe-M, Wipe-A). The Convergence setting in force (Linked Zoom, Opposite) Whichever Eye and Gang mode shows (Left or Right - Gang or Solo). The Stereo Display mode in force (Mono or Stereo).

### Clip Details

You can right-click whichever clip is currently selected in the Thumbnail Timeline and pick View Clip Details to bring up a small window holding all of that clip’s information at a glance. Drag this window wherever you like, even onto another display.
