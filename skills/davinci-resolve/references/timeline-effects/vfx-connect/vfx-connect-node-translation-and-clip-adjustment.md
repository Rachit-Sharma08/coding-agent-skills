# How clips are translated into node trees and altering VFX connect clips

Version: DaVinci Resolve 20.3 Reference Manual. Context: VFX connect.
[Chapter index](INDEX.md)
<a id="source-altering-vfx-connect-clips"></a> <a id="source-creating-multiple-versions-of-fusion-clips"></a> <a id="source-creating-multiple-versions-of-fusion-clips-on-another-machine"></a> <a id="source-how-clips-are-translated-into-node-trees"></a> <a id="source-sending-a-vfx-connect-directory-to-another-machine"></a> <a id="source-switching-versions-of-vfx-connect-clips-in-davinci-resolve"></a> <a id="source-updating-vfx-connect-clips-using-render-media-and-refresh"></a> <a id="source-using-vfx-connect"></a> <a id="source-vfx-connect"></a> <a id="source-vfx-connect-1"></a>

### VFX Connect

When the effects on offer across the Edit, Fusion, and Color page fall short of what you’re after, the VFX Connect feature of DaVinci Resolve lets you push one or more clips out of the Edit page timeline into the standalone version of Blackmagic Fusion, where heavier compositing and effects work can be done. Since Fusion runs on every one of the three platforms, this workflow is available in the macOS, Windows, and Linux builds of DaVinci Resolve alike. The whole thing is a tidy round-trip: ship clips from the DaVinci Resolve Timeline across to Fusion, build your effects, then render the finished result out of Fusion so it lands automatically back in your timeline.

### Using VFX Connect

Handing one or more clips to the standalone version of Blackmagic Fusion takes little effort. To send clips to Fusion: 1 In the Timeline, pick out the clip or clips you’d like to route to Fusion. Here, for instance, two superimposed clips are picked.

Selecting two clips to send to Fusion 2 Right-click any of the chosen clips and pick New VFX Connect Clip out of the contextual menu.

The New VFX Connect Clip dialog 3 Within the New VFX Connect Clip dialog, set these options: a) Give it a name. b) Pick a video format (for the media that gets rendered over to Fusion). c) Pick a codec to suit the format you just chose. d) To carry Alpha channels across to Fusion, switch on the Export Alpha checkbox. Doing so exports both the alpha channels baked into a clip and any alpha channels being generated within DaVinci Resolve.

e) To stash the VFX Connect Clip you’re building, together with its directory and media, somewhere particular, switch on the Custom Location checkbox, then hit the Browse button and pick a spot. If you skip this, the directory holding the VFX Connect clip and whatever source media renders alongside it lands in the same directory as the scratch disk. f) To jump straight into Fusion, switch on the “Open VFX Connect Clip” checkbox. When you do, DaVinci Resolve by default renders every video clip you picked — together with each speed effect, transform, and Color page operation applied to those clips — in the Timeline Color Space. That said, hit Cancel once the Render Composition Media dialog shows up and the Fusion project that opens points at the source media on disk instead of rendered media DaVinci Resolve would generate. 4 Once you’re done, hit Create. DaVinci Resolve makes a VFX Connect clip, showing up as a lone clip in the Timeline and over in the Media Pool. (Top) how VFX Connect clips look on the Timeline, (Bottom) the same clips in the Media Pool 5 There are two routes to opening the VFX Connect clip in Fusion:

- With “Open VFX Connect Clip” switched on, Fusion launches by itself and the clips you picked show up as Loader nodes inside Fusion.
- If it wasn’t switched on, right-click the VFX Connect clip over in the Media Pool and pick VFX Connect > Open Fusion off the contextual menu. From there, new media renders (by default), Fusion launches, and the clips you sent become a Fusion node tree — something the next section covers in fuller detail.

6 Inside Fusion, reach for the tools on hand to build the effect you’re after.

7 Optionally, ahead of rendering, to swap the Output Format, click the Output node and pick a fresh format out of the Output Format pop-up over in the Tools tab. Skip that and the Fusion composite renders in whatever format you chose back when you first sent the VFX Connect clip.

The Tools panel, where the file details that drive your rendered output get adjusted 8 Once your effect is built in Fusion, hit the Render button to bring up the Render Settings, confirm everything reads correctly, and hit Start Render. That writes the Fusion composition to the disk location, under the name you set back in step 3. Selecting two clips to send to Fusion 9 Up comes a Render Settings dialog, where you decide how the output renders — covering the Quality, Frame Range, and Size of the media you’re putting out. Happy with the defaults? Hit Start Render. A progress bar shows roughly how long the render runs. The Fusion User Manual holds more detail. 10 After the render wraps, save your Fusion project, come back to DaVinci Resolve, and the VFX Connect clip in the Timeline should now carry the new effect you built in Fusion.

### How Clips are translated into Node Trees

Over in Fusion, every clip you send shows up as a Loader node tied to that clip’s media on disk. Pick several clips and each one stacks over the clip just beneath it through a Merge node, which by default combines two images at once via an Over operator.

A pair of stacked clips, after being sent across to Fusion, shown within the Fusion node tree From that jumping-off point, you can drop in nodes (Fusion calls them Tools) to run operations of your own and craft richer effects and composites. The Fusion Reference Manual, found on the Support page of the Blackmagic Design web site, has more on working with Fusion.

