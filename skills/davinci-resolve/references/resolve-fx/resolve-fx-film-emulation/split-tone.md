# Split Tone

Version: DaVinci Resolve 20.3 Reference Manual. 

[Film emulation effects](INDEX.md)

<a id="source-split-tone"></a> <a id="source-split-tone-effect"></a> <a id="source-the-final-split-toned-image"></a>

### Split Tone Effect

With the Split Tone effect you tint shadows and highlights along opposing hue angles. You might, for instance, push orange into the highlights and teal into the shadows for a more contemporary cinematic feel.

The unaltered image 

The Preview Influence checkbox reveals where each split color lands and which one it is
### The final split-toned image
### Split Tone

- Split Tone Mode: Bundles presets together with a custom mode. Natural: Built to imitate how film behaves. Strong: A bolder, more deliberate stylized look. Custom: Hands you full command over whichever two colors you want for the Split Tone.
- Preview Influence: Reveals where the split falls, rendered in true colors.
- Shadows (custom only): Governs the shadow half of the split. Strength: How saturated the picture's darker areas become. Hue: Which color those darker areas take on.
- Highlights (custom only): Governs the highlight half of the split. Strength: How saturated the picture's lighter areas become. Hue: Which color those lighter areas take on.
- Neutrals (custom only): Shields the neutral (grey tone) regions of your image from the Split Tone effect. Protect Neutrals: Tick this box to switch the Neutrals controls on or off. Minimum Saturation: Regions sitting below this saturation stay grey. Maximum Saturation: Regions sitting above this saturation feel the Split Tone effect.
- Strength: The amount of split tone color blended into the original image.
- Pivot: Fixes where highlights and shadows part ways, establishing the spot at which the

color “splits”.

- Hue Angle: The split tone's color, read off as the angle on the vectorscope.
- Color Space Overrides: With these controls you can alter the effect's input and output gammas

and color spaces whenever a display referred workflow asks you to set them up manually. Its default value is “Use timeline,” which falls in line with the color spaces chosen under the Color Management section within the Project Settings. Input Color Space: Establishes the input color space, picked from the drop-down menu. Input Gamma: Establishes the input gamma via that same drop-down menu. Output Color Space: Determines the output color space, again chosen from the drop-down. Output Gamma: Determines the output gamma using the drop-down menu. Output White Point: Fixes the display white point. With creative aims in mind, you may pick one from the drop-down menu. The default white point here is D65.
