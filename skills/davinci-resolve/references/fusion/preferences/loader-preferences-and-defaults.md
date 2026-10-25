# Loader preferences and defaults

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](gpu-and-options.md) / [Next section](email-notification-and-server-settings.md)
<a id="source-cache"></a> <a id="source-caching-limits"></a> <a id="source-defaults"></a> <a id="source-final-render"></a> <a id="source-general"></a> <a id="source-interactive-render"></a> <a id="source-memory"></a> <a id="source-network"></a> <a id="source-submit-network-render-compositions"></a> <a id="source-the-loader-preferences"></a> <a id="source-the-memory-preferences"></a> <a id="source-the-network-preferences"></a>

### The Loader preferences

### Defaults

In the Defaults section there are two settings that govern how color depth and aspect ratio get handled for Loaders.

- Loader Depth: How color bit depth is treated when you add a Loader is governed by the Loader Depth. Pick Format and the proper bit depth is chosen for you, drawn from the file format and the data in the file's header. Pick Default and the bit depth takes whatever value the Frame Format preferences specify.

### Cache

Through the Cache preferences you manage how disk caching behaves in Fusion. You decide how and where the cache gets built, the point at which it's purged, the way it responds when source files go missing, plus numerous other cache-related options. Don't mistake this for the RAM cache, which the Memory preferences govern.

- Disable All Local Caching: Local caching is switched off by this setting.
- Cache Files from Network DiskCaches: When a tool has disk caching turned on and its disk cache

files live remotely on the network, turning this option on draws on a local copy of those cache files, much as a networked Loader's local cache does.

- Enable Local Caching of Loaders: Files get copied into whichever LoaderCache path is set below or in the Path Maps preferences.
- Cache Multi-Frame Files: Formats such as AVI or QuickTime are copied into the LoaderCache path, which can take a while for a large file.
- Don't Cache Files from Local Disks: Anything not residing on a network drive stays out of the LoaderCache path. You might switch this off when, say, you keep a fast SSD cache drive and want it serving local files too, speeding up file access during interactive work.
- Only Files Smaller Than xxx MB.: Anything bigger than the value entered here won't be copied into the LoaderCache path.
- Cache Path Separator Character: With Enable Local Caching of Loaders turned on, this setting lets you reconstruct the path of the source files within LoaderCache.

As an example, with the default "!" character in place, the original path X\Project\MyShots\ Shot0815\ becomes X!Project!MyShots!Shot0815! inside the LoaderCache path. You may employ different separator characters, the "\" character among them, which makes LoaderCache use subdirectories: X\Project\ MyShots\Shot0815\.

- If Original File Is Missing: Three choices here dictate how caching behaves once the source files turn up missing. With the Fail option, behavior matches Fusion's Default Loader exactly: the Loader won't process, possibly stalling the render. The Load Cache option pulls in the cache despite no original file being there. The Delete Cache option strips missing files out of the cache.
- Cache Location: As a convenience, this duplicates the LoaderCache path defined in the Path Maps preferences.
- Explore: Pressing this opens the LoaderCache path within a macOS X Finder window or a Windows Explorer window.
- Clear All Cache Files: Pressing this erases every cached file sitting in the LoaderCache path.

### Memory

You'll find the Memory preferences only in Fusion Studio. When you want to govern Fusion's memory as you work on DaVinci Resolve's Fusion page, head to DaVinci Resolve's Memory and GPU preferences. From time to time you'll need to tweak the Memory preferences so the computer's available memory is used to best effect. As an illustration, some users favor a larger cache memory for snappier interactive work, but for final renders they often cut the cache memory back, freeing up more memory for processing tools simultaneously or rendering several frames at once.

### Caching Limits

Among the Caching Limits are options covering Fusion's RAM cache operation. This is where you decide how much RAM goes to the RAM cache for playing comps back in the viewer.

- Limit Caching To: With this slider you fix what percentage of available memory the interactive tool cache may use. Here, available memory means the quantity of memory installed in the computer. Once the interactive cache hits the limit this setting defines, it begins evicting lower-priority frames from the cache to make room for new ones.
- Automatically Adjust In Low Memory Situations: Ticking this checkbox makes the caching adapt whenever memory runs short. Any cache purges get reported in the console.
- Leave At Least X MBytes: Use this setting to fix the hard ceiling on memory usage. Whatever the Cache Limit happens to be set to, this setting reserves how much physical memory stays free for other applications to use. As a rule, keep this value at no less than 25 MBytes.

### The Memory preferences

### Interactive Render

The Interactive Render option lets you tune how Fusion processes based on how much RAM your system has installed.

- Simultaneous Branching: When ticked, several tools get processed concurrently. Clear this checkbox should you keep running short on memory.

### Final Render

These settings govern memory usage throughout a rendering session, whether preview or final, and have no bearing on an interactive session.

- Render Slider: This slider tunes how many frames render concurrently.
- Simultaneous Branching: When ticked, several branches of a node tree get

rendered concurrently. When memory is tight, switch this off to boost rendering performance.

### Network

You'll find the Network preferences only in Fusion Studio. Their purpose is to configure and manage network rendering within Fusion Studio. You'll come across most of the settings in the Render Manager dialog.

### The Network preferences

### Submit Network Render Compositions

Into these fields you type the Master Name and IP address of the computer set to handle every network render dispatched from this machine. When a standalone render master operates on the network, these fields might come pre-filled and locked against editing. The point is to stop each person at a facility from spawning multiple unauthorized render masters. To make the master name and IP editable again, create the environment variable FUSION* NO* MANAGER and set the value to True. Refer to your operating system user guide for instructions on creating environment variables.

### General

The General preferences put the most-used options up top within the General section. What these options establish is the role the system plays during network rendering.

- Make This Machine a Render Master: Once enabled, Fusion takes in network render compositions from other computers and oversees the render. That doesn't necessarily put this computer to work on the render itself; rather, it dispatches the job to the render nodes named in the Render Manager dialog.
- Allows This Machine to Be Used as a Network Slave: Once enabled, this computer can serve as a Render node and will take in compositions for network rendering. Untick it to keep others from sending compositions to render on this computer.
- Render on All Available Machines: Tick this checkbox to disregard the groups and priorities set up in the Render Manager. Any composition this computer submits for network rendering then goes out to every available slave.
