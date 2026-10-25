# Motion effects palette and noise reduction controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: The motion effects and blur palettes.
[Chapter index](INDEX.md) / [Next section](spatial-noise-radius-and-reduction-limits.md)
<a id="source-motion-effects-palette-studio-version-only"></a> <a id="source-noise-reduction-and-motion-blur-controls"></a> <a id="source-noise-reduction-controls"></a> <a id="source-spatial-nr-controls"></a> <a id="source-temporal-nr-controls"></a> <a id="source-the-motion-effects-and-blur-palettes"></a> <a id="source-the-motion-effects-and-blur-palettes-part-1"></a> <a id="source-ultranr-noise-reduction"></a> <a id="source-using-ultranr-controls"></a>

### The Motion Effects and Blur Palettes

Here we look at the Noise Reduction and Motion Blur effects housed in the Motion Effects palette, and we dig into the Blur palette's Blur, Sharpen, and Mist features as well.

### Motion Effects Palette (Studio Version Only)

Found only in the Studio version, the Motion Effects palette holds two groups of controls for laying optical-flow-derived effects over the clips in your program. Among them are upgraded Spatial and Temporal noise reduction together with motion-estimated synthetic motion blur.

### Noise Reduction Controls

Two parameter groups give you GPU-accelerated Temporal and Spatial noise reduction, built to tame noise in troublesome clips at close to real time when your workstation has enough processing muscle. You can run either noise reduction method on its own or pair them, dialing in different amounts to suit whatever footage is in front of you. On top of that, each control group is deeply adjustable, letting you target the chroma and luma of an image with separate doses of reduction and offering plenty of choices for how that reduction gets applied.

### Noise Reduction and Motion Blur controls

### Temporal NR Controls

By studying an image over several frames, the Temporal NR controls tell noise apart from genuine detail. The motion estimation settings keep moving subjects out of that process so you avoid unwanted motion artifacts.

- Number of Frames: How many frames you'd like DaVinci Resolve to average when pulling detail away from the noise. Your choices run from 0 to 5 frames. At 0 no frame averaging happens; higher figures average across more frames but grow markedly heavier on computation the further you push them. A higher frame count also sharpens the analysis, yet it can introduce artifacts wherever the frame holds fast-moving imagery. For such fast-moving imagery, a value of 1 may serve you better. Should artifacts crop up while you need higher frame counts, try tuning the Motion Threshold to clear them.
- Motion Est. Type: Selects how DaVinci Resolve spots motion within the image. Its default, Faster, eases the processor load while sacrificing some accuracy. Picking Better excludes motion with more precision but leans harder on the processor. None switches motion estimation off entirely, so Temporal NR then covers the whole image.
- Motion Range: The trio of Small, Medium, and Large lets you tell Motion Estimation what speed of motion to anticipate excluding. With Small, the assumption is slow subjects carrying little to no motion blur, so Temporal NR reaches more of the image at any given Motion Threshold. With Large, the assumption is fast motion whose blur spans a wider area, which keeps more of the image out of Temporal NR at that same Motion Threshold. As you work the Motion Threshold parameter, settle on whichever setting best balances cutting noise against introducing motion artifacts.
- Luma Threshold: Sets how much or how little Temporal NR lands on the image's luma component. It spans 0–100, with 0 meaning no reduction whatsoever and 100 the maximum. Pushing it too far can strip fine detail out of the image.
- Chroma Threshold: Sets how much or how little Temporal NR lands on the image's chroma component. It spans 0–100, with 0 meaning no reduction whatsoever and 100 the maximum. Going too high can strip fine color detail away, though you'll often be able to push the Chroma Threshold past the Luma Threshold while artifacting stays less obvious.
- Luma/Chroma Threshold ganging: By default the Luma and Chroma Threshold parameters move as one, so changing either changes both. You can break that link, however, to feed each component its own dose of reduction wherever the noise is worst.
- Motion Threshold: Marks the dividing line between moving pixels counted as in motion (above it) and those counted as static (below it). With Motion Estimation in play, Temporal Noise Reduction stays clear of image regions above this line, so frame-averaging never touches moving areas and motion artifacts are headed off. Lower figures hold more of the image back from Temporal NR by reacting to subtler movement; higher figures admit more of the image by demanding faster motion before exclusion. The scale runs 0 to 100, where 0 applies Temporal NR to none of the pixels and 100 applies it to every pixel. Its default of 50 strikes a workable middle ground for many clips. Set the Motion Threshold too high and artifacts may surface in the moving portions of the image.
- NR Blend: Cross-fades between the image as the Temporal NR parameters shape it (at 0.0) and the image carrying no reduction at all (100.0). The parameter makes it easy to meet in the middle when your temporal noise reduction runs heavy.

