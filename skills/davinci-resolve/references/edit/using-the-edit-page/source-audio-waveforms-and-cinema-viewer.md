# Simultaneous audio waveform display in the source viewer and cinema viewer mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](viewer-controls-overview.md) / [Next section](inspector-opened-and-showing-a-clips-parameters-and-timeline.md)
<a id="source-cinema-viewer-mode"></a> <a id="source-copy-and-paste-timecode-in-viewer-timecode-fields"></a> <a id="source-export-the-current-frame-from-the-viewer"></a> <a id="source-fast-review-in-the-timeline-viewer"></a> <a id="source-metadata-editor"></a> <a id="source-opening-clips-in-the-source-viewer"></a> <a id="source-other-viewer-options"></a> <a id="source-simultaneous-audio-waveform-display-in-the-source-viewer"></a> <a id="source-the-end-of-sequence-indicator"></a> <a id="source-the-first-and-last-frame-clip-indicators"></a> <a id="source-the-safe-area-selector"></a> <a id="source-timeline-viewer-edit-overlays"></a> <a id="source-viewer-indicators"></a>

### Simultaneous Audio Waveform Display in the Source Viewer

With the Source Viewer set to Source, a pair of entries in the Option menu can overlay an audio waveform along the viewer’s lower edge, atop the video of whichever clip is currently chosen. Show Zoomed Audio Waveform: Presents a magnified slice of audio that scrolls along as the clip plays. Handy for spotting dialog and music cues during playback of a clip. Show Full Clip Audio Waveform: Displays the audio waveform across the clip’s complete source media. The stretch of audio between the In and Out points you placed in the Source Viewer is highlighted. Handy when you want to move around that clip by treating the audio waveform as a guide.

The Source Viewer with “Show Full Clip Audio Waveform” enabled

### Cinema Viewer Mode

Either the Source or Timeline Viewers can be expanded to fill the whole screen via Cinema Viewer mode, reached through Workspace > Viewer Mode > Cinema Viewer (P); the selected viewer takes over the display, which suits a test screening of your edit free from the clutter of the DaVinci Resolve Edit Page UI. That command flips Cinema Viewer mode on and off.

### Viewer Indicators

Particular frames cause indicators to show up in the Source or Timeline viewers. As an example, when the playhead sits on the very first or final frame of media a given clip holds, markers surface in the lower-left or lower-right corner of the frame to signal that no further media exists in that direction.

### The first and last frame clip indicators

When the Timeline playhead rests on the first black frame that follows the Timeline’s final video clip, an end of sequence indicator shows up in the Timeline Viewer, telling you that the frame on screen is the last of the current run of clips even though the playhead actually sits on black. That makes your work easy to follow as you are first stringing clips together.

### The end-of-sequence indicator

### Other Viewer Options

Further overlays and settings exist for tailoring the viewer’s appearance.

- Safe Area and Guides: From the upper‑right corner of the Timeline Viewer, you can enable and pick one or several Safe Area guides to lay over the Viewer. This lets you readily confirm that the key action in the frame stays well composed against various delivery requirements.
- Show Checkerboard, Black, Gray, or Alert Red Backgrounds in Viewers: Choosing Viewer Background within the Timeline View options recolors any empty region of the Viewer to the chosen option, which makes it simpler to tell apart the parts that read black due to blanking from the parts that are merely empty because of how the image has been zoomed or panned.

### The Safe Area selector

### Fast Review in the Timeline Viewer

Fast Review runs your timeline forward at varying fast-forward rates, with each rate tied to how long the corresponding clip on the Timeline is. Clips of greater length scroll by faster than brief ones. The purpose of the feature is to let you skim quickly across a heavy load of material on a timeline. To call up Fast Review on your Edit page Timeline, choose Playback > Fast Review. Tapping K or the spacebar drops you back into the usual JKL playback mode. Should you rely on the feature regularly, you can map Fast Review onto a chosen key from the Keyboard Customization window. NOTE: Fast Review applies only to timelines in the Timeline Viewer, not to clips in the Source Viewer.

### Opening Clips in the Source Viewer

Clips can be loaded into the Source Viewer in two ways, and which one is active comes down to the “Live Media Preview” setting in the Viewer options menu (that three-dots menu in the Viewer’s top right corner).