### Altering VFX Connect Clips

Whenever you’d like to tweak the Fusion composition, reopen the project in Fusion, or right-click the VFX Connect clip over in the DaVinci Resolve Media Pool and pick VFX Connect > Open in Fusion. Back in Fusion, apply any edits you like, then re-render the clip to overwrite the media rendered earlier. Building new versions this route keeps every version’s Fusion project file and rendered output intact, so moving back and forth between them is always possible. On returning to DaVinci Resolve, you might have to right-click the VFX Connect clip you just opened and pick VFX Connect > Refresh so DaVinci Resolve picks up the rerendered media from Fusion properly.

### Creating Multiple Versions of Fusion Clips

To render a fresh version while holding onto the one before it, right-click the VFX Connect clip in the Resolve Media Pool and pick VFX Connect > Create New Version.

Creating a new version of a VFX Connect composite

That spins off a duplicate of the composite in Fusion, bumping the “\_v1” portion of the filename up so it leaves the earlier version of that composite untouched. Back in Fusion, apply whatever edits the composite needs, then re-render the clip to produce another piece of media for that version. The Saver node’s filename for the media you’re now rendering also bumps up on its own, with the “\_v1” chunk shifting to the next version number — say “\_v2” for the effect’s second pass.

In the Tools panel you can see the Saver node’s revised filename driving the rendered output of this new version Once you wrap up, you’re left with a Fusion Project file plus a matching rendered media file carrying the same version number. Back in DaVinci Resolve, Resolve spots on its own that several versions sit in the VFX Connect directory and serves up each one through a Choose Version submenu for VFX Connect clips over in the Media Pool.

### Switching Versions of VFX Connect Clips in DaVinci Resolve

With several versions of a VFX Connect clip already made, you can change which one DaVinci Resolve uses for that clip by right-clicking the VFX Connect clip in the Media Pool and picking the version out of the contextual menu’s VFX Connect > Select Version submenu.

Picking the active version out of the VFX Connect > Select Version submenu TIP: To swap versions on a VFX Connect clip sitting in a timeline, right-click that clip and pick Find in Media Pool.

### Sending a VFX Connect Directory to Another Machine

When you’re passing a VFX Connect directory to somebody on a different workstation, it pays to render self-contained media for the Fusion composition so handing over everything the compositing artist needs stays easy. Skip that and you’re left tracking down and supplying the related media files by hand. Self-contained media for Fusion can be rendered two ways:

- Tick “Open VFX Connect Clip” in the New VFX Connect Clip dialog and DaVinci Resolve by default renders each video clip you picked — plus every speed effect, transform, and Color page operation applied to those clips — in the Timeline Color Space.
- Haven’t opened the VFX Connect clip in Fusion yet? You can instead right-click any VFX Connect clip over in the Media Pool and pick VFX Connect > Render Media off the contextual menu.

With that handled, there are a couple of ways to pin down where the actual VFX Connect directory lives so you can copy it for whoever’s taking on the compositing for you.

- Within the New VFX Connect Clip dialog, enable the Custom Location checkbox, after which you hit the Browse button and settle on a spot where the resulting directory is simple to copy.
- Or right-click any VFX Connect clip in the Media Pool and pick Reveal in Finder to open that VFX Connect clip’s directory.

Because your DaVinci Resolve project tracks where the VFX Connect directory sits from the moment it’s made, leave it put — DaVinci Resolve expects to find it right where it left it. After your colleague finishes the compositing in Fusion, all they have to return is the Fusion Composition file (handy for keeping the set together) along with the media they rendered; copy both to the top level of the matching VFX Connect directory and you’re set. Do that and DaVinci Resolve should pick up the rendered media on its own and refresh those VFX Connect clips on your timeline.

### Creating Multiple Versions of Fusion Clips on Another Machine

Even after you’ve passed the directory the VFX Connect process built off to someone remote, they can still spin up multiple versions of the composite that DaVinci Resolve will manage. In Fusion, reach for the Save As command to store a duplicate of the Fusion project, bumping the “\_v1” segment of the filename to the next version number — “\_v2” for the composite’s second pass, say. Be sure the duplicated Fusion project saves alongside the original, in that very same directory, otherwise DaVinci Resolve won’t be able to locate it. With it created, edit this duplicate project file however you like. When you wrap up, pick the Saver node (sitting at the very end of the Fusion node tree) and revise the filename by bumping the V1 portion of the Filename field. As an example, a clip named Output_V1.mov becomes Output_V2.mov over in the Tools tab, then you render. Rendering a DPX image sequence instead? You’ll need to rename the folder wrapping the frames, so shift the filename from “.../fusion/OutputDirectory_V1/Output_00000000.dpx” to “.../ fusion/OutputDirectory_V2/ Output_00000000.dpx” to land a properly named second version.

### Updating VFX Connect Clips Using Render Media and Refresh

Alter a grade or effect on a clip living inside a VFX Connect clip and you’ll have to right-click that clip and pick VFX Connect > Render Media to re-render fresh media files for the Fusion project. Re-render a Fusion composite that overwrites media already pointed to by a VFX Connect clip in an open DaVinci Resolve project, and you might have to refresh that media reference within DaVinci Resolve. Easiest path: right-click any VFX Connect clip in the Media Pool and pick VFX Connect > Refresh.