### Spatial NR Controls

The Spatial NR controls iron out patches of high-frequency noise across the image while trying to hold onto detail so the picture doesn't go soft. They handle noise that Temporal NR simply can't.

- Mode: Through the Mode drop-down you flip Spatial NR among three distinct algorithms. Because every mode shares the very same controls, you can jump between them on identical settings to weigh the outcomes side by side.

Faster: Leans on a computationally light reduction technique that holds up well at lower settings but can throw artifacts once values climb. Better: Hands the Spatial NR controls a higher-quality algorithm whose results far outclass Faster, though it costs more to render and forecloses splitting the Luma and Chroma Threshold sliders for per-component tuning. Enhanced: Keeps image sharpness and detail intact far more successfully as you push the Spatial Threshold sliders up to wipe out noise. The gain stands out most once those Spatial Threshold sliders sit at high values (and what counts as “high” shifts with the image at hand). Down at lower values the gain can read as subtler next

to the “Better” mode, which taxes the processor less than the computation-heavy “Enhanced” setting. On top of that, “Enhanced” lets you split the Luma and Chroma threshold sliders apart so each color component gets the dose of reduction the image calls for. UltraNR: UltraNR is an AI-driven reduction option delivering intelligently targeted results drawn from machine learning of real-world video noise patterns, rather than leaning on any fixed mathematical formula. Its usage is covered further down.

- Radius: The choices are Large, Medium, and Small. A smaller radius runs faster in real time and still looks good when your Luma and Chroma Threshold values stay low, although low NR Threshold values may leave more aliasing in detailed regions.

Working the Radius progressively higher lifts quality inside the most detailed areas when Luma and Chroma Threshold values are high, the cost being reduced speed. For most images a Medium NR Radius pairs well with medium NR Threshold settings. As so often, there's a quality-versus-speed tradeoff you can dial.

- Luma Threshold: Governs how much or how little reduction reaches the image's luma component. It runs 0–100, where 0 means none at all and 100 the full amount. Too high a value can wipe fine detail from the image.
- Chroma Threshold: Governs how much or how little reduction reaches the image's chroma component, smoothing patches of high-frequency noise while striving to keep significant edge detail crisp. It runs 0–100, where 0 means none at all and 100 the full amount. Too high a value can wipe fine color detail away, though you'll often manage to lift the Chroma Threshold above the Luma Threshold while artifacting stays harder to spot.
- Luma/Chroma Threshold ganging: Normally the Luma and Chroma Threshold parameters travel together, so a change to one is a change to both. Unlink them, though, and you can hand each component a different amount of reduction.

Say an image softens too much at some level of reduction yet shows more color speckle than luma noise — you can drop the Luma Threshold to hold detail while lifting the Chroma Threshold to clear the color noise.

- NR Blend: Cross-fades between the image as the Spatial NR parameters work on it (at 0.0) and the image with none applied (100.0). The parameter lets you easily land in the middle when your spatial noise reduction runs heavy.

### UltraNR Noise Reduction

UltraNR is an AI-driven reduction option whose intelligently targeted results come from machine learning of real-world video noise patterns instead of any fixed mathematical formula. On badly noisy footage this mode tends to outperform the rest by a wide margin, and it edges ahead even on ordinary noise reduction too. The design aim is the sweet spot between cutting the noise you want gone and avoiding the picture-softening you don't.

An under-exposed frame of a black dog lying on a black blanket atop a black couch — pretty much the worst case for video noise, pictured above.

That same frame with UltraNR engaged in the Spatial NR settings. The Show Patch icon is active, drawing a white box around the spot where the noise pattern gets sampled.

### Using UltraNR Controls

