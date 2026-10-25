# Custom tool value variables n1 n8 p1x p4x p1y p4y s1 s4

Version: DaVinci Resolve 20.3 Reference Manual. Context: Custom tool.
[Chapter index](INDEX.md) / [Previous section](auto-domain-and-change-depth.md) / [Next section](custom-tool-channel-variables-and-pixel-sampling.md)
<a id="source-basic-node-setup-2"></a> <a id="source-controls-tab-2"></a> <a id="source-custom-tool-channels-tab"></a> <a id="source-custom-tool-config-tab"></a> <a id="source-custom-tool-ct"></a> <a id="source-custom-tool-intermediate-tab"></a> <a id="source-custom-tool-node-introduction"></a> <a id="source-custom-tool-node-syntax"></a> <a id="source-custom-tool-setup-tab"></a> <a id="source-inputs-2"></a> <a id="source-inspector-2"></a> <a id="source-the-custom-tool-channel-tab"></a> <a id="source-the-custom-tool-config-tab"></a> <a id="source-the-custom-tool-controls-tab"></a> <a id="source-the-custom-tool-intermediate-tab"></a> <a id="source-the-custom-tool-node"></a> <a id="source-the-custom-tool-setup-tab"></a> <a id="source-value-variables-n1n8-p1xp4x-p1yp4y-s1s4"></a>

### Custom Tool [CT]

### The Custom Tool node

### Custom Tool Node Introduction

Among all of Fusion’s nodes, the Custom Tool node stands out as both the most intricate and the most potent. Its job is to build custom expressions and filters that reshape an image. Beyond the three image inputs it hands you, the Custom Tool node permits hooking up as many as eight numeric inputs along with up to four XY position values pulled from other controls and parameters across the node tree. The images open up per-pixel calculations over a whole roster of channels: the Red, Green, and Blue trio, then Alpha, plus Z together with Z-Coverage; the UV texture coords sit alongside the XYZ Normals, while the RGBA background color and the XY motion vector round things out. A fair bit of experience with scripting, or with C++ programming, will help you make sense of the structure and terminology the Custom Tool node leans on.

### Inputs

Three image inputs, one matte input, and one effect mask input belong to the Custom Tool node. Input: To form your composite, the orange, green, and magenta inputs blend 2D images together. Once keyed into the Custom Tool fields, they go by c1, c2 and c3 (here c stands across all three of the R, G, B channels) Matte Input: A matte built with polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools feeds the white input. Tying a matte to this input lets a matte fold into whatever equation you like. Keyed into the Custom Tool fields, that matte goes by m1. Effect Mask: The blue input takes a mask shape drawn with polylines, basic primitive shapes, paint strokes, or bitmaps out of other tools. Tying a mask to this input pins the Custom Tool effect down to only the pixels inside the mask.

### Basic Node Setup

Shown below, the Custom Tool draws in two image inputs and a matte input, then fuses them by way of some calculation. Its result may then pass along to a Merge or to further image-processing nodes. A Custom Tool serves to craft effects of your own out of C++ and scripting.

### Inspector

### The Custom Tool Controls tab

### Controls Tab

Point in 1-4, X and Y This set of four controls are 2D X and Y center controls that expressions keyed into the Setup, Intermediate, and Channels tabs can reach as variables p1x, p1y, ...., p4x, p4y. Behaving as ordinary positional controls, they may be animated or tied to modifiers just as any other node could. Number in 1-8 Whatever these controls hold becomes reachable by expressions keyed into the Setup, Intermediate, and Channels tabs as variables n1, n2, n3, ..., n8. Behaving as ordinary slider controls, they too may be animated or tied to modifiers precisely as any other node could. LUT in 1-4 What the Custom Tool node supplies here is 4 LUT splines. Whatever these controls hold reaches expressions keyed into the Setup, Intermediate, and Channels tabs by way of the getlut# function. As one example, pointing the R, G, B, and A expressions at `getlut1(r1)`, `getlut2(g1)`, `getlut3(b1)`, and `getlut4(a1)`, in turn, would have the Custom Tool node act like the Color Curves node. The options under the Config tab let you rename these controls so their meaning reads more plainly, yet expressions go on reading the values as n1, n2, ..., n8.

