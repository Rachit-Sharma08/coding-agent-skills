# Color page interface and default layout of the color page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the color page.
[Chapter index](INDEX.md) / [Next section](media-pool-and-node-editor.md)
<a id="source-gallery"></a> <a id="source-lut-browser"></a> <a id="source-showing-which-panel-has-focus"></a> <a id="source-the-color-page-in-cinema-viewer-mode"></a> <a id="source-the-color-page-in-enhanced-viewer-mode"></a> <a id="source-the-color-page-in-full-screen-viewer-mode"></a> <a id="source-the-color-page-interface"></a> <a id="source-the-default-layout-of-the-color-page"></a> <a id="source-the-default-viewer-with-transport-controls"></a> <a id="source-the-interface-toolbar"></a> <a id="source-the-lut-browser"></a> <a id="source-using-the-color-page"></a> <a id="source-using-the-color-page-part-1"></a> <a id="source-viewer"></a>

### Using the Color Page

Because DaVinci Resolve began life as a professional grading application, the Color page sits at the core of the DaVinci Resolve experience. Everything you need to manipulate color and contrast, cut noise, build limited secondary corrections, craft image effects of various sorts, adjust clip geometry, and apply countless other corrective and stylistic changes lives within the Color page. This chapter teaches you how to read the Color page interface, tailor it to your needs, and work within it to play back and move through your project’s timeline. You will also pick up how to study and compare clips before grading using stills, playheads, and the video scopes built into DaVinci Resolve.

### The Color Page Interface

The Color page splits into seven main areas that cooperate to help you build a grade. This section runs through what those areas are and how each one works.

### The default layout of the Color page

### The Interface Toolbar

Running across the very top of the Color page is a toolbar of buttons for showing and hiding different parts of the user interface. Reading left to right, they are: The Interface toolbar Gallery: Shows or hides the Gallery panel. LUTs: Shows or hides the LUT Browser. Media Pool: Shows or hides the Media Pool. Clips: Shows or hides the Thumbnail timeline. A drop-down to its right lets you select a timeline filtering option for the Thumbnail timeline. Quick Export: Brings up the Quick Export window.

Timeline: Shows or hides the Mini-Timeline. Nodes: Shows or hides the Node Editor. Open FX: Shows or hides the Open FX panel. Lightbox: Shows or hides the Lightbox.

### Showing Which Panel Has Focus

Any time you click somewhere on the DaVinci Resolve interface with the pointer, or use a keyboard shortcut to “select” a given panel (as in the Edit page), you grant that interface panel “focus.” A focused panel grabs specific keyboard shortcuts to act within itself rather than somewhere else in the interface. A highlight along the top edge tells you which panel holds focus, so you can keep tabs on which part of the current page is taking precedence, and you can move focus around as needed to get your work done. You can switch the Focus Indicator on or off under Preferences > User > UI Settings > Show focus indicators in the user interface.

The focus indicator running along the Media Pool’s top edge, beside a Viewer that lacks focus

### Viewer

The Viewer presents the frame at the playhead’s current spot in the Timeline. A header across the top of the Viewer shows the Project and Timeline names, plus a Viewer Timecode display that by default reports each clip’s source timecode. The Timeline name doubles as a drop-down that lets you jump to any other timeline in the project. A scrubber bar beneath the image lets you drag the playhead through the clip’s full length, while transport controls below that govern playback. A toolbar up top supplies controls for Image Wipes, Split‑Screen, and Highlight display. Further controls let you loop playback, flip Unmix mode on or off, switch audio playback on or off, and pick which onscreen controls show at the moment. There’s more on using the Viewer later in this chapter.

### The default Viewer with transport controls

You can also switch the Viewer into one of three alternate modes to get a larger working image. All three are reachable from the Workspace > Viewer Mode submenu.

- Enhanced Viewer: (Option-F to toggle this on and off) clears away everything flanking the Viewer on both sides, handing you a roomy working area for jobs like window positioning and rotoscoping, all while leaving the palettes and their controls on view as you work.

### The Color page in Enhanced Viewer mode

- Full Screen Viewer: (Shift-F to toggle this on and off) is there to grant extra working area for jobs like window positioning and rotoscoping. It can also show the Effects panel at full height, and you’re free to switch the Node Editor on and off to reach different effects controls as you work.

### The Color page in Full Screen Viewer mode

- Cinema Viewer: (P to toggle this on and off) stretches the Viewer to fill your workstation’s whole monitor. It comes in handy when you want to play the current Timeline free of distractions. Move the pointer over the image and transport controls plus a jog bar appear so you can drive playback. For DITs, right-clicking anywhere on the image opens a contextual menu for switching on and tailoring a video scope overlay (which you can drag to various spots on the Viewer).

### The Color page in Cinema Viewer mode

### Gallery

The Gallery holds still frames you keep for reference along with grades you may wish to copy; stills and grades are stored side by side. A button opens the Album browser, which you use to organize your stills. Down at the bottom of the Gallery, Memories let you stash grade information that you can recall via a control panel or keyboard shortcuts. The Color page Gallery mirrors what the Gallery page holds. For more on the Gallery page, see Chapter 141, “Using the Gallery.”

The Gallery has Memories, stills saved in albums and your PowerGrades

### LUT Browser

The LUT Browser gives you one central place to browse and preview every LUT installed on your workstation. Every LUT shows up in the sidebar, grouped by category.

### The LUT Browser

Out of the box, every LUT shows a test thumbnail that previews its effect, yet you can also see a live preview of the current clip under a LUT by hover-scrubbing the pointer across a given LUT’s thumbnail (more on that further down). To open the LUT Browser: in the UI Toolbar at the top of the Color page, click the LUT Browser button. Methods of working with the LUT Browser:

- To see the LUTs in any category: Click a LUT category in the sidebar to select it, and that category’s LUTs show up in the browser area.
- To make a LUT a favorite: Move the mouse over a LUT and click the star badge in its upper right-hand corner, or right-click any LUT and pick Add to Favorites. That LUT then turns up whenever you select the Favorites category.
- To search or filter for specific LUTs: Open a bin containing the LUT you’re after, click the magnifying glass icon to bring up the search field, and type text that pinpoints the LUTs you want.
- To see LUTs in Column or Thumbnail view: Use the Column or Thumbnail buttons at the LUT Browser’s top right to set how the LUTs display in the browser area.
- To sort LUTs in Thumbnail view: Open the Thumbnail Sort drop-down menu and pick the criteria to sort the LUTs by. The choices are Filename, Type, Relative Path, File Path, Usage, Date Modified, along with ascending and descending sort modes.
- To sort LUTs in Column view: Click a column header to sort on that column, and click it again and again to flip between ascending and descending modes.
- To give a LUT a new thumbnail taken from a clip: Pick the clip and frame you want as that LUT’s fresh thumbnail, then right-click the LUT and pick Update Thumbnail With Timeline Frame.
- To put a LUT’s thumbnail back to the standard one: Right-click the LUT and pick Reset Thumbnail to revert to the standard test image.
- To pull newly installed LUTs into a category: Choose the LUT category, then right-click anywhere in the browser area and pick Refresh, reloading that category’s contents from disk.

Methods of adding LUTs to a grade from the LUT Browser:

- To apply a LUT to the current node: Pick a clip in the Thumbnail timeline, then right-click a LUT and pick Apply LUT to Current Node off the contextual menu.
- To apply a LUT to a specific node: Drag a LUT out of the LUT Browser and drop it on the node you’d like it applied to. Dropping a LUT onto a node that already carries one replaces the old LUT with the new.