Turning on UltraNR is as easy as choosing it from the drop-down in the Mode section of SpatialNR. From there a single click on the Analyze button has UltraNR sample a flat patch of the image on its own to gauge the Luma/Chroma noise level, then set the analysis Luma and Chroma sliders to match. Want to fine-tune further? Let Auto find the flat patch, then switch on the “Show Patch” icon. A small white outlined square shows up on your clip marking where the AI has dropped its analysis point. You can then drag that patch by hand — and nudge its size a little via the handles — across flat areas to read the Luma/Chroma noise level. Let go of the mouse button and the luma and chroma get recalculated for the box's new spot. If it still isn't right, shift the sliders to tweak the analyzed luma and chroma slightly, luma before chroma. Happy with the outcome, you can tuck the patch away.

This new UltraNR spatial-denoise mode lives on the Color page within the Motion Effects > Spatial NR pane, and it shows up inside the Resolve FX noise reduction effect too.

The UltraNR controls as they appear within the Motion Effects pane on the Color page Using Noise Reduction The steps below outline one way to work the Noise Reduction (NR) parameters toward a measured result. Applying noise reduction to an image: 1 Switch on Temporal NR by picking 1 to 5 frames in the Number of Frames drop‑down menu. Remember that adding frames pushes this effect's render time up sharply, and depending on your footage it may or may not help the outcome much. 2 Set the Motion Est. Type and Motion Range drop-down menus to match how much motion the image holds. Heavy motion may call for Better and Large; with little motion, gentler settings will often do. 3 Keeping Luma and Chroma Threshold linked, ease either one upward until noise just begins to drop in the still areas of the image, then refine in smaller steps to find the most Temporal NR you can add before motion artifacts appear or the detail you want to keep softens too much. 4 When the image clearly carries more chroma than luma noise, unlink Luma/Chroma once luma reduction looks good, then raise the Chroma Threshold for harder Temporal NR against the color speckle. 5 If the balance between maximum reduction and freedom from motion artifacts disappoints you, revisit the Motion Threshold — drop it to keep more motion out of the operation, or lift it to fold more motion in. Still unhappy? Stronger Motion Est. Type and Motion Range settings are worth a try.

(Left) the shot beforehand and (Right) the same shot once Temporal NR has cut the noise in its still regions Remember that Temporal NR shines at clearing noise from the parts of the image that don't move. Once you've struck the best balance between reduction in the still areas and freedom from motion artifacts in the moving ones, it's time to bring in Spatial NR to mop up noise across the remainder of the picture. 6 Switch on Spatial NR by lifting either the Luma or Chroma Threshold parameters — linked out of the box — until you find a fitting balance between noise loss and an unwanted rise in softness. 7 Reaching for the Enhanced option in the Spatial NR mode drop‑down is recommended, since it produces the finest results. That choice is processor‑heavy, though, so when real-time performance matters more, drop the mode to Faster and compare. 8 When chroma noise plainly outweighs luma noise, unlink Luma/Chroma at a comfortable level of luma reduction, then raise the Chroma Threshold for more aggressive Spatial NR against the color speckle.

(Left) Before and (Right) after noise reduction improves the “look” 9 Should a high Spatial NR Luma or Chroma Threshold have been needed to knock the noise back visibly, leaving detailed areas looking chunky or aliased, pick a larger value in the Radius drop-down menu so the scene gets a finer analysis. Visual quality climbs as a result, but bigger NR Radius settings demand more from the processor and can sap real-time performance when your system lacks the GPU headroom. 10 If your noise reduction settings work yet come off too strong and leave the image looking over-processed, try lifting the Spatial NR and/or Temporal NR Blend parameters to blend between the reduction each control group adds and the image as it stood beforehand.

Try Applying Temporal NR First, then Applying Spatial NR Since Temporal NR leans on several frames to isolate noise, it usually holds detail more faithfully wherever the image barely moves. Leading with Temporal NR and landing a good result — even across only part of the frame — can cut how much Spatial NR you then need, lifting the overall quality of the finished shot. Bear in mind that Temporal NR excels in an image's static regions yet loses ground on moving subjects, whereas Spatial NR can knock down noise anywhere in the frame that falls under its threshold, motion or not. In the end, pairing the two almost always proves the winning move.
