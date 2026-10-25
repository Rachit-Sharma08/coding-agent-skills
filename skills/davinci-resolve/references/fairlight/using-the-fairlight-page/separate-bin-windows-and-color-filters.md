# Showing bins in separate windows and filtering bins using color tags

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](media-pool-preview-and-bin-types.md) / [Next section](list-panel-of-the-adr-interface-and-record-panel.md)
<a id="source-adr"></a> <a id="source-effects-library"></a> <a id="source-effects-library-favorites"></a> <a id="source-filtering-bins-using-color-tags"></a> <a id="source-filtering-clips-with-audio-in-the-fairlight-page"></a> <a id="source-showing-bins-in-separate-windows"></a> <a id="source-sort-mode"></a> <a id="source-sorting-the-bin-list"></a> <a id="source-the-audio-only-smart-bin"></a> <a id="source-the-effects-library"></a> <a id="source-the-list-panel"></a> <a id="source-using-color-tags-to-identify-bins"></a>

### Showing Bins in Separate Windows

Right-click a bin in the Bin list and you can pick “Open As New Window” to pop that bin out into a window of its own. Every such window is a Media Pool in its own right, carrying its own Bin list, its own Power Bins and Smart Bins lists, and its own display controls. That comes in most handy with two displays hooked up to your workstation, since you can drag these separated bins onto the second display while DaVinci Resolve runs in single screen mode. Hiding the Bin list both frees up room for clips and stops you from switching bins by accident when you mean to view only one bin's contents in that window. You can keep open as many extra Bin windows as you like, on top of the main Media Pool docked in the primary window interface.

### Filtering Bins Using Color Tags

On a project loaded with bins, you can mark out specific ones using any of eight colors: right-click a bin and pick the color you want out of the Color Tag submenu. For instance, mark the bins holding the clips you reach for most with a red tag. From then on a bin's color tag shows up as a colored field behind that bin's name. After you've tagged one or more Media Pool bins, the Color Tag Filter dropdown menu (the dropdown control sitting to the right of the Bin List button) lets you hide every bin but one color. To return to seeing all the bins, pick Show All from the Color Tag Filter dropdown.

### Using color tags to identify bins

Using Color Tag filtering to isolate the red bins

### Sorting the Bin List

You can order the Media Pool's Bin list (along with the Smart Bin list) by Bin Name, Date Created, or Date Modified, going up or down. Just right-click anywhere inside the Bin list and pick what you want from the Sort by submenu of the contextual menu. That same contextual menu also offers User Sort, which lets you drag every bin in the Bin list by hand into whatever order suits you. While you drag bins this way, a red line marks where the bin will land on release. Once you've used User Sort in the Bin list to arrange your bins by hand, you can flip freely between any of the other sort methods (Name, Date Created, Date Modified) and User Sort. Your hand-set User Sort order is kept, so it's easy to switch to whichever sort method serves you best at the moment without giving up your custom bin arrangement.

Moving a bin to a fresh spot within the Bin list while User Sort mode is active

### Filtering Clips With Audio in the Fairlight Page

On the Cut, Edit, Color, Fusion and Fairlight pages, the Media Pool can surface Audio Only clips through the Collections smart bin named “Audio Only,” which lives in the Collections area of Smart Bins. That makes it simple to track down the audio clips you're after when they're buried among a heap of video clips in the same bin.

### Sort mode

### The Audio Only Smart Bin

The Media Pool filter options in the option menu

Should you want a few extra options, the Media Pool on the Fairlight page can also screen out audio-only clips, or video clips that carry audio, within whichever bin is selected. To do this, click the Media Pool's Option menu and pick from its choices: Show All Clips, then Show Audio Only Clips, or else Show Clips With Audio, plus Show Audio Waveforms, along with Show Non-Rectified Audio Waveforms.

### Effects Library

The Fairlight page's Effects Library lists both the built-in Fairlight FX audio plugins that ship with DaVinci Resolve on macOS, Windows, and Linux, as well as whichever Audio FX happen to live on your workstation.

- Fairlight FX are built-in audio processing effects that run cross-platform across every platform DaVinci Resolve supports.
- Under macOS and Windows, third-party VST audio plugins are supported by DaVinci Resolve.
- On macOS, DaVinci Resolve supports Audio Unit (AU) audio plugins.

After you install third-party effects on your workstation, they show up in this Effects Library panel next to the Fairlight FX that are always on hand. With audio plugins you can drop effects onto audio clips, or run one as a real-time process across a whole audio track (touching every clip on it), to apply basic dynamics, or tonal work like compression, limiting or EQ and noise reduction, or else inventive spatial effects such as delay or reverb.

### The Effects Library

Much like the Media Pool, you open or close the Effects Library's Bin list with a button up at the top left.

### Effects Library Favorites

To mark an effect as a Favorite:

- Move the pointer over the far right of any effect until a star shows up
- Click that star to drop the effect into the Favorites effects list.
- Favorites turn up in their own region at the lower left, beside the Effects Library Bin list.

Stars indicate a flagged favorite effect, all favorites are currently filtered NOTE: Whatever you flag as Favorites in the Effects Library list also rises to the top of the Mixer's Effects dropdown menu effects list.

### ADR

DaVinci Resolve's Fairlight page carries a refined yet approachable interface for “ADR” (Automated Dialog Replacement) work. Thorough cue list handling, industry-standard audio beeps and visual cues, plus refined take handling with star ratings and layered take grouping all help you stay on top of your work while pulling the best moments from each performance. Once open, the ADR interface presents, just left of the Timeline, a trio of panels: a List panel, then a Record panel, and finally a Setup panel.

### The List Panel

Here is where you assemble a list of the cues you need to re-record, whether you build it inside the Fairlight page or bring it in from a .csv file someone hands you. It offers controls for adding, editing, importing, and exporting the cues you mean to record.
