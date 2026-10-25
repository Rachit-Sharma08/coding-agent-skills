# Video collage create background

Version: DaVinci Resolve 20.3 Reference Manual. Context: Video collage.
[Chapter index](INDEX.md) / [Previous section](video-collage.md) / [Next section](video-collage-layout.md) / [Video Collage](video-collage.md)
<a id="source-animating-tiles-and-advanced-layouts"></a> <a id="source-create-background"></a> <a id="source-create-tile"></a> <a id="source-turning-on-preview-layout-to-customize-the-layout"></a> <a id="source-video-collage-controls"></a>

### Create Background

Of the ways to build a split-screen with this effect, the Create Background option is likely the most straightforward. It produces a frame punched with holes, and behind those holes you can place several layers of video. Such clips live on tracks below the background clip in the Timeline, and you scale and position them within the holes through each clip’s own sizing controls in the Inspector (reachable as well via the on-screen Transform controls in the Viewer). The Video Collage effect goes on the uppermost superimposed video or still image clip in the Timeline, so that clip can act as the frame’s background.

Take the example below, where the Video Collage effect sits on the clip on track 5; beneath it in a stack are four more clips, each placed to land in one of the frame’s holes.

A clip stack producing a split-screen; in Create Background mode the Video Collage effect treats the uppermost clip as the background, and the clips stacked beneath are each set to slot into the holes cut in that top clip. With Create Background mode, assembling a split-screen of varied clips becomes simple, sparing you from resizing each one precisely to line up its edges and dimensions. The created frame’s width leaves a bit of room to shift and animate every individual clip inside the hole it peeks through. The outcome of the earlier example is shown below.

The finished split-screen, four clips set to peek through the holes in the upper “background” clip forming the frame; visible too are the onscreen controls tied to the track 4 clip, used here to place and resize it into position.

### Create Tile

Setting this mode up takes a touch more effort, since you have to build a layout inside one instance of the effect, yet it rewards you with more options by auto-transforming every video layer in your Timeline clip stack to match a layout of your own design. In Create Tile mode you’re best off editing a stack of superimposed clips in the Timeline, except that here any clip you mean to use as the background should sit at the bottom of the stack.

A clip stack building a Tile-mode split-screen, with the lowest clip slated to serve as the background. Next, drop the Video Collage clip onto the uppermost clip, then switch the Workflow drop-down menu over to Create Tile. Right away the current layer snaps into the first rounded tile of the default four-tile layout. To keep things clear, video tracks 4, 3, and 2 have been silenced so the current clip — now a tile — stands out against the bottom clip serving as this arrangement’s background.

The uppermost clip configured to form the layout’s first tile; with video tracks 4, 3, and 2 switched off, the top clip reads clearly against the bottom clip standing in as the background.

In the end, Paste Attributes is what copies this effect onto each Timeline clip meant to occupy a tile, and once you decide which clip belongs in which tile, the arrangement falls into place. First, though, the layout needs tailoring. To see the whole layout while you refine it, switch on the Preview Layout checkbox in the Inspector. Doing so sketches out where every tile will land under the present layout. With that preview in front of you, make whatever adjustments you wish before copying this plugin to the rest of the clips in the stack.

### Turning on Preview Layout to customize the layout

Once Preview Layout is on, the Layout controls underneath let you set the count of tile columns and rows, stagger the tiles horizontally or vertically, round or square each one by an adjustable degree, and tweak the margins and spacing. That makes spinning up a broad assortment of symmetrical layouts quite painless. For this example, we’ll build a layout of one row and three columns, staggered vertically.

The freshly tailored layout of ours, sitting beside this effect’s Inspector controls With that handled, we’ll switch Preview Layout off to concentrate on how the current clip fits the layout, and it’s plain it doesn’t quite sit right in the box. Click the Tiles button in the Inspector. Up come the Tile-specific controls, the Resize Content controls among them. Click the disclosure control to expand them, then work the Pan, Tilt, and Zoom controls until this image fills the tile edge to edge.

The Inspector’s Tiles controls with Preview Layout switched off, letting us zero in on shaping the present tile Take note as well of the Active Tile drop-down menu, which does two jobs. To start, it fixes which tile holds the current clip — something that matters down the line when you apply this effect across several superimposed clips. Beyond that, it also picks which tile you go on to refine through the Inspector’s Tile-based controls. Where called for, tiles can be styled one by one. By default the Manual Tile Management checkbox stays off, letting DaVinci Resolve refresh the tile entries in the Active Tile drop-down menu on its own so they match the number of grid positions (or grid nodes) your chosen rows and columns produce, with no effort on your part. That’s the smoothest path for simple symmetrical layouts. Flip Manual Tile Management on, though, and you can add and remove tile positions by hand, unlocking further options. For the moment we’ll keep it off.

