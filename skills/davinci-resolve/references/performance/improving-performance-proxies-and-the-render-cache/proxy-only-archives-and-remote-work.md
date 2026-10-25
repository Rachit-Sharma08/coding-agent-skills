# Archive setting options for exporting only proxy media and working remotely using proxy media

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](proxy-generator-format-and-processing.md)
<a id="source-archive-setting-options-for-exporting-only-proxy-media"></a> <a id="source-other-project-settings-that-improve-performance"></a> <a id="source-proxy-media-vs-optimized-media"></a> <a id="source-proxy-media-vs-other-playback-optimizations-in-davinci-resolve"></a> <a id="source-proxy-media-vs-the-render-cache"></a> <a id="source-proxy-media-vs-timeline-proxy-mode"></a> <a id="source-using-optimized-media-proxy-media-and-caching-together"></a> <a id="source-which-playback-optimization-method-should-i-use"></a> <a id="source-working-remotely-using-proxy-media"></a>

### Archive Setting options for exporting only Proxy Media

What you end up with, the .dra, is a folder holding a wholly self-contained copy of your project together with its proxy media. You can readily shuttle this folder between drives, or compress it and ship it over the internet.

### Working Remotely Using Proxy Media

DaVinci Resolve's proxy workflow unlocks plenty of fresh avenues for editing collaboration and media handling. A frequent pattern, for example, keeps the RAW camera master source clips in the edit suite while spinning off low-resolution proxies to carry home for laptop editing. Here's how to put together a portable proxy set for laptop editing: 1 Configure the proxies' Resolution and Format settings within the Project Settings. Here you'll likely want “Choose Automatically” paired with a low-bandwidth, edit-friendly codec such as ProRes LT or DNxHR LB. 2 In the Media Pool, select every source clip and run Generate Proxy. 3 Send a DaVinci Resolve Archive (.dra) out to an external drive, ticking Proxy Media by itself. 4 Head off. Back home, plug that drive into your home laptop and run the Restore Project Archive command in the Project Manager to pull in the archive. 5 Once you've wrapped your home session, export a timeline, bin, or project from the laptop and carry just that single file back to the edit suite to resume work against the original source media. A second common case involves shipping proxies over the internet to an editor in a different city or country. Here's how to dispatch a project to a fellow editor across the internet: 1 Configure the proxies' Resolution and Format settings within the Project Settings. Here you'll likely want a low resolution such as “quarter” or “one-eighth,” paired with a low-bandwidth, heavily compressed codec like H.265 to keep file sizes as tiny as possible. 2 In the Media Pool, select every source clip and run Generate Proxy. 3 Send out a DaVinci Resolve Archive (.dra), ticking Proxy Media by itself. 4 With your OS's file compression tools, zip the archive folder down into one big file. 5 Push the resulting .zip up to whichever online file sharing service you favor, and pass the download link to the remote editor. 6 After the other editor unzips and imports the archive, the two of you can then trade timelines, bins, and/or project files back and forth to work together. Such files run small enough to send over email or an instant messaging service. Beyond that, your editing computer may sit on ethernet wired to a Media Asset Management system capable of producing its own proxies. To edit fluidly across the network, you have to lean on low-bandwidth proxies rather than the source media. Here's how to build proxy media externally for editing across a local network: 1 Pull the original source media files into your Media Pool from whatever network storage system you're on. 2 Configure the proxy-generation settings in your Media Asset Management software to suit the amount of network bandwidth you expect to have on hand. 3 Confirm the proxies' timecode and frame rate line up with the original source media, then render the proxies to a network location. 4 Pick every one of your original source media files in the Media Pool, then choose “Link Proxy Media.” 5 Point it at the proxy media sitting at the network location where they were rendered.

### Proxy Media vs. Other Playback Optimizations in DaVinci Resolve

DaVinci Resolve still carries other ways to optimize real-time performance, so it's only natural to wonder how this stacks up against Optimized media, Timeline Proxy Mode, and the rest of the performance-optimization techniques DaVinci Resolve offers. What chiefly sets proxy media apart is that it stands on its own, travels freely, and, if you wish, can be produced by software outside DaVinci Resolve.

### Proxy Media vs. Timeline Proxy Mode

Among the earliest performance-optimization options, the one called “Proxy Mode” in earlier DaVinci Resolve releases was relabeled “Timeline Proxy Mode” as of DaVinci Resolve 17 to keep it distinct from Proxy Media. Where the newer Proxy Media feature writes genuine media files to disk, “Timeline Proxy Mode” merely drops the timeline's resolution on the fly to squeeze out better real-time playback. Make no mistake: Proxy Media and Timeline Proxy Mode are two altogether separate features, fully independent of each other.

### Proxy Media vs. the Render Cache

