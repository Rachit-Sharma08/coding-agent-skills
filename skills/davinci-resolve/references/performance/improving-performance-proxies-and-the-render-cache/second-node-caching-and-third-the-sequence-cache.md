# Second node caching and third the sequence cache

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](smart-user-cache-and-media-organization.md) / [Next section](controlling-node-caching-and-controlling-color-output-caching.md)
<a id="source-caching-specific-nodes-in-the-color-page"></a> <a id="source-choosing-a-cache-format-and-location"></a> <a id="source-controlling-fusion-output-caching"></a> <a id="source-fusion-output-caching"></a> <a id="source-manually-controlling-the-cache"></a> <a id="source-second-node-caching"></a> <a id="source-sequence-caching"></a> <a id="source-the-difference-between-the-smart-cache-and-user-cache-modes"></a> <a id="source-third-the-sequence-cache"></a> <a id="source-when-caching-happens"></a>

### Second, Node Caching

The Node Cache stands as a level of caching apart from the Fusion Output Cache, and you can set it off in several different ways, each matching one of the three distinct purposes it covers.

- Switch the Smart Cache on and nodes carrying processor-intensive operations (together with every node sitting upstream within that grade’s node tree) get cached on their own, which means, say, with Nodes 1 and 2 cached, you can keep tweaking Nodes 3, 4, and 5 to your heart’s content without having to re-render your grade to the cache. Among the operations that set caching off are Noise Reduction, Motion Blur, and any Resolve FX or OFX plugin dropped onto a node. Should you have put a Resolve FX onto a node able to play in real time, yet that node still gets flagged for caching, you can force caching off for it by right-clicking the node and picking Node Cache > Off off the contextual menu.
- Any node can be forced to cache by hand where it and its upstream nodes are dragging performance down but somehow escaping automatic flagging, done by right-clicking a node and picking Node Cache > On off the contextual menu.
- You can likewise switch the “Render Cache Color Output” option on, applied to a clip you've placed in the Timeline on either the Edit or Color pages. That forces the clip’s whole grade to be cached by way of the Node Cache, right through to the Node tree’s output. The upshot can be higher real time performance over in the Edit page, at the cost of having to fully re-cache that clip any time you touch part of its grade.
- Should you apply Resolve FX or OFX filters to clips on the Edit page, these too get cached by way of the Node Cache. Which OFX gets cached is your call through the Render Cache OFX Filter submenu within the contextual menu for clips in the Timeline. That helps where a mix of realtime and non-realtime filters rides on a clip; caching only the non-realtime ones lets you carry on tuning realtime filters with no need to re-cache. Bear in mind, though, that altering a filter being cached on the Edit page timeline forces that clip’s grade to be re-cached over on the Color page, and the reverse holds too.

Where several nodes get flagged for caching within one node tree, each node ends up cached on its own. That way, you can flip a cached node off and on for a before-and-after look without having to re-cache the entire node tree. Where a clip belongs to a group on the Color page, a Group Cache can be switched on while you sit in the Group Pre-Clip and Group Post-Clip Node Editor modes; doing so caches those portions of a group grade as part of the Node Cache.

### Third, the Sequence Cache

The Sequence Cache stands as a separate cache for effects applied specifically within the Timeline on the Edit page. Counted among these are transitions, opacity adjustments, adjustment layers and composite mode superimpositions, along with clips carrying Speed or Retime effects. Sequence Cache effects can autocache across both the Smart and User caches.

### Choosing a Cache Format and Location

You pick the cache format yourself by opening the Master Settings panel of the Project Settings, then reaching for the “Render Cache Format” drop-down menu to land on whichever you want among these: ProRes, DNxHR, or the uncompressed 10- or 16-bit float uncompressed .dvcc formats. Picking a higher quality cache format secures high quality image playback, but leans harder on the throughput and size of your available disk storage. Conversely, picking a more heavily compressed cache format opens real time playback up to weaker computers with slower and smaller storage, at the cost of slightly dented image quality. The smart move is to settle on the highest quality cache format your workstation’s storage can carry. Whatever format you land on by way of the “Render Cache Format” menu decides one thing: does image data lying out of bounds — “super white” or HDR strength highlights among it — survive once the signal is cached? Within this menu, formats ending in “– HDR” keep out-of-bounds image data, whereas formats that don't, wont. Should you notice image data (typically bright highlights) getting clipped after caching or optimizing, switch over to 16-bit float, ProRes 4444, ProRes 4444 XQ, or DNxHR 444; any of those codecs in particular suit HDR grading. As for where cache files go, that defaults to whichever volume you first add to the Scratch Disks list, found in the Media Storage panel within the System Preferences. Where no scratch disk gets named, your System disk steps in, which may bring capacity and/or performance trouble depending on the size and type of System disk you're on, plus the media format you elect to cache to. For that reason, it's almost always wise to point your first scratch disk at the largest, fastest storage volume your workstation can reach.

### When Caching Happens

While caching is on, cache indicators running along the bottom of the Timeline Ruler of the Edit page timeline report the state of the cache. Red stands for “to be cached,” while blue stands for “has been cached.”

Source, Clip, and Sequence Cache bars as they appear within the Edit page's Timeline; the red ones mark stretches still awaiting caching, while the blue ones mark stretches already cached Over on the Color page, cache indicators run node by node, marking the node in your grading node tree (every upstream node included) at which caching will occur.

