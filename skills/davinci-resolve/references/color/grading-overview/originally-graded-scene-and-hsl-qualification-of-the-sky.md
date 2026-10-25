# Originally graded scene and hsl qualification of the sky

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grading overview.
[Chapter index](INDEX.md) / [Previous section](color-and-goals-of-color-correction.md)
<a id="source-adding-style"></a> <a id="source-balancing-scenes"></a> <a id="source-corrected-and-sky-enhanced"></a> <a id="source-custom-curves-controls"></a> <a id="source-defocus-effect-created-in-real-time"></a> <a id="source-enhanced-and-balanced-final"></a> <a id="source-hsl-qualification-of-the-sky"></a> <a id="source-image-enhanced-with-curves"></a> <a id="source-image-graded-to-preserve-detail-in-highlights"></a> <a id="source-image-graded-with-highlight-detail-blown-out"></a> <a id="source-left-image-corrected-to-match-right"></a> <a id="source-link-icon-indicates-clips-are-grouped-for-grading"></a> <a id="source-never-stop-experimenting"></a> <a id="source-node-tree-adding-two-different-treatments-together"></a> <a id="source-original-image"></a> <a id="source-original-image-1"></a> <a id="source-originally-graded-scene"></a> <a id="source-quality-control"></a> <a id="source-split-screen-of-two-shots"></a> <a id="source-thumbnail-view-of-balanced-clips"></a> <a id="source-timeline-thumbnail-view-of-unbalanced-clips"></a> <a id="source-video-scopes"></a>

### Originally graded scene

### HSL qualification of the sky

### Corrected and sky enhanced

To read more about working with qualifiers, see Chapter 137, “Secondary Qualifiers.”

### Balancing Scenes

Seldom do the uncorrected shots within a scene line up flawlessly with each other. Even the angles of coverage exposed with the greatest care can carry slight differences that have to be smoothed away. At the far extreme, run-and-gun productions shot under available light frequently yield cut scenes that lurch wildly in lighting and color as one shot jumps to the next. Whether minor or major, accidental shifts between consecutive shots can draw unwanted notice to the editing and jolt the audience in ways that pull them out of the program. Smoothing out these discrepancies and matching the clips across each scene ranks among the colorist’s core duties. The signal that you are done is when color glides imperceptibly from one clip to the next throughout the scene. DaVinci Resolve offers an assortment of tools for comparing images against one another, chief among them the Gallery, where you can stash still images of clips and then set them beside other clips by way of an adjustable split screen.

### Timeline thumbnail view of unbalanced clips

### Thumbnail view of balanced clips

Calling on the Gallery to play stills, whether split or whole (toggling between the clip under adjustment and the still), makes it simpler to wield the broad DaVinci Resolve toolset and bring the color and exposure of every clip in a scene into agreement.

### Split screen of two shots

### Left image corrected to match right

A further batch of features lets you handle grades by copying them between clips, or by tying similar clips together, whether automatically or by hand through groups.

### Link icon indicates clips are grouped for grading

To read more about working with the Still Store, see Chapter 126, “Using the Color Page.” To read more about grade management, see Chapter 142, “Grade Management.”

### Adding Style

Naturally, it does not all come down to subtlety and correction. Grading music videos and commercials, for one, often warrants pouring some bold style into a piece. On this front as well, DaVinci Resolve hands you a wealth of features for bending the image in surprising directions; you might, for example, push the Custom Curves to extremes to fake the look of chemical cross‑processing.

### Custom Curves controls

### Original image

### Image enhanced with Curves

Because DaVinci Resolve processes images through nodes, you can reach for more unusual node structures to craft effects with composite modes, like a colored glow produced by combining two differently graded copies of the same image through a Layer node.

### Node tree adding two different treatments together

### Original image

### Enhanced and balanced final

You can likewise assemble intricate node trees that build particular mattes for singling out particular elements of the image. Say you wanted to keep an actor in color while the background goes monochromatic; you can generate several keys (drawn via HSL Qualification) and merge them with a Key Mixer node to construct that effect.

Node tree to isolate the man’s face and clothes

Original image The final effect, with everything but the man drained of saturation Lastly, the tools in DaVinci Resolve are not confined to color and contrast alone. A Blur palette furnishes controls for blurring, sharpening, or laying mist over all or part of the image. Paired with the other tools at hand for isolation and color adjustment, these make potent additions to your creative arsenal.

### Defocus effect created in real time

To read more about every one of these features, see Chapter 125 through Chapter 142 of this manual.

### Quality Control

Finally, bear in mind that, for all the creative latitude DaVinci Resolve grants, the deliverables you ultimately hand your client still need signal levels that suit their requirements. Programs bound for broadcast, in particular, carry firm outer limits on luma and chroma that you dare not cross, lest a show get bounced for QC (quality control) violations. Even when broadcast is not your destination, though, you ought to stay mindful of the mathematical limits of a digital video signal so you are not clipping or crushing image detail through heavy-handed adjustments you might actually want to keep. Glance at the next two images, for instance, and the hazards of heavy-handed adjustments become clear next to a clip that, creatively graded though it is, was set with the mathematical boundaries of image data in mind.

### Image graded to preserve detail in highlights

### Image graded with highlight detail blown out

On this front as well, DaVinci Resolve supplies tools built to help you keep a grip on fine-tuning the image. A Video Scopes window offers the standard Waveform, Parade, Vectorscope, and Histograms used to analyze your image data. Such scopes reveal the limits of what is achievable, make faint problems easy to catch, and let you weigh the traits of one image against another.

### Video scopes

Once you reach the point of deliberately clipping data in the highlights and shadows for a creative look, the Soft Clip controls let you bring in a gentle or pronounced roll-off, squeezing the signal’s extremes so whatever clipping you apply comes out softer and more agreeable. For deeper coverage of both the video scopes and the Soft Clip controls, turn to Chapter 126, “Using the Color Page.” as well as Chapter 134, “Curves.”

### Never Stop Experimenting

Now that you have had a very quick tour of the grading process through the lens of the DaVinci Resolve toolset, we encourage you to lean on this manual to dig into DaVinci Resolve more deeply. The further you push the various features on offer, the more you may turn up surprising uses for controls you assumed you already understood well. Have fun.
