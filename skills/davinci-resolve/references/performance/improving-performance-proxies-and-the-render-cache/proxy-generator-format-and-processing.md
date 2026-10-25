# Setting the proxy format and processing pane of the blackmagic proxy generator

Version: DaVinci Resolve 20.3 Reference Manual. Context: Improving performance proxies and the render cache.
[Chapter index](INDEX.md) / [Previous section](watch-folders.md) / [Next section](proxy-only-archives-and-remote-work.md)
<a id="source-creating-a-proxy-only-archive-to-share"></a> <a id="source-generating-proxy-media-in-other-applications"></a> <a id="source-managing-proxies-from-the-blackmagic-proxy-generator"></a> <a id="source-managing-proxy-media"></a> <a id="source-moving-proxies-using-a-davinci-resolve-archive-dra"></a> <a id="source-re-generating-proxy-media"></a> <a id="source-setting-the-proxy-format"></a> <a id="source-switching-between-proxy-media-and-original-media"></a> <a id="source-the-processing-pane-of-the-blackmagic-proxy-generator"></a> <a id="source-using-proxy-files-for-delivery"></a>

### Setting the Proxy Format

Pick whichever proxy codec you want by choosing its format from this list.

Within the Blackmagic Proxy Generator's Proxy Media Format section Starting and Stopping the Blackmagic Proxy Generator With a watch folder in place and a proxy format chosen, the only remaining step is to hit the Start button in the Processing pane, which kicks off automatic transcoding and watch-folder monitoring. Should you need to halt the process at any moment, simply hit the Stop button. Pressing the space bar likewise toggles Start/Stop.

### The Processing pane of the Blackmagic Proxy Generator

The Processing pane also surfaces the current job's status. It charts the job's progress through a count of clips rendered (x of x), a progress bar, and a percentage readout. Alongside that, it shows the current clip's name, the frames-per-second (fps) at which the render is running, and an estimate of the time still remaining.

### Managing Proxies from the Blackmagic Proxy Generator

Two options exist for handling your proxy files after they're made. They only become available once Processing mode has been stopped. Delete Proxies: This wipes every proxy file (along with the Proxy folder) out of the chosen watch folders. Extract Proxies: This duplicates all proxy files from the chosen watch folders into a new spot picked in the file system dialog. It's handy for assembling a standalone proxy-only folder you can pass to someone else on a portable hard drive or push up to cloud storage. Linking Proxies from the Blackmagic Proxy Generator in DaVinci Resolve After your proxies exist, DaVinci Resolve links them to their original source media on its own the moment you bring the watch folder's original clips into the Media Pool. Manual linking and unlinking is also possible, as the Managing Proxy Media section covers later in this chapter.

### Generating Proxy Media in Other Applications

You can also build proxy files in software beyond DaVinci Resolve, such as other NLEs or assorted media asset management systems. For the proxy to link cleanly to its source media inside DaVinci Resolve, the proxy file has to satisfy these conditions:

- A proxy file's timecode must be identical to that of the source file.
- A proxy file's name must match the source file's (extensions aside).
- A proxy file's frame rate must equal the source file's.
- DaVinci Resolve must support whatever format and codec the proxy files use.

Provided your proxy file clears these conditions, you'll be able to hand-link proxy media made in other software to source clips within the Media Pool, as described below.

### Managing Proxy Media

The status and whereabouts of all your proxy media show up in the Media Pool's List view. Right-click any column heading and tick the boxes for “Proxy” and “Proxy Media Path.”

- Proxy: This column reports the proxy status as it stands. None: Signals that no proxy media exists yet. Offline: Signals that a proxy was made but isn't turning up at the Proxy Media path. (Resolution): A figure giving the made proxy's resolution and confirming it's online.
- Proxy Media Path: Where DaVinci Resolve expects to find the proxy file. Should that spot be wrong, you can hand-relink the proxy to a fresh path.

