# Subtitles and closed captioning support and viewing subtitle caption tracks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Subtitles and closed captioning.
[Chapter index](INDEX.md) / [Next section](audio-generated-subtitle-options.md)
<a id="source-adding-subtitles-and-captions-manually"></a> <a id="source-adjusting-qc-thresholds-for-subtitlecaption-timing"></a> <a id="source-an-imported-srt-subtitle-file"></a> <a id="source-importing-subtitles-and-captions"></a> <a id="source-subtitles-and-closed-captioning"></a> <a id="source-subtitles-and-closed-captioning-part-1"></a> <a id="source-subtitles-and-closed-captioning-support"></a> <a id="source-viewing-one-subtitle-track-at-a-time"></a> <a id="source-viewing-subtitlecaption-tracks"></a>

### Subtitles and Closed Captioning

The support DaVinci Resolve offers for subtitles and closed captioning is quite advanced, and bundling in automatic subtitling tools cuts down enormously on the time and labor it takes to assemble accurate subtitle tracks. Thanks to purpose-built subtitle/closed caption tracks you can reveal or hide, the ability to import and export subtitle files, capable subtitle editing and styling at both the track and clip level, and thorough export choices, layering subtitles and closed captions onto your finished project becomes a clear, uncomplicated workflow.

### Subtitles and Closed Captioning Support

In DaVinci Resolve, subtitles ride on specially typed subtitle tracks that hold purpose-designed subtitle generators for adding and editing a program's subtitles. As a rule, each subtitle track maps to one language or purpose, and you're free to rename a subtitle track so it reflects what it holds. Subtitle tracks can be locked, carry Track Selector and Sync Lock controls, and be switched on or off just like any other track. On top of that, a dedicated subtitle-only destination control lets you pick which subtitle track your subtitle clips get edited into. What's more, subtitle generator clips can be resized, moved, edited, and overwritten in the same way as most other clips.

Subtitle track with Track Selectors, Lock, Sync Lock, and enable/disable controls

### Viewing Subtitle/Caption Tracks

A key way subtitle tracks differ from other track types is that no more than one subtitle track can be on view at any moment. In practice, that means when you keep several subtitle tracks—each holding a different language—clicking the Enable control on one subtitle track switches all the rest off.

### Viewing one subtitle track at a time

### Adjusting QC Thresholds For Subtitle/Caption Timing

So you can stick to guidelines laying out the recommended duration, line length, and pace of captions and subtitles, the Subtitles panel of the Project Settings carries parameters you set to flag you whenever a given subtitle clip runs past the thresholds for Characters Per Line, Minimum Caption Duration, and Maximum Characters Per Second.

The Subtitles Setup parameters in the Subtitles panel of the Project Settings While you're editing a subtitle clip, these thresholds drive an automatic calculation of how many lines and characters a particular subtitle clip is allowed given its duration. As an instance, run past the calculated threshold and that caption's CPS value turns red as a warning.

A subtitle's CPS value has gone red here, signaling that it overshoots the current QC threshold Adjusting QC Thresholds for Individual Subtitle Tracks Although setting the subtitle QC thresholds in the Project Settings usually suffices for a single deliverable, those deliverables carrying multiple subtitle tracks across different languages might call for separate parameters on each track, permitting longer line lengths, more screen time, and so on to suit each language's distinct traits. To tune the subtitle settings per track on their own: 1 Pick the subtitle track in the Timeline you'd like to change. 2 Open the Inspector and choose the Track tab. 3 Within the Subtitle Settings pane, clear the Use Project Settings checkbox. 4 Make whatever changes you need to the Max Line Length, Min Duration, and Max CPS controls. From now on these settings override the Subtitle Project Settings for the selected track alone.

The Subtitle Settings sitting in the Inspector's Track pane let you tailor parameters on a per-subtitle-track basis.

### Importing Subtitles and Captions

More often than not, putting subtitles or closed captions onto a DaVinci Resolve timeline means importing a subtitle file prepared somewhere else. At present, DaVinci Resolve handles subtitle files in a number of formats, among them .srt, .srtx, .vtt, .xml, and .ttml. To bring in a subtitle or closed captioning file by way of the Media Pool: 1 Open the Media Pool. 2 Browse to the folder that holds your subtitles. Compatible subtitles turn up as a blank clip icon bearing a subtitle icon down in its lower left corner. 3 Pull the subtitle into the Media Pool by dragging, by importing through the contextual menu, or by any of the other methods you'd use to bring video clips into the Media Pool. To bring in a subtitle or closed captioning file by way of the Import Subtitle function: 1 Open the Media Pool. 2 Right-click any bin in the Bin list, or anywhere across the Media Pool browser's background, and pick Import Subtitle. 3 When the file dialog opens, locate and pick the subtitle file you'd like to import, then click Open. 4 The subtitle file shows up as a subtitle clip in the Media Pool, ready to be edited into a subtitle track. A badge marks it as a subtitle clip.