(Left) The Active Tile drop-down while Manual Tile Management sits off; (Right) the Active Tile controls once Manual Tile Management is on, now showing the extra manual tile management controls At this point we’ve built a custom overall layout and shaped the stack’s top clip to fill the layout’s first tile. The job now is to apply this effect to the next two clips in the stack (recall the bottom clip becomes a background, so it doesn’t need this plugin). In the Timeline, select the top clip carrying the effect and press Command-C to copy it. Next, select the following two clips, right-click one, and pick Paste Attributes (Option-V). Once the Paste Attributes window opens, tick the Plugins checkbox under Video Attributes and click Apply. Those two clips vanish as the Video Montage effect lands on them and they settle into Tile 1, just as the top clip did.

Paste Attributes spreading the effect copied off the top clip onto the rest of the clips in this arrangement To slot each clip into its proper layout tile, go through the clips in the arrangement one at a time: open the Inspector’s Effects panel, click the Tiles button there (if you need to), and assign each clip to the next free tile via the Active Tile drop-down menu. Here the top clip occupied Tile 1, so the second clip down goes to Tile 2 and the third clip down to Tile 3.

Assigning the Active Tile for each layer in the Timeline TIP: Switch on the Open FX Overlay of the Timeline Viewer and every tile gains an overlay, so a click on a tile in the Viewer makes it the Active Tile. You’re free to reshuffle which clips land in which tiles through this control, though for now we’ll keep it straightforward. As you proceed, each tile fills in and the finished layout emerges, the background clip sitting behind it all. Where needed, the Resize Content controls (in Tiles mode) let you rescale each tile’s contents for a better fit.

The layout as it stands, every clip in the stack mapped to its own separate tile

NOTE: Suppose you’ve customized a layout, pasted attributes across the other clips meant for it, and given each clip its slot — and then you decide a Globals layout control needs changing. You’ll have to repeat the whole cycle: copy the updated effect, paste attributes onto the other clips, and re-slot each one into its proper layout position so the change carries across to them too. Those, then, are the broad workflows behind the Video Collage effect. Plenty more is possible, naturally, but this is the foundation for putting together your first layout.

### Animating Tiles and Advanced Layouts

Among the Video Collage effect’s stronger features is how quickly and simply it lets you build animated intros and outros for every tile. You can let these run fully automated over a duration of your choosing, or set their duration by keyframing it yourself. Every animation can be eased automatically, and motion blur is available for the Fly, Shrink, and Rotate animations. Used in Create Background mode, these controls animate the transparent holes — through which the background’s other clips show — to “open or close” and reveal what lies behind. Used in Create Tile mode, it’s the tile itself and its contents that animate, flying, shrinking, rotating, and/or fading into or out of view.

Through the Tile Animation controls you can generate automatic Intro and/or Outro animations. On top of that, while in Tiles mode you can keyframe the Mute parameter, the Start and End Column and Row parameters, the Tile Styling and Drop Shadow parameters, and other tile traits — one at a time or all at once. The Start and End Column and Row parameters in particular let you make tiles that stretch across several grid positions and shift tiles from one grid position to the next. Skip the keyframing and you can still build more layout varieties featuring asymmetric mixes of big and small tiles. Add keyframing and you can readily craft intricate grid-based animations that march tiles from spot to spot and have them grow and shrink to swallow neighboring tiles in the layout, all with very little keyframing.

The Tile Animation controls generate automatic Intro and/or Outro animations. Bear in mind that, when several instances of the Video Collage effect ride on superimposed Timeline clips, once your overall layout is set and Paste Attributes has copied a given instance of this effect with that layout onto the remaining clips, all you need do is keyframe each tile instance inside whatever clip carries it. What’s more, because Intro and Outro animations cover a clip’s full length, you can stagger each Intro and Outro animation simply by staggering the clips in the Timeline.

TIP: Should you alter the length of clips in a stack that’s producing a Video Collage effect, the Synchronize Keyframing controls in Globals mode can shift every keyframe on that instance of the Video Collage effect by an equal amount. You could reach the same result by pulling up every Video Collage parameter’s keyframe track or Curve Editor in the Timeline and dragging the keyframes manually, but this offers a faster shortcut.

### Video Collage Controls

What follows is a thorough rundown of every parameter the Video Collage effect provides.

- Workflow: Sets what Video Collage puts out, according to how you plan to use it. Create Background: Yields a frame full of holes, behind which you can place separate video layers to show through.

Create Tile: Yields one tile, transformed and styled to act as a single piece of a multi-tile layout

- Preview Layout: Switching Preview Layout on gives you a graphical preview of the whole layout and how the tiles knit together. Under Create Tile mode, it lets you dial in the layout’s appearance before you copy the clip and use paste attributes to spread this effect across the rest of the video layers you want gathered into a split-screen.
- Globals/Tile buttons: Toggle between the Globals controls, which surface tools for adjusting the overall layout, and the Tiles controls, which let you pick the currently active tile and style it.
