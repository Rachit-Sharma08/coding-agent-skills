# Opening and altering multicam clips and performing a multicam edit

Version: DaVinci Resolve 20.3 Reference Manual. Context: Multicam editing.
[Chapter index](INDEX.md) / [Previous section](multicam-clip-creation-and-modification.md) / [Next section](multicam-timeline-editing-and-line-cut.md)
<a id="source-multicam-controls-in-the-source-viewer"></a> <a id="source-multicam-keyboard-controls"></a> <a id="source-opening-and-altering-multicam-clips"></a> <a id="source-performing-a-multicam-edit"></a> <a id="source-switching-the-source-viewer-to-multicam-viewing"></a> <a id="source-the-source-viewer-showing-multicam-switching-controls"></a>

### Opening and Altering Multicam Clips

Once a multicam clip is built and dropped into a timeline, you can adjust it several ways by right-clicking it in the Media Pool and picking “Open in Timeline.” Doing so swaps the Timeline contents for a vertical stack of superimposed angles, one to a track, each shifted from the Timeline start so they line up with one another.

When opened, a multicam clip resembles a timeline holding a vertically stacked set of clips. With the multicam clip opened, you can prepare it for editing in several ways:

- You can nudge a multicam clip left or right to adjust its sync (picking an angle and using the Period (.) and Comma (,) “nudge” keyboard shortcuts is one handy approach).
- You can remove the track of an angle you have no use for (right-click the track header and pick Delete Track).
- You can reorder tracks to change the sequence in which angles show up (right-click any track header and pick Move Track Up or Move Track Down).
- You can rename tracks to alter the angle name that shows by default in the Multicam Viewer and that also surfaces in the Timeline once you do cut-and-switch editing.
- You can switch off audio or video tracks for angles you would rather not see yet don’t want to discard.
- You can grade each multicam angle on its own (covered later in this section).

When you have finished adjusting the multicam clip’s contents, close it via the path control at the bottom left corner of the Timeline. Click the name of the edited timeline to return, ready for the following steps. A path control lets you exit the multicam clip

### Performing a Multicam Edit

After you have built one or more multicam clips and edited them into a timeline, carrying out the multicam edit itself is straightforward. 1 Open the Timeline you made to contain the multicam clip or clips in your edit, and place the playhead where editing should begin. 2 Pick Multicam from the Source Viewer mode drop-down.

### Switching the Source Viewer to Multicam viewing

The Source Viewer switches to present every angle inside that clip as switching controls. 3 Pick how many angles to display from the drop-down menu at the lower right of the Source Viewer. On a computer that isn’t especially fast, you may have to cut down the number of angles you view to keep real time playback.

Choosing how many angles to view in the Multicam Viewer When the number of angles inside the multicam clip crossing the playhead in the Timeline exceeds what the Multicam Viewer is set to display, page controls show up to the left of this drop-down menu so you can choose which group of angles to see. You can move to another page of angles by one of these means:

- Click any dot to jump to that page of angles.
- Click the arrows to move among next/previous sets of angles.
- Choose Edit > Multicam > Previous Page (Option-Shift-Left Arrow) or Next Page

(Option-Shift-Right Arrow).

4 Choose whether your switch affects both audio and video together, video on its own, or audio on its own, with the Audio/Video selection buttons located at the bottom center of the Multicam Viewer. Identical results come from the menu: Edit > Multicam > Video and Audio handles both at once (Option-Shift-[ ); for picture by itself there is Video Only (Option-Shift-] ); and for sound by itself there is Audio Only (Option-Shift-\).

These buttons let you pick whether the switch affects video, audio, or both at once. 5 Begin playback, and as you watch the program run, do one of these:

- Click any angle in the Multicam Viewer; this drops a cut into the Timeline and moves to that angle. While you cut-and-switch, every cut lands in the Timeline at once as playback rolls forward.
- Option-click any angle to swap the angle on the current clip without adding a cut. This is useful whenever you later regret the angle you cut to and simply wish to change the whole stretch back to your previous cut. The same outcome is reachable from the menu via Edit > Multicam > Previous Angle, bound to Command-Shift-Left Arrow, or its counterpart Next Angle, bound to Command-Shift-Right Arrow.

While playback runs, the whole Timeline mix sounds along with whatever you are switching, keeping you in context.

A timeline being assembled through cut and switch. 6 Once your multicam cutting is done, simply halt playback. To start refining the Timeline by trimming, pick Source from the Source Viewer mode drop-down; from there you can re-cut and trim those multicam clips on the Timeline exactly as you would any others.

### Multicam Controls in the Source Viewer

When it is in Multicam mode, the Source Viewer offers four groups of controls for setting up and running multicam editing.

- Multicam Angle buttons: Every multicam angle shown in the Source Viewer is a button listing the angle name beneath it. Clicking one of these buttons drops a cut and switches the angle of the next clip, whereas Option-clicking swaps the angle of the clip sitting at the playhead without dropping a cut.
- Audio/Video Selection buttons: A click on any of these toggles which tracks — audio, video, or both audio and video — apply to the cut you make on the Multicam clip. Choosing Audio yields an audio-only cut, choosing video yields a video-only cut, and audio and video cuts the pair together.
- Multicam display drop-down: Sets the count of angles shown as you switch. Depending on how your workstation performs, lowering the angle count can boost playback while you edit. The choices are a grid of 1x1, 1x2, 2x2, 3x3, or 4x4 angles to view.
- Multicam Page buttons: When more angles intersect the Timeline playhead in the multicam clip than the Multicam Viewer is currently displaying (set by the multicam display drop‑down), page controls turn up that let you pick a particular set of angles. A click on any dot jumps straight to that page, while the arrows step through the next and previous groups of angles.

### The Source Viewer showing Multicam switching controls

### Multicam Keyboard Controls

A complete set of keyboard shortcuts is also available for multicam editing.

- Multicam Cut: (Clip > Multicam Cut submenu) Tapping number keys 1 through 9 performs a cut-and-switch, identical to a click on one of the angle buttons of a multicam clip in the Source Viewer.
- Multicam Switch: (Clip > Multicam Switch submenu) Tapping Option-1 through 9 performs a switch, identical to an Option-click on one of the angle buttons of a multicam clip in the Source Viewer.
- Previous/Next Angle: (Edit > Multicam submenu) Tapping Command-Shift-Left or Right Arrow steps you to whichever angle comes before or after. The same controls also loop around to the first or last angles within the multicam clip.
- Audio/Video Switching: (Edit > Multicam submenu) Tap Option-Shift-[ to make the Multicam Viewer cut or switch Video and Audio in tandem. Tap Option-Shift-] for the Multicam Viewer to cut or switch Video only. Tap Option-Shift-\ for the Multicam Viewer to cut or switch Audio only.
- Previous/Next Page: (Edit > Multicam submenu) Tapping Option-Shift-Left or Right Arrow steps you to whichever page of multicam angles comes before or after, in cases where the angle count exceeds what the Viewer’s current multi-angle setting can display.
