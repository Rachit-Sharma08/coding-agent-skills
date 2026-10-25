# Filtering the edit index and exporting the edit index

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](edit-index-columns-overview.md) / [Next section](markers-and-source-and-timeline-viewers.md)
<a id="source-exporting-the-edit-index"></a> <a id="source-filtering-the-edit-index"></a> <a id="source-the-tracks-index"></a> <a id="source-tracks"></a> <a id="source-tracks-index-columns"></a>

### Filtering the Edit Index

The options in the Edit Index's option menu let you filter for particular things you want to inspect—whether running through every marked clip to catch any notes that need handling, singling out all offline clips, or combing through edits to spot anything needing a fix. The Edit Index can be filtered these ways:

- Show All: Shows all entries in the list. Pick this option after using any of the others to return to viewing the whole timeline.
- Show Active Track Items: Filters out every clip sitting on tracks above or below the ones marked with a destination control. Say you have three video tracks with the destination control on track V2; then every clip on tracks V1 and V3 gets hidden from the Edit Index.
- Show Video Track Items: Strips every audio clip out so the list holds video clips alone.
- Show Audio Track Items: Strips every video clip out so the list holds audio clips alone.
- Show Flags: Singles out clips carrying flags in the list. A submenu lets you choose to show every clip with

flags or only clips with a particular color of flag.

- Show Markers: Singles out every clip carrying markers in the list. A submenu lets you choose to show all

clips with markers or only clips with a particular color of marker.

- Show Clip Colors: Singles out every clip tagged with clip colors in the list. A submenu

lets you opt to show every clip tagged with any clip color at all, or just those tagged in one specific color.

- Show Through Edits: Filters for only the clips holding through edits—cuts where continuous timecode runs from the outgoing into the incoming half of the edit—which, depending on the reason they exist, you might choose to remove or to leave alone.
- Show Offline Clips: Singles out every offline clip (those that have come unlinked from their matching source media on disk) in the Timeline, so you can jump to each one fast and sort out the issue.
- Show Clip Conflicts: Filters for every clip wearing a clip conflict warning badge (signaling reel, name, and timecode metadata that overlaps another clip's) in the Timeline, so you can jump to each one fast and confirm the right clip is in use.
- Show Clips With Speed Effects: Filters for every clip in the Timeline carrying linear or variable Speed Effects.
- Show Clips With Composite Effects: Filters for every clip whose Composite mode or Opacity settings differ from the default (Normal, 100).
- Show Clips With Transform Effects: Filters for every clip with changed Transform settings.
- Show Clips With Filters: Filters for every clip that has Resolve FX or OFX filters applied.
- Show Stills and Freeze Frames: Filters for every clip that's a still or that carries freeze frame speed

effects applied to them.

- Show Compound Clips and Nested Timelines: Filters for every compound clip and nested timeline in

the Timeline.

- Show VFX Connect Clips: Filters all Fusion Connect Clips.

### Exporting the Edit Index

Should you have filtered a run of edits in the Edit Index you'd like to pass to someone else, doing so is simple. For instance, you might filter the Edit Index down to a list of every offline clip in the current timeline, then export that list as a .csv or .txt file to hand your assistant editor so they can track down the media required. Both file types play nicely with spreadsheet and database software, should you wish to pull the data into a different application. Exporting the Edit Index goes like this: 1 Open the Edit Index option menu and pick Export Edit Index off the contextual menu. 2 Within the Export Edit Index window, choose where the exported file should be saved, then choose a format from the bottom drop-down menu. Two export choices exist: a Comma Separated Values (.csv) file, or alternatively a Tab Delimited Values (.txt) file. 3 Click Save.

### Tracks

A number of the most-used track controls are gathered together in the Track Index. You reach the Track Index by clicking the Index Pane and choosing the Tracks Tab. The index lays out all the current tracks in your timeline along with their position and attributes. Each of these can be changed right inside the Track Index.

### The Tracks Index

### Tracks Index Columns

Every track exposes a handful of information columns. You can reorder these columns by pulling the column headers right or left, according to which information weighs most for you. A click on a track row picks that track for changes.

The information columns on hand are:

- Color: The track's present color is shown. Right-click anywhere in the row and pick Change Track Color to choose a new one.
- #: Shows the present track order. To reorder the tracks, drag this column's number up or down through the track hierarchy and release. Bear in mind the literal absolute track number (V1, A1, etc.) doesn't budge—what shifts is which track is mapped to that number.
- Name: The Track's name. You can click into this field to rename the track.
- Track Controls: The very track controls found in the Track Header in the Timeline can be reached here too: Lock/Unlock, Disable/Enable Video Track, Solo, and Mute.
- Format (audio track only): Shows the audio track's present format. You can switch this format to any other by right-clicking anywhere in an audio track's row and choosing Change Track Type to, then picking a new format off the contextual menu.
- Monitor (audio track only): Picks which tracks can be chosen in the monitor drop-down menu up at the top right of the Edit Timeline or Fairlight page windows.
- ADC (audio track only): Ticking this box switches on Automatic Delay Compensation (ADC) for the track.

Right-clicking one track or several in the track index lets you delete every selected track by choosing Delete Tracks off the contextual menu. A click on the Tracks Index's option menu lets you bring in or leave out track types (video, audio, subtitle) from the tracks.
