# Brightness contrast and channel booleans

Version: DaVinci Resolve 20.3 Reference Manual. Context: Brightness contrast, Channel booleans.
[Chapter index](INDEX.md) / [Previous section](chromatic-aberration-auto-gain-brightness-contrast.md) / [Next section](color-corrector-correction-tab-colors-menu.md) / [Brightness Contrast BC](chromatic-aberration-auto-gain-brightness-contrast.md)
<a id="source-aux-channel-inspector"></a> <a id="source-aux-channel-tab"></a> <a id="source-basic-node-setup-2"></a> <a id="source-channel-booleans-bol"></a> <a id="source-channel-booleans-controls"></a> <a id="source-channel-booleans-node-introduction"></a> <a id="source-color-channel-tab"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-examples"></a> <a id="source-inputs-2"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-the-channel-booleans-node"></a>

### Common Controls

Settings Tab You'll see the Inspector's Settings tab on other Color nodes as well. These shared controls get a detailed treatment toward the close of this chapter, in the “The Common Controls” section.

### Channel Booleans [Bol]

### The Channel Booleans node

### Channel Booleans Node Introduction

The Channel Booleans node runs an assortment of mathematical and logical operations across an image's channels. It operates by letting one image's channels reshape another image's channels. Should no foreground input be present, any option that calls for the foreground's color channels falls back on the background input's color channels instead. NOTE: Watch out for a similarly named Channel Boolean (3Bol), a 3D node meant for remapping and altering the channels of 3D materials. For 2D channel work, reach for the Channel Booleans (spelled with an “s”) node (Bol).

### Inputs

In the Node Editor the Channel Booleans node carries four inputs, yet only the orange Background input must be filled. Background: This orange input takes a 2D image that the foreground input image then modifies. Effect Mask: The blue effect mask input wants a mask shape made from polylines, simple primitive forms, paint strokes, or bitmaps out of other tools. Wiring a mask here keeps the channel booleans adjustment to just the pixels lying inside that mask. Foreground: The green foreground input takes a 2D image that serves to modify the background input image. Matte: The white matte input lets you fold external mattes into the foreground and background operations.

### Basic Node Setup

As a remarkably versatile tool, the Channel Booleans node lends itself to a wide array of uses. In the example that follows, the z-depth channel is copied out of the foreground input (green) and into the background image (orange).

A Channel Booleans set to copy from foreground to background

### Inspector

### Channel Booleans controls

### Color Channel Tab

The Color Channels tab splits its controls into a pair of columns. The left-hand side lists target channels for whatever image feeds the orange background input. Over on the right, a drop-down menu lets you decide whether to alter the BG image using its own channels (the BG suffix after the list name) or using channels from an image wired into the node's green foreground input (the FG suffix in the drop-down list). Operation This menu picks which mathematical operation acts on the chosen channels. The available options run as follows: Copy Duplicates a value out of one color channel and into another. For instance, to build a matte, route the foreground red channel into the Alpha channel of the background.

- Add: Adds the color values of one color channel onto another channel.
- Subtract: Takes the color values of one color channel away from another color channel.
- And: Runs a logical AND across the color values between one color channel and another. Typically the

foreground image strips bits out of the background image's color channel.

- Or: Runs a logical OR across the color values between one color channel and another. Typically the foreground

image contributes bits to the background image's color channel.

- Exclusive Or: Runs a logical XOR across the color values between one color channel and another. Typically the

foreground image toggles bits in the background image's color channel.

- Multiply: Multiplies a color channel's values together. The image looks darkened by this

since the values span 0 to 1. White, valued at 1, leaves the result unchanged. Gray, valued at 0.5, yields a darker image, that is, one half as bright.

- Divide: Divides a color channel's values. The image looks lightened by this as the values span 0 to 1.
- Maximum: Weighs the two images against each other and keeps the maximum, or brightest, value from each.
- Minimum: Weighs the two images against each other and keeps the minimum, or darkest, value from each.
- Negative: Flips the FG input to produce a negative version of the image.
- Solid: Solid drives a channel up to its full value of 255. Handy for raising the Alpha to full value.
- Clear: Clear drops a channel to a value of zero. Handy for wiping the Alpha.
- Difference: Difference takes the greater color values of one color channel away from the lesser values of another color channel.
- Signed Add: Signed Add removes regions sitting below mid-gray and contributes regions sitting above mid-gray, which helps when crafting effects from embossed gray images.

To Red, To Green, To Blue, To Alpha Each of these menus stands for one of the output image's four color channels. Through the drop-down menu you pick which source-image channel feeds that output channel. By default it copies the channels off the foreground channel. You may choose any of the four color channels, plus a handful of auxiliary channels such as Z-buffer, saturation, luminance, and hue.

### Inspector

### Aux Channel Inspector

### Aux Channel Tab

This tab holds a row of menus through which you assign a source to each of the output image's auxiliary channels. Enable Extra Channels Tick the Enable Extra Channels checkbox and the Channel Booleans node becomes able to emit images carrying channels past the standard RGBA. With it on, the rest of the Aux Channels tab controls can route data into those auxiliary channels.

### Examples

When you want to push one image's Alpha channel into its own color channels, point the red, green, and blue channels at Alpha BG. Put the Operation on Copy. To pull the Alpha channel out of a different image, switch the operation type to Alpha FG. To swap an image's current Alpha channel for the Alpha of another image, pick “Do Nothing” on To Red, To Green, and To Blue and “Alpha FG” on To Alpha. Feed the image holding the Alpha into the foreground input of the Channel Booleans node. Set Operation: “Copy.” That very operation is also offered in the Matte Control node. To fold any mask into an image's Alpha channel, pick “Do Nothing” on To Red, To Green, and To Blue and “Matte” on To Alpha. Feed the mask into the foreground input of the Channel Booleans node. Set Operation: “Copy.” To take another image's red channel pixels away from the blue channel, pick “Do Nothing” on To Red and To Green and “Red FG” on To Blue. Feed the image holding the red channel you're subtracting into the foreground input of the Channel Booleans node. Set Operation: “Subtract.”

### Common Controls

Settings Tab The Inspector's Settings tab turns up on other Color nodes too. A full account of these shared controls waits at the end of this chapter, under the “The Common Controls” section.
