# Referenced composition behaviors and rules and adding Fusion composition generators

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md) / [Previous section](fusion-single-clip-composition-setup.md) / [Next section](mediain-timeline-clips-and-source-color-space.md)
<a id="source-adding-clips-from-the-file-system"></a> <a id="source-adding-clips-from-the-media-pool"></a> <a id="source-adding-fusion-composition-generators"></a> <a id="source-audio-with-media-pool-clips"></a> <a id="source-creating-a-fusion-composition-clip-in-a-bin"></a> <a id="source-finding-clips-in-the-media-pool-from-the-node-editor"></a> <a id="source-inspector-properties-of-mediain-nodes"></a> <a id="source-mediain-node-inputs"></a> <a id="source-referenced-composition-behaviors-and-rules"></a> <a id="source-resetting-a-fusion-clip"></a> <a id="source-using-fusion-transitions"></a> <a id="source-using-mediain-nodes"></a>

### Referenced Composition Behaviors and Rules

A handful of extra behaviors and rules are worth knowing when you put referenced compositions to use.

- Referenced compositions maintain the original source resolution of your clips.
- When you pick several clips, make certain each one shares some overlap with the top selected clip.

Lacking that overlap, the context menu command for building a referenced composition across layers won’t be offered.

- Make a project composition out of several overlapping clips and you get one composition tied to the top selected clip.
- The referenced composition brings along extra Media In nodes (one for each track). Media In 1 points to the top selected clip. The Media In nodes after it point to timeline tracks (layers) sitting beneath the top clip.
- Deleting a timeline clip leaves the composition it was tied to intact.
- Edit what sits inside a referenced composition’s track, and the matching Media In updates on its own to surface the new clips, edits, effects, and transitions.

From the timeline clip’s context menu, you can:

- Reset Reference Composition: To reset the composition. This affects all referenced clips.
- Unlink Reference Composition: Strips the composition reference off the selected clip. The composition stays put in the Media Pool, yet the clip’s effect is wiped. Handy when you mean to link to a different referenced composition.
- Find Reference Composition in Media Pool: Locates, within the Media Pool, the reference composition this clip belongs to.

NOTE: Referenced compositions don’t support clips that run at different frame rates or clips carrying speed changes.

### Adding Fusion Composition Generators

A Fusion Composition generator lives in the Generator category of the Edit page Effects Library. It’s handy for dropping an empty placeholder onto the Timeline that you plan to flesh out afterward on the Fusion page into a fuller Fusion composition. Here’s how to make a blank Fusion clip over on the Edit page: 1 Open the Effects Library and pick the Effects category. 2 Cut a Fusion Composition clip into the Timeline by whatever route suits you best. a) Drag a Fusion Composition clip onto the Timeline and you’ll get a clip running as long as the “Standard generator duration” preference, which defaults to 5 seconds. b) Or set In and Out points on the Timeline and drag the Fusion Composition clip onto any of the Timeline viewer’s editing overlays to carry out that kind of edit, inserting, overwriting, “place on top,” or ripple overwriting it into a particular spot on the Timeline for a particular length. 3 A fresh clip called “Fusion Composition” shows up on the Timeline. At first it reads as pure black in the Timeline viewer, being a blank composition holding nothing. 4 Rest the playhead above that clip and open the Fusion page. Because this composition is empty, the Node Editor holds nothing but one MediaOut node. From here, you can drop in whatever media, generators, and other effects you need.

### Creating a Fusion Composition Clip in a Bin

Inside any bin of the Media Pool you can spin up an empty Fusion Composition clip without ever making a Timeline. This route can be handy for building motion graphics or titles when no Timeline exists or when you expect to reuse the clip across several Timelines. To create a blank Fusion Composition clip in a bin: 1 Pick the Media Pool bin where you’d like the Fusion Composition saved. 2 Right-click an empty spot in the bin and pick New Fusion Composition. 3 Inside the New Fusion Composition clip dialog, fill in a Name for the clip, a duration, and a frame rate, then press Create. 4 The clip turns up in the bin. To open it in Fusion, take one of these routes:

- Double-click the Fusion Composition
- Right-click the Fusion Composition clip and pick Open in Fusion Page

### Resetting a Fusion Clip

