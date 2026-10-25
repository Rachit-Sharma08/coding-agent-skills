# Hiding markers by color and deleting markers by color

Version: DaVinci Resolve 20.3 Reference Manual. Context: Marking and finding clips in the timeline.
[Chapter index](INDEX.md) / [Previous section](markers-in-the-media-pool-overview.md) / [Next section](timeline-track-colors-and-search.md)
<a id="source-assigning-clip-colors"></a> <a id="source-clip-color-appearance"></a> <a id="source-color-labeling-clips-in-the-timeline"></a> <a id="source-custom-clip-colors"></a> <a id="source-deleting-markers-by-color"></a> <a id="source-hiding-markers-by-color"></a> <a id="source-renaming-clips-in-the-timeline"></a> <a id="source-track-colors"></a>

### Hiding Markers By Color

View > Show Markers lets users reveal and conceal markers by color, or display every one at a time. This proves handy when, say, you lean on marker color to route information to particular artists — green for Fairlight mixing notes, orange for Fusion page compositing notes. People working on those pages can then conceal every marker but the color they care about, so only the markers that matter to them stay in view.

### Deleting Markers By Color

Mark > Delete All Markers lets users clear every marker of one particular color in a single sweep, or wipe out all markers entirely.

### Renaming Clips in the Timeline

To keep things organized, you can craft custom clip names bound to one specific timeline. That's useful for surfacing clip information that stays put, reads at a glance, and doesn't make you click a flag or marker to see it. Clips renamed this way change only within the current timeline and leave the Clip Name in the Media Pool alone. Renaming clips on the Timeline is done through the File Inspector, typing a fresh name into the Name field.

Renaming a clip in the File Inspector's Name field The fresh name appears in the Timeline track along the bottom of the clip.

The new clip name shown in the Timeline. IMPORTANT: Renaming a clip in the Timeline touches only that clip's instance in that particular Timeline. It leaves the original Clip Name in the Media Pool untouched, and likewise doesn't rename that same clip wherever it lives in other timelines. To rename a clip throughout your whole DaVinci Resolve project, change the Clip Name in the Media Pool instead. TIP: To carry a custom clip name across more than one timeline, copy and paste the clip from timeline to timeline, and the pasted copy keeps its custom name. From that moment on, though, the two clip names stand independent of one another.

### Color Labeling Clips in the Timeline

Out of the box, the various clips carry particular colors that mark each clip type. On top of that, clips with effects on them (Inspector adjustments, volume level changes, speed changes, and the like) take on a darker tint of their default color so you can spot at a glance which clips have been altered. The table below sets out what those default colors are.

Clip Type Video Clip Audio Clip Generator Text Clip with effects

Color Steel Blue Light Green Light Purple Beige Shaded darker

### Custom Clip Colors

Beyond that, you can hand clips one of 16 colors. A clip holds only a single assigned color. And unlike flags, clip colors stick to the individual clip, so giving one use of a clip in the Timeline a clip color does nothing to any other clips drawing on the same source media in the Media Pool.

### Clip Color Appearance

The way these colors show up hinges on where the clip lives. Two options exist:

- Clip thumbnails in the Media Pool or in the Color page's Thumbnail timeline display a small colored dot at the thumbnail's top-right corner.

Thumbnails with label colors showing as dots in the corner

- Clips in the Timeline get tinted all over except across the thumbnail area of video clips. Edit a clip onto a track that's itself been colored and the clip color wins out over the track color.

A timeline whose audio clips have been tinted so the editor can tell at a glance what each one is NOTE: Clip colors stand apart from flags, which show up as badges across the Timeline, Media Pool, and Color page.

### Assigning Clip Colors

You can set clip colors from numerous spots throughout DaVinci Resolve. To give one or more clips a clip color, take one of these routes:

- Turn to the Media page to set clip colors on Media Pool clips via the Shot & Scene preset in the Metadata Editor. Clip colors don't surface in the Media Pool. To strip a clip color, click the X left of the Clip Color buttons in the Metadata Editor.
- Right-click one or more chosen clips in the Timeline and pick a color off the Clip Color submenu of the contextual menu. To strip a clip color, pick Default Color from that same submenu.
- Colorists can right-click one or more chosen clip thumbnails on the Color page and pick a color off the Clip Color submenu of the contextual menu. To strip a clip color, pick Default Color from that same submenu.

### Track Colors

Track colors offer another way to organize clips visually. Each track takes a color code drawn from one of 16 different colors. Those color codes carry over to the Fairlight page too, where they correspond to the Edit page Mixer, plus the Fairlight page Mixer and Audio Meters. To recolor any track:

- Right-click the track header and pick a color off the Change Track Color submenu.
