# Copy aux and gamut

Version: DaVinci Resolve 20.3 Reference Manual. Context: Copy aux, Gamut.
[Chapter index](INDEX.md) / [Previous section](color-matrix-and-color-space.md) / [Next section](gamut-basic-node-setup.md) / [Continue Gamut Gmt / Basic Node Setup](gamut-basic-node-setup.md)
<a id="source-basic-node-setup-2"></a> <a id="source-controls-tab-2"></a> <a id="source-copy-aux-controls"></a> <a id="source-copy-aux-cpa"></a> <a id="source-copy-aux-node-introduction"></a> <a id="source-gamut-gmt"></a> <a id="source-gamut-node-introduction"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inspector-2"></a> <a id="source-kill-aux-channels"></a> <a id="source-settings-tab-3"></a> <a id="source-the-copy-aux-node"></a> <a id="source-the-gamut-node"></a>

### Copy Aux [CpA]

### The Copy Aux node

### Copy Aux Node Introduction

You turn to the Copy Aux node to move channels around between the visible channels and the auxiliary data channels inside a single 2D image. As a rule, those auxiliary channels come rendered out of 3D applications. Among the auxiliary channels the Copy Aux node handles you'll find z-depth and background color, texture coordinates plus coverage, object ID alongside material ID, normals together with vectors and back vectors, and world position as well. Copy Aux is largely a convenience node, given that the same copying can be pulled off, with more effort, through a Channel Booleans node. Channel Booleans works on individual channels, whereas Copy Aux works on channel groups. By default, the Copy Aux node lifts its output's depth on its own to line up with the aux channel's depth. Copy Aux supports static normalization ranges too. What static normalization has over the dynamic normalization Fusion's viewers perform is that the colors hold steady over time. Picture viewing the Z or WorldPos values for a ball: you get a smooth gradient running white to black. Now suppose a different 3D object enters the background at some point. Dynamic normalization washes the ball nearly all white while that background object becomes the new black. Dynamic normalization also brings on flicker trouble when you view vector/disparity channels, which can make visually comparing the aux channels of two frames at different times hard.

### Inputs

A pair of inputs belongs to the Copy Aux node, one for the main image and one for an effect mask. Input: Of these, the orange input is the only connection you have to wire. It brings a 2D image in for the Copy Aux node to act on. Effect Mask: The optional blue effect mask input takes in a mask shape drawn from polylines, basic primitive shapes, paint strokes, or bitmaps that other tools supplied. Attaching a mask here pins the Copy Aux operation to only the pixels lying within that mask. The tool has an effect mask applied to it after its processing wraps up.

### Basic Node Setup

Much like a great many 2D image-processing nodes, the Copy Aux node takes a 2D image such as a Loader node or the MediaIn1 below. From there its output keeps the node tree going by linking to another 2D imageprocessing node or a Merge node.

A Copy Aux node acting on a MediaIn1 node

### Inspector

### Copy Aux controls

### Controls Tab

You use the Controls tab to copy groups of auxiliary channels into the RGBA channels. Copy Aux carries a fair few options, yet most of the time you just pick the channel to copy and leave the rest of the functionality aside. Mode The Mode menu decides whether the auxiliary channel goes into the RGBA color channel (Aux to Color) or the other way round (Color to Aux). Leaning on this option, you can have one Copy Aux node pull an auxiliary channel into color, run a few compositing operations on it, then have a second Copy Aux node write the color back into the auxiliary channel. With Mode set to Color to Aux, every option on the Controls tab apart from the Aux Channel menu is tucked out of sight. Aux Channel The Aux Channel menu picks which auxiliary channel gets copied from or written to, according to the current mode. Suppose the aux channel abcd holds a single valid component; it then copies as aaa1. With two valid components it becomes ab01, with three it becomes abc1, and a full four components copy as abcd. So the Z-channel, to illustrate, copies as zzz1, while texture coordinates turn into uv01 and normals into nxnynz1. Out Color Depth Out Color Depth governs the color depth of the output image. The bulk of aux channels hold float values, or if they're integer valued they can hold values past 255. Copying float values into an int8 or int16 image can be a snag, since negative values and values over 1.0 stand to be clipped. Precision can slip away as well. This option sets what occurs if the input image's RGBA channel depth isn't enough to hold the copied aux channel. Take care copying float channels into integer image formats, because they can get clipped should you not configure Copy Aux properly. For this node, every aux channel counts as float32 apart from ObjectID or MaterialID, which count as int16.

