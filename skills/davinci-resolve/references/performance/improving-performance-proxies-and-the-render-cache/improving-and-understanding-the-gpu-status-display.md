# Improving and understanding the gpu status display

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Next section](optimized-media-creation.md)
<a id="source-adjusting-performance-mode"></a> <a id="source-frame-rate-and-gpu-indication-green-is-good"></a> <a id="source-full-hdhalf-uhdquarter-8k-uhd"></a> <a id="source-full-uhdhalf-8k-uhd"></a> <a id="source-half-hdquarter-uhdeighth-8k-uhd"></a> <a id="source-height-4320-2160-1080-540-270"></a> <a id="source-improving"></a> <a id="source-improving-performance-proxies-and-the-render-cache"></a> <a id="source-improving-performance-proxies-and-the-render-cache-part-1"></a> <a id="source-performance-mode-improves-overall-performance"></a> <a id="source-prioritizing-audio-or-video-playback-in-the-edit-page"></a> <a id="source-proxy-resolution-full-8k-uhd"></a> <a id="source-quarter-hdeighth-uhdsixteenth-8k-uhd"></a> <a id="source-reducing-decode-quality-improves-raw-media-performance"></a> <a id="source-timeline-proxy-mode-improves-effects-performance"></a> <a id="source-understanding-the-gpu-status-display"></a> <a id="source-width-7680"></a>

### Improving Performance, Proxies, and the Render Cache

### Improving

Performance,

Proxies, and

the Render Cache

As a high-performance application, DaVinci Resolve is built to deliver real time effects across a wide range of workstations. This section lays out the assorted ways you can keep an eye on your performance to confirm real time playback is holding, together with a number of methods for tuning real time performance, among them on-the-fly proxies and the background Render Cache.

### Understanding the GPU Status Display

Each viewer in DaVInci Resolve carries a GPU status indicator plus a frame-per-second (FPS) meter, both sitting in the Viewer’s title bar, that report your workstation’s performance the moment playback begins. Because DaVinci Resolve leans on one or more GPUs (graphics processing units) for all image processing and effects, the GPU status display reveals how much processing power whatever clip is playing happens to be drawing.

### Frame rate and GPU indication, green is good

When the status indicator glows green, there’s ample GPU processing headroom to spare. As the demand on GPU resources mounts, that green graph eventually shifts to red, signaling that the GPU power on hand can’t sustain steady real time playback.

Red means playback has dropped below real time Sooner or later, as you stack on more and more effects and corrections, you’ll hit the ceiling of available performance, which pushes DaVinci Resolve to either drop frames or slow the video down to preserve high image quality — a state the red FPS indicator flags. Whenever real time performance comes up short, DaVinci Resolve offers an assortment of controls and options for boosting real time playback and effects. Each suits a different scenario, and they all combine, letting you strike the best balance between image quality and performance as you work. Every one of these methods can be configured so it leaves your delivered output untouched.

### Prioritizing Audio or Video Playback in the Edit Page

When there isn’t enough processing power to play the clip or clips sitting under the playhead — owing to the grade, transforms, or effects active at that spot in the Timeline — you get to dictate precisely how DaVinci Resolve’s performance degrades, by toggling “Show All Video Frames” on or off from the Edit page Viewers’ Option menu. Show All Video Frames off: This is the default, well-suited to video editing. It favors audio playback and lets video frames drop when processing power runs thin, giving a more conventional playback feel. Show All Video Frames on: An alternative that shines during effects work, where you need to watch every single frame play in sequence. Audio takes a hit while each video frame plays slower-than-real-time, where necessary, to keep playback going. Bear in mind this setting comes into play only when GPU performance is wanting. Across stretches of the Timeline where performance is sufficient, playback stays uncompromised.

### Performance Mode Improves Overall Performance

