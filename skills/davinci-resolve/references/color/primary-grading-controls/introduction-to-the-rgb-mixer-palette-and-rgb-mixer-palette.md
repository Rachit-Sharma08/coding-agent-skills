# Introduction to the RGB mixer palette and RGB mixer palette

Version: DaVinci Resolve 20.3 Reference Manual. Context: Primary grading controls.
[Chapter index](INDEX.md)
<a id="source-example"></a> <a id="source-introduction-to-the-rgb-mixer-palette"></a> <a id="source-preserve-luminance"></a> <a id="source-primary-grading-controls"></a> <a id="source-primary-grading-controls-1"></a> <a id="source-resetting-the-rgb-mixer"></a> <a id="source-rgb-mixer-palette"></a> <a id="source-swap-channels-buttons"></a> <a id="source-the-normal-green-channel-for-the-rgb-mixer"></a> <a id="source-using-the-rgb-mixer-in-monochrome-mode"></a>

### Primary Grading Controls

The subject here is the more arcane tweaks at your disposal — blending colors from one channel into another by way of the RGB Mixer.

### Introduction to the RGB Mixer Palette

With the RGB Mixer palette you can feed varying quantities of image data out of one channel and into another, which opens up a broad span of both artistic and practical uses. On top of that, the RGB Mixer serves two ends: reshuffling the color channels, or folding chosen proportions of each color channel into a monochrome image.

### RGB Mixer palette

Out of the box, the RGB Mixer palette is configured to blend whatever quantity of the Red, Green, and Blue color channels you like into any of the others. Every color channel comes with its own control group of Red, Green, and Blue sliders for carrying out the mix, and the screenshot above shows where those sit by default. The full sweep of each slider runs from –2.00 to +2.00. Because of that, you’re also free to subtract any mix of color channel values from a given channel. As an illustration, dropping the Red control group’s Green slider to –.24 takes 24 percent of the Green channel out of the Red channel.

The Auto Normalize control on the Red channel of the RGB Mixer Beyond those sliders, the RGB Mixer carries one Auto Normalize control per channel. Each of these per-channel normalize controls lets a user reshape channel mixes while leaving the overall luminance untouched. Tweak any single color channel and the remaining ones automatically offset whatever you changed.

### Example

In the Original image, a cyclist wears a helmet marked with a green stripe:

### The normal Green channel for the RGB Mixer

Pulling down the Green channel within the green output would ordinarily wash the whole image with a magenta tint

With Auto Normalize switched on, the remaining pair of channels offset what you did to green. The hue shift then lands chiefly on the green helmet stripe — now shifted to cyan — while the rest of the image barely moves.

### Preserve Luminance

Tick the “Preserve Luminance” checkbox and whatever channel change you make is stopped from shifting the image’s luma, because the other two channels are pushed up or down automatically to make up for it. The next example shows that, with “Preserve Luminance” enabled, dropping the Green control group’s Green slider drives the Red and Blue channels up by an equal measure — visible in the Parade scope. The reverse holds too: lift one color channel’s slider and the other two fall by that same measure so total image brightness holds steady.

How an RGB Mixer change looks with “With luminance level preserved” switched on. Notice that dragging the green channel slider down simultaneously lifts red and blue.

### Resetting the RGB Mixer

A click on the Reset button in the RGB Mixer’s upper-right corner returns every slider to its default, namely Red = 1.00 for Red output, Green = 1.00 for Green output, Blue = 1.00 for Blue output, and all other sliders = 0.

### Swap Channels Buttons

Along the bottom of the RGB Mixer sit three buttons that make trading one channel for another effortless. That can serve a creative look, or fix things when two channels got flipped by mistake. Swap Red and Green: Trades those two color channels. Swap Green and Blue: Trades those two color channels. Swap Red and Blue: Trades those two color channels.

### Using the RGB Mixer in Monochrome Mode

Switch on the Monochrome checkbox and two sliders inside every Output group go inactive. That leaves only three controls in play: the Red > Red slider, then the Green > Green slider, plus the Blue > Blue slider. Since every color channel within an image is itself a grayscale channel, those RGB sliders in Monochrome mode let you blend chosen proportions of the Red, Green, and Blue color channels to build bespoke grayscale renderings of a shot.

Sliders at their default values when Monochrome mode is enabled It helps to look at where the Red, Green, and Blue sliders rest by default to see why this matters. So as to mirror how the human eye responds to different wavelengths of light, the Rec. 709 video standard pins down a standalone Luma (Y’) component as the sum of 0.2126 of the Red channel, 0.7152 of the Green channel, and 0.0722 of the Blue channels. Those proportions show up, rounded to whole-number percentages, as the defaults 21, 71, and 7. That is the conventional route to a black-and-white rendering of a color picture, and it gives results indistinguishable from dialing the Saturation parameter down to 0. That said, history offers other recipes for translating real-world color into varied grayscale readings. Photographers, for one, frequently pair colored filters with black & white film stocks — a yellow/green filter, say, to flatter the skin tone of fair-complexioned subjects. An even earlier instance is the choice of black & white film stocks with differing sensitivities; old orthochromatic stocks ignored red wavelengths altogether, capturing only blue and green to form a picture. Turning Monochrome mode on for the RGB Mixer hands you the freedom to brew your own blends of all three color channels and stress whichever creative qualities you’re after. As one case, dialing more blue in while cutting red and green can lend skin tones a darker, metallic sheen. The screenshots that follow present several renderings of one image, each with a different monochrome mix.

One image shown in three monochrome mixes. The topmost version comes from dropping saturation to 0. Just as you can with the parameters in Color mode, the RGB Mixer’s Monochrome mode lets you take one color channel away from the others to reach still more creative results.
