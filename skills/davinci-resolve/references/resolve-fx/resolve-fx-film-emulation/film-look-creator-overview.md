# Film Look Creator setup and color spaces

Version: DaVinci Resolve 20.3 Reference Manual. Studio version only.

[Film emulation effects](INDEX.md)

<a id="source-color-space-overrides"></a> <a id="source-film-look-creator-studio-version-only"></a> <a id="source-main-controls-2"></a>

### Film Look Creator (Studio Version Only)

The Film Look Creator lets you readily reshape both the color and the physical qualities of an image to imitate motion picture film stock, all inside a single Resolve effect. Rather than chasing any one manufacturer's film stock, it lays down a base “Blackmagic” film look that you can then bend in all sorts of creative directions. The Film Look Creator reworks an image's contrast, saturation, hue, and exposure. It packs in the tools you'd want for film emulation as well — halation emulation, film gate, flicker, weave, vignetting, bloom, and more.

At left, the original video; at right, its Film Look Creator Bleach Bypass Super 16mm rendition A good number of the Film Look Creator's pieces have their own dedicated equivalents over in the Resolve FX library. Even so, the Film Look Creator rolls these film look tools into one Resolve effect with a vastly streamlined control set. Should you ever want finer command over some facet of the look, you can simply switch off that module of the effect and drop a dedicated Resolve Effect into the node tree instead. Apply this effect and an underlying Blackmagic film look is laid in automatically up front. Over 60 parameters drive that film look, all handed to you the moment the plugin is active (with every effect off). These parameters come carefully tuned and “baked in” to the Blackmagic film stock. Although you can't touch those, the plugin's upper region carries extra controls for refining and shaping looks of your own. Built for scene referred workflows, the Film Look Creator works with any camera source and output display. Under either Resolve Color Management or ACES this falls into place on its own, because the plugin defaults to the timeline color space for both input and output. It functions on manually display referred timelines (DaVinci YRGB, for instance) too, but there the user has to hand-pick the source footage's transform and the display transform, which you handle within the plugin's Color Space Overrides section. NOTE: The Film Look Creator does its best work on video that fills the whole frame. Effects such as Halation and Film Gate can behave unexpectedly when the video sits smaller than the frame size. Where needed, fill the frame with the Sizing controls, or head to Project Settings > Image Scaling > Input/Output Scaling and pick “Scale Full Frame with Crop” in place of the default “Scale entire image to fit.”
### Main Controls

These controls build this effect's foundation.

- Presets: Sets every control automatically for a chosen preset look. “Clean Slate” skips the underlying Blackmagic Film Look and leaves you a clean image to start from. “Default No Effects” switches the Blackmagic Film Look on while turning off all the extra effects beneath.
- Color Blend: Lets you blend the underlying color look with whatever changes you've made to other color settings and split tone controls.
- Effects Blend: The master control for tuning the strength of the spatial effects below. At 0% the effects are fully off, and at 100% you get the Film Look Creator's complete output.
- 3D LUT Compatible: Ticking this box strips out the spatial effect options that a 3D LUT can't represent. That lets you carry your custom film look over to other programs and camera hardware through a LUT.
### Color Space Overrides

These controls let you reassign the effect's input and output gammas and color spaces whenever you have to set them up by hand for a display referred workflow. Bear in mind that altering them applies no tone mapping. Their default, “Use timeline,” lines up with the color spaces you've chosen in the Color Management section of the Project Settings.

- Input Color Space: Fixes the input color space; pick one from the drop-down menu.
- Input Gamma: Fixes the input gamma; pick one from the drop-down menu.
- Output Color Space: Fixes the output color space; pick one from the drop-down menu.
- Output Gamma: Fixes the output gamma; pick one from the drop-down menu.
- Output White Point: Fixes the display white point. For creative ends, you can pick one from

the drop-down menu. The default white point is D65.

Open when refining the look: [Color and glow](film-look-creator-color-and-glow.md).

Open when shaping film texture and frame motion: [Grain and gate](film-look-creator-grain-and-gate.md).
