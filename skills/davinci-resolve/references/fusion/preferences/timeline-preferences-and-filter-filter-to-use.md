# Timeline preferences and filter filter to use

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](script-and-script-preferences.md) / [Next section](user-interface-and-user-interface-preferences.md)
<a id="source-area-sampling"></a> <a id="source-file-io"></a> <a id="source-filterfilter-to-use"></a> <a id="source-network"></a> <a id="source-open-gl"></a> <a id="source-settings-for-filters"></a> <a id="source-the-timeline-preferences"></a> <a id="source-the-tweaks-preferences"></a> <a id="source-timeline-options"></a> <a id="source-tweaks"></a>

### The Timeline preferences

### Filter/Filter to Use

The Filter menu fills the hierarchy area beneath it with that setting and lets you edit the filters. The Filter to Use menu picks the default filter setting found in the Keyframes Editor Options menu.

### Settings for Filters

This area serves to build a new filter and spell out its settings. Begin by clicking the New button and typing the new Filter’s name. Then tick any of the tools you want the filter to hold. Only ticked tools turn up in the Keyframes Editor or Spline Editor once the filter is picked. You can also duplicate the filter with the Copy button or drop a filter from the list by clicking the Delete button.

### Timeline Options

The Timeline Options set which options in the Keyframe Editor start out switched on. A run of checkboxes maps to buttons in the Timeline, letting you fix the states of those buttons at the moment a new comp is built.

To dig further into the Keyframes Editor functions, turn to Chapter 71, “Animating in Fusion’s Keyframes Editor,” within the DaVinci Resolve Reference Manual, or to Chapter 9 in the Fusion Reference Manual.

- Autosnap Points: As you move points in the Keyframes Editor, they’ll snap to the fields or to the frames, or else stay free to move.
- Guides: As you move points in the Keyframes Editor, the point will snap to the guides set down in the Timeline graph.
- Autosnap Guides: As you move or create guides, they’ll snap to the fields or to the frames, or else stay free to move.
- Autoscale: Holds the Timeline scales steady while you change the graph’s editable spline content. Set to scroll, the Timeline scrolls horizontally and vertically to bring all, or nearly all, of the spline points into view as you change the graph’s editable spline content. Set to Fit, the Timeline zooms so every point fits within the graph, where needed.
- Tools Display Mode: This menu fixes the default sort order of the tools shown in the Keyframes Editor. You can change that default by way of the Sort order menu at the upper right of the Keyframes Editor.

### Tweaks

The Tweaks preferences hold a cluster of settings for fine-tuning Network rendering in Fusion Studio along with graphics hardware behavior.

### Network

The Network section serves to steer and watch the health of communication packets over TCP/IP while rendering across a network in Fusion Studio.

- Maximum Missed Heartbeats: This setting fixes how many times the network can be checked before communication with a Render node is cut off.
- Heartbeat Interval: This sets how much time passes between network checks.
- Load Composition Timeout: This timeout option fixes how long the Render Manger will hold on

waiting for a composition to load before it moves to another task.

- Last Slave Restart Timeout: This timeout option fixes how long the Render Manager will

hold on waiting for a render salve to answer before it turns to another render slave.

### The Tweaks preferences

### File I/O

The File I/O options serve to steer performance as frames or large media files are read off both direct and network-attached storage.

- I/O Canceling: This option switches on an operating-system feature that lets queued operations be canceled once the function that asked for them stops. It can sharpen responsiveness, above all while loading large images across a network. Switching it on will specifically sway performance while loading and reaching formats that do a great deal of seeking, such as the TIFF format. Since this option hasn’t been tested across every hardware and OS configuration, it’s wise to switch it on only once you’ve thoroughly tested your hardware and OS configuration with drive loads from both local disks and network shares.
- Enable Direct Reads: Ticking this checkbox brings a more efficient method to bear when loading a large chunk of contiguous data into memory, since it cuts down I/O operations. Not every operating system carries this ability, so it may bring on unknown behavior.
- Read Ahead Buffers: This slider fixes the count of 64K buffers devoted to reading ahead during a file I/O operation. A larger count makes pulling frames off disk more efficient, yet leaves things less responsive to changes that call for interactive disk access.

### Area Sampling

The Area Sampling options let you fine-tune RAM usage on Render nodes by trading speed for lower RAM demands.

- Automatic Memory Usage: This checkbox fixes how area sampling draws on the memory at hand. Area sampling comes into play for Merges and Transforms. With the checkbox ticked (default), Fusion gauges the RAM at hand while processing the tool and works out the right trade-off between speed and memory. Where less RAM is at hand, Fusion runs at a higher proxy level internally and takes longer to render. The image quality isn’t hurt in any way — only the time it takes to render. In node trees handling images bigger than 4K, overriding the automatic scaling and pinning the proxy scale by hand can be worthwhile. Doing so can hold RAM in reserve for later operations.
- Pre-Calc Proxy Level: Clearing the Automatic Memory checkbox switches on the Pre-Calc Proxy Scale slider. Higher values draw on less RAM but stretch render times considerably.

### Open GL

This section steers how Fusion puts your graphics card to work when compositing in 3D with the Renderer 3D node. Most settings can stay as they are, but because OpenGL hardware ranges so widely in capability and different driver revisions can now and then bring bugs, these tweaks can come in handy when you hit unwanted behavior.

- Disable View LUT Shaders: OpenGL shaders can frequently speed up View LUTs dramatically, though this can occasionally carry small trade-offs in accuracy. This setting forces Fusion to process LUTs at full accuracy on the CPU instead. Give it a try when View LUTs don’t seem to land the result you want.
- Use Float16 Textures: When your graphics hardware handles 16-bit floating-point textures, switching this on has int16 and float32 images sent up to the viewer as float16 in their place, which can lift playback performance.
- Texture Depth: Fixes the depth at which images are uploaded to the viewer.

Auto: The Auto option (recommended) lets Fusion strike the best balance of performance and capability. int8: Much like the Use Float16 Textures switch, this option can send images up to the Display View as int8; that route can run faster yet leaves a narrower range for View LUT correction. Native: With the Native option, images go up at whatever their native depth is, and so nothing is converted.

- Image Overlay: The Image Overlay is a viewer control paired with Merge and Transform tools to show a translucent overlay of the transformed image. It can help you picture the transformation when it falls outside the image bounds, though it may cost performance on selecting the tool if cache memory runs low. Three settings are on offer: None, Outside, and All.

None: This setting never shows the translucent overlay or controls, which can cut the need for background renders and, in some cases, speed up the display. Outside: This shows only those parts of the control that fall outside the image bounds, which can ease visual confusion. All: Shows every overlay of every selected tool.

- Smooth Resize: This setting can switch off the viewer’s Smooth Resize behavior while showing floating-point images. Some older graphics cards can’t filter floating-point textures or may be very slow at it. When Smooth Resize doesn’t sit well with float images, try setting this to flt16 or int.
- Auto Detect Graphics Memory (MB): Keeping Fusion open beside other OpenGL programs like 3D animation software can leave graphics memory short. In such cases you can lower by hand how much memory Fusion may use on the card. Setting this too low or too high may bring on performance trouble or data loss.
- Use 10-10-10-2 Framebuffer: Where both your graphics hardware and monitor are capable of 30-bit color — Nvidia Quadro/AMD Radeon Pro, plus certain Nvidia GeForce/AMD Radeon cards — this setting draws viewers at 10 bits per primary accuracy in place of 8 bits. Banding drops sharply while showing 3D renders or images deeper than 8-bit.
