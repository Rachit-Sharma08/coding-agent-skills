# Naming timeline tracks and the tracks index

Version: DaVinci Resolve 20.3 Reference Manual. Context: Creating and working with timelines.
[Chapter index](INDEX.md) / [Previous section](drt-timeline-import-export-backup-and-restore.md) / [Next section](timeline-scrolling-and-wheel-controls.md)
<a id="source-naming-timeline-tracks"></a> <a id="source-the-tracks-index"></a> <a id="source-toggle-track-header-control-states-by-clicking-and-dragging"></a> <a id="source-tracks-index-columns"></a> <a id="source-using-the-tracks-index"></a> <a id="source-using-timeline-snapping-and-zooming"></a> <a id="source-zoom-around-mouse-pointer"></a>

### Naming Timeline Tracks

For those who care about staying organized, the tracks on a timeline can be named to spell out their purpose. To rename a track: 1 Confirm the Timeline View Options are set to either Filmstrip view or Thumbnail view, and that audio tracks stand tall enough, so track names show. 2 When changing any track's name, select it by clicking the default “Video X” or “Audio X” track name, after which you type whatever name you prefer and press the Return key.

### Using the Tracks Index

The Tracks Index offers a straightforward track list that lets you view and manage every track header from a single spot. It also surfaces more audio detail than the Timeline's track header section does. The Tracks Index comes into its own when you're handling projects packed with video and audio tracks. You reach it by clicking the Index pane and picking the Tracks tab. The list that appears displays all the timeline's current tracks plus their position and attributes. Every one of these is adjustable right within the Track Index.

### The Tracks Index

### Tracks Index Columns

Each track exposes several columns of information. Those columns can be reordered by dragging the column headers left or right, according to whichever information matters most to you. A click on a track row selects that track for modification. A right-click on a track or tracks lets you delete them via the contextual menu. Using the Tracks Index for video tracks:

- Color: Displays a bar in the track's assigned color. Right-clicking the track lets you change its color.
- #: Displays the track's number.
- Name: Displays the track's name. You can edit this field.
- Track Controls: Surfaces the Lock plus the Enable/Disable Video track toggle. Every one of these controls is active.

Using the Tracks Index for audio tracks:

- Color: Displays a bar in the track's assigned color. Right-clicking the track lets you change its color.
- #: Displays the track's number.
- Name: Displays the track's name. You can edit this field.
- Track Controls: Surfaces the Lock Solo, and Mute controls. Every one of these controls is active.
- Format: Displays the audio track type. Right-clicking this field lets you change the audio track type.
- ADC: Displays how much Automatic Delay Compensation is currently on the track. A click on the checkbox switches the automatic delay compensation on or off.
- VCA: Displays the track's VCA group number.
- Tags: Displays whatever tags have been assigned to the track.

Using the Tracks Index for subtitle tracks:

- Color: Displays a bar in the track's assigned color. Right-clicking the track lets you change its color.
- #: Displays the track's number.
- Name: Displays the track's name. You can edit this field.
- Track Controls: Surfaces the Lock plus the Enable/Disable Subtitle toggle. Every one of these controls is active.

Using the Tracks Index options:

- To search for a specific track: Click the search icon (magnifying glass) and type in your search terms.
- Choosing which track types appear in the Tracks Index: Click the Option menu to decide which track types the list carries. The choices are: Video, Audio, and Subtitle.

### Toggle Track Header Control States by Clicking and Dragging

In the Edit page you can flip several Track Header controls at once (Lock Track, Visibility, Auto Track Selection, and so on) just by clicking an icon and dragging the pointer up or down across the track headers. This works for one control type at a time, and not across both Audio and Video tracks together.

Click the Lock icon at A1 and drag the pointer down as far as A3 to lock every audio track that falls between them

### Using Timeline Snapping and Zooming

As you get ready to make an edit into the Timeline, the snapping and zoom controls can be set to whatever state best suits the task at hand. Say you're cutting an insert shot into a fast-paced stretch of edits in the Timeline; you might want to zoom in so you can better see exactly where the incoming clip should land. With so many edits clustered there, turning snapping off can help keep the clip from leaping to the closest edit point when you need to nudge the incoming clip onto one precise frame. Playhead Snapping: Switching clip and playhead snapping on or off is done by clicking the Snapping button in the toolbar, or by pressing N. While snapping is on, the In and Out points and markers of clips snap to each other and to the playhead. You can also press N to briefly toggle snapping while dragging a clip in the Timeline, or while scrubbing the playhead with the pointer (snapping goes back to its earlier state once you finish the operation). Timeline Zoom presets:

Arranged left to right: the Full Extent, Detail, and Custom Zoom controls Full Extent Zoom: As clips get added or removed, this mode adjusts the zoom level on the fly so the entire Timeline stays in view. As your timeline expands with added clips, the zoom level drops automatically so the new clips fit inside your Timeline Viewer. The opposite happens too: the zoom level rises automatically as clips are removed. Detail Zoom: This setting zooms the Timeline in on the Playhead down to the frame level so you can quickly make fine timing adjustments. Custom Zoom: Zooms the Timeline to whatever level the Zoom Slider just to its right is set at. Zoom Slider: Pull the zoom slider toward the left for zooming out, toward the right for zooming in. Pressing Command-Minus (–) and Command-Equal (=) also handles zoom out and zoom in. No matter the method, zooming always stays centered on the playhead's present position, even with the playhead off screen. To fit every clip across the Timeline's width: Press Shift-Z. Being a toggle, a press of Shift-Z fits your whole edited sequence across the width of the Timeline, while another press of Shift-Z brings the Timeline back to whatever zoom level you had earlier. That keyboard shortcut makes moving around the Timeline simple while zoomed in, because you can hit Shift-Z, send the playhead to a different part of the Timeline you'd like to work on, and hit Shift-Z again to zoom straight into that fresh location in the Timeline.

### Zoom Around Mouse Pointer

You can configure the Edit Timeline zoom controls to remain centered on the pointer as you zoom in or out, rather than centering on the Timeline playhead as they normally do, by choosing View > Zoom Around Mouse Pointer. That can come in handy when you're navigating longer timelines. With this option on, zooming the Timeline in and out using your pointing device's scroll control while you hold the Option key keeps the Timeline centered on the pointer. Turn this option off to go back to zooming in or out centered on the playhead position only.
