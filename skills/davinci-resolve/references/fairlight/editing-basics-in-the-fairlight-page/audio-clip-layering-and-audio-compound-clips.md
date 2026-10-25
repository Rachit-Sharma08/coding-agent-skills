# Audio clip layering and audio compound clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Editing basics in the Fairlight page.
[Chapter index](INDEX.md) / [Previous section](clip-attributes-and-dialogue-matching.md) / [Next section](playhead-fades-and-overlap-crossfades.md)
<a id="source-adjusting-the-curve-of-the-fade"></a> <a id="source-audio-clip-layering"></a> <a id="source-audio-compound-clips"></a> <a id="source-audio-crossfades"></a> <a id="source-batch-fade-and-crossfade-editor-in-the-fairlight-page"></a> <a id="source-batch-fade-options-in-the-fairlight-menu"></a> <a id="source-fades-and-crossfades"></a> <a id="source-tracks-and-clips-highlighted-for-batch-fades"></a> <a id="source-using-fades"></a>

### Audio Clip Layering

Audio layering is a special audio editing mode that lets you stack several audio clips in one track, where audio clips edited into the upper layers mute the overlapping stretches of audio clips on lower layers. With audio layering switched on, stacked audio clips behave much like stacked video clips set to 100% opacity, the ones on top hiding (or muting) the ones below.

An illustration of layered multiple-audio performance editing, in which the uppermost layer silences the overlapping stretches of audio clips sitting on layers below Audio layering earns its keep in any case where you’re piecing together segments of several takes into one voiceover, audio vocal track, or dramatic performance, since you can pick which segments to use by their stacked position in the pile of clips on that track, all while keeping the other takes underneath should they prove useful down the line. TIP: Track layering can be used on the Edit page as well.

To enable audio layering:

- Choose Timeline > Layered Audio Editing so a check mark shows beside the command. From that point on, all overlapping audio gets layered rather than overwritten.

To view audio layering: 1 Choose View > Show Audio Track Layers, which brings up the track layers belonging to every audio track — and to every lane inside a given audio track — across the Timeline. With layering on, space opens above each Timeline track, handing you a region for editing layered audio clips. 2 To bring an audio clip or segment in as a layer inside a particular audio track, drag it over from elsewhere in the Timeline or out of the Media Pool, then drop it into the empty space above whatever audio is already in that track.

Dragging one audio clip so it layers above another 3 Work the various stacked layers of audio so the segments of each take you like end up on top. Only the topmost clip segments will be heard. Audio segments that overlap beneath stay silent. To set another layer on top, drag it from where it is to the empty space at the top of the track.

Dragging a bottom audio layer to appear on top 4 Once you’re done editing clips in track layers, choose View > Show Audio Track Layers once more to tuck the individual layers away, so only the topmost clips show as a flat sequence in each track and lane.

Tuck the layers away and every audio layer collapses onto one track, looking as though the top clips overwrote what lay below — yet the silenced material beneath survives

### Audio Compound Clips

DaVinci Resolve handles audio compound clips, built just like any other compound clip — by selecting several audio clips, right-clicking one, and choosing New Compound Clip. On top of that, compound clips with video clips may now hold several audio items too. Open a compound clip that holds audio in the Edit or Fairlight pages — right-click an audio compound clip and choose Open in Timeline — and breadcrumb controls show up beneath the Timeline, letting you step out of the compound clip and back to the master Timeline.

An audio compound clip being opened; spot the path control down at the Timeline’s lower left

### Audio Crossfades

Any edit point between two audio clips with enough handles can take a Cross Fade transition, the same as with video transitions. Three approaches exist: drag and drop one out of the Effects Library; right-click an edit and pick an option off the contextual menu; or select an audio edit point and head to Timeline > Add Audio Only Transition (Shift-T). A Cross Fade transition is a fast, easy means of fading the outgoing clip’s volume down while at once fading the incoming clip’s volume up, which builds a smooth aural transition between two audio clips.

An audio Cross Fade transition applied between two clips Double-click a Cross Fade transition to open it into the Inspector, where these parameters come up:

