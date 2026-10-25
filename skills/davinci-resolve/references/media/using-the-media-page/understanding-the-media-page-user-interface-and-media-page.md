# Understanding the media page user interface and media page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the media page.
[Chapter index](INDEX.md) / [Next section](list-view-and-thumbnail-view.md)
<a id="source-adding-volumes-that-dont-appear-in-this-list"></a> <a id="source-media-storage-browser-with-scrubbable-clip-view"></a> <a id="source-playing-dcp-and-imf-packages"></a> <a id="source-playing-media-in-the-media-storage-browser"></a> <a id="source-showing-which-panel-has-focus"></a> <a id="source-the-interface-toolbar"></a> <a id="source-the-interface-toolbar-1"></a> <a id="source-the-media-page"></a> <a id="source-the-media-storage-browser"></a> <a id="source-the-media-storage-browser-area"></a> <a id="source-the-media-storage-browsers-volume-list"></a> <a id="source-understanding-the-media-page-user-interface"></a> <a id="source-using-the-media-page"></a> <a id="source-using-the-media-page-part-1"></a>

### Using the Media Page

Within DaVinci Resolve, the Media page acts as the chief hub for bringing in media and arranging clips. It is likewise the spot where every timeline you cut in DaVinci Resolve or pull in from elsewhere gets arranged. Even though both timelines and clips live in the Media Pool, a core principle of how DaVinci Resolve operates is that a project's source media is kept apart from its timelines. That separation lets you handle and refresh the clips that timelines rely on without fuss — bringing clips in, rearranging them, flipping between offline and online media, and sorting out whatever issues crop up. The Media page also houses a great deal of the central machinery behind on-set workflows, along with the bulk of the functions involved in the ingest, organization, and sound-syncing steps tied to digital dailies workflows.

### Understanding the Media Page User Interface

Out of the box, the Media page splits into five separate regions, laid out to make finding, picking, and handling your project's media straightforward.

### The Media page

A large share of the functionality, and the majority of the commands, live inside the contextual menus that pop up when you right-click clips within the Media Storage browser or Media Pool.

### The Interface Toolbar

Running across the very top of the Media page sits a toolbar whose buttons reveal and conceal various pieces of the user interface. Listed from left to right, those buttons are:

### The Interface toolbar

- Media Storage full/half height button: Stretches the Media Storage browser to span your display's full height when you want extra browsing room, trading away a smaller Media Pool.
- Media Storage: Toggles the Media Storage browser between shown and hidden. Tucking the Media Storage browser away frees up additional space for the Viewer.
- Clone Tool: Reveals or conceals the Clone tool, which copies media off camera cards or hard drives.
- Audio Panel: Conceals or reveals the Audio Panel.
- Metadata: Conceals or reveals the Metadata Editor.
- Inspector: Conceals or reveals the Inspector Panels.
- Capture: Flips the Viewer and Audio Panel into Capture Mode, surfacing the controls needed

for cuing up a device-controllable deck, and batch recording from tape.

- Audio Panel/Metadata Editor full/half height button: Stretches the Audio Panel or Metadata

Editor to span your display's full height when you need extra room for either of those functions.

### Showing Which Panel Has Focus

Each time you click somewhere on the DaVinci Resolve interface with the pointer, or rely on a keyboard shortcut to “select” a given panel (as you might on the Edit page), you hand that panel of the user interface “focus.” A focused panel grabs particular keyboard shortcuts so they act inside that panel rather than somewhere else in the interface. Off by default, ticking the “Show focus indicators in the user interface” box within the UI Settings section of the User Preferences makes an orange highlight show along the top edge of the focused panel, helping you track which portion of the current page holds sway. You can shift focus as needed to accomplish whatever you set out to do.

Here the Focus indicator rides along the Media Pool's top edge, alongside a Viewer lacking focus

### The Media Storage Browser

