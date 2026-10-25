# Magic mask v1 legacy version identifying more than one person

Version: DaVinci Resolve 20.3 Reference Manual. Context: Magic mask v1 legacy version.
[Chapter index](INDEX.md) / [Previous section](magic-mask-v1-legacy-version-stroke-list.md) / [Next section](legacy-magic-mask-stroke-list.md) / [Magic Mask v1 (Legacy Version)](magic-mask-v2-and-magic-mask-v1-legacy-version.md)
<a id="source-about-hats"></a> <a id="source-adding-negative-strokes-to-the-reflection-to-remove"></a> <a id="source-adding-strokes-to-guide-mask-creation"></a> <a id="source-creating-a-soft-edged-hair-mask"></a> <a id="source-dealing-with-accessories"></a> <a id="source-dealing-with-hair"></a> <a id="source-identifying-more-than-one-person"></a> <a id="source-using-magic-mask-as-a-garbage-matte"></a> <a id="source-using-matte-finesse-controls"></a>

### Identifying More Than One Person

Within either Person or Feature mode, you may add strokes that mark more than one person, or the features of more than one person. No special trick is involved; just draw strokes over each person you want to isolate, or over the matching feature of each person you want to include (say, drawing a stroke across three people's faces while in Face mode).

Strokes drawn over several people will isolate them all together inside a single mask.

### Using Matte Finesse Controls

Plenty of times a mask that looks troublesome can be salvaged with the Smart Refine and Matte Finesse controls over on the right of the Magic Mask palette. When the mask misses by only a few pixels and the color change you have in mind is fairly gentle, you can likely lean on Blur Radius and In/Out Ratio to build a soft edge that tapers off right at the subject's outer boundary (avoiding any halo) to carry your adjustment.

(Top) The initial mask's hard edges don't quite reach the edges of the woman's arm closely enough for a subtle adjustment, (Bottom) Calling on the Blur Radius and In/Out Ratio controls to form soft edges that stay within the subject and yield a usable mask

### Using Magic Mask as a Garbage Matte

When a person's outer edge isn't being picked up tightly enough for Magic Mask to deliver a usable result for a more drastic color change, you are generally better served by growing the result into a snugly fitting garbage matte, then isolating the person or features through other means, such as a keyer in the Qualifier palette. Even here, you will find that

Magic Mask usually beats rotoscoping a reasonably tight garbage matte over a moving figure with windows.

(Top) The initial mask doesn't sit close enough to the edges for a drastic adjustment, (Bottom) Reaching for the Mode/Shape/Radius/Iterations/Blur Radius controls to grow the matte into a garbage matte suited to other keys

### Dealing With Hair

Wispy or frizzy hair, stray strands flung back, and the tips of dreadlocks or heavily moussed hair that taper to points will frequently call for extra care with this tool. Bear in mind that the Magic Mask tool isn't built for soft, translucent mask edges the way a keyer is. For hair that hangs loose and free, you can often coax out a workable result by using the Matte Finesse controls to grow a softened copy of the matte until it covers the whole hairstyle. Should that bleed too much into the edges of other features on the subject you are isolating, build a dedicated hair mask in Features mode by drawing Hair strokes. From there, the Matte Finesse controls on the right of the palette let you fashion softened edges that sit well against the outer boundary of the hairstyle you are isolating.

### Creating a soft-edged hair mask

From here you might attempt separate color adjustments across two distinct correction nodes, one handling the subject's hair and another using Magic Mask to isolate everything except the hair. Or, if you would rather have one matte that isolates the whole subject, bring in extra instances of the Magic Matte tool (one to a node): let one node isolate just the face and body minus the hair, and a third node isolate the entire subject but with a very soft edge. After that, a Key Mixer node can merge all these masks together with the original hair mask you made, feeding a complete key into yet another node that carries out the correction.

(Left) Nodes 2, 3, and 4 build three separate masks that a key mixer combines and routes into the Key input of Node 5 for an adjustment, (Right) The end result of this three-mask method. Soft-edged hair can be tough, yet Magic Mask shines on plenty of elaborate hairstyles full of intricate shapes and hair accessories, jewelry and ribbons included. The stylized coiffures seen in European and Chinese period movies and shows, for instance, give the DaVinci Neural Engine no trouble whatsoever, all the more so because such styles are typically bound tight with no wispy hair. Lopsided hairstyles may need additional strokes to pick up hair that runs noticeably longer on one side of the face. The same can hold for offbeat styles, like hair molded into pronounced sculptural forms. Finally, tight braids that lay bare scalp skin also test the kind of hard masks Magic Mask turns out, so in those cases you are better off treating Magic Mask as a garbage matte and bringing in a keyer to craft a detailed soft mask.

### About Hats

Magic Mask copes with a remarkably broad range of hats drawn from every era. Trouble can arise from a hat's tassels or fine touches like feathers (in our tests, that feather perched on Errol Flynn's Robin Hood cap couldn't be brought in reliably, even while the cap itself posed no difficulty). On top of that, veils attached to hats may or may not register easily, though one more stroke usually clears the issue up.

### Dealing With Accessories

Objects a person holds, handkerchiefs or umbrellas say, are best handled in Object mode. Jewelry and watches raise a particular difficulty, since they tend to be so slim and small that leaving them out is hard, yet depending on the adjustment you intend you may not want them in at all. How things turn out depends on how thick the items are and how your subject is framed, but on the whole you will probably fare better by just adding a stroke or two to fold these items into the isolation, given that dropping fine detail like a necklace can get messy.

### Adding Strokes to Guide Mask Creation

What follows are a few pointers on drawing strokes to analyze the image. To pick out people, begin with one short positive stroke (blue) placed over the center of the face or body.

Drawing the first stroke to mark an entire person Based on what you get, you may need further strokes to tell an arm or frizzy hair apart from the background. When adding a stroke to an arm or hair, keep it off the very edge; the aim isn't to outline the subject but to use strokes inside the subject's body to spell out which features belong to it and which do not.

Adding a stroke to the arm so it gets included too As you go, fight the temptation to pile on strokes. A single one may be all it takes, or perhaps two or three, but going past five strokes on any one subject or feature is liable to create more trouble than it cures.

### Adding negative strokes to the reflection to remove

For faces, open with one short stroke across the middle of the face, running along the nose, or from the eyes down to the lips. Depending on what comes back, you may want more strokes to mark the chin, a beard, or to set the forehead apart from wispy hair.

Drawing strokes to mark a face; note that extra strokes are required to take in the beard. A sound approach is to lay down a single stroke and then track it across the clip's full length (covered further along in this section). Watching the whole clip reveals which portions of the mask might act up, and that tells you where to drop additional strokes so the person reads more clearly against the background, tidying up the resulting mask. Each time you add a stroke, track it too and observe how it goes. If you catch background areas wrongly slipping into the mask, drop a negative stroke (red) to signal that those image regions ought not be isolated. Short strokes, longer ones, and zig zags all serve backgrounds well. Because strokes merely nudge the analysis to refresh the mask, you can experiment with different stroke types to discover what serves best, then delete any stroke that fails to deliver. Just as with positive strokes, never use more than are strictly required to reach the result you are after.

(Left) The microphone wrongly read as part of the woman being interviewed, (Right) Drawing negative strokes to brand the microphone as background, sweeping a zig-zag pattern to tag the whole microphone

In much the same way, when you are isolating features like a face and some other feature, hair perhaps, keeps intruding, you can place a negative stroke on the hair to declare it no part of the face. If the resulting mask contains a “hole” that actually belongs to the background rather than the subject, try drawing a stroke that links that hole back to the rest of the background.

Drawing strokes to join the background to itself, clearing away part of the mask that doesn't belong to the person If an “island” turns up in the mask that genuinely belongs to the subject and not the background, try drawing a stroke across the island that ties one solid stretch of the mask back to itself.

Drawing strokes to fill an island within the subject being isolated Naturally, pulling a mask out with strokes is only the opening stage of making a usable mask. The Quality, Consistency, and Smart Refine controls let you tune the image's stroke analysis to strike the best balance between performance and quality for the mask type you need. Those controls work in close partnership with whatever strokes you draw to pull out a mask. A bank of Mask Finesse controls then lets you work the resulting mask, reshaping and softening it to better fit whatever adjustment you are attempting. Each of these controls was covered earlier in this section.
