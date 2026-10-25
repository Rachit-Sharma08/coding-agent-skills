# Setting up a composition and reading clips into Fusion studio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md) / [Previous section](fusion-loader-saver-and-loader-parameters.md) / [Next section](photoshop-psd-and-quicktime.md)
<a id="source-aligning-clips-in-a-fusion-studio-composition"></a> <a id="source-dpx"></a> <a id="source-file-format-options"></a> <a id="source-loader-node-inputs"></a> <a id="source-openexr"></a> <a id="source-presetting-proxy-quality"></a> <a id="source-reading-clips-into-fusion-studio"></a> <a id="source-setting-up-a-composition"></a> <a id="source-using-proxies-for-better-performance"></a>

### Setting Up a Composition

Your source media may arrive in many formats, among them HD, UHD, and 4K or bigger. A single comp frequently holds a mixture of formats. Every format carries its own traits, spanning resolution, color depth, and gamma curve. While Fusion happily blends material of differing formats inside one composite, it pays to understand how Fusion Studio sets up and combines materials of differing formats as it loads and merges them. Opening Fusion Studio gives you an empty composition. Your very first task on a fresh composition is to set the preferences so they match the output format you ultimately want. Those preferences fall into two distinct groups: the global preferences and the preferences belonging to whichever composition is currently open.

Even though the Node Editor settles the final output resolution, the Frame Format preferences govern the default resolution given to new Creator tools (such as text, background, fractals, and the like), the aspect ratio, and the frame rate used during playback.

Frame Format preferences for images generated in Fusion. When you work with the same frame format every day, your global Frame Format preferences ought to reflect the footage you reach for most. As an example, on a project where most source content is 1080p high definition, lining up the global preferences with the frame format of that HD source content you commonly use makes sense. To define the default Frame Format for new compositions, proceed as follows: 1 Choose Fusion Studio > Preferences. 2 In the sidebar, click the disclosure triangle for Global and Default Settings so the Globals group expands. 3 Pick the Frame Format category so its options come into view. Choices you make in the Global Frame Format category fix the default frame format for every new composition you build. They leave existing compositions and the one presently open alone. To alter an existing composition, you must open that comp, then choose the Frame Format controls shown beneath the comp’s name in the sidebar. To dig deeper into preferences, consult the DaVinci Resolve Reference Manual at Chapter 75, “Preferences,” or else the Fusion Reference Manual at Chapter 15.

### Reading Clips into Fusion Studio

With the Frame Format preferences in place, you typically kick off a composite by reading in source media. As Fusion reads media, it neither converts nor relocates the original files; it just reads them where they sit, on whatever storage volume holds them. Throughout, you stay tied to the original source files in their original spot. A Loader tool is what reads source media into a comp. Even though Fusion Studio offers other tools that generate imagery such as gradients, fractals, or text, every still image, image sequence, or movie file has to enter your comp through a Loader tool.

Loader and Saver tools handle bringing media into Fusion Studio and rendering it back out. Use any of these to add media to your comp:

- Hit Effects to bring up the Effects Library, then pick Tools > I/O > Loader.
- Click the Loader icon in the toolbar.
- Over the Node Editor, right-click and then pick Add Tool > I/O > Loader.
- Drag a file out of an OS file browser window onto the Node Editor.

Drag several files onto the Node Editor and each one gets its own Loader. Yet drag a single frame belonging to an image sequence and the whole image sequence reads into the comp through one Loader, provided the numbering runs in order. To pull in just one frame of an image sequence:

- Hold Shift as you drag a single frame from an image sequence onto the Node Editor. That is useful for reading in sequentially numbered photographs from a digital camera.

Whatever clip, image file, or graphic you carry into Fusion is represented by a Loader. Still, Fusion Studio can take in other media types as well. The File > Import menu accepts Photoshop PSD files and SVG splines, plus 3D models saved in the Alembic, FBX, and OBJ format. TIP: Choosing File > Import > Footage spawns a fresh composition together with a Loader node for that footage, and the chosen media supplies the composition’s name automatically.

To learn more about the Loader node, turn to Chapter 105, “I/O Nodes,” within the DaVinci Resolve Reference Manual, or Chapter 45 of the Fusion Reference Manual.

### Aligning Clips in a Fusion Studio Composition

Drop a clip into a composition and its Loader node lands at frame 0 of that composition. The part of the clip that actually matters to you, though, might not kick in until a handful of frames or several seconds further on. So that you can line up the timing of every media element, each Loader carries timing and trimming options in the Inspector. On top of that, you can hold the first or last frame longer than the original media runs, and reverse or loop the clip to stretch your composition’s range. The Inspector’s upper region holds the Global In and Global Out settings. That range slider fixes where in your composition the clip starts and stops, working just like dragging a clip along a track in a Timeline. Down at the bottom of the Inspector, the Hold First Frame and Hold Last Frame dials let you freeze frames when the clip falls short of the composition’s global time.

