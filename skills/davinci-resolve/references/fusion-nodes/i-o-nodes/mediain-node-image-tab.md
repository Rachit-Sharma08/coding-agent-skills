# Mediain node image tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Mediain node.
[Chapter index](INDEX.md) / [Previous section](loader-node-loader-import-tab.md) / [Next section](mediain-node-and-mediaout-node.md)
<a id="source-basic-node-setup-1"></a> <a id="source-i-o-nodes-part-2"></a> <a id="source-image-tab"></a> <a id="source-inputs-1"></a> <a id="source-mediain-node-image-tab"></a> <a id="source-mediain-node-introduction"></a> <a id="source-mediain-node-mi"></a> <a id="source-the-mediain-node"></a>

### MediaIn Node [MI]

### The MediaIn node

### MediaIn Node Introduction

NOTE: The MediaIn node turns up solely within DaVinci Resolve. The MediaIn node forms the bedrock of every composition you build inside DaVinci Resolve's Fusion page. In most situations it stands in for the Loader node that Fusion Studio relies on for bringing in clips. Four routes exist for adding a MediaIn node to the Node Editor.

- On the Edit or Cut page, park the playhead over a clip in the Timeline, then click the Fusion page button. The clip out of the Edit or Cut page Timeline shows up as a MediaIn node within the Node Editor.
- Drag clips out of the Media Pool into the Node Editor, which spawns a MediaIn node in the Node Editor.
- Drag clips straight out of an OS window into the Node Editor, which spawns a MediaIn node

in the Node Editor.

- Pick Fusion > Import> PSD while bringing PSD files into the Node Editor. Each PSD layer comes

in as a separate MediaIn node. NOTE: Even though a MediaIn tool sits in the I/O section of the Effects Library, it doesn't act as a route for bringing in clips. After clips arrive, whether out of the Media Pool, dragged off the OS window, or through the Import PSD menu option, the MediaIn node's Inspector is where you handle trimming, looping, and stretching the footage, plus assigning the source's color and gamma space.

### Inputs

The lone input on the MediaIn node is meant for an effect mask that crops the image the MediaIn pulls in. Effect Mask: The blue input takes a mask shape made by polylines, basic primitive shapes, paint strokes, or bitmaps coming from other tools. Wiring a mask here confines the source image so it surfaces solely within the mask. An effects mask gets applied to the tool once the tool has been processed.

### Basic Node Setup

The MediaIn node is, as a rule, the launch point for all composites carried out within the Fusion page of DaVinci Resolve. It holds the clip out of the Edit page or Cut page. Any clip pulled in out of the Media Pool likewise gets added as a MediaIn node.

A pair of MediaIn nodes: one drawn off the Edit page Timeline, the other off the Media Pool Inspector

### MediaIn node Image tab

### Image Tab

Whenever a clip arrives out of the Media Pool, or by a drag off an OS window, the Image tab on the MediaIn node carries controls for trimming, making a freeze frame, looping, and reversing the clip. You can additionally re-pick the clip the MediaIn points to on your hard drive. A subset of these controls is on hand whenever the MediaIn node gets pulled in out of the Edit or Cut page Timeline.

Global In and Out The Global In and Out handles, brought into play solely once a clip arrives by way of the Media Pool (or else an OS window), serve to fix this node's start and end inside the Fusion effect. Reach for Global In to fix the frame on which the clip begins, and Global Out to fix the frame on which the clip wraps up inside the comp's global range. The node yields no image on frames falling beyond this range. Should the Global In and Out values be lowered until the span between the In and Out values drops under the count of frames on hand in the clip. Fusion trims the clip on its own by nudging the Trim range control. Should the Global In/Out values be raised until the span between the In and Out values exceeds the count of frames on hand in the clip, Fusion stretches the clip on its own by nudging the Hold First/Last Frame controls. Stretched frames get shown within the range control by turning the color of the held frames green inside the control. So as to slide the clip through time or shift it across the project while leaving its length intact, rest the mouse pointer at the center of the range control and pull it across to the new spot, or else key the value in by hand inside the Global In value box.

- Clip Name: Surfaces the name of that clip.

Process Mode Reach for this menu to pick the Fields Processing mode that Fusion applies while loading the image. The Has Fields checkbox control inside the Frame Format preferences fixes the default option, plus the default height too. Options on offer take in:

- Full frames
- NTSC fields
- PAL/HD fields
- PAL/HD fields (reversed)
- NTSC fields (reversed).

The two reversed options bring fields in in the reverse order and thus leave the fields spatially swapped in time order and in vertical order alike. Media Source: Through this control you pick where media gets sourced from; the three options on offer take in: Timeline, Background, and Media Pool.

- Timeline: Links the clip out of the Edit Timeline (default).
- Background: This draws frames off the lower video tracks in the edit. While you toggle the Media

Source over to Background, the composited result of all the lower tracks becomes visible.

- Media Pool: Links the clip straight out of the Media Pool, sidestepping the Edit Timeline.

Layer: With Multilayer or Photoshop PSD files, this picks which layer in the file to use. For a Fusion Clip built out of several video layers on the timeline, this points instead at every layer's own index number. Trim The Trim range control serves to clip frames off the start or end of a clip. Nudge the Trim In to drop frames off the start, and nudge Trim Out to fix the clip's last frame. The values applied here act as offsets. A value of 5 in Trim In would take the fifth frame in the sequence as the start, passing over the first four frames. A value of 95 would halt frame loading past the 95th frame.

Hold First Frame/Hold Last Frame For the stated count of frames, the clip's first or last frame stays held thanks to the Hold First Frame and Hold Last Frame controls. Held frames join the loop whenever the footage gets looped. Reverse Tick this checkbox to flip the footage so the last frame plays first and the first frame plays last. Loop Tick this checkbox to loop the footage on through to the project's end. Whatever stretching of the clip via Hold First/Last Frame or shortening via Trim In/Out joins the looped clip. Source Color Space Lets you pick a color space for the image data this MediaIn node outputs.

- Auto: draws on the Timeline color space, or — where Resolve Color Management (RCM) is switched on — whatever color space RCM hands over.
- Space: Space gives you a Color Space drop-down menu to pick a particular setting from, while a “horseshoe” graph paints a visual picture of whichever color space you’ve chosen.

Source Gamma Space Lets you pick a gamma setting for the image data that this MediaIn node puts out. Having set the gamma curve type, you may opt to strip the curve away so as to steer a linear workflow.

- Auto: Draws on the Timeline gamma, or — where Resolve Color Management (RCM) is switched on — whatever gamma RCM hands over.
- Space: Gives you a Gamma Space drop-down menu to pick a particular setting from, while a visual graph paints a picture of whichever gamma setting you’ve chosen.
- Log: Brings up the Log Type drop-down menu, where you pick a particular log encoding profile. A visual graph paints a picture of the log setting you chose off the menu. For finessing the gamma output, further options are offered: Lock RGB, Level, Soft Clip, Film Stock Gamma, Conversion Gamma, plus a Conversion table.
- Remove Curve: From the material, the matching gamma curve gets stripped away — or a log-lin conversion gets run on it — which in effect turns it into a linear output space.
- Pre-Divide/Post-Multiply: When the need arises, lets you turn “straight” Alpha channels into premultiplied Alpha channels.