- Duration: How long the transition runs, shown in both seconds and frames.
- Alignment: A dropdown for choosing where the transition lands in relation to the edit point it’s

applied to. The available settings are “End on Edit,” “Center on Edit,” and “Begin on Edit.”

- Transition style: Picking –3dB, 0dB, or +3dB pins the Fade In and Fade Out levels alike

to a single value. For more on what these levels signify, see the parameter that follows.

- Fade In/Fade Out levels: Three options act on the incoming and outgoing halves of

the Cross Fade effect on their own. 0dB lays down a linear fade (this is the default). +3dB lays down a boosted curve; applied to both Fade In and Fade Out, it can make up for sagging levels in the middle of a Cross Fade. –3dB lays down an attenuating curve, deliberately pulling the Cross Fade’s level down.

NOTE: Building and editing crossfades is possible on the Edit page as well as the Fairlight page.

### Fades and Crossfades

Working with fades and crossfades is part of audio editing on the Fairlight page. This section walks you through building these effects so you can segue smoothly between audio clips. A Dolby Atmos master file dropped on a timeline as a clip can take basic fades. Complex fades and batch fades, however, aren’t supported.

### Using Fades

As on the Edit page, every audio clip carries fader handles, which surface in the top right and top left corners once your pointer hovers over that clip.

Hovering the pointer over a clip surfaces its fader handles Drag one of these handles outward and you build a fade effect whose duration equals the distance you dragged the handle.

Creating a fade effect by pulling out one of the fader handles With a fade effect built, you can reshape the fade’s curve by dragging the handle that sits right atop the fader curve. Dragging the handle up and down changes the curve’s angle, while dragging it left and right changes the curve’s shape. This way, you can build fade effects of every kind.

### Adjusting the curve of the fade

### Batch Fade and Crossfade Editor in the Fairlight Page

Several fades become available to several clips with several tracks selected, greatly widening fade functionality. The Batch Fades window holds fade shapes for Fade In, Cross Fade, and Fade Out. You set the Fade Length by frame for each of these fade types, and an option lets you overwrite existing fades on the highlighted clips.

All of the settings in the Batch Fades window Each Fade type carries six options for precise use. When you add Fades between sources, settling the shape matters so only the media you intend lands in the fade. The curves show the ramping slopes of the fade. Every box carries similar controls for steering its own Fade type. 1 Beside the Fade type name sits the on/off toggle 2 Six Fade curves are there to build exactly the fade needed. 3 A Length box sets how many frames the fade spans, 4 A click box overwrites any earlier fades, where needed. The Crossfade box carries three extra controls. 1 Equal Power holds the signal level steady through the fade. 2 Equal Gain comes into play when crossfading media that could phase once combined. If a music cue is crossfaded, for instance, the fade’s mid-point could bring a jump in level or added phasing trouble. This option holds the gain across the fade for that sort of media. 3 Unlinked allows a different curve type on each side of the crossfade. This window holds onto whatever settings were last made, so after a run of Fade types is chosen, Batch Fades can be applied without reopening it — a single click from the Fairlight menu does the job across highlighted regions. Whatever you set in the Batch Fades window carries over to the Apply Batch Fades command in the Fairlight menu.

### Batch Fade options in the Fairlight menu

Here the graphic shows clips and tracks highlighted and set for Batch Fades to be applied.

### Tracks and clips highlighted for Batch Fades

The graphic below shows how the Batch Fades land. Clips that aren’t connected get Fade In and Fade Out. Clips that are connected get Crossfades. The Batch Fades window settles each of the Fade parameters and then lays them onto all of the selected clips. In this example, the Overwrite box was left unchecked. Compare the fades that were already there and notice they keep their original Fade length and shape.

Every one of the highlighted clips now carries fades drawn from the Batch Fades window.

NOTE: When the media runs too short, a dialog box warns you that there aren’t enough handles and that the fade couldn’t be created. From there you can choose to trim clips, skip clips, or cancel the Batch Fade. Cancel and you can then adjust the settings to better suit the media.
