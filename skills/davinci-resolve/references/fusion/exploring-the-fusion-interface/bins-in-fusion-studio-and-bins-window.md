# Bins in Fusion studio and bins window

Version: DaVinci Resolve 20.3 Reference Manual. Context: Exploring the Fusion interface.
[Chapter index](INDEX.md) / [Previous section](control-point-interpolation.md) / [Next section](fusion-and-fusion-studio-keyboard-remapping.md)
<a id="source-bins-in-fusion-studio"></a> <a id="source-bins-interface"></a> <a id="source-customizing-fusion"></a> <a id="source-fusion-studio-floating-frame"></a> <a id="source-resizing-panels"></a> <a id="source-showing-and-hiding-panels"></a> <a id="source-the-bin-list-sidebar"></a> <a id="source-the-bin-studio-player"></a> <a id="source-the-bin-studio-player-1"></a> <a id="source-the-bins-icon-view"></a> <a id="source-the-bins-toolbar"></a> <a id="source-the-bins-window"></a> <a id="source-the-console"></a> <a id="source-the-console-window"></a> <a id="source-the-fusion-settings-window"></a> <a id="source-the-ui-toolbar-of-the-fusion-page"></a>

### Bins in Fusion Studio

Bins over in Fusion Studio play much the same role as the Media Pool does in DaVinci Resolve. Bins are organizing panels that give you a tidy way to reach frequently used tools, settings, macros, compositions, and media content. They hold all your custom content and resources within arm's reach, so you can call on them without digging through your hard drives. Bins can also travel across a network to smooth a collaborative workflow alongside other Fusion Studio artists.

### The Bins window

To open the Bins window: Choose File > Bins from the menu bar. As with the Media Pool in DaVinci Resolve, dropping an item into the Fusion bins forges a link between the on-disk item and the bins. Fusion makes no copy of the file in its own cache or drive space. The file holds its original format and stays put in its original spot.

### Bins Interface

The Bins window is in fact a standalone application for stashing content you might want to reach for again down the line. Two panels split the Bins window. On the left, the sidebar is a bin list where items get sorted into categories, while the right panel shows the chosen bin's content.

### The Bin list sidebar

The Bin list sorts content into bins or folders through a hierarchical List view. You're free to arrange these folders to match your workflow, though standard ones come supplied for Clips, Compositions, Favorites, Settings, and Tools. Parent folders house subfolders that carry the content. The Tools bin, for one, acts as parent folder over every category of tools. To reach subfolders, click the disclosure arrow beside the parent folder's name. Choosing a bin from the bin list throws that folder's contents up in the Contents panel as thumbnail icons.

### The Bins icon view

Running along the bottom of the bin, a toolbar opens up organization, playback, and editing controls.

### The Bins toolbar

New Folder: Spins up a fresh folder inside the current window. New Reel: Spins up an empty reel able to hold several clips cut together into a timeline. New Clip: Brings up a dialog for linking a fresh media file into a bin. Studio Player: Brings up a playback viewer for a chosen clip.

Icon/List view: This button flips between showing a bin's contents in thumbnail view and in list view. Checkerboard: Lays a checkerboard pattern over a clip thumbnail to flag transparency. Thumbnail size: Hands you a handful of preset sizes for thumbnail icons.

Right-clicking anywhere across the bin window throws up a pop-up menu reaching most of a bin's features. Right-clicking an item inside a bin shows that same menu plus extra options for renaming, playing, or deleting the item.

### The Bin Studio Player

Choose a clip inside a bin and press the Studio Player button — or just double-click the clip — and the Studio Player opens. You can lean on the Studio Player to view clips, view metadata, and jot notes.

### The Bin Studio Player

To read further about Bins, turn to Chapter 13, “Bins” in the Fusion Referance Manual.

### The Console

The Console is a window where you can watch the error, log, script, and input messages that may spell out in fuller detail something Fusion is attempting. It's likewise where you read FusionScript outputs, or feed FusionScripts in directly. Within DaVinci Resolve, you reach the Console by choosing Workspace > Console, or by choosing View > Console in Fusion Studio. A Console button also sits in the Fusion Studio User Interface toolbar. Now and then the Status bar flashes a badge to tip you off that there's a message in the Console worth a look.

### The Console window

Up top, a toolbar on the Console holds the controls that steer what the Console displays. Off to the top left, the Clear Screen button wipes the Console's contents. The four buttons after it flip the visibility of error messages, log messages, script messages, and input echoing. Limiting the view to one kind of message can help you track down what you're after when you're racing the clock at 3:00 in the morning. The three buttons beyond those let you pick the input script language. Lua 5.1 stands as the default and ships with Fusion. Python 2.x and Python 3.x call for you to set up the matching Python environment on your machine. Since scripts in the Console run right away, you can hop between input languages whenever you like. Down at the foot of the Console is an Entry field. Scripting commands typed here run in the current comp context. You enter scripts a line at a time, and they fire off immediately. For more information on scripting, see the Fusion Scripting Manual.

### Customizing Fusion

This section lays out how you can tailor Fusion to fit whatever workflow you happen to be chasing.

### The Fusion Settings Window

Fusion carries a settings window of its own, reached in DaVinci Resolve via Fusion > Fusion Settings, or inside Fusion Studio via Fusion > Preferences on macOS, while on Windows or Linux it's File > Preferences. A whole assortment of options for tailoring how Fusion works lives in that window. To read further, the place to look is Chapter 75, “Preferences,” within the DaVinci Resolve Reference Manual — or else Chapter 15 of the Fusion Reference Manual.

The Fusion Settings window set to the General panel Saving Fusion Layouts You can tailor how panels are laid out and configured to fit your desktop and monitor size, or simply to match your own taste. Within DaVinci Resolve, set up and resize whichever panels you want shown, and then: Choose Workspace > Layout Presets > Save Layout Presets.

Over in Fusion Studio, set up and resize whichever panels you want shown, and after that:

- Press the Grab Document Layout button over in the Preferences > Layout panel so the layout sticks for every new Composition.
- Press the Grab Program Layout button to hold onto where any floating views sit and how big they are, then tick the Create Floating Views checkbox so the floating windows spring back up when Fusion restarts.

### Showing and Hiding Panels

Up at the top of the screen, the UI toolbar lets you bring up the panels you need and tuck away those you don't. It's the quickest route to throwing together a layout for whatever you're after in the moment.

### The UI toolbar of the Fusion page

### Resizing Panels

You can reset each panel's overall size through preset configurations, or tune them by hand. The viewers and the Work panel run opposite one another. The more room handed to the Work panel, the less is left for the viewers. To resize a panel, drag by hand anywhere along the raised border that rings the panel's edges.

Dragging the edge between two viewers to resize it

### Fusion Studio Floating Frame

Fusion Studio ships with a Floating Frame window able to hold any panel. To drop a panel into the Floating Frame, do this: 1 Within Fusion Studio, choose Window > New Floating Frame. 2 Right-click inside the Floating Frame and pick the panel out of the Add View submenu. Across multiple monitors, you can opt to scatter floating panels over your displays for extra freedom.
