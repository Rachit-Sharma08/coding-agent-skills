# Beauty operating mode

Version: DaVinci Resolve 20.3 Reference Manual. Context: Beauty studio version only.
[Chapter index](INDEX.md) / [Next section](beauty-and-custom-mixer.md)
<a id="source-advanced"></a> <a id="source-automatic"></a> <a id="source-beauty-studio-version-only"></a> <a id="source-feature-recovery"></a> <a id="source-operating-mode"></a> <a id="source-resolve-fx-refine"></a> <a id="source-resolve-fx-refine-part-1"></a> <a id="source-smoothing"></a> <a id="source-smoothing-1"></a> <a id="source-texture-recovery"></a> <a id="source-ultra-beauty"></a>

### Resolve FX Refine

With these plugins you can carry out various sorts of focused enhancements.

### Beauty (Studio Version Only)

Beauty is a plugin built for governing texture. Within Ultra Beauty mode, you can selectively soften image detail above a set threshold while keeping detail that sits below a set threshold. That lets you smooth away the larger textures you'd rather not have, all while either keeping or even amplifying the smaller textures you do want. For faces and skin, the plugin offers an additional way to smooth out larger, unwanted blemishes while holding onto the edge detail and underlying structures like pores that you'd want to keep, letting you improve a subject's complexion on shoots that lacked hair and makeup, without over-softening genuine skin detail into an overly fake plastic look.

(Left) The original image, (Right) A face where Beauty has softened the complexion yet held onto fine facial detail Keep in mind that this plugin serves more than skin detail, and it does more than soften. After you've isolated the fine detail you'd like to keep in a subject, you can instead amplify it for heavily textured results. The plugin works well on any subject whose textures call for refinement. TIP: It's best run inside a qualification that isolates the specific feature you mean to smooth. Its default settings deliver a moderate degree of smoothing and fine detail recovery suited to faces in closeup, yet they won't fit every situation, so some fine-tuning is always required. For naturalistic outcomes, this plugin gives its best when applied with restraint.

### Operating Mode

The Beauty plugin offers three operating modes: an Automatic mode whose simpler operation suits you when the goal is the smoothest or most textured result possible while still keeping key details, an Advanced mode for those wanting finer control, and an Ultra Beauty mode that adds further controls letting you hold onto the fine detail you want while smoothing away the coarse details you don't.

### Automatic

Automatic mode surfaces straightforward controls for smoothing or coarsening detail.

- Amount: Lets you set how much smoothing or coarsening gets applied.
- Scale: Lets you dial down or up the degree of smoothing or coarsening reached

through the Amount slider's range.

### Advanced

Advanced mode brings out additional manual controls for smoothing or coarsening detail, without Ultra Beauty mode's complexity.

- Show Split View: Ticking this box places a four-up display in the Viewer presenting the Smoothing, Texture Recovery, Feature Recovery, and Final Output outputs in turn. It's handy to keep open while tuning the advanced options below.

The Advanced Beauty mode's Split View, which presents the Smoothing view (top left) alongside Texture Recovery (top right), then Feature Recovery (bottom left) plus Final Output (bottom right).

### Smoothing

With these parameters you strip out imperfections. Two smoothing controls are yours to adjust. Push them hard enough to wipe out every detail you mean to smooth away. Whatever harm over-smoothing causes gets undone in Texture and Feature Recovery.

- Smoothing Threshold: Move this slider to set how much image detail is kept.
- Diffuse Lighting: Tunes how much detail lands in the mid-tones.
- Preview Smoothed: Displays only the smoothing operation's result in the Viewer.

### Texture Recovery

Through these parameters you bring back patches of fine texture from the source video across flat areas set apart from the edges.

- Texture Threshold: Move this slider to set how much fine texture in the image is kept.
- Add Texture: Raises or lowers the scale of the texture within the Texture Threshold. Positive

figures add texture, whereas negative figures take it away.

- Preview Texture: Displays only the Texture Recovery operation's result in the Viewer.

### Feature Recovery

These parameters let you decide how much of the recoverable Smoothing and Textures gets brought back into the image.

- Recovery Amount: Move this slider to set how much of the detail you've isolated (shown white on the Feature Recovery view) returns to the image.
- Preview Recovery Areas: Displays only the Feature Recovery operation's result in the Viewer.

### Ultra Beauty

The Ultra Beauty controls unlock the Beauty plugin's full strength, supplying preview modes for inspecting various facets of how the plugin behaves, all while you specifically set the degree of smoothing or coarsening you want, how much texture to keep, and which further features of the subject you want recovered from this operation to fine-tune the outcome.

### Smoothing

With these parameters you strip out imperfections. Two smoothing methods are on offer to pick from. Push these controls hard enough to wipe out every detail meant to be smoothed away. Any harm from over-smoothing gets undone in Detail Recovery. To gauge the smoothing on its own, lower the Detail Recovery strength and texture down to zero.

- Flatten: Cuts texture and screens out detail. Strength: How much smoothing effect lands on the image. Levels: Governs how strongly the image is abstracted toward smooth levels. Quality: Governs how sharp the resulting effect is, Full being sharpest and Fastest blurriest.
- Filter: Flattens the image's smooth areas, leaving edges only where they separate one flat region from another. Strength: How much smoothing effect lands on the image. Filter Radius: Governs which scale of details gets filtered. Edge Threshold: Governs the level at which an edge is kept or smoothed over. A low threshold holds onto even faint edges, while a high one smooths over a growing number of edges unless they're very high contrast.