- With Live Media Preview on (the default), skimming a thumbnail in the Media Pool also surfaces the skimmed frame in the Source Viewer, so in effect every clip you skim in the Media Pool opens into the Source Viewer. While you skim, the thumbnail’s playhead stays tied to the playhead shown on the Viewer’s jog bar.
- With Live Media Preview off, you have to either double-click a Media Pool clip to bring it into the Source Viewer, or highlight a Media Pool clip and hit the Return key to load it there. Whichever route you take is entirely down to taste.

### Timeline Viewer Edit Overlays

When you drag a clip out of the Media Pool or Source Viewer onto the Timeline Viewer, edit overlays appear so you can settle on the type of edit simply by deciding which overlay receives the clip.

The overlay that surfaces as you drop a clip onto the Timeline Viewer offers a spread of edit choices This overlay lays out every edit type DaVinci Resolve provides. That roster covers Insert and Overwrite, Replace, Fit to Fill, Place On Top, plus Ripple Overwrite and the Append at End edit — and each one is reachable from the Edit menu as well. It is a handy way to perform three-point edits if drag-and-drop editing appeals to you, while also serving as a tidy refresher on the edit types on hand, given how many options there are. Out of the box, the wider empty zone to the left of these overlays falls to the highlighted Overwrite overlay, and the smaller buttons each carry out one of the remaining edit types on offer. That said, the User Preferences’ Editing panel holds a “Timeline overlay retains the last performed action” checkbox; tick it and DaVinci Resolve hangs onto whichever edit type you last used and highlight it on this overlay each time you drag a fresh clip across the Timeline Viewer, signaling that your most recent edit is now the default whenever you drop clips left of the overlay. To illustrate, with that option on, once you do a place on top edit, the next clip you release into the empty zone left of the overlays produces another place on top edit. The option ships off by default.

### Copy and Paste Timecode in Viewer Timecode Fields

Across the Media, Edit, and Color pages, right-clicking most Viewer timecode fields brings up a contextual menu offering Copy and Paste commands for moving timecode values around. Alternatively, click inside a timecode field and use the ordinary Copy (Command-C) and Paste (Command-V) keyboard shortcuts. The trick even carries across pages. Whatever timecode you paste has to be legitimate timecode — for instance, 0 hour timecode cannot be pasted onto a 1 hour timeline.

Right-clicking on a timecode field to use the Copy Timecode command

### Export The Current Frame from The Viewer

Exporting a still frame from the Viewer is now possible on the Media, Cut, and Edit pages. Follow these steps to send a still frame out of the Viewer: 1 Pick either the Source or Timeline viewer as the export source. 2 Drive the Viewer’s playback controls to land on the frame you want exported. 3 Choose File > Export > Current Frame as Still. 4 Type the still frame’s name in the File System viewer. 5 Set the still frame’s desired format in the File System viewer. 6 Press the Export button.

### Metadata Editor

A Metadata Editor lives on both the Media and Edit pages. On the Edit page, the Metadata Editor appears in the very spot the Inspector uses, right of the Source and Timeline Viewers. Pick a clip in the Media Pool or Timeline and its metadata shows up in the Metadata Editor, with the title bar noting whether the clip under review comes from the Timeline or the Media Pool. Select several clips and only the final one’s details show. Along its header the Metadata Editor carries read-only facts about the chosen clip — the file name, directory, duration, frame rate, resolution, and codec among them. Since there is such an abundance of metadata fields, a couple of drop-down menus up top let you swap which set of metadata the Metadata Editor presents. Metadata Presets (on the left): Where you have built your own custom metadata sets through the Metadata panel of the User Preferences, this drop-down picks which one is shown. Oddly enough, it sits at “Default” by default. Metadata Groups (on the right): This drop-down toggles among the assorted metadata groups on offer, each clustered around particular tasks or workflows. At its core the Metadata Editor is a run of editable fields below the header where you can examine and change the various metadata criteria available. For more on editing clip metadata and on building custom metadata presets, see Chapter 19, “Using Clip Metadata.”

A Timeline clip’s Clip Details panel as shown in the Clip Metadata Editor
