# Edit page user interface and edit page in its entirety

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Next section](timelines-grades-and-versions.md)
<a id="source-bins-power-bins-and-smart-bins"></a> <a id="source-filtering-bins-using-color-tags"></a> <a id="source-importing-media-into-the-media-pool-on-the-edit-page"></a> <a id="source-media-pool-bins-opened-as-new-windows"></a> <a id="source-navigating-the-edit-page"></a> <a id="source-showing-bins-in-separate-windows"></a> <a id="source-showing-which-panel-has-focus"></a> <a id="source-sorting-the-bin-list"></a> <a id="source-the-edit-page-in-its-entirety"></a> <a id="source-the-edit-page-user-interface"></a> <a id="source-the-interface-toolbar"></a> <a id="source-the-media-pool"></a> <a id="source-the-media-pool-in-thumbnail-mode"></a> <a id="source-using-color-tags-to-identify-bins"></a> <a id="source-using-the-edit-page"></a> <a id="source-using-the-edit-page-part-1"></a>

### Using the Edit Page

This chapter walks you through using and setting up the Edit page user interface so you’re ready to edit projects in DaVinci Resolve. To learn how the Edit page handles importing and conforming projects cut in other applications for color correction and finishing inside DaVinci Resolve, turn to Chapter 56, “Conforming and Relinking Clips.”

### The Edit Page User Interface

Over time the Edit page has grown into a source-record style NLE packing nearly every editorial tool you’ll want, from creative editing all the way through finishing. Three main regions make up the Edit page: the browsers along the left, the Viewers up top, and the Timeline down at the bottom. Together they let you import, edit, and trim timelines using a flexible range of tools and methods.

### The Edit Page in its entirety

### The Interface Toolbar

Running across the very top of the Edit page is a toolbar whose buttons reveal and conceal different parts of the user interface. Taken in order from the left: The Interface toolbar. Media Pool/Effects Library/Edit Index height button — this lets the area occupied by the Media Pool, Effects Library, and/or Edit Index stretch to your display’s full height (two can show at a time), handing you more browsing room while the timeline narrows. At half height, the Media Pool/Effects Library/Edit Index stay pinned to the top of the UI (only one shows at a time) and the timeline spans your display’s full width. Media Pool: Reveals or conceals a scaled-down version of the full Media Pool page, opening access to every video clip, audio clip, and image used in the project. Effects Library: Reveals or conceals the repository holding all the transitions, generators, OpenFX, and audio filters you can put to use on the Edit page.

Index: Reveals or conceals the Edit, Tracks, and Markers indexes. Sound Library: Reveals or conceals the libraries of sound effects and music registered with DaVinci Resolve. To learn more about working with the Sound Library, turn to Chapter 170, “Using the Fairlight Page.”

Keyframes: Brings up the Keyframes and Curves Editor. Quick Export: Brings up the Quick Export Dialog for delivering an export of your timeline straightforwardly. Mixer: Reveals or conceals the Audio Mixer, handing you graphical controls for tweaking your sound mix. Metadata: Reveals or conceals the Metadata Editor. Inspector: Reveals or conceals the Inspector, which lays out the transform and compositing effects on selected clips, or the editable options of selected effects like transitions or generators.

### Navigating the Edit Page

Every panel in the Edit page user interface can be handed focus through the Workspace > Active Panel Selection submenu. On top of that, the keyboard shortcuts below assign focus to a range of targets — select bins and clips, the Source and Timeline Viewers, plus the Timeline, the Effects Library, Edit Index, and Inspector.

Key Command-1 Command-2 Command-3 Command-4 Command-5 Command-6 Command-7 Command-8 Command-9 Q

Function — taking each key in turn: Media Folders, then Media Clips, next the Source Viewer, after that the Timeline, followed by the Timeline Viewer, then Effects, then the Edit Index, with n/a next, the Inspector after that, and finally Q, which performs Toggle between Source and Timeline Viewers

### Showing Which Panel Has Focus

Each panel you work in carries “focus,” which means that clicking an item or control inside a given panel turns it into the active panel and routes the keyboard shortcuts shared across many panels to the one you’re working in. To see which panel currently holds focus, switch on the “Show focus indicators in the User Interface” checkbox within the UI Settings panel of the User Preferences. Once it’s on, a red line across the top of the active panel signals that it has focus.

The focus indicator shown along the top edge of the Media Pool, sitting beside a viewer that lacks focus.

### The Media Pool

On the Edit page, the Media Pool holds every piece of video, audio, and still image media you’ve imported to edit into the project at hand, plus all the timelines you’ll be editing into. The Media Pool is mirrored across the Media, Cut, Fusion, Color, and Fairlight pages as well, letting you reach any audio or video clip, graphic, or timeline from whatever page they can be used on.

### The Media Pool in Thumbnail mode

The Bin list along the left presents a hierarchical list of bins for organizing your media, and it organizes your timelines too. The Media Pool starts out with one bin, named “Master,” yet you can add as many further bins as you need to sort timelines and clips by right-clicking anywhere

