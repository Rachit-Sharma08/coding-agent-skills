# Dynamic keyframes dynamics and static keyframes marks

Version: DaVinci Resolve 20.3 Reference Manual. Context: Keyframing in the color page.
[Chapter index](INDEX.md) / [Previous section](introduction-to-keyframing-and-keyframe-editor-interface.md) / [Next section](resolvefx-keyframe-tracks-and-sizing-keyframing-tracks.md)
<a id="source-corrector-keyframing-tracks"></a> <a id="source-dynamic-keyframes-dynamics"></a> <a id="source-keyframed-nodes-have-a-badge"></a> <a id="source-mixing-and-converting-dynamic-and-static-keyframes"></a> <a id="source-no-dynamic-interpolation-following-the-static-keyframe"></a> <a id="source-static-keyframes-marks"></a> <a id="source-try-creating-keyframed-changes-in-a-separate-node"></a> <a id="source-using-specific-keyframing-tracks"></a>

### Dynamic Keyframes (Dynamics)

The keyframe you'll lean on most is the Dynamic keyframe, and it's the variety meant for animating a transition from one state into another. If a grade must brighten gradually to offset shifting light, for example, Dynamic keyframes are the tool. Almost any parameter or control on the Color page accepts keyframes, though bear in mind the Interface controls won't animate alongside the dynamically keyframed changes underway. Rather, the visible Interface controls tied to keyframed changes snap from their starting spot at one keyframe to their ending spot once the playhead arrives at the following keyframe. Curves can make this especially baffling, since they too can be interpolated with Dynamic keyframes, the same as any control or parameter. Simply remember the underlying settings really are animating, despite the controls staying put. To animate a node using Dynamic keyframes: 1 Within the Keyframe Editor's Timeline ruler, drag the playhead to whichever frame ought to kick off a change. 2 Drop a Dynamic keyframe onto that frame through one of these methods:

- Choose Mark > Add Keyframe (Command-[).
- Switch on the Auto Keyframe button for the track you intend to animate in the Keyframe Editor. Dynamic keyframes are diamond-shaped.

3 If needed, tweak your clip at this opening spot of the animated change. With Auto Keyframe running, you'll have to make a tweak before a keyframe gets created.

4 Next, slide the playhead to the frame marking the second spot of the animated change you're building, and lay down another Dynamic keyframe if you're placing them by hand, or do another tweak if Auto Keyframe is active. 5 Once that second keyframe exists, apply whatever adjustments the clip needs to reach the final look you're after. From there, scrubbing from the first keyframe through to the second ought to reveal a smooth animated transition from the first adjustment into the second. After you wrap up, be sure Auto Keyframe gets switched back off if it had been on.

### Static Keyframes (Marks)

Static keyframes, also called marks, are the keyframes you reach for to produce sharp, single-frame jumps from one state into another. They're commonly placed to flag the edit points dividing one shot from the next where several shots live inside a single clip. That said, Static keyframes also help in any case calling for an instant switch from one setting to another, like building a lightning effect.

Static keyframes are round. To automate a node using Static keyframes: 1 Locate the frame where the sudden change should happen, and lay a keyframe at that frame with one of these methods:

- Choose Mark > Make Static Keyframe (Command-]).
- Static keyframes (marks) are round. 2 Slide the playhead to any frame ahead of the keyframe to alter the whole stretch of the clip running up to it, or slide it to any frame past the keyframe to alter the whole stretch of the clip that follows. The playhead need not sit right over the keyframe, though if it does, you'll be tweaking the clip's second portion.

NOTE: When Static keyframes are automating grading changes across several shots living inside a single clip, remember you can't tack on nodes from one keyframe to the next the way you could had you cut the clip apart on the Edit page.

### Mixing and Converting Dynamic and Static Keyframes

Generally, building several animated changes inside a clip means reaching for all Dynamic keyframes. Likewise, a run of sharp changes means all Static keyframes. Still, blending Dynamic and Static keyframes is allowed, provided you keep these rules in mind:

- Place a Dynamic keyframe just rightward of a Static keyframe: No interpolation happens going from the Static keyframe over to the Dynamic one. Flip it around, though, and dropping a Static keyframe rightward of a Dynamic keyframe does interpolate.