Node Cache indicator showing up as a red-tinted node number, here on node two within the Color page's Node Editor

Two routes lead to caching. First, while either Smart or User caching is on, caching always fires whenever you play clips bearing red caching indicators. Second, where background caching sits on in the Project settings (on by default), and you leave your project untouched for a user-definable number of seconds (tunable over in the Master Settings panel of the Project Settings), caching kicks off on its own through stretches of user inactivity. So take that as your cue to grab those coffee, mate, or tea breaks; DaVinci Resolve will carry on working in your stead.

### The Difference Between the Smart Cache and User Cache Modes

The Smart Cache option of the Render Cache submenu hands you the simplest experience when you'd rather “set it and forget it.” Picking Smart fires off an assortment of automatic caching behaviors built to sharpen DaVinci Resolve playback; it does so by rendering whatever clip formats, timeline effects, and grading operations are known to tax performance, while still letting you flag by hand clips you'd like cached that the Smart Cache passed over. The User Cache, by contrast, does not on its own cache clips in processor-intensive formats, making it a solid pick when your workstation can play every media format you're running in real time. As a rule, the User cache leans on you to govern what gets cached and what doesn't by flagging specific clips and effects by hand. The Master Settings panel of the Project Settings does, however, hold three options you can switch on so that, with User Cache mode active, Fusion Effects, composites, and transitions get cached on their own (you'll find these options in the Optimized Media and Render Cache group). Of those settings, only “Automatically cache Fusion Effects in User Mode” sits on by default. What follows lays out the differences between the Smart and User cache modes for each kind of caching DaVinci Resolve performs.

### Fusion Output Caching

- In Smart mode: Take every clip whose “Render Cache Fusion Output” reads either Auto (the default) or On; for those, three kinds of effects get rendered. First, H.264, H.265, DCP, JPEG2K, or camera raw clips edited into a timeline get cached. Camera Raw clips get cached using the currently chosen project or clip debayer settings. Second, Speed effects get cached at the source level, which makes shifting cached speed effects clips around the Timeline possible without having to re‑cache them. Last, Fusion Clips or clips carrying Fusion Effects get cached too, and clips flagged by hand likewise get cached in Smart mode.
- In User mode: Clips with Render Cache Fusion Output set to On get cached, while clips set to Auto get skipped, save for clips carrying Fusion Effects, which cache on their own in Auto mode once the “Automatically cache Fusion Effects in User Mode” Project Setting is on.

### Caching Specific Nodes in the Color Page

- In Smart mode: On its own DaVinci Resolve caches every node that uses Motion Blur, Noise Reduction, or Resolve FX and OFX plugins. Nodes flagged by hand also get cached in Smart mode.
- In User mode: DaVinci Resolve caches only nodes flagged by hand, done by rightclicking them and picking Node Cache > On to force that node to cache in User mode, together with every upstream node to the left of them.

Cache Color Output Is Actually Node Caching for the Whole Grade

- In Smart mode: Clips flagged by hand with Render Cache Color Output switched on cache the entire output of the Color page node graph, in effect caching that clip’s whole grade. This pays off most where you want sharper trimming and playback performance over on the Edit page. Flagging a clip for caching also brings about caching of EVERY SINGLE VERSION tied to that clip as well.
- In User mode: Clips flagged by hand with Render Cache Color Output switched on likewise cache the entire output of the Color page node graph.

Within the Edit Page, Caching of Resolve FX and OFX Counts as Node Caching Too When such filters ride on clips over in the Edit page, their caching can be set by hand only, whether you sit in Smart or User mode. Cached are only those filters you've flagged by right-clicking the clip they ride on and picking them in the Render Cache OFX Filter submenu.

### Sequence Caching

- In Smart mode: On its own DaVinci Resolve caches every superimposed clip riding a composite mode that isn't “Normal,” every transition, plus any clips bearing opacity or speed effects. Clips can't be flagged by hand for Sequence caching.
- In User mode: Where you've switched User mode on and discover your workstation lacks the muscle to play composite and opacity effects on the Edit page, you can force these classes of effects to cache on their own while in User mode; a set checkboxes does it, sitting in the Optimized Media and Render Cache section under the Master Settings of the Project Settings. Once those options are on, you also pick up the means to keep specific tracks out of caching, by right-clicking the track header of any video track you'd like excluded from caching and picking Exclude track from caching. Keeping a whole track out of caching offers a tidy way to stop a track packed with effects that already play in real time on your workstation, a track of titles for instance, from burning time and storage by being cached where there's no need.

### Manually Controlling the Cache

This section walks through how to govern by hand each kind of caching that is manually controllable in DaVinci Resolve.

### Controlling Fusion Output Caching

You can govern by hand which clips in the Timeline get cached and which don't. Pick a clip or several, whether from the Edit page's Timeline or the Color page's Thumbnail Timeline, then right-click one of those chosen clips or thumbnails and pick an option off the Render Cache Fusion Output submenu. Three options are on offer:

- Auto: The clip caches in Smart mode only where it's a format earmarked for caching or where a speed effect rides on it. The clip caches in User Mode only where “Automatically cache transitions in User Mode” sits on.
- On: The clip caches in either Smart or User mode, whatever format or effects ride on it.
- Off: The clip won't cache at all, under either Smart or User modes.
