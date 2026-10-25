# Optimized media improves overall performance and creating optimized media

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](improving-and-understanding-the-gpu-status-display.md) / [Next section](smart-user-cache-and-media-organization.md)
<a id="source-choosing-resolution-automatically"></a> <a id="source-creating-optimized-media"></a> <a id="source-customizing-the-type-of-optimized-media-you-create"></a> <a id="source-deleting-optimized-media"></a> <a id="source-height-4320-2160-1080-540-270-135"></a> <a id="source-optimized-media-for-raw-source-clips"></a> <a id="source-optimized-media-improves-overall-performance"></a> <a id="source-rediscovering-lost-optimized-media"></a> <a id="source-sharing-optimized-media-between-projects"></a> <a id="source-switching-between-optimized-and-original-media"></a> <a id="source-using-optimized-media-for-delivery"></a> <a id="source-width-7680-3840-1920-960-480-240"></a>

### Optimized Media Improves Overall Performance

When you’re cutting processor-intensive source formats like camera raw, H.264, or 8K media and your computer can’t comfortably keep up in real time, you can build pre-rendered, lowoverhead duplicate media to edit with in their place, managed automatically alongside the originals. This goes by the name “Optimized Media.” Optimized Media speeds up your work by letting you edit using a more processor-efficient media format and resolution, all while keeping the ability to flip your project back to the original source media anytime you wish. In other words, you edit with Optimized media and revert to the original source media once it’s time to finish and output. Flipping between them is as simple as picking, under the Playback menu, Use Optimized Media if Available — that command toggles Optimized media on and off. One advantage of optimized media for working faster is that it’s pre-generated: render it once and the files serve you for the whole stretch of work on that project (unless you alter the raw media’s debayering settings). Optimized media also boosts the playback of clips right across DaVinci Resolve — over on the Media page, plus within the Edit page’s Media Pool and Source Viewer — whereas the comparable yet distinct Fusion Output Cache part of the Smart Cache only helps clips already on the Timeline by caching them at the Timeline resolution. That makes optimized media a fit for editing workflows of every sort. Choosing the Appropriate Optimized Media Format for Your Project You may pick the Format of the optimized media you generate using controls in the Master Settings panel of the Project Settings. Note that the format you select through the “Optimized Media Format” menu governs whether out-of-bounds image data (those so-called “overshoots”), along with Alpha Channels, survive when the clip is cached.

- Preventing Clipping: Reach for 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR 444 whenever you intend to grade with optimized media. That holds especially for HDR grading.
- Preserving Alpha Channels: Note as well that your chosen format decides whether Alpha Channels carry through when the clips being optimized contain them. At present the formats that retain alpha channels are DNxHR 444, ProRes 4444 XQ, ProRes 4444, Uncompressed 16-bit Float, and Uncompressed 10-bit.

### Creating Optimized Media

Building optimized media to work with is straightforward. Resolve looks after the link between source clips and the optimized media you produce on its own, so your only job is to decide which clips get optimized media. You can hand-pick the clips to optimize, or lean on a Smart Bin to procedurally round up every clip matching one or more formats you need optimized. Either way, you’re free to optimize only the clips in formats that actually call for it, which saves time. Say you’re cutting a project that’s half camera raw media and half DNxHD media; you likely need only the camera raw media optimized, so you can build a Smart Bin that pulls all of it together by Resolution, Codec, File Name, or whatever other metadata fits. With it gathered, selecting all those clips for the next step is simple. To build optimized media for one or several selected clips: right-click any one of them and, from the contextual menu, choose Generate Optimized Media.

Every bit of optimized media lands in the same directory the Cache files use, which by default is the first scratch disk shown in the Preference dialog’s Media Storage panel. You can also point the Cache and Optimized files elsewhere through the “Cache files location” setting, which lives in the Project Settings under the Master Settings panel.

### Optimized Media for Raw Source Clips

As a rule, after you’ve generated optimized media, DaVinci Resolve tracks it and keeps drawing on it no matter what changes you bring to your project, the Timeline resolution included. That said, altering the camera raw settings of optimized clips automatically throws out their optimized media, leaving you to re-generate it for those clips.

### Customizing the Type of Optimized Media You Create

A group of controls in the Master Settings panel of the Project Settings dictates which sort of media files come out when you generate optimized media.

The Project Settings’ Master Settings panel and its options for producing optimized media Two settings touch Optimized Media within the Optimized Media and Render Cache section:

