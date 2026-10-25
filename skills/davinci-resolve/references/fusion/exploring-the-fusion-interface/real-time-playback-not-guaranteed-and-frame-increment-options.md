# Real time playback not guaranteed and frame increment options

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](fusion-time-ruler-and-transport-controls.md) / [Next section](fusion-studio-transport-controls-and-navigation-shortcuts.md)
<a id="source-audio-monitoring"></a> <a id="source-audio-toolbar-button"></a> <a id="source-controlling-playback"></a> <a id="source-frame-increment-options"></a> <a id="source-fusion-studio-transport-controls"></a> <a id="source-looping-options"></a> <a id="source-real-time-playback-not-guaranteed"></a> <a id="source-render-range-fields"></a> <a id="source-the-current-time-field"></a> <a id="source-the-fusion-page-viewer-quality-and-proxy-options"></a> <a id="source-the-render-start-and-render-end-time-fields"></a> <a id="source-transport-controls-in-fusion-studio"></a>

### Real-Time Playback Not Guaranteed

A great many of the effects built on the Fusion page demand heavy processing, so smooth playback at the project’s full frame rate cannot be promised unless your composition has been cached beforehand (covered farther on).

### Frame Increment Options

A contextual menu appears when you right-click either the Play Reverse or the Play Forward button. Inside it you can assign a frame increment value, after which a keyboard shortcut will advance the playhead in either sub-frame or multi-frame steps. Stepping by several frames at once comes in handy while rotoscoping. Stepping by a fraction of a frame helps when rotoscoping or when reviewing interlaced frames one field at a time (0.5 of a frame).

To set the step size the playhead jumps by, right-click either the Play Forward or the Play Backward button.

### Looping Options

Toggling the Loop button turns playback looping on or off. Right-click the same button to pick which looping behavior is applied:

- Playback Loop: The playhead runs to the end of the Time Ruler and then restarts from the top.
- Ping-pong Loop: Once the playhead hits the end of the Time Ruler, playback reverses back toward the start of the Time Ruler, and from there it keeps bouncing back and forth.

### Render Range Fields

Use the pair of time fields on the left of the transport controls to adjust the Render Range. Either type values in frames or drag inside the fields to set the In and Out of the render range used for previews and caching.

### The Render Start and Render End time fields

### Audio Monitoring

When you play a composition on DaVinci Resolve’s Fusion page, the audio comes from the Edit or Cut page Timeline. The Audio toolbar button to the left of the transport controls lets you decide whether to listen to that audio or silence it. To help you time your animations, the audio waveforms show up in the Keyframes Editor. TIP: Any Timeline track whose Mute button is on will not be audible from within Fusion. In Fusion Studio, audio is brought in through the Loader node’s Audio tab. This audio support exists in Fusion Studio mainly as a scratch track, for lining up effects against audio and clip timing. As a rule, final renders are produced without audio. Audio plays back only when it has been loaded through a Loader node. To listen to the audio from a particular Loader node: right-click the Speaker icon and pick the file name holding the audio you wish to hear.

### Audio Toolbar Button

Acting as a toggle, the toolbar’s Audio button turns the clip’s audio playback on or mutes it. Right-clicking the same button also brings up a contextual menu, from which you can pick a MediaIn node on the Fusion page or, in Fusion Studio, an external WAV file to use for playback.

### The Current Time Field

Sitting at the right end of the transport controls, the Current Time field reports the frame number at the playhead, matching the frame currently shown in the viewer. Click and drag within it to scrub the playhead forward and backward. You may instead type time values into the field to advance the playhead by an exact amount. While defining ranges or typing frame numbers to reach a given frame, the values you enter may include sub-frame fractions. For example, a range could run from –145.6 to 451.75, or the playhead could sit at 115.22. This proves quite useful for animating parameters, since keyframes can land exactly where they belong instead of snapping to a whole-frame boundary, yielding more natural animation. Working in sub-frame time also lets you drive time remapping nodes — or simply scale keyframes in the Spline view — while keeping precision intact.

### The Fusion Page Viewer Quality and Proxy Options

Right-click anywhere inside the transport control area — except over the Play Forward/Play Reverse buttons — to switch Fusion quality controls on or off. From there you can either turn on high-quality playback and accept the longer processing it requires, or drop into one of several proxy modes that briefly reduce your composition’s display quality so the software keeps up while you work. None of these choices affect final output, which always renders at full quality. High Quality While assembling a composition, the speed at which you can work usually matters more than how the displayed image looks. The High Quality setting lets you choose between snappier interactivity and final render quality. With High Quality switched off, demanding, time‑consuming steps such as area sampling, anti-aliasing, and interpolation are bypassed so the viewer image renders sooner. Switching High Quality on forces a full-quality render to the viewer that matches exactly what final delivery produces. Motion Blur The Motion Blur button works globally. Switching Motion Blur off temporarily suspends motion blur across the whole composition, no matter which individual nodes have it turned on. Doing so can markedly accelerate viewer renders. Before this button does anything, motion blur has to be enabled on the individual nodes first. Proxy The Proxy setting is a draft mode meant to speed up processing as you build your composite. Switching Proxy on lowers the resolution of the images sent to the viewer, shortening render times by processing only one pixel out of every x rather than every single pixel. A slider governs the value of x; you will find it within the Proxy section of the Fusion > Fusion Settings > General panel. Auto Proxy This control likewise serves as a draft mode for speeding up processing as you build your composite. Switching Auto Proxy on lowers the image resolution only while you click and drag to tweak a parameter. The moment you let go of that control, the image returns to full resolution. This makes adjusting processor-intensive operations feel smoother, sparing you the jerkiness of waiting for each frame to render at full quality. To dial in the auto proxy ratio, adjust the matching slider housed under the Proxy section of the Fusion > Fusion Settings > General panel.

Selective Updates As you work in Fusion, only the tools required to show the viewer image are refreshed. The Selective Update options pick which mode governs previews and final renders. These too live under the Proxy section of the Fusion > Fusion Settings > General panel. Here are the three:

- Update All (All): Drives every node in the current node tree to render. Its chief purpose is refreshing all the thumbnails on display in the Node Editor.
- Selective (Some): Renders only those nodes feeding directly into the current image. The label reflects that nothing but the selective nodes get rendered. It is the default.
- No Update (None): Suppresses rendering altogether, a help when you need to apply many changes to a composition that renders slowly.

### Transport Controls in Fusion Studio

In Fusion Studio, the transport controls offer playback buttons, time fields along the left for defining the global range and render range, and a Render button that kicks off rendering of the composite. The right side carries additional controls for proxy and motion blur, and the field at the far right shows the current time.

### Fusion Studio transport controls

### Controlling Playback

Beneath the Time Ruler in Fusion Studio sit eight transport controls. The first four are Composition First Frame, Step Backward, Play Reverse, and Stop; the remaining four are Play Forward, Step Forward, Composition Last Frame, and Loop.
