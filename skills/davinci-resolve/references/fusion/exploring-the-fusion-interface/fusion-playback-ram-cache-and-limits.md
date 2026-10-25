# Fusion ram cache for playback and memory limits of the ram cache

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](fusion-studio-transport-controls-and-navigation-shortcuts.md) / [Next section](customizing-the-toolbar.md)
<a id="source-displaying-cached-frames"></a> <a id="source-memory-limits-of-the-ram-cache"></a> <a id="source-the-fusion-ram-cache-for-playback"></a> <a id="source-toolbar"></a>

### The Fusion RAM Cache for Playback

As you put a node tree together, every image processing operation renders live so the finished result shows in the viewers. Yet as each frame renders — and particularly once you start playback in either direction — these processed images are saved automatically into a RAM cache, allowing you to replay those frames at full speed. While playback runs, the frame rate actually reached appears in the Status bar at the bottom of the Fusion window. Naturally, if you play past the cached portion of the Time Ruler, the uncached frames must first render before they join the cache. Caching priority goes to the nodes currently on screen, according to which nodes are loaded into which viewers. Other nodes may end up cached as well, depending on factors such as how much memory is free and how processor-heavy those nodes are.

### Memory Limits of the RAM Cache

DaVinci Resolve offers just one control for capping the RAM devoted to caching, and it lives in the DaVinci Resolve Preferences Memory and GPU panel.

Limit Fusion Memory Cache To: This slider fixes the upper bound of RAM that Fusion may use for caching. That amount is carved out of the RAM already given to DaVinci Resolve. At most you can hand Fusion 75% of DaVinci Resolve’s overall RAM allotment. Whenever you are away from the Fusion page, that RAM is freed for the other pages in DaVinci Resolve. Fusion Studio, by contrast, provides two controls for capping cache RAM, both in the Preferences Memory panel.

- Limit Caching To: This slider fixes the upper bound of RAM spent on caching. The default of 60% on a 32-GB system caps the cache at 19.2 GB. The most you can grant Fusion Studio is 80% of total system memory, which keeps a minimum reserve for other programs and the operating system.
- Leave at least # MBytes: This number field tightens caching further whenever the system’s free RAM falls under the value you enter. Setting it to 200 MB, for example, tries to keep 200 MB of RAM available for the OS or other programs. Setting the field to 0 lets Fusion Studio consume the entire amount allowed by the Limit Caching To setting and ignore other apps.

Once the cache grows to the Fusion Caching/Memory Limits value in the Memory panel of the Preferences, lower-priority cache frames get dropped automatically to free space for fresh caching. A percentage indicator at the far right of the Status bar along the bottom of the Fusion window lets you watch how much of the RAM cache is in use.

### Displaying Cached Frames

A green line along the bottom of the Time Ruler marks every cached frame for the node you are currently viewing. Wherever the Time Ruler is green, playback should run at full speed.

A green line denotes frames whose playback cache is ready. Temporarily Preserving the Cache When Changing Quality or Proxy Settings Toggling the composition’s quality settings or proxy options does not throw the cache away at once. Instead the green line goes red, signaling that the cache is being held and can serve again when you return to the original quality level or switch proxy mode off. If, though, you play across those frames under the new quality or proxy settings, the held cache is replaced by a fresh cache at the current quality or proxy setting.

A red line shows that cached frames from a different quality or proxy setting are being held.

One case breaks this rule, however. If you cache frames under the High Quality setting and afterward switch High Quality off, the green frames stay green rather than turning red. The High Quality cached frames keep being used even though the HiQ setting is now off.

### Toolbar

Found just below the Time Ruler, the toolbar holds buttons for dropping frequently used nodes into the Node Editor in a hurry. Clicking one of them places that node right after whichever node is selected in the node tree, or, when nothing is selected, drops in a standalone instance of that node. You can tailor the Toolbar and save versions of it for particular tasks.

The toolbar carries buttons for adding frequently used nodes to the Node Editor. By default it is split into sections that gather related, commonly used nodes. Hover the pointer over any button and a tooltip reveals that node’s name.

- Loader/Saver nodes (Fusion Studio Only): The Loader node is the main node for choosing and bringing in clips from the hard drive. The Saver node handles writing or rendering your composition out to disk.
- Generator/Title/Paint nodes: The Background and FastNoise generators see frequent use across all sorts of effects, while the Title generator is an everyday staple, as is Paint.
- Color/Blur nodes: ColorCorrector, ColorCurves, HueCurves, and BrightnessContrast rank as the four most-used color adjustment nodes, and the Blur node is everywhere.
- Compositing/Transform nodes: The Merge node is the main node for layering one image over another. ChannelBooleans and MatteControl both matter greatly for moving channels from one node to another. Resize changes the image resolution, permanently altering what resolution is available, whereas Transform applies pan/tilt/rotate/zoom in a resolution-independent way that always refers back to the source image’s original resolution.
- Mask nodes: The Rectangle, Ellipse, Polygon, and BSpline mask nodes let you draw shapes for rotoscoping, building garbage masks, and other purposes.
- Particle system nodes: Clicking three particle nodes from left to right builds a complete particle system. pEmitter releases particles into 3D space, pMerge combines several emitters and particle effects into more elaborate systems, and pRender produces a 2D result you can composite against other 2D images.
- 3D nodes: A set of seven 3D nodes lets you assemble rich 3D scenes. Clicked from left to right, they auto-attach to one another to form a quick 3D template. ImagePlane3D brings 2D stills and movies in for compositing into 3D scenes. Shape3D produces assorted geometric primitives. Text3D creates 3D text objects. Merge3D combines several 3D image planes, primitive shapes, and 3D text into complex scenes, and Camera3D frames that scene however you choose. SpotLight lights the scenes in various ways, and Renderer3D renders the finished scene, outputting 2D images plus auxiliary channels usable for compositing the 3D output against other 2D layers.

While you are just getting started with Fusion, these nodes really are everything you need to build most ordinary composites. Even after you grow into an advanced user, you will keep finding that these remain by far the operations you reach for most.
