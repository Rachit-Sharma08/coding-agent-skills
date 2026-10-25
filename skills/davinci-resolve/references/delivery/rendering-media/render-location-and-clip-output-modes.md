# Choosing a location to render and single clip vs individual clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Rendering media.
[Chapter index](INDEX.md) / [Previous section](custom-preset-editing-import-and-export.md) / [Next section](render-formats-codecs-and-mp4-controls.md)
<a id="source-all-other-render-settings-for-output"></a> <a id="source-choosing-a-location-to-render"></a> <a id="source-individual-clips"></a> <a id="source-render-a-single-clip-or-individual-clips"></a> <a id="source-single-clip"></a> <a id="source-single-clip-vs-individual-clips"></a> <a id="source-video-panel"></a>

### Choosing a Location to Render

Your very first call when rendering output is deciding where it gets rendered. Fittingly, this is the first batch of controls sitting at the top of the Render Settings parameters.

- Filename: A preview of how the file will be named, drawn from the settings in the File panel covered later. What shows here is shaped by the Custom/Timeline name and File suffix fields, together with the “Use x digits in the filename” settings. You can also edit the editable parts of this filename preview right here.
- Location: Hit the Browse button to pick a directory where the media that DaVinci Resolve outputs should be written. Once you've picked a directory, its path name shows up in the “Render job to” field.

### Single Clip vs. Individual Clips

Although the Deliver page's Render Settings present plenty of options, there are essentially two broad ways to render your project, set by which of the “Render” radio buttons you click within the Output group.

### Render a single clip or individual clips

### Single Clip

Choosing the Single clip option configures a render in which every clip in the session goes out together, as one media file in whatever format you pick. That means you're rendering the chosen range of the session into a single MXF or QuickTime file, or into a single set of image sequences.

- Timecode: Whatever timecode gets written out is set by the “Start timeline timecode at” value of the timeline you're rendering. Media files hold a continuous timecode track, whereas image sequences carry timecode written into each frame’s data header and worked into the file name (as a frame count).
- Frame Rate: When you render a project running mixed frame rates, rendering to a single clip converts every clip across the whole session to the project frame rate, drawing on either the project-wide or clip-specific “Retime process” setting.
- Effects: Render a single clip and most effects get “baked into” the rendered output.

IMPORTANT: Any time clip filtering is on (through the dropdown menu to the right of the Clips button), you can't pick Single Clip rendering. You can tell clip filtering is on by an orange line beneath the Clips button in the UI toolbar.

### Individual Clips

Picking the Individual clips option configures a render where each clip goes out as its own media file in whatever format you pick. You wind up holding as many separate media files as the count of clips within whichever range you picked to render.

- Timecode: The timecode written to each clip is copied straight from the original source media, which makes reconforming media easy for projects moving back and forth between DaVinci Resolve and NLEs.
- Frame Rate: For a project that mixes frame rates, rendering to source keeps every clip on its own native frame rate, which lets round-trip workflows carry on.
- Effects: You decide whether any timeline-based effects get ignored or “baked into” the individual clips by checking or unchecking the Render Timeline Effects box.
- Resolution: You decide whether the individual clips render at the timeline size or at their original source resolution by checking or unchecking the Render at Source Resolution box.

### All Other Render Settings for Output

Here we cover the various render settings on offer for tailoring your output. Some may be hidden depending on which Render Setting mode you picked, but this section lays out the full roster found in the Advanced panel of controls. Pick one of the Easy Setups and certain settings lock while others stay editable, according to what that setup needs. Should none of the Easy Setups fit the job in front of you, leave the Easy Setup dropdown menu on none and choose the settings the task requires by hand.

### Video Panel

Every video-oriented parameter sits in this panel.
