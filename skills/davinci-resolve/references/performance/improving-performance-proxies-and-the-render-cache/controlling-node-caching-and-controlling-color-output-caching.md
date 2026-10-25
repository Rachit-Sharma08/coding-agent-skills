# Controlling node caching and controlling color output caching

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](second-node-caching-and-third-the-sequence-cache.md) / [Next section](camera-original-indicators-and-proxy-generation.md)
<a id="source-automatic-cache-deletion"></a> <a id="source-clearing-cached-media"></a> <a id="source-controlling-color-output-caching"></a> <a id="source-controlling-edit-page-filter-caching"></a> <a id="source-controlling-node-caching"></a> <a id="source-creating-and-using-proxy-media"></a> <a id="source-proxy-handling-display"></a> <a id="source-the-cache-manager"></a> <a id="source-the-cache-manager-1"></a> <a id="source-the-camera-original-preferred-icon"></a> <a id="source-the-proxy-media-resolution-and-format-settings"></a> <a id="source-the-proxy-only-icon"></a> <a id="source-the-proxy-preferred-icon"></a> <a id="source-using-cached-media-when-rendering-in-the-deliver-page"></a> <a id="source-using-proxy-media"></a> <a id="source-where-is-proxy-media-saved"></a>

### Controlling Node Caching

You can govern by hand which nodes in a grade get cached and which don't. Right-click any node in a node tree, then pick an option off the Node Cache submenu. Three options are on offer:

- Auto: The flagged node and every upstream node cache in Smart mode only where it holds an operation earmarked for caching.
- On: The node always caches in either Smart or User mode, whatever operations it carries out.
- Off: The node won't cache, under either Smart or User modes. That lets you keep nodes out of caching in Smart mode where they manage real time operation on your system.

### Controlling Color Output Caching

Every clip in the Timeline (Adjustment clips included) carries a Color Output setting you can flip on or off: over on the Edit page, right-click the clip where it sits in the Timeline and pick Render Cache Color Output off the contextual menu. A check mark marks when this setting sits on.

### Controlling Edit Page Filter Caching

You can pick which of the Resolve FX or OFX filters riding on a particular clip ought to be cached: over on the Edit page, right-click the clip where it sits in the Timeline, then pick which of the filters in the Render Cache OFX Filter submenu you'd like cached. Each filter riding on that clip turns up in this submenu in the order it rides on the clip, and you can flip the caching of specific filters on and off (chosen filters show with a check mark to the left of their menu item).

### Using Cached Media When Rendering in the Deliver Page

Over on the Deliver page, within the Render Settings, the Video panel holds a “More options” section, and there the “Use Render Cached Images” option lets you write media straight from the cache, rather than re‑rendering the effects from the ground up, to save rendering time as you output your project. Should you intend to lean on this option, it's wise to set the cache format to a suitably high-quality format so as to secure the best results.

### Clearing Cached Media

Each project’s cache sticks around; the cache is held for later use even once the project gets closed and reopened down the road. Should you need to wipe a project’s cache to win back space on a storage volume, three options sit in the Delete Render Cache submenu:

- All: Wiping all media in the cache lets you reset every single cached clip.
- Unused: You can opt to wipe only Unused cache clips that no longer line up with clips or

effects in the Timeline.

- Selected clips: You can make a hand-picked selection of clips in the Timeline, then wipe the cache

tied to just those clips. To clear a project’s cache: with the project open, pick Playback > Delete Render Cache > All, Unused, or Selected Clips.

### The Cache Manager

There's an advanced render cache management window on hand to help you readily eye the size of, and tend, your cache data across various projects spanning all your project libraries. You reach this cache manager from Playback > Manage Render Cache. The Cache Manager window hooks into the Project Manager, letting you pick cached media from any library your system can reach, not merely the current project library. Here's what the Cache Manager does: Location: Through this drop-down menu you settle which type of project library to connect to. The choices are: Local, Network, Cloud, and All. Project Library: Through this drop-down menus you settle which project library's projects you want to tend. It lists every project library in the chosen Location, and you can pick one for management. You can also pick All to surface every project library in that location. Project: The main window lays out every project in the Project Libraries chosen above. It's broken into sortable columns by Location, Project Library, Project Name, and Render Cache. Tick the box in the Render Cache column to mark any projects whose cache you'd like to wipe. Clear Selected Cache: Press this button to wipe the Cache for all the marked projects. At the time of writing this function offers neither a warning dialog nor an undo, so be sure you've marked the right caches for deletion. Close: Shuts the Cache Manager.

