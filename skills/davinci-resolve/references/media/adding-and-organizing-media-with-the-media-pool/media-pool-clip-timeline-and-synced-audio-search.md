# Finding clips and or timelines within the media pool and finding synced audio

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](media-pool-thumbnail-sorting-and-list-columns.md) / [Next section](relink-selected-clips-and-change-source-folder.md)
<a id="source-adding-and-organizing-media-with-the-media-pool-part-4"></a> <a id="source-finding-clips-andor-timelines-within-the-media-pool"></a> <a id="source-finding-media-in-the-media-storage-panel-and-finder"></a> <a id="source-finding-synced-audio"></a> <a id="source-finding-timeline-clips-in-the-media-pool"></a> <a id="source-finding-timelines-in-the-media-pool"></a> <a id="source-going-immediately-to-a-file-system-location-in-the-media-browser"></a> <a id="source-list-view-clip-usage-column"></a> <a id="source-relink-media"></a> <a id="source-relinking-media-simply"></a> <a id="source-the-update-usage-dialog"></a> <a id="source-thumbnail-clip-usage-indicators"></a> <a id="source-tracking-media-usage"></a> <a id="source-updating-clip-usage-for-all-timelines"></a>

### Finding Clips and/or Timelines Within the Media Pool

Clicking the magnifying glass button at the top-right corner of the Media Pool brings up the Search Options, which by default let you find one or more clips within the currently selected bin or bins, going by the metadata picked in the Filter By drop-down menu just to its left.

The Search Options drop-down menu (pictured here in the Edit page Media Pool) governs which metadata your search targets A separate drop-down right beside the magnifying glass icon controls the breadth of that search. It governs whether the search combs through every bin in the active project for the stated criteria, or limits itself to the open bin alone, or to the bins picked out in the Bin list, useful when you’re after a media instance held at a specific hierarchical spot of the Media Pool. Sitting beside the magnifying glass icon, that drop-down is where the bin search parameters get set

To track down a clip in the Media Pool: 1 (Optional) Via the drop-down beside the Search button — the one that reveals the Media Pool’s Search and Filter by controls — pick either All Bins or Selected Bins. 2 (Optional) Should you be searching Selected Bins, reveal the Bin list and pick whichever bin or bins you mean to search. 3 (Optional) Pick a criteria off the Search Options drop-down menu at the Media Pool’s upper right; All Fields hunts across every metadata column in the Media Pool simultaneously, while a particular criteria narrows the search down. 4 Enter a search term into the Search field. As soon as your typing begins, any clip not matching the search criteria is hidden for the moment. Click the cancel button on the right side of the search field to restore the full set of clips in the Media Pool.

### Finding Synced Audio

Once dual-system audio and video clips have been synced together inside DaVinci Resolve, the steps below let you locate the audio clip a given video clip was synced with. To pin down the audio clip a particular video clip got synced with:

- Put the Media Pool into List view, and check the file name shown in the Synced Audio column.
- Right-click whichever video clip has been synced to audio, then pick “Reveal synced audio in

Media Pool” off the contextual menu. The bin housing the synced audio clip opens, with that clip selected.

### Finding Timeline Clips in the Media Pool

Got a clip in a timeline and need the matching clip it conforms to back in the Media Pool? Right-click the clip, then pick Find in Media Pool off the contextual menu.

### Finding Timelines in the Media Pool

To pin down where the open timeline lives within the Media Pool, head to Timeline > Find Current Timeline in Media Pool.

### Finding Media in the Media Storage Panel and Finder

Should you need to determine the on-disk location of a clip’s source media file, right-click the item within the Media Pool and pick Reveal in Media Storage panel. The Library jumps straight to the folder containing your chosen media file, which sits selected in the Library browser over on the right. There’s also a macOS-only capability: right-click an item in the Media Pool and pick Reveal In Finder. Up comes a file system window displaying the media file the clip is linked to.

Reveal Media Pool Bin from Multi-Bin or Search Displays After a clip search leaves you with hits scattered over several bins, you’re now able to surface that clip’s home in the Media Pool: right-click it and, from the contextual menu, pick Reveal Media Pool Bin.

### Going Immediately to a File System Location in the Media Browser

In reverse, dragging a folder out of the macOS Finder and onto the Media Storage panel makes the Media Storage panel refresh instantly to display that folder’s location.

### Tracking Media Usage

As clips get added to timelines, two mechanisms kick in for keeping tabs on which clips are used in which timelines.

### Thumbnail Clip Usage Indicators

Every time you open a timeline, all thumbnails in the Media Pool refresh automatically to display highlighted usage bars showing you which portions of that clip the timeline uses.

Two colored highlights along the bottom of the thumbnail mark which portions of a clip the currently open timeline uses If you right-click a thumbnail that displays usage, a Usage submenu presents a list of every instance of that clip in the currently open timeline. Picking an instance from that list sends the playhead to that clip in the Timeline.

### List View Clip Usage Column

Surfacing the Usage column while the Media Pool is in List view lets you read a value for how many times a clip turns up in the current timeline. This usage column now updates automatically; no user intervention is required.

Once analyzed, a Usage column reports the count of a clip’s appearances within a timeline.

### Updating Clip Usage for all Timelines

It’s also possible to review which clips have seen use throughout all the timelines in your project. Off the Media Pool Options menu, pick the “Update Usage for Entire Project” option.

### The Update Usage dialog

DaVinci Resolve may ask the user to load all timelines, when needed, and refresh usage counts for Media Pool clips. Depending on how many timelines you have in your project and how complex they are, this can take a while. Once it finishes, that cross-timeline usage tally appears within the Media Pool’s List view under the Usage column. NOTE: For every clip item showing up in the Timeline, the Usage column ticks upward by one. So a clip made of one video item joined with one video item will read 2 in the Usage column.

### Relinking Media Simply

DaVinci Resolve tracks the link between clips in your project and their matching source media on disk. If for any reason the source media tied to clips in your project goes missing, DaVinci Resolve offers several distinct ways to relink those clips in the Media Pool. This section recaps the relinking methods. For fuller coverage of conforming projects and relinking media, refer to Chapter 56, “Conforming and Relinking Clips.”

### Relink Media

Should DaVinci Resolve come up empty looking for your media, the Media Pool on the Cut and Edit page lights up its Relink Media icon in orange.

The Relink Media icon that appears for unlinked media When you click it, a dialog box opens listing the volumes the absent files originally came from. With those details in hand you can hunt the media down on your file system, identify the particular hard drive involved, or check with a client about whether they handed off the media from that volume. Pressing the Locate button reconnects the missing clips to whatever new file location you point it at. Should the fast search that the Locate buttons kick off fail to turn up media you are certain exists, you can launch a thorough, deep scan of the disk by pressing the Disk Search button.

The Relink Media dialog listing the volume names from which the absent clips first came
