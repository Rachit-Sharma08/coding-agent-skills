# Effects inspector controls and adding filters to video clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: Effects overview.
[Chapter index](INDEX.md) / [Previous section](editing-effects-and-transitions-and-the-effects-library.md) / [Next section](adjustment-clips-and-paste-attributes.md)
<a id="source-adding-filters-to-video-clips"></a> <a id="source-adjusting-multiple-clips-at-the-same-time"></a> <a id="source-fusion-effect-templates-cache"></a> <a id="source-render-in-place"></a> <a id="source-the-effects-inspector-controls"></a> <a id="source-the-fairlight-fx-noise-reduction-custom-ui-interface"></a>

### The Effects Inspector controls

These controls include:

- Enable button: A toggle control positioned left of the parameter group’s name lets you, in a single move, disable and re-enable each parameter belonging to that group. Orange means that track’s enabled. Gray is disabled.
- Parameter group title bar: Double-clicking any parameter group’s title bar collapses or opens them. More usefully still, Option-double-clicking one parameter group’s title bar collapses or opens every parameter group together.
- Keyframe and Next/Previous Keyframe buttons: This button lets you add or strip keyframes at the playhead’s position to or from every single parameter inside the group. While the button glows orange, a keyframe sits at the playhead’s current position. While it is dark gray, no keyframe is present. The left and right arrow buttons let you hop the playhead between keyframes for additional tuning.
- Reset button: Lets you restore every parameter inside that group to its default settings.

### Adding Filters to Video Clips

For generating assorted effects, DaVinci Resolve handles built-in Resolve FX as well as third-party OFX plugins. You can put these effects on Edit page clips and equally on Color page nodes. This section walks through applying, editing, and removing these filters on the Edit page. For more on video effects in the Color page, consult Chapter 151, “Using Open FX and Resolve FX.” For a thorough rundown of each Resolve FX plugin shipped with DaVinci Resolve, consult Part 12, “Resolve FX Overview.” Ways to apply video filters on the Edit page: To apply a video filter to a clip:

- Pull any filter out of the Effects Library and drop it onto whichever Timeline clip should receive it.
- Double Click a filter within the Effects Library to place it on the currently selected clip.
- Pull the Filter from the Effects Library across to the Inspector to place it on the chosen clip.
- Pull the Filter from the Effects Library across to the Viewer to place it on whatever clip is on view.

To apply a video filter to multiple clips: Highlight all the clips you intend to filter in the Timeline, then drag any filter out of the Open FX category of the Effects Library onto any one of the selected clips. This action can be undone.

Applying a video filter to a single clip in the Timeline

To edit a clip’s video filters: Highlight that clip and open the Inspector’s Effects tab. The effects get further sub-grouped by type: Fusion, Open FX, or Audio. When a clip carries no effects, this panel appears dimmed.

Resolve FX controls show up in the Effects panel of the Inspector. Certain video filters carry custom onscreen controls adjustable in the Viewer. Those can be surfaced on the Edit page through the OFX mode of the Viewer.

Switching on the onscreen controls for Resolve FX within the Edit page Timeline Viewer

After they are enabled, the OFX onscreen controls show up in the Viewer.

Modifying onscreen controls foµr Resolve FX in the Edit page Timeline Viewer A good number of audio filters carry custom controls that show up in a floating window. To surface a filter’s custom controls: Open the parameters, if they are not already open, by double-clicking that filter’s title bar. For filters carrying custom UI, a button should show up at the top of the parameters. Clicking that button opens a floating window holding every custom control. Once you have finished tuning the custom controls, close the window.

### The Fairlight FX Noise Reduction custom UI interface

Ways to work with video filters in the Inspector:

- To reorder several video filters placed on a clip: Click the move up or move down buttons within any filter’s title bar, just left of each filter’s Trash Can button.
- To switch a filter off or back on: Hit the toggle control found at the leftmost edge of each filter’s heading row. Orange means that track’s enabled. Gray is disabled.
- To remove a filter: Click the Trash Can button.
- To reset a filter: Press the Reset button positioned at the far right of that filter’s title bar.
- To open or collapse a filter’s parameters: Give the title bar a double-click.
- To open or collapse the parameters of all filters: Hold Option and click the title bar.

Once placed on a clip, video filters can likewise be keyframed or automated the same as any other Inspector setting, producing dynamic effects that evolve over time.

### Render in Place