To send a Fusion clip back to how it started out, right-click the Fusion clip on the Edit page Timeline and pick Reset Fusion Composition. You’re free to select several Fusion clips and reset them all in one go.

### Using Fusion Transitions

Certain Fusion transitions can be found in the Edit page Effects Library. With these transitions you can carry two clips plus the transition joining them into the Fusion Page. From there the transitions can be reworked and saved back onto the Edit page Timelines, or saved as a fresh, reusable Fusion Transition that turns up in the Edit Page Effects lIbrary. Here’s how to apply one and open it: 1 Open the Effects Library and pick the Video Transitions category. 2 Scroll down to the foot of the transition list, then drag any one of the Fusion Transitions onto a Timeline cut. 3 Right-click the Fusion Transition on the Timeline and pick Open in Fusion Page. 4 The Fusion page opens carrying two MediaIn nodes that stand for the two halves of the transitions. Those MediaIn nodes feed into a cross dissolve or a cluster of nodes that build the transition. From here you can rework the transition with masks or other nodes, then head back to the Edit page to view the outcome.

A Noise Dissolve Transition opened in the Fusion page.

To learn how to build your own custom Fusion Transitions that appear in the Effects Library, turn to Chapter 68, “Node Groups, Macros, and Fusion Templates,” found in the DaVinci Resolve Reference Manual, or to Chapter 6 over in the Fusion Reference Manual.

### Adding Clips from the Media Pool

On the Fusion page you can open the Media Pool and drag clips right onto the Node Editor to slot them into your node tree. Dragging a clip into a blank spot of the Node Editor turns it into one more MediaIn node, left unconnected, sitting ready for you to merge into your current composite in any number of ways.

Pulling a clip out of the Media Pool (Top), then dropping it into your composition (Bottom). TIP: When you drag a clip from the Media Pool over a connection line joining two other nodes in the Node Editor, that clip is added as the foreground clip on a Merge node. As you bring in further clips from the Media Pool, those clips join the composition, much the way Ext Matte nodes you put into the Color page Node Editor become part of that clip’s grade.

### Audio with Media Pool Clips

By default, audio from a clip pulled in via the Media Pool is silenced. Getting that Media Pool clip’s audio to play takes two steps. To hear audio from a clip brought in through the Media Pool, proceed like so: 1 Pick the clip in the Node Editor. 2 Over in the Inspector, open the Audio tab and choose the clip’s name from the Audio Track drop-down menu. 3 On the toolbar, right-click the speaker icon, then choose the MediaIn belonging to the Media Pool clip to solo its audio. The speaker icon contextual menu now lets you flip back and forth among all the MediaIn nodes.

### Finding Clips in the Media Pool from the Node Editor

Elaborate Fusion Compositions may hold several MediaIn nodes to keep tabs on. You can pinpoint the exact clip in the Media Pool tied to a MediaIn node by selecting that node, then picking Clip > Find Clip in Media Pool (Option-F).

### Adding Clips from the File System

There’s also the option to drag clips out of the file system straight onto the Node Editor. Do that and they get added to the currently selected bin of the Media Pool on their own. So if you keep a library of stock animated background textures and have just tracked down the one you want with your file system’s search tools, you can simply drag it right onto the Node Editor and put it to use immediately.

### Using MediaIn Nodes

On the Fusion Page, the MediaIn nodes form the bedrock of every composition you build. This section goes deeper into the controls on hand for tuning MediaIn and Loader nodes.

### MediaIn Node Inputs

A MediaIn node carries a single Effects mask input plus a single output. Where the Effects mask input is concerned, attaching a mask node such as a Polygon or B-Spline node produces an alpha channel on the MediaIn node. TIP: Hook up a mask node with no shapes drawn and that mask puts out full transparency, so the picture the MediaIn node outputs comes out uselessly blank. If you mean to rotoscope over a MediaIn node, first make a disconnected mask node, then with that mask node selected (its controls showing in the Inspector) and the MediaIn node loaded in the viewer, draw your mask. Once you’ve closed the shape you’re drawing, you can wire the mask node into the MediaIn node’s input, and you’re set.

### Inspector Properties of MediaIn Nodes

Exactly which Inspector options show up for your composition’s MediaIn nodes hinges on the way you brought the media in.
