# Sharpening edges and softening

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sharpen studio version only, Sharpen edges studio version only, Soften and sharpen studio version only.
[Chapter index](INDEX.md)
<a id="source-adjust-small-skin-texture-granularity"></a> <a id="source-chroma"></a> <a id="source-detail-levels"></a> <a id="source-edge-detection-controls"></a> <a id="source-main-controls"></a> <a id="source-main-controls-1"></a> <a id="source-main-controls-2"></a> <a id="source-resolve-fx-sharpen"></a> <a id="source-resolve-fx-sharpen-1"></a> <a id="source-sharpen-edges-studio-version-only"></a> <a id="source-sharpen-studio-version-only"></a> <a id="source-soften-and-sharpen-studio-version-only"></a>

### Resolve FX Sharpen

Compared with the sharpen operation in the Blur palette, these plugins bring a fresher, finer-grained way to sharpen particular details within images. The trio of plugins each apply the very same core algorithm, but aim it at distinct jobs.

### Sharpen (Studio Version Only)

What the Sharpen filter does is split the image into four tiers of detail: first the underlying structure, then the fine scale details, next the medium scale details, and finally the large scale details, with each tier covering structures of a different size that together make up the whole image. Thanks to this, the Sharpen filter lets you dial in separate sharpening amounts for the fine, medium, and large structures of the image, handing you tremendous command over how each of these tiers of image detail is treated.

### Main Controls

Controls the overall sharpening effect.

- Sharpen Amount: The main global control through which sharpening is added to the image. For finer tuning, reach for the controls under Detail Levels to set how much sharpness lands on each structure size this plugin reaches. 1.800 is the default value. 0 is no sharpening, 5.000 is maximum sharpening.

### Detail Levels

Lets you tailor the sharpen effect in numerous highly targeted ways.

- Fine Detail Size: Where the threshold for what counts as a fine detail lies is set by this slider, which in turn shifts which image structures the Medium and Large Details sliders reach as well. Pulling this slider down leaves the image's larger structures out of the sharpening. The default is 0.050.
- Fine Detail: Left at its default, the Fine Details slider rules the sharpness of the tiniest detail — think skin pores and strands of hair, or little speckles across textured surfaces. Turn the settings down for less sharpening on these structures, or up for more.
- Medium Details: The sharpness of rougher detail — freckles, wrinkles, hair clusters, and surface features with stronger edge definition — is ruled by this slider. Turn the settings down for less sharpening on these structures, or up for more.
- Large Details: The sharpness of the image's biggest details is ruled by this slider, covering eyelids, the shadows along the edges of lips and noses, the lines where hair meets the face, and the highest-contrast edge detail right across the image. Turn the settings down for less sharpening on these structures, or up for more.

### Chroma

A special purpose control that you want to handle with care.

- Sharpen Chroma: Sharpens only the image's chroma, leaving the luma (Y) untouched.

### Sharpen Edges (Studio Version Only)

A take on the Sharpen filter trimmed down for spotting edges and building a key that confines sharpening to an image's chosen edge detail. It is a handy filter when you want to take the edge off of mildly soft-focus clips.

### Main Controls

Controls the overall sharpening effect accomplished with this plugin.

- Sharpen Amount: The main global control for laying sharpening onto the edges this filter picks out.
- Sharpen Radius: Sets how coarse or fine the detail introduced via Sharpen Amount turns out.

### Edge Detection Controls

These controls let you tailor the sharpen effect in very precise ways.

- Display Edges: Switching on this checkbox gives you a grayscale preview of which edges are being picked out for sharpening as you work the rest of this group's controls. With the checkbox on, you can see exactly how the section's other four controls reshape the key that decides which parts of the image get sharpened.
- Pre Denoise: Smooths the matte so stray pixels of noise drop away. Lowering Pre Denoise lets you cut edges you would rather not sharpen out of the key and calm edges left jagged by heavy noise. Pushing Pre Denoise up feeds more edges into the sharpening and reinforces the edges already present.
- Edge Detect Threshold: Sets how pronounced an edge has to be before it makes it into the key. Lowering this parameter pulls more edges into the operation, whereas raising it keeps edges out.
- Edge Mask Strength: Boosts how intense the edges in the key are. Lowering Edge Mask Strength weakens the edges and tones down the sharpening there. Raising Edge Mask Strength strengthens the edges and pulls more of the image around each detected edge into the sharpening.
- Edge Blur: Governs how soft the key's edges are. Lowering Edge Blur tightens the key and narrows which edges sharpening touches. Raising Edge Blur loosens the key and can draw a broader band of image detail into the sharpening.

### Soften and Sharpen (Studio Version Only)

A take on the Sharpen filter trimmed down so you can both smooth certain details and sharpen others according to how big the structures are. While it works on any image where you want to smooth some features and sharpen others, it most often comes into play for toning down unwanted blemishes, wrinkles, or scarring when applied inside a window or qualifier that isolates the skin. What makes Soften and Sharpen useful is that the Small Texture slider lets you keep some natural skin detail — pores and other tiny lifelike touches — while the Medium and Large Texture controls smooth out unwanted detail in whatever balance reads as natural. TIP: For the most natural outcome, hold Small Texture at 0 or barely above, drop Medium Texture only as far as needed to play down whatever detail deserves it, and lower Large Texture a touch less to soften bigger blemishes while keeping the face's overall detail. That reasoning is why the defaults sit at Small 0.000, Medium –0.800, and Large –0.300.

### Main Controls

Every one of the Small, Medium, and Large Texture sliders swings into both negative and positive territory. At a value of 0, the matching details of the image stay exactly as they are. Going negative strips those matching details away, and at –1.000 you are left with nothing but the image's smooth underlying structure. Going positive sharpens those matching details, topping out at a value of 1.000.

- Small Texture: Works on the very finest detail, like pores in the skin and individual hair strands.
- Medium Texture: Acts on rougher detail, such as freckles, wrinkles, and bunches of hair.
- Large Texture: Hits the image's biggest details, among them eyelids, eyebrows, the edges of lips

and noses, and the edges where hair meets the face. TIP: Whether something reads as a small, medium, or large structure hangs largely on how the shot frames its subject. Those structures shift according to whether you are grading a subject in a long shot (where they look small) or a subject in closeup (where they look large).

### Adjust Small Skin Texture Granularity

Through this control you can tune where the line falls between the Small and the Medium/Large texture controls from the group just above.

- Small Texture Size: Sets the threshold separating Small Textures from Medium and Large Textures, helping you fine-tune the Small Texture you mean to keep. Raising this value sweeps more of the image in as small details, while lowering it shuts more of the image out of small details.