### The Custom Tool Setup tab

### Custom Tool Setup Tab

Setup 1-4 As many as four distinct expressions can be worked out within the Custom Tool node’s Setup tab. The Setup expressions run a single time per frame ahead of every other calculation. Their results then reach the rest of the Custom Tool node’s expressions as variables s1, s2, s3, and s4. NOTE: Since these expressions fire just once per frame rather than for each pixel, reaching for per-pixel variables such as X and Y or channel variables such as r1, g1, b1 serves no purpose. The values you may use take in constants, variables such as n1..n8, time, W and H, plus functions such as `sin()` or `getr1d()`.

### Custom Tool Intermediate Tab

Intermediate 1-4 One more set of four expressions can be worked out within the Inter tab. The Inter expressions run once per pixel after the Setup expressions have run yet ahead of the Channel expressions. You may use per-pixel channel variables such as r1, g1, b1, and a1. Their results come through as variables i1, i2, i3, and i4.

### The Custom Tool Intermediate tab

### Custom Tool Config Tab

Random Seed Lean on this to fix the seed behind the `rand()` and `rands()` functions. A click of the Randomize button drops a random value into the seed. You might call on this control whenever several Custom Tool nodes are wanted, each yielding its own different random results.

### The Custom Tool Config tab

Number Controls Eight sets of Number controls are present, each lining up with one of the eight Number In sliders in the Controls tab. Clearing the Show Number checkbox tucks away the matching Number In slider, while editing the Name for Number text field renames it. Point Controls Four sets of Point controls are present, each lining up with one of the four Point In controls in the Controls tab. Clearing the Show Point checkbox tucks away the matching Point In control along with its crosshair in the viewer. In like manner, editing the Name for Point text field renames the control.

### The Custom Tool Channel tab

### Custom Tool Channels Tab

RGBA, Z, UV Expressions, and XYZ Normal Expressions Through the Channel tab you lay out one expression for every channel the image makes available. Each such expression runs once per pixel. Out of that comes the value carried by that pixel in the image’s output. As a rule, Color Channel expressions (RGBA) ought to hand back floating-point values between 0.0 and 1.0. Anything past that gets clipped should the destination image be an integer. The remaining expression fields ought to yield values fitting their channel (e.g., between -1.0 and 1.0 for Vector and Normal fields, 0.0 to 1.0 for Coverage, or any value at all for Depth). The Channel expressions are free to draw on the results of both the Setup expressions (as variables s1–s4) and the Inter expressions (as variables i1–i4).

### Custom Tool Node Syntax

### Value Variables n1..n8 p1x..p4x p1y..p4y s1..s4

Numeric Inputs Position Values (X-axis) Position Values (Y-axis) Setup Expression Results

Value Variables i1..i4 time x y w (or w1..w3) h (or h1..h3) ax (or ax1..ax3) ay (or ay1..ay3)

Inter Expression Results Current Frame The current pixel’s horizontal co-ordinate, lying between 0.0 and 1.0 The current pixel’s vertical co-ordinate, lying between 0.0 and 1.0 Width of Image (for image1..image3) Height of Image (for image1..image3) Image Aspect X (for image1..image3) Image Aspect Y (for image1..image3)

NOTE: Drop any trailing number off w, h, ax, and ay to pull the primary image’s dimensions and aspect.

Channel (Pixel) Variables c1..c3 r1..r3 g1..g3 b1..b3 a1..a3 z1..z3 cv1..cv3 u1..u3 v1..v3 nx1..nx3 ny1..ny3 nz1..nz3 bgr1..bgr3 bgg1..bgg3 bgb1..bgb3 bga1..bga3 vx1..vx3

Current Channel (for image1..image3) Red (for image1..image3) Green (for image1..image3) Blue (for image1..image3) Alpha (for image1..image3) Z-Buffer (for image1..image3) Z Coverage (for image1..image3) U Coordinate (for image1..image3) V Coordinate (for image1..image3) X Normal (for image1..image3) Y Normal (for image1..image3) Z Normal (for image1..image3) Background Red (for image1..image3) Background Green (for image1..image3) Background Blue (for image1..image3) Background Alpha (for image1..image3) X Vector (for image1..image3)