- Match Aux Channel Depth: The output image's RGBA channels have their bit depth raised to meet the aux channel's depth. Put concretely, that makes the output image's RGBA channels either int16 or float32. Tread carefully with this option, because if your color channels are normally int8, for instance, you're now spending 2x or 4x the memory on them. In particular, the Z, Coverage, TextureCoordinate, Normal, Vector, BackVector, WorldPosition, and Disparity channels always come out as float, while the Material/ObjectID channels come out as int16.
- Match Source Color Depth: The output image's RGBA channels keep the same bit depth as the input image. That can lead to a few surprises. If your input image is int8, for example, the XYZ components of normals (floating-point numbers in the [-1, 1] range) get clipped down to the non-negative [0, 1] range. For a starker case, think about what becomes of Z values. Z values are floating-point numbers held in the [-1e30, 0] range, and they all get truncated into the [0, 1] range, leaving your Z-channel packed with zeroes.
- Force Float32: The output image's RGBA channels are always given a bit depth of float32.

Channel Missing Channel Missing settles what occurs when a channel isn't there. It governs, for instance, what happens when you've opted to copy Disparity to Color but your input image carries no Disparity aux channel.

- Fail: The node fails and writes an error message out to the console.
- Use Default Value: This loads the RGBA channels with the default value of zero for everything

except Z, where it's -1e30. Kill Aux Channels Tick this and Copy Aux copies the chosen channel into RGBA and then puts out an image that's nothing but RGBA, with the other channels killed off. It helps when you want to bump up how many Copy Aux frames can be cached for playback—say, to play back a long disparity sequence. One handy tip: you can also apply the Kill Aux feature with just Color to Aux > Color for a lengthier color playback.

### Kill Aux channels

Enable Remapping Switch remapping on and the aux channel you've got selected gets rescaled, mapping the range linearly per the From and To slider picks described below. The Remapping options run ahead of the conversion operation. So, ahead of any clipping, you might give the From > Min-Max values a setting of -1, 1 so your normals get rescaled into the [0, 1] range, or hand them [-1000, 0] so your Z values move out of [-1000, 0] and into the [0, 1] range.

Bear in mind the Remapping options operate per channel. As a result, normals can take a default scale of [-1, +1] > [0, 1], whereas Z can be handed [-1000, 0] > [0, 1]. Toggle between normals and Z and both settings are retained. This can pay off in that you're able to lay out the remapping ranges and save them as a setting to reuse later. Remapping comes in handy for squeezing the aux channels into a fixed [0, 1] range for viewing, or, for instance, when you'd like to compress normals into the [0, 1] range so they fit in an int8 image.

- From > Min: The aux channel value that lines up with To > Min.
- From > Max: The aux channel value that lines up with To > Max. You're allowed to make

the max value smaller than the min value, which flips/inverts the values.

- Detect Range: This sweeps the current image to find the min/max values, then sets the

From > Min/ From > Max Value controls to whatever it found.

- Update Range: This sweeps the current image to find the min/max values, then widens the

existing [From > Min, From > Max] region so it takes in the min/max values the sweep turned up.

- To > Min: The smallest output value, defaulting to 0.
- To > Max: The largest output value, defaulting to 1.
- Invert: After rescaling has carried everything into the [To > Min, To > Max] range, this

flips/inverts the range.

### Settings Tab

Here too the Inspector's Settings tab is mirrored across the rest of the Color nodes. You'll find these shared controls covered fully at the chapter's conclusion, in the “The Common Controls” section.

### Gamut [Gmt]

### The Gamut node

### Gamut Node Introduction

The Gamut node carries controls for converting one color space into another and for stripping out or adding gamma curves. This node, together with the Cineon Log node, mostly serves to linearize images coming in and then put the right output gamma curve back on at the tail end of a node tree.

### Inputs

The Gamut node comes with two inputs: one handling the main image and the other an effect mask for confining where the conversion applies. Input: This orange input is the lone connection you're required to make. It feeds in a 2D image output that serves as the source for the gamut conversion. Effect Mask: The optional blue effect mask input takes a mask shape fashioned from polylines, basic primitive shapes, paint strokes, or bitmaps that came from other tools. Wiring a mask to this input restricts the Gamut operation to just the pixels sitting inside that mask. An effect mask is laid on the tool after the tool has been processed.