Proxy Media exists to put easy-to-edit primary source material onto the Timeline, lifting performance before you ever begin editing. The Render Cache exists to lift the real-time performance of clips weighed down by enough heavy effects (Resolve FX, color corrections, noise reduction, compound clips, fusion compositions, and so on) to bog playback down even at the current Timeline resolution. Proxy Media stands alone and travels freely (move clips wherever you please; you just relink them after), whereas Render Cache media was never meant to be moved or touched externally and serves only the project it was built for.

### Proxy Media vs. Optimized Media

At first glance, Proxy Media and Optimized Media seem to do much the same job. Each is built to turn out lower-bandwidth, easier-to-edit renditions of source media. Yet Optimized Media is handled internally by DaVinci Resolve, can't be exported, and stays out of the user's reach. Proxy Media, by contrast, produces wholly portable, independent media that the user can manage with ease.

### Using Optimized Media, Proxy Media, and Caching Together

Exactly how you combine DaVinci Resolve's assorted performance-boosting features is left up to you, but bear in mind they aren't an either/or choice. You could, for instance, generate optimized media from your project's camera raw original clips, then switch on Timeline Proxy Mode playback to lift the performance of your 4K timeline, and flip on Smart Cache to hurry your Color page work along as you pile Fusion effects, noise reduction, and Resolve FX or OFX onto every clip. Each of these optimization methods cooperates cleanly and seamlessly with the others to raise your performance while holding your project's image quality as high as the Optimized, Proxy, and Cache formats you've chosen in the Master Settings panel of the Project Settings allow.

### Which Playback Optimization Method Should I Use?

DaVinci Resolve's array of playback optimization features exists expressly to push performance higher and offset shortfalls in hardware, storage, and bandwidth, yet knowing the right moment to reach for each one is key to making them work properly. A quick reference follows below.

- Timeline Proxy Mode: My timeline plays, but the pace is just a touch sluggish.
- Cache Clip: A handful of my clips carry heavy effects and I'd like help running them back in real time.
- Optimized Media: I'd like help running all my source footage back in real time, and this is the only machine

I'll be cutting on.

- Proxy Media: I'd like help running all my source footage back in real time, plus I have to collaborate and pass this media around to other users, programs, or external storage spots.

### Other Project Settings That Improve Performance

On top of leaning on proxies, dropping raw decoding quality, building optimized media, and switching on the Smart and User caches, the Project Settings window offers five further options, and the User Preferences adds one more within its UI Settings panel, all of which you can call on to push real-time performance further on an underpowered machine, trading away some image quality as you work. You can then flip these settings back to their higher-quality modes ahead of rendering.

- Set timeline resolution to: (Master Project Settings, Timeline Format) Since DaVinci Resolve is resolution independent, you may switch the resolution whenever you like, and every window, track, sizing change, and piece of keyframe data is recomputed automatically to suit the new size. Dropping the Timeline resolution as you grade lifts real-time performance by cutting how much data gets processed, though you'll want to raise Timeline resolution back to the size you need before rendering. It amounts to much the same thing as the Proxy command, except here you pin down precisely which resolution you'd like to work at.
- Enable video field processing: (Master Project Settings, Timeline Format) Even on interlaced material, you may keep this option off to gain real-time performance. Once you're done, flip the setting back on ahead of rendering. Whether field processing truly needs to be on, though, hinges on the sort of corrections you're making. Should you apply any filtering or sizing such as blur, sharpen, pan, tilt, zoom, or rotate, then field processing ought to be on for rendering. Should you only be tweaking color and contrast, field processing isn't needed.
- Video bit depth: (Master Project Settings, Video Monitoring) Monitoring at 8-bit lifts real-time performance, at the risk of possibly bringing banding into the monitored image.
- Monitor scaling: (Master Project Settings, Video Monitoring) Lets you pick which transform filter handles scaling video to fit the Video format resolution you've set. The choices are Bilinear and Basic.
- Resize Filter: (Image Scaling) A drop-down menu through which you select a different image transform filter (Bilinear, say) that trades quality for being lighter on the processor. A “Force sizing highest quality” checkbox in the Deliver page's Render Settings list, however, helps guard against your final media getting rendered at this reduced-quality setting by accident.
- Hide UI overlays: (User Preferences, Playback Settings) Off by default. If a single GPU is handling both display and CUDA or OpenCL processing, or your display GPU is underpowered, or you don't have the PCIe bandwidth the current resolution or frame rate demands, switching this option on may win you better real-time performance. With it on, onscreen controls like the cursor, Power Window outlines, and split-screen views are turned off and hidden throughout playback. Pause playback and all onscreen controls return.
- Minimize interface updates during playback: (User Preferences, Playback Settings) On by default. With it on, this setting lifts real-time performance by tucking away the Viewer's on-screen controls (cursor, Power Window outlines, split-screen views among them) for the duration of playback. Stop playback and the onscreen controls return.
