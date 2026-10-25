# Magic mask v1 legacy version stroke list

Version: DaVinci Resolve 20.3 Reference Manual. Context: Magic mask v1 legacy version.
[Chapter index](INDEX.md) / [Previous section](magic-mask-v1-legacy-version-the-magic-mask-interface.md) / [Next section](magic-mask-v1-legacy-version-identifying-more-than-one-person.md) / [Magic Mask v1 (Legacy Version)](magic-mask-v2-and-magic-mask-v1-legacy-version.md)
<a id="source-choosing-what-to-isolate"></a> <a id="source-features-mode"></a> <a id="source-mask-adjustment-controls-and-matte-finesse"></a> <a id="source-object-mode"></a> <a id="source-person-mode"></a> <a id="source-stroke-list"></a>

### Stroke List

As soon as you begin drawing strokes that mark features for mask generation, those strokes show up in this Stroke list.

- Stroke list header: Sitting on the left side of the Stroke list, the header holds controls for selecting, enabling/disabling, and naming each stroke, should you want that degree of organization. Right-click any stroke's header and you get controls to Reset Tracking Data and to switch the mask type between feature and not feature.
- Under Object mode, you simply get a flat list of strokes, each one helping to define either the object you intend to isolate or the background.
- Under Person mode, you likewise get a flat list of strokes, each one helping to define either the person you intend to isolate or the background.
- Under Features mode, an extra drop-down menu sets which particular feature a guidance stroke is meant to mark. The strokes are arranged hierarchically by their matching feature, so every Face stroke, for instance, sits beneath a Face title bar. Each feature's title bar carries a toggle that flips that feature off and on, and turning it off withdraws that feature's input to the overall mask being built.
- Stroke timeline area: A Timeline ruler lays out the length of the clip you are currently masking. Every stroke in this list owns a track showing how many of its frames have been tracked, and as you track a stroke its track fills with colored bars marking which frames now hold tracking data.

Strokes marking a person or object get blue tracks, whereas strokes marking what isn't the feature get red ones. This timeline lets you keep tabs on which strokes still need tracking and reshape the tracking data as required to land a usable result.

### Mask Adjustment Controls and Matte Finesse

Two groups of controls exist for refining whatever mask the Magic Mask palette outputs. The upper group governs how the mask is built from the analysis data, letting you tune the mask result according to the image's traits. Among them: Quality: A pair of options balances quality against performance. Faster turns out a lower-quality mask in a hurry, fine for garbage matting, while Better turns out a more detailed, higher-quality mask at greater processing cost. Smart Refine (Person Mode): This control grows or shrinks the resulting mask off the image analysis, in such a way that growing the mask won't push it far into neighboring image areas that aren't joined to that person. The operation adds no softness; rather, it scales the overall mask this palette produces up or down. Here 0.5 is unity, 0 is the most expansion, and 1 is the most contraction. Refine Range (Object Mode): This control tunes the resulting mask's sensitivity off the image analysis, letting you dial the mask to take in more or less of the chosen object. Here 30 is unity, 100 is the greatest sensitivity, and 1 is the least. The second group of mask controls works on the mask once it has been generated. Most of them are the very same Matte Finesse controls found in the Qualifier palette, handy for sorting out trouble masks or for softening edges when you need a more feathered outcome. For fuller detail on the Matte Finesse controls, turn to Chapter 137, “Secondary Qualifiers.”

One more control, though, belongs to the Magic Mask palette alone. Consistency: Once you have tracked each stroke so it follows the subject across the clip's length, this setting decides how much temporal smoothing is needed to tame jitter along the resulting mask's edges in low-confidence zones, such as frizzy hair or see-through clothing. Crank it up and more smoothing reaches the mask edges, but at higher processing cost and with a possible loss in how tightly the mask tracks motion in the image. Dial it down for speed and accuracy, accepting that more edge jitter may slip into the mask, which can prove distracting in the final adjustment you are making. The parameter starts at 0, so your opening pass with Magic Mask always launches from the most accurate (and possibly liveliest) use of this feature's analysis.