In List view the proxy columns lay out each clip's Proxy Media status and location Linking Clips to Proxy Media When you've built proxy media in another piece of software, or relocated the internally built proxy media away from its default home in “ProxyMedia,“ the proxies will need hand-linking to their source media files inside your Media Pool. Here's how to link proxy media onto a source clip: 1 Pick one or more clips in the Media Pool you want to attach proxy media to. 2 Right-click one of those chosen clips and pick “Link Proxy Media” off the contextual menu. 3 Through the file browser, locate the specific proxy file or directory (where several clips are involved) to establish a new Proxy Media path, then click Open. Pick a wrong file or directory and a warning dialog box pops up with no linking taking place. 4 When the linking succeeds, the proxy media icon turns up on the clip's thumbnail in the Media Pool.

The Proxy Icon sitting at the thumbnail's lower-left corner, a sign that proxy media is linked for this clip Here's how to unlink proxy media off a source clip: 1 Pick a clip or clips in the Media Pool you want to detach proxy media from. 2 Right-click any clip and pick “Unlink Proxy Media” off the contextual menu. Doing so severs the metadata link running from proxy to source and resets the Proxy column's status to “None.” NOTE: Unlinking a proxy file leaves it intact. The proxy file stays put on the hard drive where it was first made. At the time of writing, removing proxy files calls for deleting them by hand through your OS file system, outside DaVinci Resolve.

### Re-generating Proxy Media

Nothing stops you from making several proxy files for a single clip. That's handy when you want to dial in different Camera Raw parameters and weigh them against each other, or to turn out proxy files at varied resolutions. To generate a new proxy: 1 Apply whatever tweaks you like to the current clip's settings. 2 Right-click that same clip and pick “Generate Proxy Media” off the contextual menu. The new proxy file lands in the same directory as the proxy file linked before it, with “\_s00x” tacked onto its file name to set it apart. While the newest proxy is linked to the source file automatically, your earlier proxy versions stay on disk, leaving you free to relink the various versions by hand whenever you need.

### Switching Between Proxy Media and Original Media

To flip between playing back your original source media and the proxy media, use the Proxy Handling icon in the Viewer on the Cut page, or on the Edit page go to Playback > Proxy Handling and choose one of the options below.

- Disable All Proxies: This shuts the proxies off entirely and compels original-media playback alone. Where the original media is missing, the clip gives way to a Media Offline graphic.
- Prefer Proxies: This plays proxy files back, and where a clip has no proxy file, the original media steps in on its own. Where the original media is missing, the proxies serve instead, and the timeline carries a purple line for as long as the original clips are absent.
- Prefer Camera Originals: This plays the original media files back, and where a clip lacks an original media file, the proxy media steps in on its own, with the timeline carrying a purple line for as long as the original clips are absent.

TIP: No matter the proxy mode, a purple line across your timeline flags missing original media and serves as a visual cue to help you spot those absent clips.

### Using Proxy Files for Delivery

Out of the box, the Deliver page always falls back to the original source media for final output, guaranteeing the top-quality render. Ticking the “Use proxy media” box under the Advanced Settings of the Deliver page's Video Render settings flips this, so DaVinci Resolve turns to proxy media for final output instead. That can pay off when you need to trim rendering time while cutting dailies, or to quickly knock out timeline outputs for producers or audio engineers where master quality isn't strictly called for. You'll likewise have to tick the “Use proxy media” box whenever you're editing with proxies and lack access to the original source media.

### Moving Proxies Using a DaVinci Resolve Archive (.dra)

Shifting proxies from one DaVinci Resolve system over to another can prove slow and troublesome if you hand-copy a host of separate assets (proxies, graphics, source files, etc.) out of scattered folders and locations. The simplest route by a wide margin for relocating whole projects between systems is to hand that file management off to DaVinci Resolve, by building a DaVinci Resolve Archive (.dra). An archive file holds not just your project but every piece of its media too, preserving the original project's file paths and organization. To build a DaVinci Resolve Archive file, right-click any project in the Project Manager and pick “Export Project Archive” off the drop-down menu. Inside this mechanism, a new Archive setting in DaVinci Resolve renders proxy handling clean and effortless.

### Creating a Proxy-Only Archive to Share

Within the Archive Options dialog, ticking Proxy Media while unticking Media Files and Render Cache tells DaVinci Resolve to build an Archive from the proxy media alone. That lets you assemble a slim, easily shipped version of your project, whether to carry to another computer or to pass to an editor working from afar. Where a clip has no proxy media (a graphic, say, or a media file you never made a proxy for to begin with), the original media exports automatically so that nothing winds up offline.