### No dynamic interpolation following the static keyframe

Should you create the wrong keyframe type by mistake, swapping it for the one you wanted is simple. To turn one keyframe variety into the other: 1 Select the keyframe you'd like to convert by clicking it. 2 Right-click that selected keyframe and pick either Change to Dynamic Keyframe or Change to Static Keyframe.

### Try Creating Keyframed Changes in a Separate Node

Worth remembering: keyframed changes don't have to live inside the very nodes handling your other adjustments. To add some automated changes while leaving the nodes you've already tuned untouched, just spin up a fresh node to hold your keyframed work. That way, if the outcome disappoints, or you end up hopelessly snarled in an absurdly intricate web of keyframes, resetting either the keyframes alone or the whole node stays easy and leaves the rest of your grade alone.

### Keyframed Nodes Have a Badge

Any node carrying keyframed parameters shows a keyframe badge over in the Node Editor so it's quick to spot. Keep in mind those badges hold off appearing when you merely add a keyframe and only surface once a real keyframed adjustment is in place.

Keyframed nodes display a badge in the Node Editor.

### Using Specific Keyframing Tracks

When you simply work in the Color mode of the All/Color/Sizing command for keyframing, every parameter on the active node picks up a keyframe each time you apply just one. Often that's more than you need, though, in cases where a single setting or a small group of settings is all that calls for keyframing. You might, for instance, want to keyframe a color tweak to shift color temperature and brightness as the camera sweeps past a window, while leaving the Windows palette controls unkeyframed because you'd rather tune them on their own. The way to do that is to open a Corrector track and reveal the keyframing tracks inside.

Individual keyframing tracks within a Color Corrector node Keyframing tracks make it possible to keyframe distinct groups of similarly behaving parameters apart from each other. One keyframing track, for example, handles every color adjustment parameter, while another oversees the parameters housed in the Qualifier palette. To reveal a node's keyframing tracks:

- Click the disclosure triangle beside the number of whichever node you're keyframing.

To keyframe an individual keyframing track manually: 1 Apply whatever tweaks the active node needs, then click its disclosure triangle so its keyframing tracks appear. 2 In the Keyframe Editor, move the playhead to the spot the first keyframe should occupy; now right-click within the keyframing track you mean to animate and choose Add Static Keyframe or Add Dynamic Keyframe (a Dynamic keyframe is used for illustration here). On that keyframing track, a keyframe materializes right where the playhead sits. 3 In the Keyframe Editor, advance the playhead to wherever the following keyframe should land. Right-click inside that same keyframing track once more, picking either Add Static Keyframe or Add Dynamic Keyframe (a Dynamic keyframe is shown for this illustration).

Keyframing only the Circular Power Window by way of its own dedicated keyframe track Now you're free to make whatever changes the controls overseen by the keyframing track you keyframed require, building the animated effect you need. TIP: Individual keyframing tracks can also be animated through automatic keyframing, which gets covered more fully further along in this chapter.

### Corrector Keyframing Tracks

Every parameter that governs color and contrast control adjustments, plus assorted effects, Power Windows, and other tweaks, gets organized into various sub-tracks living within the Corrector track.

- Linear Win: Controls parameters corresponding to the Linear window.
- Circ Win: Controls parameters corresponding to the Circular window.
- Polygon Win: Controls parameters corresponding to the Polygon window.
- PowerCurve: Controls parameters corresponding to the PowerCurve window.
- Gradient Win: Controls parameters corresponding to the Gradient window.
- Color Corrector: Controls all parameters found in the Camera Raw, Color Wheels,

Primary Controls, RGB Mixer, and Curves palettes.

- Qualifier: Controls all parameters in the Qualifier palette.
- Defocus: Controls all parameters in the Blur and Key palettes.
- NR: Controls the Spatial and Temporal Noise Reduction and Motion Blur parameters

found in the Motion Effects palette.

- Open FX: Governs every parameter belonging to whatever OFX plugin sits on the active node.
- Node Format: Governs every parameter of the Sizing palette's node sizing mode tied to

the current node.
