# Edit index columns overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the edit page.
[Chapter index](INDEX.md) / [Previous section](timelines-grades-and-versions.md) / [Next section](filtering-the-edit-index-and-exporting-the-edit-index.md)
<a id="source-edit-index-columns"></a> <a id="source-using-the-edit-page-part-2"></a>

### Edit Index Columns

Each event fills several columns of information. You can reorder these columns by dragging them left or right, according to which information matters most to you. The columns of information on offer are:

- #: The event number (matching the clip number shown in the Color page’s Thumbnail timeline).
- Reel: The corresponding clip’s reel name.
- Match: Flags clips carrying clip conflicts, which show a question mark in this column.

The flag vanishes once the clip conflict is resolved.

- V: Video event.
- C: The event type (C for cut, D for dissolve or transition).
- Dur: A number giving a transition’s duration in frames.
- Source In/Source Out: The Source In and Source Out timecode marking the span of timecode

that clip references; it corresponds to where each clip’s In and Out point sits in timecode relative to the source media it draws from.

- Record Duration: The clip’s duration in the Timeline, set by the Record In/Out timecodes.
- Record In/Record Out: Record In and Record Out timecode marking that clip’s place in the Timeline.
- Name: The clip’s name.
- Comments: Whatever comments rode along in the EDL that got imported. For example, clip names exported from the original NLE to serve as reel names in RED workflows using EDL import.
- Source Start/ Source End: The very first and last frame of media on hand in the Source Media for that clip.
- Source Duration: The duration, in timecode, of the whole source media available in that clip.
- Codec: The corresponding clip’s codec.
- Source FPS: The corresponding clip’s frame rate.
- Resolution: The corresponding clip’s frame size.
- Color: The color of the flags or markers on that clip.
- Notes: Notes typed inside markers applied to clips or the Timeline.
- EDL Clip Name: Shows the imported EDL’s name, where that’s on hand.
- Marker Keywords: Lists every keyword found in a particular marker.

The Edit Index lets you tailor its columns so the details that matter to you come first. Ways to tailor the Edit Index's metadata columns: To show or hide columns: Right-click atop any Edit Index column and pick an entry from the contextual menu list to check or uncheck a given column. Columns left unchecked stay out of sight. To rearrange column order: Pull any column header rightward or leftward to reorder the columns. To resize any column: Pull the divider between two columns right or left to make that column narrower or wider.

The Edit Index also lets you tailor column layouts. After you've built a column layout that suits your particular need, you can store it to bring back later. Ways to store and reuse a custom column layout: Building a column layout: Get the columns a given task needs shown, hidden, resized, and rearranged, then right-click a Media Pool column header and pick Create Column Layout. Into the Create Column Layout dialog, type a name, then click OK. Bringing a column layout back: From a right-click on any Media Pool column header, pick the name of whichever layout you want. All your custom layouts gather at the top of the list. Removing a column layout: From a right-click on any Media Pool column header, pick the layout's name out of the Delete Column Layout submenu.