- Resolution: Lets you decide whether optimized media is built at the same size as your original media files (pick Original) or whether its bandwidth is trimmed further by cutting its resolution to a Half, Quarter, Eighth, or Sixteenth. The “Choose automatically” option seeks a balance of visual quality and efficiency by lowering the resolution only of media files larger than the Timeline resolution you’ve currently selected, applying whatever reduction ratio best fits the Timeline resolution.
- Optimized Media Format: Lets you set the format and codec used to generate optimized media. Choices run to Uncompressed 10-bit and Uncompressed 16-bit float for top quality. Further choices span ProRes Proxy up through 4444 XQ and DNxHR LB up through 444. Every choice stores image data in the optimized, proprietary .dvcc image format. Smaller formats eat up less of your scratch disk, yet there are two solid reasons to opt for higher-quality formats when making Optimized Media.

Preventing Clipping: Keep in mind that your chosen format settles whether out-of-bounds image data survives once the signal is optimized. Should you notice image data (usually superwhite levels) getting clipped after optimization, move to 16-bit float, ProRes 4444, or ProRes 4444 XQ; in fact, any of these three codecs make suitable optimized formats for HDR grading. Preserving Alpha Channels: Keep in mind too that your chosen format settles whether Alpha Channels endure when the clips being Optimized hold them. At present the formats that retain alpha channels are DNxHR 444, ProRes 4444 XQ, ProRes 4444, Uncompressed 16-bit Float, and Uncompressed 10-bit.

### Choosing Resolution Automatically

The Resolution setting’s “Choose automatically” option deserves a little more detail. With it on, only source media whose resolution tops the chosen Timeline resolution yields downsized optimized media. The degree to which each clip is downsized tracks how far it exceeds the Timeline resolution. Working in a 1080 resolution project, for instance, 8K clips produce quarter-resolution optimized media and 4K clips produce half‑resolution optimized media, so that all the optimized media lands roughly around 1080 resolution. Clips at 1080 and below produce optimized media at the same resolution as their source clips. In a 4K project, by contrast, 8K clips produce half-resolution optimized media, and every other clip at 4K or smaller produces optimized media at the source clips’ own resolution.

The Proxy Resolution tiers run as follows: Full 8K UHD; then Full UHD/Half 8K UHD; next Full-HD/Half UHD/Quarter 8K UHD; after that Half-HD/Quarter UHD/Eighth 8K UHD; then Quarter-HD/Eighth UHD/Sixteenth 8K UHD; and finally Eighth-HD/Sixteenth UHD — a table of optimized resolutions spanning various television frame sizes

### Width 7680 3840 1920 960 480 240

### Height 4320 2160 1080 540 270 135

### Switching Between Optimized and Original Media

Deciding whether or not you’re on optimized media takes no effort. Just choose Playback > Use Optimized Media if Available to flip your whole project between optimized media (when it exists) and the original media. On top of that, a checkbox in the Render Settings of the Deliver page lets you decide whether to render faster with optimized media or to render off the original media alone.

NOTE: Optimized media plays no part in Media Management operations, nor does it figure into Archive operations within the Project Manager.

### Sharing Optimized Media Between Projects

Optimized Media now carries across every project within the same project library (it used to be locked to one project). So if you generate optimized media for a clip in one project, that very same optimized media serves that clip in any other project sitting in the same project library. The whole thing is automatic and asks nothing of you. It sharply trims the space you need when working with the same media spread across different projects.

### Rediscovering Lost Optimized Media

Hard as it is, under certain rare conditions you can still lose track of optimized media you’ve made. Say you generate optimized media on a different workstation but neglect to save the project; DaVinci Resolve may then lose the link tying your Media Pool clips to the optimized media files you built. When that happens, you can rediscover the optimized media and spare yourself a regeneration. To rediscover lost optimized media: within the Media Pool, select the clips you know carry optimized media, then right-click any one of them and pick Rediscover Optimized Media out of the contextual menu.

### Deleting Optimized Media

Whatever optimized media you generate inside a project sticks around; it’s kept for later use even after the project is closed and reopened down the road. If you need to clear optimized media to reclaim space on your scratch volume (or wherever you’ve chosen to keep your project’s cache files), you have to delete it by hand in your OS. By default, the Optimized Media lives on the first volume named in the Media Storage tab of the System Preferences.

### Using Optimized Media for Delivery

Sitting in the More options section of the Render Settings on the Deliver page, the “Use Optimized Media” option lets you output from Optimized Media instead of the original media to shave off rendering time. If this option is part of your plan, it’s wise to set the Optimized media format to a fittingly high-quality, HDR-capable format so the results come out their best.
