# Relink selected clips and change source folder

Version: DaVinci Resolve 20.3 Reference Manual. Context: Adding and organizing media with the media pool.
[Chapter index](INDEX.md) / [Previous section](media-pool-clip-timeline-and-synced-audio-search.md)
<a id="source-change-source-folder"></a> <a id="source-relink-selected-clips"></a>

### Relink Selected Clips

The simplest way to reconnect project clips that have dropped offline is the aptly titled “Relink selected clips” command. Of all the options, it gives you the most freedom, matching project clips against clips in any file system directory you point it at, and leaning on file name and timecode as the main signals for tying each clip to its media file on disk. Relinking in this manner causes DaVinci Resolve to disregard the clip's original file path, which makes it the right command when media has been shuffled around on disk. To relink selected clips: 1 Do one of the following:

- In the Media Pool browser, pick one or more clips you want to relink, then right-click any of the chosen clips or the chosen bin and select “Relink Selected Clips” from the contextual menu.
- From the Media Pool Bin list, pick a bin holding clips you want to relink, then right-click any of the chosen clips or the chosen bin and select “Relink Clips for Selected Bin” from the contextual menu.

2 Once the Relink File dialog appears, point it at a directory where the files you want to relink to should be found, and click OK. DaVinci Resolve then hunts for each clip whose file name matches inside the subdirectories of your chosen directory, leaning on the original file paths of the clips being relinked so the job goes as fast as possible. Because it checks the clips' original directories first, relinking can move along quickly. 3 Should any clips remain unfound through the approach in step 2, a second dialog offers you the chance to run a “deep search.” Clicking Yes tells DaVinci Resolve to comb through every subdirectory beneath the directory you picked back in step 2. That can take considerably more time, yet it ought to succeed fully as long as the needed media lives somewhere inside the chosen directory tree. 4 If certain clips are still missing, you get the choice of either pointing the search at a different directory entirely or stopping.

### Change Source Folder

Suppose you have relocated media tied to a DaVinci Resolve project through your file system but left the directory layout it sits in untouched: the Change Source Folder command can then swiftly reconnect chosen Media Pool clips to the media's new file path on disk, taking the original file paths as its reference. Where it is workable, this relinking approach suits SAN-based projects well, since it spares you the painfully long search times the Relink command might incur while it flexibly digs through a deeply nested folder hierarchy. To relink your Media Pool clips to a new location: 1 In the Media Pool, pick one or more clips, right-click any chosen clip, and select Change Source Folder from the contextual menu. The Relink Media window opens showing the material's original path, along with controls to pick a fresh directory. 2 Click the “Browse” button positioned to the right of the Change To field, then work through the file navigation dialog to locate the media file's new home, select it, and click Open. 3 If the right media file turned up, click Change. If not, click Cancel.