IMPORTANT: For Consistency to work as intended, a stroke must span at least a handful of frames. That means tracking each stroke so it follows the camera's and subject's motion, which lengthens the stroke's duration. Since Consistency sets out to wipe one- or two-frame “noise” from the mask's shape, strokes that last only briefly may find their effect canceled out entirely.

### Choosing What to Isolate

The pages here go deeper into the various isolation choices on offer and suggest where each one works best.

### Object Mode

Of all the options, Object mode is the simplest to settle on. In short, turn to it for any subject that isn't a person. Things like cars, pets, and food all make solid candidates for Object mode. The one clear exception is clothing such as shirts, hats, and the like worn by a human, since worn garments come out far better when isolated in Person mode instead. Positive strokes in Object mode grab regions of comparable contrast and color, which lets you stitch intricate shapes together. As a rule, an object demands more strokes to actively pin down than a person does, owing to the wider assortment of shapes at play. Negative strokes in Object mode carve away the parts of the object you would rather not isolate, whether that is something easy like pulling a car's wheels out of a mask or something trickier like dropping certain books from a mask of a bookshelf.

### Person Mode

With Person chosen, each stroke you lay over somebody works to isolate that person's whole body, or as much of them as the screen reveals. That sweeps in every garment they have on: a shirt or pants, shorts, a dress or skirt, a bathing suit, knickers, jumpsuits, a hat, footwear, and even armor or a space suit (yes, we have tried both), whatever the case. Clothing is, for the most part, correctly read as part of the isolation mask you are building. That said, very loose, flowing garments may call for an extra stroke or two to be recognized in busy visual compositions. Negative strokes, while you are in Person mode, flag everything that isn't the person being isolated, keeping the background and/or any other people out of the mask being built. They aren't required, though; reach for a negative stroke only when you spot a problem, such as a chunk of background sneaking into the isolation mask.

### Features Mode

Choosing Features brings a drop-down menu to the top of the Stroke list. Your first step is to pick from that menu the feature you want to isolate, after which you draw strokes over the chosen feature (face, hair, and so on) you mean to isolate. Every feature's set of strokes can be switched on or off to fold that feature into the overall mask under construction.

- Face: Isolates only the face and ears, eyes and glasses included, while leaving out the hair and the neck (which counts as part of the torso). Facial hair, big beards especially, usually falls outside an opening stroke placed on bare facial skin, so you can keep to just the skin if that is what you want; a further stroke on the beard, however, brings it into the face isolation.
- Hair: Isolates the hair alone, ending at the bangs and ears and shedding as much of the face as it can. Curly, frizzy, or wispy hair yields oversized masks that try to take in as much hair detail as possible. This tool won't produce fine transparency. Delicate, irregular hair detail can give rise to jittery edges, though the Consistency control can rein that in.
- Torso (Exposed Skin): Isolates the bare skin sitting above the waist and below the face, leaving the arms out. Enable this selection when you need to isolate the neck, neckline, and whatever part of the chest shows through v-necks, plunge necks, tank tops, crop tops, or bikini tops.
- Clothing (Top): Whatever clothing sits above the waist; bare skin is left out.
- Clothing (Bottom): Whatever clothing sits below the waist; bare skin is left out.
- Arms (Exposed Skin): The bare stretches of arms or hands. Shirt and dress sleeves are left out,

as are sun sleeves.

- Shoes: Shoes of most styles will be isolated.
- Legs (Exposed Skin): Isolates the bare skin below the torso, while skipping socks and leggings.
- Hat: Hats of most styles will be isolated, though slim accessories like trailing ribbons or

feathers may be left out. Bear in mind that whichever feature you have set out to isolate, you can always lay down negative strokes to drop other parts of the person or their clothing that are wrongly creeping into the mask. IMPORTANT: While drawing strokes in Features mode, accidentally placing a stroke over some feature other than the one picked in the drop-down menu atop the Stroke list will yield a thoroughly wrong mask. Should that occur, delete the stroke you just drew, confirm which feature is currently selected, and then either redraw the stroke or switch to the correct feature you want to isolate.
