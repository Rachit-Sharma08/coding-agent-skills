# Replay titles and audio track display

Version: DaVinci Resolve 21 New Features Guide. Context: Editing.
[Chapter index](INDEX.md) / [Previous section](font-browser-toolbar-and-show-font-previews-preference.md) / [Next section](multiclip-image-position-and-audio-channel-changes.md)
<a id="source-audio-transcription-offers-external-subtitle-word-timing"></a> <a id="source-compare-timelines-with-timeline-backup-snapshots"></a> <a id="source-drt-timeline-import-supports-link-and-conform-options"></a> <a id="source-edit-edl-clip-name-in-the-edit-index"></a> <a id="source-edit-page-timecode-display-can-show-frames-subframes-or-audio-samples"></a> <a id="source-for-clip-color-markers-and-flags"></a> <a id="source-improved-waveforms-markers-and-fades-display-for-shorter-edit-timeline-tracks"></a> <a id="source-intelliscript-supports-final-draft-imports"></a> <a id="source-mono-audio-appears-on-both-left-and-right-channels-when-added-to-stereo-tracks"></a> <a id="source-paste-and-remove-attributes"></a> <a id="source-select-all-transitions-in-the-cut-and-edit-pages"></a> <a id="source-source-timelines-support-destination-track-selectors"></a> <a id="source-subtitle-inspector-supports-find-and-replace"></a> <a id="source-the-import-timeline-dialog"></a> <a id="source-the-normal-sized-timeline-tracks"></a> <a id="source-the-replay-titles-palette"></a> <a id="source-the-smallest-sized-timeline-tracks"></a> <a id="source-tracks-index-lets-you-show-or-hide-tracks"></a> <a id="source-up-to-2x-faster-speed-warp-metal-option-on-macos"></a>

### The Replay Titles Palette

### Mono Audio Appears on Both Left and Right Channels When Added to Stereo Tracks

DaVinci Resolve 21 has altered what happens when you add mono audio to stereo tracks. Drop a mono audio clip onto a stereo timeline now and the mono clip plays across both the left and right channels. It used to go to the left channel only. Within the Fairlight timeline, this clip shows in a darker shade on the right channel to signal that the effect is extrapolated across channels.

### Improved Waveforms, Markers and Fades Display for Shorter Edit Timeline Tracks

In DaVinci Resolve 21, when you work with shorter tracks on the edit page, the way those tracks display has been reworked to pack the most information onto even the tiniest track sizes. Specifically

- Audio waveforms stay visible.
- Markers shrink in size rather than just vanishing.
- Fade handles and transitions stay usable.
- The status icons and clip name won’t cover one another.
- Clip names can be switched off.

### The normal sized timeline tracks

### The smallest sized timeline tracks

### Source Timelines Support Destination Track Selectors

You can now put Destination Track selectors to work in Source Timelines to limit tracks while doing dual timeline editing.

### DRT Timeline Import Supports Link and Conform Options

Import a DaVinci Resolve Timeline (.drt) file into a project and a new Import Timeline dialog opens, laying out the timeline settings along with a checkbox option to set project settings from the imported timeline. You can now also tick the box “Automatically link to existing media pool clips” to spare yourself the step of relinking the files by hand in the Media Pool.

### The Import Timeline dialog

### Compare Timelines with Timeline Backup Snapshots

Should you want to see the changes you’ve made to a timeline measured against any of its earlier backed-up timelines, you can right-click the timeline and choose Compare with Timeline Backup to open the Compare Timeline window. The Compare Timeline window stacks the two timelines together and highlights where they differ. You pick which backup to measure against from the drop-down menu up top in the window. To dig deeper into the Compare Timeline window, turn to Chapter 34, “Creating and Working with Timelines” within the DaVinci Resolve Reference Manual. The current timeline set side by side with an earlier backup

### Subtitle Inspector Supports Find and Replace

You can now find and replace particular words or phrases across a whole subtitle track using the subtitle inspector. To switch on the find and replace tool, click the search icon sitting at the subtitle inspector’s upper right. That first selection option is where you decide whether to highlight any words that contain the text or to narrow it to finding the whole word only. Then key the text you want to find into the search field and press the Search button. Once a term turns up, it gets highlighted in yellow in the Caption tab, and you can move through found items by clicking the backward and forward arrows beside the search button. A numeric readout shows how many “hits” the tool turned up, along with which particular instance of that hit is currently picked. Tick the Replace box to open the replace tool, letting you key in the text you mean to swap for the original search tool. Click the Replace button to overwrite the chosen instance, while Replace All swaps every instance of that search in the subtitle track for the new term. Click any caption in the caption tab to load it straight into the Caption box, letting you adjust the found text.

A click on the search icon (circled red) within the Subtitle Inspector brings up the search and replace tools. Every match turns yellow across all the captions.

### Tracks Index Lets You Show or Hide Tracks

From the Tracks Index on the Edit page, you can now reveal or conceal tracks; just click the eye icon sitting to a track’s left. Concealing V1 by way of the Tracks tab within the Index

### Edit EDL Clip Name in the Edit Index

You can now edit the EDL Clip Name field straight in the Edit Index. Turn this column on by right-clicking the column header and ticking EDL Clip Name. Click in the column to add or change the clip name in the text field.

### Audio Transcription Offers External Subtitle Word Timing

DaVinci Resolve 21 can now run word timing analysis on captions you’ve keyed in by hand or imported. That means word-level highlighting no longer obliges you to generate subtitles within DaVinci Resolve, and when you fix internally generated subtitles, you can re-analyze the caption to land accurate word timing for animated subtitles.

Once you’ve made a change, hit Update Word Timings to bring the subtitle clip’s timing back in line.

Here is how to retime a subtitle / caption: 1 On the timeline, pick the subtitle clip you mean to retime. 2 Within the Video Inspector Caption tab, hit the Update Word Timings button. Pick Synchronize Word Timings off the context menu to retime every subtitle on a track Here is how to retime every subtitle clip on a subtitle track: 1 Right-Click the subtitle track header. 2 Pick Synchronize Word Timings off the context menu. In the same way, you can pull in transcriptions for media pool clips and let Resolve figure out the timing: right-click a clip and choose AI Tools > Audio Transcription > Import and Detect Timing. Pulling in a subtitle for a media pool clip and working out its timing.

### IntelliScript Supports Final Draft Imports

On top of plain text files, Intelliscript will now let you import Final Draft (.fdx) files to match and build a timeline from a script using clips in your media pool.

### Edit Page Timecode Display can Show Frames, Subframes or Audio Samples

Within the Edit page timeline, timecode can now be read carrying Frames, Subframes, and Audio Sample information instead of timecode on its own. To swap the display, right-click the Timecode display in the Timeline, then choose what you want off the dropdown menu. Picking a different timecode display type by right-clicking the timecode box.

### Up to 2x Faster Speed Warp Metal Option on macOS

DaVinci Resolve 21 on macOS now puts forward a Speed Warp Metal option for Motion Estimation within the Retime and Scaling controls. This is a purpose-built version of Speed Warp that leans on the Mac's hardware. It ought to massively quicken the DaVinci Neural Engine Speed Warp operations.

### Select all Transitions in the Cut and Edit Pages

There’s a new menu command that automatically picks every transition in a timeline, or within a set in-out range. The track selector controls can also rein it in. Timeline > Select Transitions

### Paste and Remove Attributes

### For Clip Color, Markers and Flags

Clip Color, Markers, and Flags are now parameters you can pick for the Paste Attributes and Remove Attributes commands.