### The Cache Manager

### Automatic Cache Deletion

A User Preference lets you wipe your local cache on its own after a set number of days, keeping your drive from clogging up with older projects. You'll find it at DaVinci Resolve > Preferences > User > Cache Management > Delete cache older than xx days. Tick the box to wipe on their own any cache files older than the number of days entered in the field. Tending these files by hand stays open to you from the Playback > Manage Render Cache menu, yet this new preference lets you arrange a cleanup operation and forget it.

### Using Proxy Media

DaVinci Resolve carries a Proxy Media workflow that supplies a playback optimization option, easing the trade of projects online, work on projects from afar, and work alongside external media asset management systems. It builds a plain yet flexible system for editing collaboration that you can tailor to your specific requirements.

### Creating and Using Proxy Media

Proxy Media boils down to more heavily compressed (and possibly lower resolution) renditions of your source media, tied to your source media in DaVinci Resolve through metadata. It's done so that flipping back and forth between the original and proxy media as your needs dictate stays easy. As a rule this lets you lean on lower bandwidth proxy media for stronger real-time effects performance and full speed playback while editing, then readily return to source media — heavier on bandwidth and the processor — once you reach color correction, finishing, and final output. Beyond delivering better performance, these proxy files are wholly portable, which lets you shift your entire project with ease from workstation to workstation, even across the internet, alongside far more compact proxy media. Your proxies' resolution and format get fixed over in the Optimized Media and Render Cache section, which lives in the Master Settings panel under the Project Settings. Two settings govern the actual media files turned out by the Generate Proxy Media command. Proxy Media Resolution: Pick “Original” to keep proxies at the same resolution as the source media. Should you prefer, trim the resolution of the proxy media files by picking Half, Quarter, Eighth, or Sixteenth to spare bandwidth. The “Choose Automatically” option weighs visual quality against efficiency by trimming the resolution only of media files larger than the currently chosen Timeline resolution, applying whatever reduction ratio best fits the Timeline resolution. Proxy Media Format: Lets you pick the specific QuickTime format and codec your proxy files come out in. Several ProRes and DNxHR varieties are there to pick from, plus H.264 and H.265 options. Whichever format you pick comes down to the bandwidth and quality tradeoffs a particular project calls for. Say you merely want better playback speed off RAW media while holding image quality; you might lean toward a high‑quality codec like ProRes 422 HQ, or DNxHR HQX. Where your aim is shipping your media over the internet to another editor, a more compressed format might suit — ProRes Proxy, say, or even H.264 or H.265 — so that file sizes stay small.

### The Proxy Media Resolution and Format settings

To generate proxy media in DaVinci Resolve: 1 Within the Media Pool, select every clip for which you'd like proxies built. 2 Right-Click any chosen clip and pick “Generate Proxy Media” off the contextual menu. DaVinci Resolve will throw up a progress bar and hand you a time estimate for completion as it renders your chosen clips out to the format and codec set by the Proxy Media Resolution and Format settings. NOTE: Where, inside the Media Pool, a separate audio file sits synced to your source clip, whatever proxies come out of that clip will carry the synced audio, though that audio rides embedded within the video clip rather than emerging as a separate file.

### Where is Proxy Media Saved?

Proxy media gets created at the “Proxy generation location” destination; you'll come across it in the Working Folders section, sitting under the Master Settings of the Project Settings. The proxies then get sorted further into subfolders by original source clip location. Holding enough free space on this drive to fit the proxies matters. Once made, these proxy files can be shifted to any other drive location on the system, should you wish, then re-linked to their source files. This location can be overridden: tweak the Proxy Generation Location options, which sit among the Media Storage settings within the DaVinci Resolve Preferences.

### Proxy Handling Display

Across both the Media Pool and the Timeline, down in the lower left corner of a clip, a proxy status icon can be found. That icon shifts to tell you precisely which kind of media DaVinci Resolve is drawing on at the moment.

### The Proxy Only icon

Purple PXY Only: This icon flags that only proxy media is on hand; the camera original media has gone missing.

### The Proxy Preferred icon

Purple PXY over a White Background: This icon flags that both camera originals and proxy media for this clip are present, and that proxy media is the one in use.

### The Camera Original Preferred icon

White HQ over a Purple Background: This icon flags that both camera originals and proxy media for this clip are present, and that original media is the one in use.
