# Mediain node parameters for clips in a timeline and source color space

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md) / [Previous section](referenced-compositions-and-generators.md) / [Next section](fusion-loader-saver-and-loader-parameters.md)
<a id="source-aligning-clips-from-the-media-pool"></a> <a id="source-audio-tab"></a> <a id="source-getting-clips-into-fusion-part-2"></a> <a id="source-mediain-node-parameters-for-clips-in-a-timeline"></a> <a id="source-source-color-space"></a> <a id="source-source-gamma-space"></a> <a id="source-the-mediain-audio-tab"></a>

### MediaIn Node Parameters for Clips in a Timeline

Build a composition from clips off the Edit page Timeline, and the MediaIn nodes for those clips show fewer parameters than ones imported straight from the Media Pool, since the timing of clips already cut into a Timeline is already locked in.

The parameters on the Inspector Image tab for a Timeline-sourced clip Image Tab

- Clip Name: Displays the name of that clip.
- Process Mode: Lets you decide whether the clip that node stands for is handled as

Full Frames, or through one of the named interlaced approaches.

- Media Source: With this control you pick where the media comes from; the three

choices on offer are: Timeline, Background, and Media Pool. Timeline: Ties the clip to the Edit Timeline (default). Background: This draws frames from the edit’s lower video tracks. Flip the Media Source over to Background and the composited result of every lower track becomes visible. Media Pool: Ties the clip straight to the Media Pool, skipping past the Edit Timeline.

- Layer: With Multilayer or Photoshop PSD files, this picks which layer inside the file gets used. On a Fusion Clip built from several video layers on the timeline, it instead points to each layer’s index number.

### Source Color Space

To support a linear workflow, the Color Space Type menu assigns the media’s color space. In contrast to the Gamut tool, it carries out no real color space conversion; instead it writes the source space info into the metadata whenever that metadata isn’t already there. Downstream, that metadata can then be picked up by a Gamut tool set to the From Image option, or by a Saver where explicit output spaces have been defined.

- Auto: Passes along any metadata that might be in the incoming image.
- Space: Lets the user choose the color space out of an assortment of options.

### Source Gamma Space

To support a linear workflow, the Curve Type menu works out, or lets you pick, the Gamma setting for the picture and offers the choice of stripping the Gamma curve away.

- Auto: Passes along any metadata that might be in the incoming image.
- Space: Lets you pick a particular setting from a Gamma Space drop-down menu, while a

visual graph shows you a depiction of the gamma setting you’ve picked.

- Log: Much like the Log-Lin node, this choice exposes particular log-encoded gamma profiles so

you can pick whichever one fits your content. A visual graph offers a depiction of the log setting you have chosen. Pick Cineon from the Log Type menu and, for fine-tuning the gamma output, extra options appear: Lock RGB, Level, and Soft Clip, plus Film Stock Gamma, Conversion Gamma, and a Conversion table.

- Remove Curve: Based on whichever gamma space is chosen, or on the gamma space turned up in Auto mode, the matching gamma curve is stripped off the material, in effect converting it so it outputs in a linear color space.
- Pre-Divide/Post-Mujltiply: When the need arises, lets you turn “straight” alpha channels into pre-multiplied alpha channels.

TIP: Everything on the DaVinci Resolve Fusion page is processed at 32-bit floating-point bit depth, no matter what the content’s real bit depth happens to be.

### Audio Tab

The MediaIn node’s Inspector holds an Audio tab, from which you can opt to solo just that clip’s audio or listen to every audio track on the Timeline.

### The MediaIn Audio tab

On the MediaIn node, the Audio tab is where you pick the playback track, slip the audio timing, and clear the audio cache If the audio falls out of sync during Fusion playback, the Audio tab’s Sound Offset wheel lets you nudge the audio in subframe frame increments. That slipped audio is changed only on the Fusion page. Every other page holds onto the original audio placement. Purging the Audio Cache The audio together with its settings is cached so things run faster. Whenever you alter which audio tracks you want playing in Fusion, or use the Sound Offset wheel to slip the audio tracks, you have to purge the audio cache. Likewise, going back to the Edit, Cut, or Fairlight page and changing the audio levels means you have to purge the audio cache. Whenever the audio playback shifts in any way, clear it by pressing the Purge Audio Cache button over in the Inspector. Your audio then refreshes the next time the composition plays back.

### Aligning Clips from the Media Pool

Drop a clip from the Media Pool or your file system straight into a composition, and the MediaIn node you end up with carries more options than clips taken off the Edit page Timeline do. Those extra options make it simpler to line up the Media Pool clips with other clips off the Edit or Cut page Timeline. On top of that you can trim clips, hold the first or last frame longer than the source media runs, and reverse or loop the clip to gain more range for your composition.

The Inspector parameters for a clip imported from the Media Pool

What follows is a rundown of the controls tacked on beyond those that show up when a clip comes from the Edit or Cut page Timeline.

- Global In/Out: This control sets where this node sits inside the composition. As an example, a clip dropped into the comp from the Media Pool lands at frame 0. The MediaIn node from the Edit page Timeline, though, might not begin until a far later frame, depending on where it was cut into the Timeline. Reach for Global In to name the frame the clip begins on so it lines up with media off the Edit page Timeline. Checking and changing how various clips in the comp line up is easiest while the Keyframes Editor is open.

To shift the clip in time or align it with other clips without altering its length, set the mouse pointer in the center of the range control and drag it to the new spot, or type the value in by hand into the Global In value control. Should the Global In and Out values be dialed down until the span between the In and Out values falls below the n number of frames the clip has available, Fusion trims the clip on its own by tweaking the Clip Time range control. Should the Global In/Out values be raised until the span between the In and Out values runs past the number of frames the clip has available, Fusion lengthens the clip on its own by tweaking the Hold First/Last Frame controls. Those added frames are shown in the range control by turning the held frames purple in the control.

- Trim: With the Trim range control you cut frames off a clip’s beginning or end. Move the Trim In to drop frames at the head, and set Trim Out to name the clip’s final frame. The numbers entered are offsets. Putting 5 into Trim In makes the sequence’s 5th frame the starting point and skips the first four. Setting Trim Out to 95 halts frame loading once the 95th has been read.
- Hold First Frame/Hold Last Frame: Using the Hold First Frame and Hold Last Frame controls, the clip’s first or last frame is held for however many frames you specify. When the footage loops, these held frames carry into the loop.
- Reverse: Tick this checkbox to play the footage backward, so the last frame leads off and the first frame comes at the end.
- Loop: Tick this checkbox to repeat the footage through to the project’s end. Whatever you add with Hold First/Last Frame or remove with Trim In/Out becomes part of the looped clip.
