# Automatic smart bin creation and manual smart bin creation

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](media-pool-selection-and-bin-organization.md) / [Next section](smart-bins-and-metadata.md)
<a id="source-adding-and-organizing-media-with-the-media-pool-part-3"></a> <a id="source-automatic-smart-bin-creation"></a> <a id="source-manual-smart-bin-creation"></a>

### Automatic Smart Bin Creation

Adding metadata to your clips can power the automatic creation of sets of “Smart Categories,” which are Smart Bins generated and arranged by the presence of particular categories of metadata and shown in the Smart Bins section of the Media Pool sidebar. Turning this behavior on or off is a matter of opening the User Preferences to its Editing panel, where the checkboxes within the Automatic Smart Bins group let you decide which metadata spawns Smart Bins on its own.

Preferences that set which metadata is allowed to spawn Smart Bins on its own. The metadata that can give rise to Smart Bins covers:

- Clip Keywords
- Marker Keywords
- People Keywords (added via People Detection)
- Scene metadata
- Shot metadata

These categories follow a hierarchy, with each one collapsed by default to conserve space. Click the disclosure triangle on any category to expose all the Keyword, People, Scene, or Shot Smart Bins available in the current project. Choosing the Smart Category’s top bin lets you view every clip referenced by every Smart Bin nested inside it, whereas choosing individual Smart Bins shows only the clips that particular Smart Bin references.

A Smart Category as it appears within the Smart Bins region of the Media Pool sidebar. Dragging and dropping clips can hand them Automatic Smart Bin Properties, since metadata entry need not flow in one direction alone, starting from keystrokes in the metadata editor. With certain Automatic Smart Bin categories (keywords, shot, and scene), dragging several clips out of the Media Pool onto an existing smart bin passes that bin’s properties to all those clips in one move.

To automatically assign Smart Bin Properties to a range of clips: 1 Build a Smart Bin in one of these categories: Keywords, Shot, or Scene. 2 Pick every clip you want the Smart Bin property applied to. 3 Drag those clips out of the Media Pool and drop them onto the Smart Bin. As an example, you might build a smart bin with the Keyword: “Sunset.” That bin would show up on its own beneath the Keywords category in the Smart Bins. You could then pick all the sunset shots in your Media Pool and drag them onto that bin to hand the “sunset” keyword to every one of those clips at the same moment.

NOTE: Dragging and dropping clips to assign Smart Bin properties works only with the Automatic Smart Bin Keywords, Shot, or Scene categories. Dragging clips onto any other Smart Bin does nothing.

### Manual Smart Bin Creation

Hand-building Smart Bins with custom rules to filter very specific collections of media and timelines you want to work with is easy. To show or hide the Smart Bin area of the Bin list:

- Pick Show Smart Bins from the Media Pool option menu to flip the visibility of all Smart Bins on or off.

To build a Smart Bin: 1 When required, reveal the Bin list, pick Show Smart Bins from the Media Pool option menu, then right-click any empty spot in the background of the Smart Bin region of the Bin list, and pick Create Smart Bin. 2 Within the Create Smart Bin dialog, type a name for the filter, and rely on the controls below to define one or more filter criteria (there is no limit to how many filter criteria you add):