Drag the Global In/Out range slider to shift a clip in time so it shows up at the right moment in a comp. Just under the filename in the Inspector sits a Trim In and Out range slider, which fixes the clip’s start frame and end frame. Pulling the Trim In strips frames off the clip’s head, while pulling the Trim Out strips frames off its tail. Even when you strip frames from a clip’s head, the Global In is always what decides where in time the clip starts in your comp. Take a Loader whose Global In sits on frame 0: trim the clip to begin on frame 10, and frame 10 of the source clip lands at the comp’s start on frame 0.

Use the Trim In/Out to drop needless frames off a clip’s head or tail. Rather than fiddling with timing in the Inspector, the Keyframes Editor makes it far clearer visually. To dig further into the Keyframes Editor and changing a clip’s time, turn to Chapter 71, “Animating in Fusion’s Keyframes Editor,” within the DaVinci Resolve Reference Manual, or Chapter 9 of the Fusion Reference Manual.

### Loader Node Inputs

A Loader node carries a single Effects mask input plus a single output. As for that Effects mask input, wiring a mask node like a Polygon or B-Spline node into it spawns an alpha channel on the Loader node automatically. TIP: Connect a Mask node that has no shapes drawn and the mask puts out total transparency, which leaves the image coming from the MediaIn node empty. To rotoscope over a MediaIn node, start by making a Mask node that is left unconnected; with that Mask node selected and the Media In node showing in the viewer, draw your mask. After you close the shape you are drawing, wire the Mask node into the MediaIn node’s input and you are set.

### Using Proxies for Better Performance

For increased performance, you can do one of two things:

- Build smaller media files and store them on disk through Optimized Media in DaVinci Resolve
- Render out proxy files using Saver nodes in Fusion Studio

On top of that, both applications can make proxies on the fly, with no new files written to disk, by way of the Proxy and Auto Proxy options found in the transport controls area. Switching on the Proxy and Auto Proxy options takes one of two routes, which depends on the Fusion version you run:

Proxy and Auto Proxy options in the transport controls right-click menu.

- On the Fusion page, right-click the blank region behind the transport controls to switch on the Proxy option.
- Within Fusion Studio, hit the Proxy (Prx) button found in the transport area, which turns proxy usage on.

What the Proxy option does is lower the image resolution while you view and work. Rather than drawing every pixel, it interactively handles one pixel out of every x. Within Fusion Studio, you fix the value of x by right-clicking the Prx button and picking a proxy ratio from the drop-down menu; pick 5 from that menu, for instance, and the ratio becomes 5:1. On the Fusion page, you set the proxy ratio by choosing Fusion > Fusion Settings and adjusting the Proxy slider in the General panel.

Through the Proxy menu you set how many pixels get skipped during processing. The Auto Proxy button tells Fusion to degrade the image interactively only during the moments you are making an adjustment, after which it snaps back to full resolution once you let go of the control. Much as with the Prx button in Fusion Studio, you set the Auto Proxy ratio by right-clicking the APrx button and picking a ratio off its menu. With a Loader node selected, the Inspector shows a Proxy Filename field, letting you name a clip that loads whenever Proxy mode is active. That way, smaller copies of the image can load to quicken file I/O off disk and processing. It really helps with high-resolution files such as EXR that may sit on a remote server. Keeping lower-resolution copies of the elements locally cuts network bandwidth, interactive render times, and memory consumption. The proxy clip you build must carry the same frame count as the original clip, and where image sequences are involved, that clip’s sequence numbers must begin and end on the same frame numbers. Should the proxies share the original files’ format, they will draw on the same format options in the Inspector as the originals do.

### Presetting Proxy Quality

In Fusion Studio, instead of right-clicking the Proxy button to fix proxy quality, you can preset both the standard and the Auto Proxy quality from the Fusion Preferences window. Within that window, the General pane holds sliders for standard Proxy files as well as Auto Proxy files. Those sliders set the default ratio that builds proxies whenever the Proxy and Auto Proxy modes are switched on. None of this touches the final render quality. TIP: Although the proxies get processed at a smaller size than the originals, the viewers scale the pictures so they still read at the original resolutions.

### File Format Options

Across DaVinci Resolve and Fusion Studio, the Fusion interface surfaces format-specific options in slightly differing ways. Whereas Fusion Studio keeps most file-specific options on the Loader’s Format tab, the Fusion page generally puts those options on the main Image tab of the MediaIn node. OpenEXR stands as the lone exception: its many options get their own separate tab even within the Fusion page’s MediaIn node. Options are not present for every file format. Extra options appear on load only for the DPX, OpenEXR, PSD, and QuickTime formats.

### DPX

For DPX files, the Format tab on Fusion Studio’s Loader node serves to turn image data from logarithmic into linear. Many people leave these settings on bypass and instead handle the Log to Linear conversion with a Cineon Log node.

### OpenEXR

OpenEXR delivers a compact, adaptable high dynamic range (float) format. It accommodates an assortment of extra non-RGBA channels along with metadata. You can view and switch on those channels from the Inspector’s Format tab.

Inside a Loader node Inspector, the Aux channels belonging to EXR files appear on the Format tab.