### An imported .srt subtitle file

TIP: Within the Media Pool, subtitle files relink the same way video clips do.

To put a subtitle clip onto the Timeline: 1 To drop a subtitle clip onto a timeline automatically and line its position up by timecode:

- Right click the subtitle and pick "Insert Selected Subtitles to Timeline Using Timecode." The subtitle clip breaks apart into individual subtitles that land in the subtitle track, with each subtitle lined up against the timeline's timecode.

2 To put a subtitle clip onto a timeline by hand when you lack matching timecode, do one of the following:

- Drag a subtitle file you've imported up into the empty gray strip above your video tracks, and a subtitle track gets created automatically to hold those subtitles
- Drag a subtitle file you've imported onto an existing subtitle track As you drag the subtitle clip, it gets broken apart on the spot so each title lands on the Timeline as a separate subtitle clip, its timing offset reckoned against where the first frame of that file's first subtitle sits.

(Top) The Timeline as it began, (Bottom) The same Timeline once dragging a subtitle file in has spawned a fresh subtitle track 3 Line the imported subtitles up so they sit against the first frame of your program they're meant to match, then drop the titles into the track. Should you accidentally drop the subtitles in the wrong spot, no problem—you can always select them all and slide them earlier or later, the same as any other clips. 4 If you've brought in a new subtitle track, you can rename it to spell out which language and country that track answers to. Bear in mind that subtitle track names get used while exporting or encoding subtitles, so be sure your tracks are named properly ahead of export/delivery. 5 Should you wish to restyle every subtitle you've just put in—say, to shrink them or swap the font—then click the header of the subtitle track you'll work on, open the Track panel of the Inspector, and choose the formatting you want that track to adopt. For a rundown of every subtitle clip you've added, select the header of the subtitle track you just created and open the Captions panel in the Inspector. Down at the bottom of the Captions panel, a list hands you a handy means of moving through a track's subtitles (with the Prev and Next buttons) and making selections. Set the Inspector to full height and you'll get even more room to browse the subtitle list.

The Captions list lays out each caption or subtitle riding a track, ready for you to select, edit, delete, or move through

### Adding Subtitles and Captions Manually

At other points, you might have to build subtitles yourself. Before you do, you'll first need to put in one or more subtitle tracks. With those tracks in place, you can attach subtitle generators to them by a number of routes. Add as many subtitle tracks as the job demands, one per language you need. To add new subtitle tracks:

- Right-click in any track header of the timeline that's currently open, then pick Add Subtitle Track. An empty subtitle track appears atop the Timeline, carrying the name "Subtitle 1," and should Subtitle Tracks have been hidden, they become visible now. Once you've put in a new subtitle track, you can rename it to spell out which language and country that track answers to. Bear in mind that subtitle track names get used while exporting or encoding subtitles, so be sure your tracks are named properly ahead of export/delivery. You're able to show and hide subtitle tracks whenever you need to clear room in the Timeline for working on other tracks. Subtitles on whichever subtitle track is currently selected stay visible all the same, no matter whether the subtitle tracks are shown.

Showing and hiding subtitles tracks:

- Open the Timeline View options, then click the Subtitle button to flip the visibility of subtitles tracks on and off.

The show/hide subtitle tracks button in the Timeline View Options To put individual subtitles onto a subtitle track: 1 Should you want to adjust a particular subtitle track's default style before you begin adding subtitles, click the header of the subtitle track you'll work on, open the Track panel of the Inspector, and choose the formatting you want that track to use. 2 With several subtitle tracks present, click the destination control of whichever subtitle track you mean to add titles to. They carry labels ST1, ST2, ST3, etc. 3 Move the playhead to the frame where the new subtitle should start.

Placing the playhead at the spot where a fresh subtitle ought to start 4 To add a new subtitle clip, take one of these routes:

- Open the Inspector and click Create Caption within the Captions panel of the Inspector. If one or more captions already sit in that subtitle track, click the Add New button over the caption list instead.
- Right-click anywhere across the subtitle track and pick Add Subtitle to drop in a subtitle clip beginning at the playhead's position
- Open the Effects Library, click the Titles category, then drag a Subtitle generator onto whichever Subtitle track you want it to land on.

Manually adding a subtitle

5 If you need to, you can now edit the clip so it better matches the dialog being spoken or the sound being described, by dragging the clip left or right, or by dragging the clip's start or end to resize it. 6 With the new subtitle clip you've made still selected, turn to the Captions panel in the Inspector to type that particular subtitle's text. The text shows up on the subtitle clip as you type it.

Editing the text of the subtitle we just created Each time you add a subtitle, an entry lands in the subtitle list down at the bottom of the Captions panel in the Inspector. That list gives you yet another handy way of moving through a track's subtitles (with the Prev and Next buttons) and making selections.
