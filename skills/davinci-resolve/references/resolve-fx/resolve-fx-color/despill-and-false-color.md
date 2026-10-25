# Despill and false color

Version: DaVinci Resolve 20.3 Reference Manual. Context: Despill, False color studio version only.
[Chapter index](INDEX.md) / [Previous section](gamut-stabilization-contrast-dctl-and-dehaze.md) / [Next section](gamut-limiter-and-gamut-mapping-and-invert-color.md)
<a id="source-camera-model"></a> <a id="source-color-bands"></a> <a id="source-despill"></a> <a id="source-false-color-studio-version-only"></a> <a id="source-general"></a> <a id="source-preprocessing"></a> <a id="source-resolve-fx-color-part-2"></a> <a id="source-resolve-fx-false-color-camera-preset-and-legend"></a> <a id="source-scalelegend"></a>

### Despill

Strips away the color cast thrown onto a subject by light bouncing off the green or blue screen. That cast can linger even after the green screen's been keyed out. The Despill filter helps in cutting down spill after keying, or alongside keys or masks generated elsewhere.

- Key Color: Sets which color gets pulled off the subject—Red, Green, or Blue.
- Strength: How much Despill to apply. 1.000 matches having despill "on" in the earlier version

of the 3D Keyer checkbox. Having strength be adjustable is useful, since you get to hold on to more of the source color information whenever the situation permits. As an instance, a lighter despill makes sense if the fresh composited background is itself going to be green.

The Despill FX clearing a green color cast off the subject's arms and hair. The top shows no despill, the bottom full despill.

### False Color (Studio Version Only)

False Color is meant to mirror precisely the false color readout of a Blackmagic Design camera, yet it can also serve as a creative effect—recreating camera HUDs, infrared sensors, and custom posterization looks by remapping pixel brightness onto adjustable color bands and gradients. The color set can either echo the False Color setting on a particular Blackmagic Design camera or be tailored from a list of creative style presets supplied for use or inspiration. Those presets can be reshaped by setting how many colors are in play and spelling out the tonal range each color covers.

### Resolve FX False Color Camera preset and legend

Resolve FX False Color thermal creative preset and legend

### General

- Plugin Mode: This menu flips between matching a particular Blackmagic Design Camera's False Color setting and reaching the creative presets. With Specific Camera Model picked, the Camera Model section appears so you can select the camera and settings you want. With Creative picked, the Color bands section appears for selecting and tailoring the preset.

### Camera Model

The Camera Model controls show up once Specific Camera Model is picked from the Plugin Model menu. Through these menus you match the False Color of a camera configuration.

- Camera: Selects the exact Blackmagic Design camera sensor.
- Camera Mode: Selects the dynamic range setting.
- ISO Level: Sets the ISO or light sensitivity setting.

### Color Bands

These controls show up once Creative is picked from the Plugin Model menu. The Color Bands cluster of controls handles selecting and reshaping how the False Color presets look.

- Creative Style: Picks whichever of the effect's built-in style presets you want.
- Number of Bands: Lets you decide how many distinct colors make up the scale.
- Show Sliders: Brings out the Top and Bottom controls that let you pick a color's particular range

expressed as percentages. As an instance, dialing a Red color value to sit between Bottom 45 and Top 55 will shade red every part of the image whose brightness on the waveform monitor falls between 45 and 55%.

- Color: Hands you either a color swatch or a picker for choosing the band's color.

### Preprocessing

This cluster of controls handles laying tonal and blur processing onto the image.

- Blur: Applies a blur filter to the image before analysis.
- Black Level: Grows or shrinks the shadow range handed to colors landing lower on the

False Color legend.

- White Level: Grows or shrinks the highlight range handed to colors landing higher on the

False Color legend.

- Gamma: Nudges the mid-tone range toward whichever colors sit lower or higher along the False Color legend.

### Scale/Legend

This section governs how visible the False Color legend is and how it looks, sitting at the frame's left. The Legend lays out how dark-to-light inputs get mapped onto new colors. It is burned in to the image.

- Show Scale: Shows or hides the Legend.
- Show Values: Toggles whether numeric values appear on the Legend. Those numeric values stand for

differing scales according to the Value Style menu.

- Show Labels: Toggles whether data point labels appear on the Legend. Those labels flag the key data

points across the tonal range—black clipping, white clipping, and middle gray among them.

- Contrast: Grows or shrinks the transparency of the underlay behind the Legend's background.
- Value Detail: Grows or shrinks how many axis value labels get shown on the Legend.
- Value Style: This menu carries three options for the scale used by the Legend's numeric values.

Percentage: Applies a percentage scale to the Legend, climbing from 0% at the base to 100% at the peak. Hundredths: Applies a Hundredths scale to the Legend, climbing from 0 at the base to 100 at the peak while omitting the “%” symbol. Normalized: Applies a Normalized scale to the Legend, climbing from 0.0 at the base to 1.0 at the peak.
