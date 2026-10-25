# Flags and markers

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Next section](marker-colors-ranges-and-properties.md)
<a id="source-adding-markers-to-clips"></a> <a id="source-adding-markers-to-timelines"></a> <a id="source-marking-and-finding-clips-in-the-timeline"></a> <a id="source-marking-and-finding-clips-in-the-timeline-part-1"></a> <a id="source-timeline-markers-placed-for-future-reference"></a> <a id="source-using-flags"></a> <a id="source-using-markers"></a>

### Marking and Finding Clips in the Timeline

As your project moves along, it helps to flag key details about each clip, along with notable moments in each timeline, by combining Flags, Markers, and clip Label colors. You can attach these to source clips sitting in the Media Pool, or to clips already cut into timelines. Markers in particular can also go onto the Timeline ruler itself, which helps you track important moments or notes and assists with snapping. Along the way you’ll also be reshaping clips in assorted ways — unlinking and relinking the audio and video of various clips, and switching clips on and off in the timeline.

### Using Flags

A Flag tags a clip in its entirety, and it simultaneously flags every other clip in the Timeline drawing on the same Media Pool source clip, which makes it a convenient way to spot at a glance which clips in a given timeline trace back to one Media Pool source.

The Flag and Marker buttons and pop-ups. Clips can carry several flags at once, drawn from an assortment of colors. Beyond tagging particular media files, flags prove handy for timeline filtering on the Color page, column sorting in the Media Pool, and plenty of other operations. Ways to flag clips:

- To flag a clip from the toolbar: Pick one clip or several, then either click the Flag button to tag that clip with the active color, or open the Flag drop-down in the toolbar to pick another color before clicking the Flag button. On the Edit page, flags show up in the Timeline laid over the name bar of every clip.
- To flag a clip: Pick one clip or several, then choose Mark > Add Flag > Current Selected (G) to drop markers of a given color straight onto clips and the Timeline. You can map the individual flag color commands to specific keyboard shortcuts if you’d like to drop a particular flag color with a single keystroke.
- To flag a clip from within the Source Viewer: Bring a clip up in the Source Viewer; then, while focus rests on the Source Viewer, choose Mark > Add Flag > Current Selected (G). Each individual flag color command can be bound to its own keyboard shortcut if you want a given flag color available at a keystroke.
- To clear every flag off a clip: Pick the clip or clips whose flags you want gone, open the Flag drop-down in the toolbar, then choose the topmost “Clear All” option.
- To reveal or conceal one color of flags: From the View > Show Flags submenu, pick whichever flag color you’d like hidden; to bring every color back, choose View > Show Flags > All instead.
- To filter all flagged clips in the Edit Index: Open the Option menu of the Edit Index and choose Show Flags. Every flagged clip turns up in a list, with one column displaying the color(s) of the flags on each entry in that list.

### Using Markers

Markers serve to draw the eye to a single frame inside a particular clip. Each marker can take its own color and carry custom name and note text. Anytime you type text into a marker, that marker shows a small dot signaling that more information sits inside it. After placement, and provided snapping is turned on, a marker snaps onto In and Out points, onto edit points, onto the playhead, and onto fellow markers, which makes it simple to lean on markers to “measure” the edits and trims you perform in the Timeline.

### Adding Markers to Clips

You can drop markers along the jog bar belonging to source clips shown in the Source Viewer (or the Media page Viewer), and likewise onto clips you’ve selected inside a timeline.

Markers placed on a source clip

(Top) Markers set on a source clip; below them, markers set on a clip within the Timeline. Once you add markers to a source clip, those markers surface in the Media Pool too, as hierarchically disclosable items hanging off that clip in List view (Thumbnail view doesn’t show markers). Further detail on working with markers in the Media Pool’s List view comes later in this chapter.

When the Media Pool sits in List view, markers can be seen as separate clips, each identified by its marker name.

The steps that follow lay out how markers get added onto clips, and onto timelines, within DaVinci Resolve. When marking a source clip, whether in the Source Viewer or the Media Page Viewer, do one of these:

- To set a marker and nothing more, bring the playhead to the frame you want to mark, then press M.
- To set a marker and open the marker dialog straightaway during playback so you can type a name or note in it, press Command-M (or press M twice). Playback halts until you’ve entered the text you want and closed the marker dialog, whereupon playback resumes.
- Position the playhead over the frame you mean to mark; from there, right-click within the jog bar and pick a marker color out of the Add Marker submenu of the contextual menu.

To mark a clip in the Timeline, do one of the following:

- Pick the clip or clips you mean to mark, bring the playhead to the frame of a selected clip in the Timeline, then click the Marker button in the toolbar (or press M) to drop a marker at that frame in the active color (when several overlapping clips are selected, the marker lands on every one of them).
- To set a marker mid-playback and pop open the marker dialog right away for a name or note, pick the clip or clips you mean to mark, run playback through the selection until you reach the spot to mark, then press Command-M (or press M twice). Playback stops until you type some text and close the marker dialog, after which playback carries on.
- Pick the clip or clips you mean to mark, then open the Marker drop-down to pick another color, and click the Marker button.

In the Timeline, markers show up at the top of the title bar of whichever clip carries them.

### Adding Markers to Timelines

Markers of any color can likewise be dropped into the Timeline ruler to flag particular times for later reference, or to jot notes about issues you want to follow.

### Timeline markers placed for future reference

Keep in mind that every marker you set on clips or in the Timeline also turns up inside the Mini-Timeline of the Color page, which makes leaving notes for later reference while grading straightforward.

Clip and Timeline markers, here shown within the Color page’s Mini-Timeline. After one or more markers are set on clips, and as long as snapping is on, they snap onto clip In and Out points, onto edit points, onto the playhead, and onto fellow markers. To mark the Timeline itself, first confirm all clips are deselected, then do one of these:

- Press M.
- Click the Marker button to drop a marker in the active color into the Timeline ruler.
- To set a marker mid-playback and immediately open the marker dialog for a name or note, pick the clip or clips you mean to mark, then press Command-M (or press M twice). Playback halts until you type some text and close the marker dialog, after which playback carries on.
- Open the Marker drop-down to pick another color, then click the Marker button.
- Right-click in the Timeline ruler and pick a marker color from the Add Marker submenu of the contextual menu.
- Choose Mark > Add Marker > Current Color (M) to apply the active marker color. As an alternative, choose Mark > Add Marker > Blue/Cyan/Green/and so on to drop a marker of a particular color straight onto clips or the Timeline. Each of these commands can be tied to a specific keyboard shortcut if you’d like a given marker color available at a keystroke.
