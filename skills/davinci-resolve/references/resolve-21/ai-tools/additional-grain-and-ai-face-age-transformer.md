# Additional grain and ai face age transformer

Version: DaVinci Resolve 21 New Features Guide. Context: Ai tools.
[Chapter index](INDEX.md) / [Previous section](depth-map-and-lens-properties.md) / [Next section](face-location-and-tracking-and-age-shift.md)
<a id="source-additional-grain"></a> <a id="source-ai-face-age-transformer"></a> <a id="source-ai-tools-part-2"></a> <a id="source-the-model-aged-by-30-years"></a> <a id="source-the-model-de-aged-by-20-years"></a> <a id="source-the-original-footage"></a>

### Additional Grain

With this toolset you lay a grain layer across the whole image.

- Add Grain: Tick this box to switch on this toolset.
- Strength: Move this slider to set how much grain gets added to the image.
- Size: Move this slider to set the size of the grain particles.
- Softness: Move this slider to set how blurry or crisp the grain particles are.
- Saturation: Move this slider to set how colorful the grain particles are.

### AI Face Age Transformer

The Face Age Transformer lets you artificially age or de-age your subject’s face. Being an AI tool, the Face Age Transformer will automatically add or take away wrinkles, skin tautness, and other aging-related traits on your subject, and keep them tracking consistently along with their head movements and position.

### The original footage

### The model aged by 30 years

### The model de-aged by 20 years

For now, Face Age Transformer puts age onto the face alone; there’s no promise the subject’s neck, ears, or hair color will shift along with it. Now and then, areas beyond the face do get touched. Should that happen, you may want to lay a separate tracking mask over the face so the effect stays penned to the face by itself. Faces that are deliberately dirtied or thrown into shadow can likewise trip up the AI analysis. Running the Face Age Transformer breaks into two parts. Part one is pinpointing and tracking the face you mean to age; part two is dialing in how much aging gets laid on.
