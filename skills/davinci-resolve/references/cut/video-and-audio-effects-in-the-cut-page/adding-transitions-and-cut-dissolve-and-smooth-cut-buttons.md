# Adding transitions and cut dissolve and smooth cut buttons

Version: DaVinci Resolve 20.3 Reference Manual. Context: Video and audio effects in the cut page.
[Chapter index](INDEX.md) / [Next section](transition-editing-removal-and-defaults.md)
<a id="source-adding-dissolve-using-keyboard-shortcuts"></a> <a id="source-adding-dissolves"></a> <a id="source-adding-other-kinds-of-transitions"></a> <a id="source-adding-smooth-cuts"></a> <a id="source-adding-transitions"></a> <a id="source-changing-a-transition-to-a-cut"></a> <a id="source-favorited-transitions"></a> <a id="source-the-cut-dissolve-and-smooth-cut-buttons"></a> <a id="source-transitions-thumbnails"></a> <a id="source-video-and-audio-effects-in-the-cut-page"></a> <a id="source-video-and-audio-effects-in-the-cut-page-part-1"></a>

### Video and Audio Effects in the Cut Page

As your edit takes shape, you'll regularly need to put effects on clips—to make titles, fold clips together through compositing, drop in plugins that lend clips a certain look, ramp clips faster or slower, or transform clips so as to zoom into them or shift them about the frame. The Cut page carries controls for all of this and then some.

### Adding Transitions

Transitions like dissolves or wipes can go on an edit to signal a shift in topic, a shift in

location, or time passing. A Smooth Cut transition can likewise be dropped in to mend unwanted cuts in

interview clips or other cases where the subject's position—or the background—doesn't shift much in

the frame. Three buttons over at the bottom right of the Media Pool make it simple to add

and clear away dissolves and Smooth Cut transitions.

### The Cut, Dissolve, and Smooth Cut buttons

### Adding Dissolves

Being the most standard, everywhere-seen kind of transition, dissolves are also the simplest to make. Park the playhead on or near an edit you'd like turned into a dissolve, then, down at the Media Pool's bottom left, click the Dissolve button. A one second Cross Dissolve gets added to whichever edit point lies closest to the edit point.

(Left) A playhead moved near an edit point, (Middle) A dissolve being added, (Right) An edit point that's selected

### Adding Dissolve Using Keyboard Shortcuts

A dissolve can also be added by picking one or more edit points (or by sliding the playhead near an edit you want and pressing V to grab the nearest one), then pressing Command-T to drop in a dissolve, which is the standard transition. The keyboard also lets you add a transition lined up with the start, middle, or end of the edit point. To do that, pick an edit point, tap the U key over and over so as to cycle among the start, center, or end of the edit being selected, then press Command-T for the standard transition. That standard transition lands with its alignment set by the edit selection you made; picking the start of the edit drops a transition ending on the edit; picking the end of the edit drops a transition starting on the edit, and choosing the center of the edit drops a transition centered the same way.

A transition lined up with an edit point's beginning, center, and end

### Changing a Transition to a Cut

To take out a dissolve and thereby turn a transition back into a cut, bring the playhead at or near the edit holding the dissolve, then click the Cut button—quick to do when you're on the DaVinci Resolve Editor Keyboard, which carries a dedicated Cut button.

TIP: As another route, you can pick one or more transitions in the Timeline and press the

Delete key to clear them.

### Adding Smooth Cuts

Smooth Cuts are special-purpose transitions built to render short jump cuts in the middle of a clip unnoticeable. The way it works is by drawing on AI powered Speed Warp processing to line up the same features on both sides of a cut, automatically morphing a subject from one position into another across the transition's span. To add a Smooth Cut: 1 Set the playhead on or near an edit. 2 Down at the Media Pool's bottom left, click the Smooth Cut button. A one second Smooth Cut gets added to whichever edit point lies closest to the edit point. A Mode dropdown menu hands you two choices: Faster and Better. Better is the default, with excellent quality and the knack for holding onto subjects' motion across the transition's span. Faster morphs between stills of the outgoing and incoming frames. In most real situations Better mode hands you the superior result, though some cuts or effects come out better with the Faster option. The Smooth Cut effect performs best on footage such as sit-down interviews and close-up head shots that carry minimal background and subject motion, and where the subject's position barely differs from one side of the cut to the other. Smooth Cut shines, for instance, when you're paring pauses, partial repeats, filler sounds like "um" or "you know," and other speech disfluencies from an interview clip so the dialog tightens, and your aim is to kill the small "jump" at the cut without cutting away to B-roll. A short two or four frame Smooth Cut transition laid on the edit can render this sort of edit invisible, provided the speaker doesn't move much during the cut. The busier the shot's background and the more the speaker shifts position, the tougher it gets to land a useful Smooth Cut result. Even though any transition defaults to one second, you'll find Smooth Cut transitions often fare far better kept short; 2- to 6-frame Smooth Cut transitions tend to do the best job of hiding jump cuts. NOTE: Beginning with DaVinci Resolve 20, Smooth Cut relies on a new AI powered Speed Warp to carry out the transition. Should you rather go back to the older optical flow version, just clear the Speed Warp box in the Transition inspector.

### Adding Other Kinds of Transitions

So that choosing transitions, titles, and effects feels more intuitive, DaVinci Resolve presents each effect as a thumbnail picture alongside the text name. That lets a user breeze through the many options and pick the right effect by sight rather than recall its name alone. Transitions and titles can be previewed ahead of dropping them on the Timeline, so you can quickly audition several options before settling on one.

### Transitions Thumbnails

To preview a transition ahead of dropping it into the Timeline, make sure "Hover Scrub Preview" is ticked in the Transitions option menu, then just rest your pointer on any transition in the Transitions tab and slide it across the thumbnail. The transition previews in the Viewer using the two clips nearest the Smart Indicator on the Cut page, or the two clips nearest the playhead on the Edit page.

A scrub over a Transition Thumbnail previews that transition in the Viewer. Once you've settled on your transition, it can go onto any edit point by way of the methods below: Methods of adding different transitions:

- To add a transition by dragging it from the Transitions Browser: Out of the Effects Library, drag a video transition to an edit point on the Timeline so it centers at, ends at, or starts at the edit point. Where the heads and tails of the two clips don't overlap, you may be unable to place a transition where you'd like.
- To add a transition using the Transitions Browser's contextual menu: Choose one or several edit points (limited to one per track), then right-click a video transition over in the Effects Library and pick Add to Selected Edit Points and Clips. That one transition lands on each selected edit point together.
- To add a transition by double-clicking in the Transition Browser: A double-click on a transition in the Cut page's Transitions Browser applies it straight to the edit point that the Smart Indicator references.
- To add a transition through the Transition Browser's alignment icons: A double-click works on one of three transition alignment icons sitting at the bottom of the in the Cut page's Transition Browser.
- To add a transition to all edit points on a timeline: Click the Timeline Actions menu and pick Add Transition to All Edits. This drops the last used transition onto every edit point across a timeline.

### Favorited Transitions

Any transitions you've flagged as favorites (whether by clicking the star icon on the thumbnail or by picking Add to Favorites off the contextual menu) are reachable in the Favorites tab of the Effects library.
