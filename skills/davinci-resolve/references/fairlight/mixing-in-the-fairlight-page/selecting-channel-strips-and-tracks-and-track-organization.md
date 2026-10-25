# Selecting channel strips and tracks and track organization

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mixing in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](introduction-to-mixing-and-mixer.md) / [Next section](what-is-an-effects-insert-and-input.md)
<a id="source-changing-track-type"></a> <a id="source-color-coding-tracks"></a> <a id="source-deleting-tracks"></a> <a id="source-disabling-multiple-tracks-via-the-mixer"></a> <a id="source-disabling-tracks"></a> <a id="source-fairlight-mixer-signal-path"></a> <a id="source-managing-channel-strips-using-the-index"></a> <a id="source-rearranging-tracks"></a> <a id="source-rearranging-tracks-1"></a> <a id="source-rearranging-tracks-by-moving-a-mixer-channel-strip"></a> <a id="source-selecting-channel-strips-and-tracks"></a> <a id="source-showing-and-hiding-tracks"></a> <a id="source-toggling-lock-record-solo-and-mute"></a> <a id="source-track-organization"></a>

### Selecting Channel Strips and Tracks

Selecting a track in the Timeline simultaneously selects its matching Mixer channel strip, and the reverse holds true as well:

- For a single track, a plain click does it.
- To grab a run of adjacent tracks, click a first track or channel strip, hold down Shift, and

click on last item you want in your selection.

- Within the Mixer, you can equally select several channel strips by clicking and dragging a

bounding box around the tracks you want to select.

- For tracks or channel strips that aren’t side by side, command-click each one you

want to add to your selection.

Picking several channel strips selects the matching tracks over in the Timeline

### Track Organization

Three organizational attributes belong to every channel strip, helping you recognize which strip handles which portion of the mix. Track color: each track can wear its own color code as an aid to organization. That color shows up in the Timeline track header, the Mixer, and the meters so you can tell at a glance which track ties to which channel strip and meter. A strip’s track color and track number sit at its top.

Track number: this is where the number of the corresponding timeline audio track is shown for each channel strip. Track name: this echoes the name found in the track header of a Timeline track. Rename an audio track in either the Timeline or the Mixer, and the new name shows up here.

Each track’s name sits between the assignment buttons and the arm/solo/mute buttons

### Rearranging Tracks

To move tracks and busses around within the Mixer, click and hold a track name and drag it left or right to wherever you want it. The technique applies whether you’ve selected one channel strip or several. While you drag the mouse, a white line marks the destination, and the Index updates to match the change.

### Rearranging tracks by moving a Mixer channel strip

### Disabling Tracks

To switch off an audio track from the Mixer, right-click the track number atop its channel strip and pick Disable Track from the contextual menu; running through the same steps again turns the track back on. To disable several tracks together, select them, Option right-click any track number among them, and pick Disable Tracks from the contextual menu.

### Disabling multiple tracks via the Mixer

### Managing Channel Strips Using the Index

Gathering every track of the current Timeline into one list view, the Index makes timelines packed with tracks far simpler to handle. Its columns surface each track’s visibility, track number, name, controls, channel format, monitor assignment (where there is one), ADC controls, and VCA assignment. Through the controls in those columns you can run the current Timeline’s tracks — revealing or hiding them, flipping track controls, or reordering them. A right-click on one or more selected tracks additionally lets you color code them or switch the track type.

Both the Timeline and the Mixer have all their tracks listed in the Index’s Tracks panel.

### Showing and Hiding Tracks

The Index’s Tracks panel lets you tuck away tracks you aren’t working on so the ones you do need have more room. TIP: To toggle visibility across several tracks fast, click and drag upward or downward across the eyeball button of each track you want to flip.

### Color Coding Tracks

Pick one or more tracks, then right click any of those selected and choose a hue from the contextual menu’s Change Track Color submenu.

### Toggling Lock, Record, Solo, and Mute

Much like visibility, the Lock, Record, Solo, and Mute controls let you turn many tracks on or off in a hurry: click and drag upward or downward across the Lock, R, S, or M buttons you wish to toggle.

### Rearranging Tracks

Within the Index’s Tracks tab, reorder tracks by clicking any track strip region between the other controls and then dragging that track upward or downward in the Index. A white line during the drag indicates where the track lands once you let go. You may even grab an unbroken run of tracks and shift them all to a fresh position in the Timeline in one move. Managing the Dividing Line The Index defaults to two track zones — one holding audio tracks and another holding busses and VCAs, with a dividing line between them. Busses and VCAs can be pulled up out of that divider into any spot and any order. That comes in handy, for example, with a run of dialogue tracks where you want to bring the dialogue bus right up beside them. Drag the dividing line wherever you like, so you can preserve the two-zone split yet rearrange what each shows. After the order changes in the Index, the Mixer panel and the Meter panel both reflect it. Reordering busses and tracks lets you tune your workflow to whatever group of tasks is at hand. Single Mixer View The three-dot Option menu at the top of the Mixer panel includes a Single Mixer view choice. Single Mixer view drops the divider line out of the Index’s Tracks tab altogether, giving one uninterrupted scroll of the tracks across both the Mixer panel’s horizontal scroll and the Index’s vertical scroll. The divider can be brought back whenever you want.

NOTE: To put the bus order back to how it started, pick “Reset Bus Order” from the three-dot Options menu at the Mixer’s upper right.

### Changing Track Type

An audio track’s track type denotes its channel width and format, and you’re free to change it whenever you like. A mono track, for instance, could become a stereo, 5.1, or 12 channel adaptive track. To do so, select one or more tracks, right-click any of them, and pick another type from the contextual menu’s Change Track Type submenu. NOTE: Bear in mind that moving from a wider track type down to a narrower one may require you to also specify which channels of the larger source audio file remain audible on the smaller type. That’s set through the Clip Attributes choice on a clip’s contextual menu, using the Audio tab.

### Deleting Tracks

Remove a single track by right-clicking it and picking Delete Track from the contextual menu. To wipe out several selected tracks at once, right-click any track in the group and pick Delete Tracks from the contextual menu.

### Fairlight Mixer Signal Path

A mixer’s signal path — its layout, or “topology” — sets out how audio signals travel from one stage to the next. On the Fairlight channel strip, the standard flow runs like this: 1 Audio source: the Input menu picks where the signal originates — file playback, a bus, live input, and so on. 2 Path Settings: reached through the Input menu, these let you tweak the incoming signal. 3 Track FX: the built-in effects, namely Voice Isolation (Studio only) and Dialogue Leveler, off by default. 4 Effect: any Fairlight FX, AU, or VST effects. 5 Dynamics: a dedicated per-channel dynamics processor offering expander/gate, compressor, and limiter. 6 EQ: a dedicated 6 band EQ with adjustable gain, frequency, and Q. 7 Output Routing: covers panning and bussing. From there the channel strip’s main fader governs the level feeding any main output busses it’s assigned to. Bus Send faders set the level going to whatever destination a mixer channel send targets, and can be configured pre­‑or post-fader.
