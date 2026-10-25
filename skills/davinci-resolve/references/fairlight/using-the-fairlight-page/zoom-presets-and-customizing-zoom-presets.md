# Zoom presets and customizing zoom presets

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](scroller.md) / [Next section](playhead-modes-and-visible-video-tracks.md)
<a id="source-customizing-clip-display-in-the-timeline"></a> <a id="source-customizing-the-timelines-display"></a> <a id="source-customizing-zoom-presets"></a> <a id="source-grid-view-options"></a> <a id="source-selecting-the-audio-clip-view-options"></a> <a id="source-setting-the-tempo-grid-from-a-range-selection"></a> <a id="source-setting-the-tempo-grid-start"></a> <a id="source-setting-the-tempo-grid-start-location"></a> <a id="source-tempo-grid-options"></a> <a id="source-tempo-grid-setup-window"></a> <a id="source-time-scale-options"></a> <a id="source-timecode-grid-resolution"></a> <a id="source-timeline-view-dialog"></a> <a id="source-zoom-presets"></a>

### Zoom Presets

Presets 1-7: Each of these buttons selects one of seven available zoom levels.

### Customizing Zoom Presets

Any Zoom preset can be tailored in Fairlight through the settings found in the Timeline View dialog, which you bring up by right-clicking a preset button.

### Timeline View dialog

You’re able to type in a one-of-a-kind preset name, and it surfaces as a tooltip whenever the mouse cursor rests on the matching preset button. Ticking the checkbox marked “Preset Updates Dynamically” instructs Fairlight to refresh and store the preset live as the view changes, governed by whichever checkboxes you’ve enabled in the Controls section. Any of the presets may be designated the default Zoom setting.

### Grid View Options

Choosing the Grid View options, with the Timecode Time Scale options on view Edit Grid Options Show Grid: Toggling this reveals or conceals the grid line running across the tracks beneath the Timeline. Snap to Grid: With this on, any clip you insert, reposition, or trim on a track locks onto the closest grid line.

### Time Scale Options

Timecode: Choose this and the grid tracks Timecode at whatever resolution you’ve picked. Tempo: Choose this and the grid tracks bars and beats at whatever resolution you’ve picked.

### Timecode Grid Resolution

With the Timecode Time Scale option switched on, the Grid conforms to whichever Timecode Grid Resolution you chose. Available Timecode Grid resolution choices are: 1 second, 1 Frame, 1/2 Frame, and 1/4 Frame.

### Tempo Grid Options

Selecting the Grid View options; Tempo Time Scale options shown These Tempo Grid options below dictate how the grid behaves once the Tempo option is chosen:

- Resolution: Picks the Grid resolution you want, measured in bars and beats:

Bar, 1/2 Note, 1/4 Note, 1/8 Note, 1/16 Note.

- Tempo: Here you type the tempo as a BPM value.
- Time Signature: Choose your time signature from these: 4/4, 3/4, 6/8.
- Song Start: Here you type where the Song Start Timecode sits.

### Setting the Tempo Grid Start

To establish where the Tempo Grid begins:

- Right-click the spot you want along the Timeline ruler.
- Pick Set Tempo Grid start.
- The tempo grid’s opening bar and beat jump over to that spot.

### Setting the Tempo Grid start location

### Setting the Tempo Grid from a Range Selection

To derive the Tempo value for the Tempo Grid out of a range selection:

- Draw a range selection across the Timeline.
- Right-click any point on the Timeline ruler and pick Set Tempo Grid BPM from the contextual menu.
- When the Tempo Grid Setup window opens, type how many bars the selection spans.
- Should you wish, tick Set Start from Playhead.
- Click Set Tempo From Range.
- Dismiss the Tempo Grid Setup window. The tempo over in the Tempo Grid Options settings refreshes to match.

### Tempo Grid Setup window

TIP: When deriving tempo from a range selection, pick a passage of the music where counting out the bars/beats to define the range is straightforward.

### Customizing Clip Display in the Timeline

Go to Fairlight > View Clip Info Display to bring up a dialog that lets you tailor what data appears along the bottom of every clip in the Fairlight timeline. Within this dialog you can opt to show no clip name at all, the file name, or the clip name, and you can pick from an assortment of metadata you might want on hand while working with clips in the Timeline.

### Selecting the audio clip view options

### Customizing the Timeline’s Display

Several approaches exist for tailoring the Timeline so you get a clearer look at your work.
