# Connecting motion track data to match move and offsetting the position of a match moved image

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using the tracker node.
[Chapter index](INDEX.md) / [Previous section](positioning-the-tracker-onscreen-control.md)
<a id="source-connecting-motion-track-data-to-match-move"></a> <a id="source-offsetting-the-position-of-a-match-moved-image"></a>

### Connecting Motion Track Data to Match Move

Now that a successful analysis is in hand, the time has come to put it to work building the Match Move effect. To smooth this along, we’ll double-click the tracker’s name within the Tracker List of the Inspector, and enter a fresh name that’s simpler to keep track of (heh). Giving your trackers your own names makes a given tracker easier to track down across later contextual menus and lets you stay clear on which trackers are following which subjects as your compositions grow ever more involved.

Renaming a tracker to make it easier to find

Now the moment has come to wire the track we just built to the text so it starts moving. After loading the Merge1 node into the viewer so we can see the text against the overall composite we’re building, we’ll select the Text1 node so its parameters open up within the Inspector, then click the Layout panel icon (the second button from the left) to reveal the Layout controls, which are the text-specific transform controls used for placing the text object within the frame. These are the very controls you work when the Text node onscreen controls are used to reposition or rotate text.

Shown here within the Layout panel are a Text node’s Layout controls The Center X and Y parameters, though each can be adjusted on its own, also act together as a single target for the purpose of hooking up to tracking to set up match moving animation fast. You arrange this through the contextual menu that pops up when you right-click any parameter inside the Inspector, which holds an assortment of commands for adding keyframing, modifiers, expressions, and other automated routes to animation, hooking up to motion tracking among them. By right-clicking anywhere along the line of controls for Center X and Y, we can pick Connect To > Tracker1 > Bridge Track: Offset position off the contextual menu, which ties this parameter to the tracking data we analyzed before.

Wiring the Center X and Y parameter onto the Bridge Track: Offset position motion path that we just analyzed Right away, the text shifts so its center position lines up with the center of the tracked motion path at that frame. That tells us the center of the text is being match moved onto the motion track path.

The text now aligns with the motion track coordinate

### Offsetting the Position of a Match Moved Image

In fact, we’d like to offset the match-moved text so it rides higher within the frame. To pull this off, we pick the Tracker1 node once more and use the Y Offset 1 dial control to nudge the text upward, since any change we make now to the Bridge Track dataset carries over to the center of the text that’s tied to it.

Leaning on the X and Y Offset controls within the Tracker1 node to shift where the text layer sits relative to the tracked motion path The offset we build shows up as a dotted red line that lets us see the real offset the X and Y Offset controls are producing. This, in fact, is exactly why we hooked into the Bridge Track: Offset position option earlier.

The text shifted away from the tracked motion path; that shift reads as a dotted red line within the viewer

Now, playing through this clip lets us watch the text move right alongside the bridge.

A pair of frames showing the text match moved so it tracks the bridge throughout the shot