in the Media Pool’s empty area and picking Add Bin. To rename a custom bin, double-click its name and type a new one, or right-click the bin’s name and pick Rename Bin. Up in the Edit page toolbar’s upper left-hand corner, a button reveals or conceals the Bin list. Off to the right, the browser area displays the contents of whichever folder is selected. Each timeline you build, and each AAF, XML, or EDL file you bring in, turns up here. Within a single project you can build or import however many timelines you require. Just as on the Media page, the Media Pool can appear in Metadata, Icon, or List view. List view lets you sort the contents by any one of a subset of the full metadata available in the Metadata Editor of the Media page. Editors will find particular value in the columns covering Name and Reel Name, the various timecode streams, then Description, Comments, Keyword, Shot, Scene, Take, Angle, and Circled — followed by Start KeyKode, Flags, Usage, Resolution, and Frames Per Second. To learn more about the Media Pool’s many features, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.” The sections coming up summarize a few key Media Pool features for your convenience.

### Importing Media Into the Media Pool on the Edit Page

Adding clips to the Media Pool over on the Media page gives you the richest organizational flexibility and feature set, but when you’re sitting on the Edit, Cut, Fusion, Color, or Fairlight page and need a few clips imported quickly for immediate use, a couple of routes are open to you. To add media by dragging clips out of the Finder onto the Edit page Media Pool (macOS only): 1 Pick one or more clips in the Finder. 2 Drag them into the Media Pool of DaVinci Resolve, or onto a bin in the Bin list. Those clips join your project’s Media Pool. To lean on the Import Media command found in the Media Pool of the Edit page: 1 Having opened the Edit page, right-click in the Media Pool anywhere and pick Import Media. 2 In the Import dialog, pick one or more clips to bring in and click Open. Those clips join your project’s Media Pool. To learn more about the Media Pool’s many features, turn to Chapter 18, “Adding and Organizing Media with the Media Pool.” Below, a few key Media Pool features are summarized for your convenience.

### Bins, Power Bins, and Smart Bins

The Media Pool actually holds three kinds of bins, each one occupying its own section of the Bin list. You can reveal or conceal the Power Bin and Smart Bin areas of the Bin list by ticking or unticking Show Smart Bins and Show Power Bins in the Media Pool option menu. Here’s how the bin kinds differ:

Bins: Plain, manually populated bins. Drag and drop whatever you want into a bin, and there it stays until you choose to move it to another. Bins can be nested hierarchically, so you’re free to build a Russian-dolls nest of bins. Making new bins is as simple as right-clicking within the bin list and, from the contextual menu, picking Add Bin. Power Bins: These stay hidden by default. They too are manually populated bins, yet they’re shared across every project in your current project library, which makes them perfect for shared title generators, for graphics movies and stills, for sound effects library files, for music files, and for other media you want to reach quickly and easily from any project. To make a new Power Bin, reveal the Power Bins area of the Bin list, then right-click inside it and pick Add Bin. Smart Bins: These are procedurally populated bins, meaning custom rules built on metadata dynamically filter the Media Pool’s contents each time you select a Smart Bin. That turns Smart Bins into quick ways of organizing projects for which you (or an assistant) has invested the time to attach metadata to your clips through the Metadata Editor — supplying Scene, Shot, and Take information, along with keywords, comments and description text, plus countless other details that speed up finding what you’re after when you need it. To make a new Smart Bin, reveal the Smart Bin area of the Bin list (if it isn’t showing), then right-click inside it and pick Add Smart Bin. A dialog opens where you can edit that bin’s name and the rules it applies to filter clips, then click Create Smart Bin.

### Showing Bins in Separate Windows

Right-clicking a bin in the Bin List lets you pick “Open As New Window” to break that bin out into a window of its own. Every such window is a Media Pool in its own right; it carries a Bin List of its own, the Power Bins and Smart Bins lists, plus its own display controls.

### Media Pool bins opened as new windows

This pays off most when two displays hang off your workstation, since you can drag these separate bins onto the second display while DaVinci Resolve runs in single screen mode. Hiding the Bin list not only frees up more room for clips, it also keeps you from accidentally switching bins when all you want is to view one particular bin’s contents in that window. You may keep as many extra Bin windows open as you like, on top of the main Media Pool docked in the primary window interface.

### Filtering Bins Using Color Tags

When a project carries a great many bins, color tags let you mark particular bins with one of eight colors. Tagging a bin is as easy as right-clicking it and picking the color you want from the Color Tag submenu. You might, say, mark the bins holding the clips you reach for most often with a red tag. A bin’s color tag then shows up as a colored background behind that bin’s name. After you’ve tagged one or more Media Pool bins, the Color Tag Filter drop-down menu (the drop-down control just right of the Bin List button) filters away every bin but a single color. To return to seeing all the bins on hand, pick Show All from the Color Tag Filter drop-down.

### Using Color Tags to identify bins

Using color tag filtering to isolate the red bins

### Sorting the Bin List

The Media Pool’s Bin list (and Smart Bin list) can be sorted by Bin Name, Date Created, or Date Modified, ascending or descending. Just right-click anywhere within the Bin list and, from the contextual menu’s Sort by submenu, pick the options you want. That same contextual menu also offers User Sort, which lets you drag every bin in the Bin list by hand into whatever order suits you. While you drag bins in this mode, a highlighted line shows the new position a bin will take when you drop it. Once you’ve used User Sort in the Bin list to arrange your bins by hand, you can flip back and forth among the remaining sorting methods — Name, Date Created, Date Modified — and User Sort, with your manual User Sort order preserved, so you can lean on whichever bin-sorting method serves you best at the moment without losing your custom bin organization.

Within User Sort mode, dragging a bin into a fresh spot in the Bin list.
