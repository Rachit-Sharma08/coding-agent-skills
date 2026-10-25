# Preview player in the media pool and bins power bins and smart bins

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](3d-pan-window-and-monitoring-panel.md) / [Next section](separate-bin-windows-and-color-filters.md)
<a id="source-bins-power-bins-and-smart-bins"></a> <a id="source-the-preview-player-in-the-media-pool"></a> <a id="source-using-the-fairlight-page-part-3"></a>

### The preview player in the Media Pool

- A range of viewing controls fills the title bar up top. At the upper left, a dropdown menu picks the zoom level for the audio waveform on display. Just right of it, a Timecode window reports either the clip’s duration or the duration bracketed by In and Out points. Continuing rightward, a live performance indicator reflects playback performance. Centered there is the title of the clip you’ve currently got selected, and a dropdown to its right lists the last 10 clips you’ve looked through. At the far right, a Timecode field reports where the playhead currently sits (right-click it for a contextual menu that switches which timecode shows and that copies and pastes timecode).
- The middle of the Media Pool Preview Player lays out the waveforms across all channels of the clip you’ve selected, at whichever zoom level is active.
- Down at the bottom, the transport controls comprise a jog bar for scrubbing, Stop, Play, and Loop buttons, and buttons that set In and Out.

### Bins, Power Bins, and Smart Bins

In fact the Media Pool holds three distinct sorts of bins, and the Bin list keeps each one in a section of its own. Within that list, the Power Bin and Smart Bin zones can both be brought into view or tucked away using the Media Pool Options menu (…), whose Show Smart Bins and Show Power Bins entries handle exactly that. The distinctions among the bin types break down as follows:

- Bins: Plain bins that you fill by hand. Drop whatever you wish into a bin and there it stays, right up until you choose to shift it into a different bin. Bins can be arranged in a hierarchy, so feel free to nest one bin within another. Making a fresh bin is just a matter of right-clicking inside the bin list and picking Add Bin off the contextual menu.
- Power Bins: Tucked away by default. Power bins are common to every project in your current project library, which makes them a natural home for assets you reuse — shared title generators, then graphics movies plus stills, alongside sound effects library files, music files, and any other media you'd like to reach fast from any project. Whatever materials you drop into Power Bins go there by hand; it's a manual process. To start a new Power Bin, reveal the Power Bins region of the Bin list, then right-click inside it and pick Add Bin.
- Smart Bins: These bins assemble “custom collections” of media, leaning on metadata or analysis to fill themselves dynamically, so their contents shift according to whatever the Smart Bin is told to watch for. A sound effects Smart Bin, say, surfaces only sound effects, and that bin's contents swell or shrink with however many effects files the project has spotted, a figure that can move over time. Smart Bins make organizing a project's contents quick and tidy.

A handful of Smart Bin types get built automatically (look under Preferences > User> Editing > Automatic Smart Bins). You can let Resolve's Audio Classification analysis sort your files into categories (which builds “Collections” smart bins on its own). Alternatively, add metadata to your clips by hand through the Metadata Editor — Scene, Shot, and Take details, keywords, comments and description text, and so on — to speed up finding what you need later. You're also free to define your own rules for a Smart Bin. To build a new custom Smart Bin, confirm the Smart Bin region of the Bin list is on screen, then right-click inside it and pick Add Smart Bin. A dialog opens where you set that bin's name and the rules it applies to filter clips, after which you click Create Smart Bin.

NOTE: To see Smart Bins beyond Keywords and Collections, you first have to switch on any extra Smart Bin options under Smart Bin Preferences > User > Editing > Automatic Smart Bins.