Through the Media Storage browser you can view every volume hooked up to your workstation, scanning them for media you would like to preview and ultimately bring into your DaVinci Resolve project in some fashion. Where other applications lean on a kind of import dialog, DaVinci Resolve hands you the Media page for tackling involved media import tasks. So that media import goes smoothly, the Media Storage browser is split into two regions, the Volume List and the Media Browser.

### Media Storage browser with scrubbable clip view

### Playing Media in the Media Storage Browser

You can pick media in the Media Storage Browser and play it straight in the Media page Viewer, with no import needed, provided it sits in a format DaVinci Resolve handles. That comes in handy for previewing clips you are weighing for a project, and equally so for quality control review sessions of media you have exported out of DaVinci Resolve. Any clip played in the Media page Viewer is also sent out to video, assuming you have a supported Blackmagic output interface. You can additionally route the video to a second monitor by picking Workspace > Video Clean Feed and choosing your monitor. What's more, if you pick Workspace > Dual Screen > On, the second computer display can present a row of video scopes on the Media page, which can assist you in QC-ing a program you are delivering.

### Playing DCP and IMF Packages

The Media Storage Browser can likewise be used to pick and play DCP and IMF packages exported either through EasyDCP or through the native DCP/IMF export capabilities of DaVinci Resolve. Just track down the package, pick it, and play it in the Viewer as you would any other clip. It gets sent out to video and examined by the video scopes. DCP and IMF packages may also be brought in from Media Storage into the Media Pool for assorted workflows. For more information, see Chapter 188, “Delivering DCP and IMF.”

### The Media Storage Browser’s Volume List

Down the left side of the Media Storage browser runs a list of every volume presently reachable by your DaVinci Resolve workstation. Its purpose is to help you locate media you want to bring into your project by hand. Scratch volumes: Marked by a usage statistic to the right of the volume name reporting how full that volume is, these are the disks you have added in the Media Storage panel of the System Preferences window. The first of these scratch disks holds Gallery stills and cache files. Available volumes: Marked by disk icons, this lists every fixed, removable, and network volume currently reachable by your workstation. With the “Automatically display attached local and network storage locations” checkbox switched on in the Media Storage panel of the DaVinci Resolve Preferences, fresh volumes you attach to your workstation ought to surface in this list on their own. The list is hierarchical; clicking the disclosure triangle beside any volume reveals a further list of that volume's subdirectories, each carrying its own disclosure triangle. The Media Storage browser lets you burrow through as many subdirectories as you require.

### Adding Volumes That Don’t Appear in This List

Should you need to reach a storage volume that is absent from this list — for instance when you are running the version of DaVinci Resolve sold in the Apple App Store — you can right-click on any empty part of the Volume list's background and pick “Add New Location,” which brings up a dialog for choosing a volume to add.

When you are running the Apple App Store version of DaVinci Resolve, attached storage volumes are not auto-mounted by default. You can, however, switch it on within the DaVinci Resolve Preferences, over in the Media Storage panel. Further detail lives in the DaVinci Resolve Preferences section; consult Chapter 4, “System and User Preferences.” Media Storage Browser Favorites Below this lies the Favorites area. When there are particular directories you keep returning to, you can pin them to the Favorites so you avoid wading through tangled hierarchies every time you reach for the media you need. Customizing and working with the Favorites is straightforward. Ways to arrange favorite file system locations in the Media Storage Browser:

- To add a favorite: Within the Media Storage browser folder list, right-click whatever folder you want, then pick “Add folder to favorites” from the contextual menu. Your new favorite shows up at the bottom of the Favorites area.
- To open a favorite: Click any favorite to reveal that directory's contents inside the Media Storage browser.
- To remove a favorite: Right-click whichever favorite you want gone, and pick “Remove folder from favorites” from the contextual menu.

### The Media Storage Browser Area

After you have picked a volume or subdirectory in the Media Storage browser, you can take in its contents through List view, Thumbnail view, or Metadata view to dig through the media on hand as you hunt for what you need.