Performance Mode, located in the Playback Settings of the User Preferences, sizes up your computer’s configuration — the CPU, GPU, connected video interface, and the rest — and automatically tunes DaVinci Resolve’s behind-the-scenes image processing settings to deliver the best interactivity on your machine. By default it’s on Automatic, though you’re free to adjust its impact by hand or shut it off entirely. With it enabled, Performance Mode markedly improves how editing, mixing, and grading feel on less powerful computers. Even while Performance Mode is on, DaVinci Resolve continues to output to video, render in the Delivery page, and process through the Media Management command at top quality. So Performance Mode sacrifices nothing in the quality of your output, which means creative editors and audio mixers can keep this setting on at all times. On less powerful computers, finishing editors and colorists may catch subtle differences in the image on your computer monitor between Performance Mode on and off, and that’s precisely why the setting can be switched off — wholly or partly via checkboxes in the Playback Settings panel of the User Preferences — for cases where GUI interactivity matters less than what’s on your onscreen display.

### Adjusting Performance Mode

Within the Playback Settings panel of the User Preferences, two radio buttons let you pick between Automatic (default) and Manual behavior once you switch on Performance Mode in DaVinci Resolve. On Automatic, Performance mode tunes a range of operations on its own, aiming to weigh performance against the required level of image quality — quick onscreen response while never giving up the highest quality for video output. On Manual, three separate settings are open for you to disable in cases where a given performance tradeoff produces an unacceptably visible drop in image quality under Performance Mode: Optimized Sizing: Concerns the handling of image resizing. Optimized Decode Quality: Concerns the handling of clip resolution against timeline resolution. Optimized Image Processing: Concerns the handling of image processing operations.

### Timeline Proxy Mode Improves Effects Performance

If you’d rather not drop frames or play below real time speed whenever the GPU Status indicator sits in the red, one instant fix is to switch on the Use Timeline Proxies option in the Playback menu. Timeline proxies ease processing demands by drawing on DaVinci Resolve’s resolution independence to drop your clips’ resolution on-the-fly, lifting real time playback performance without your having to spend time caching part or all of the timeline or building optimized media (both covered later).

To turn Use Timeline Proxies on and off:

- Choose Playback > Timeline Proxy Resolution > Half Resolution, Quarter Resolution, or None.

Switching on one of the proxy resolutions cuts the working resolution to either half or a quarter of whatever your project’s current Timeline resolution happens to be. Running at a temporarily lowered resolution lifts your workstation’s real time performance, while Resolve’s resolution independence ensures that every window you draw and every sizing operation you perform scales properly to your project’s actual resolution.

### Proxy Resolution Full 8K UHD

### Width 7680

### Full UHD/Half 8K UHD

### Full-HD/Half UHD/Quarter 8K UHD

### Half-HD/Quarter UHD/Eighth 8K UHD

### Quarter-HD/Eighth UHD/Sixteenth 8K UHD

A table laying out half and quarter proxy resolutions across various television frame sizes

### Height 4320 2160 1080 540 270

IMPORTANT: Timeline Proxy Mode stands wholly apart from, and independent of, the creation of Proxy Media covered later in this chapter. As features, Timeline Proxy Mode and Proxy Media bear no connection to one another.

### Reducing Decode Quality Improves Raw Media Performance

The Use Proxy command lifts performance where grades and effects are what’s pushing your project’s playback below real time, yet Use Proxy does nothing when real time performance is being consumed by the need to debayer raw media. You could of course lift playback performance by investing the time to generate optimized media (see below), or alternatively render to the Fusion Output Cache once the Smart Cache is switched on (covered later in this chapter), but the quickest route is to open the Camera Raw panel of the Project Settings and lower the Decode Quality for the raw media formats in play:

- Decode Quality: Camera raw formats like R3D and F65 admit debayering at varying quality levels. To gain more real time performance, pick a lower quality setting while you work, then bump it back up to a higher quality when you render the final output.

Which resolution-reduction choices you get depends on each raw format’s particular capabilities, but they cover at minimum full, half, and quarter resolution (R3D and Sony Raw add full, half, quarter, eighth, and sixteenth). The Canon RAW, Panasonic Varicam RAW, and Phantom Cine formats are exceptions, decoding only to full resolution. Should you lower the decode quality of raw media formats in your project for the sake of performance, then ticking “Force debayer res to highest quality” — a checkbox in the Deliver page’s Render Settings list — makes DaVinci Resolve render every raw format at the best quality on offer — so there’s no risk of forgetting to restore the decode quality when the moment comes to render your deliverables.