Render in Place lets you render and bake in every effect placed on a single clip in the Edit page Timeline. This command, available only on the Edit page, generates a brand-new media file that swaps in for the original clip on the Timeline. That new file is written into the very folder holding the original source file, and gets added to the Media Pool by itself. Render in Place can help you boost playback performance on a computationally heavy clip, or serve to build a fresh high-quality master media with effects finalized and baked in. Suppose, for instance, you have assembled a clip carrying an elaborate speed ramp, and you intend to pass it along to a fellow editor or to a vfx artist within a round-trip rendering workflow, yet you are uneasy about how other programs might read those speed effects. In that case you could render the clip in place at master quality, then go on to render and hand off the program. This operation does not run in only one direction. Later on, should the clip turn out not to have been as locked-down as you had hoped and a change becomes necessary, the “Decompose to Original” choice restores the original clip carrying its original effects. To Render in Place: 1 On the Edit Page timeline, pick one or more clips. When several clips are picked, each one is rendered in place separately, though the whole thing runs as one batch operation. 2 Right-click that selection and pick “Render in Place” out of the contextual menu. 3 Set the appropriate Render Clip Options, after which you click the “Render” button. Start Timecode: Establishes the clip’s opening timecode value. Format: Picks the media file format. Codec: Picks the video codec. Type: Lays out the compression parameters belonging to the chosen codec. Include Handles: Lets you state how many frames ahead of and behind the clip In/Out points get rendered. Include Video Effects: Tick this checkbox to bake in every effect placed on the clip, among them sizing, Open FX or Resolve FX, and speed effects. Leaving this checkbox off renders the clip with the speed effects baked in but none of the others.

Include Fusion Composition: Switch this checkbox on to bake in whatever compositions are attached to the clip. Include Color Grading Effects: Switch this checkbox on to bake in whatever color grading is attached to the clip out of the Color page. Render at Source Resolution: When ticked, the freshly rendered media matches the resolution of the original source media instead of the timeline resolution.

The Render in Place options 4 In the File dialog that pops up, pick where the resulting media should be saved. Settle on a location and click Open. A progress bar surfaces to indicate how long the operation runs. After it wraps up, your new media is kept at the chosen spot, added to the Media Pool, and proceeds to swap in for each matching source clip on the Timeline. If you have run Render in Place and then have second thoughts, or some last-minute change reaches you afterward, you can easily decompose back to the original clip with its editable effects so as to make the change. To Decompose to Original: 1 On the Edit Page timeline, pick one or more clips that have previously been Rendered in Place. 2 Right-click that selection and pick “Decompose to Original” out of the contextual menu. Back onto the Timeline comes the original clip, along with every one of its editable effects. Media generated through the Render in Place process is neither deleted from the source folder nor pulled out of the Media Pool. In effect it is a new clip.

### Fusion Effect Templates Cache

Fusion effect templates placed on timeline clips offer more granular caching plus automatic render caching options. Within the timeline clip context menu, the Render Cache Fusion Effect Filter menu carries an Auto option switched on by default. While render cache is set to Smart, any Fusion effects and templates placed on a clip cache themselves automatically. Switching auto off lets you cherry-pick which effects to cache individually. While render cache is set to User, the Auto option caches the Fusion effects automatically, provided the project setting to Automatically Cache Fusion Effects in User mode is on. With that project setting off, Auto mode caches no Fusion effects unless you pick them out one by one.

### Adjusting Multiple Clips at the Same Time

There is a simple route to tuning the Inspector parameters of several clips together, without resorting to Paste Attributes (covered later in this chapter). All it takes is selecting every clip you wish to change at once, then modifying the Inspector parameter you want to adjust. The upshot is that every selected clip shifts by the same amount. This holds for compositing effects, transforms, text parameters, filters, and audio settings — pretty much anything that can be surfaced in the Inspector for several selected clips at once. Once several clips are selected, the Inspector shows “Multiple Clips” as its title. Should the selected clips hold differing values in the parameter you are tuning, that parameter shows two dashes in its value field. You have two routes for adjusting multiple clips:

- When you want a relative adjustment across all selected clips while preserving their original offsets from one another, drag the virtual slider in the parameter field, which will show a + or – ahead of however many units your adjustment is.
- When instead you want every selected clip set to the same value, double-click in the number field, type the value, and press Return.

Performing a relative shift of plus 4.9 to the Rotation Angle across every selected clip
