# Stereo align and z to disparity

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereo align, Z to disparity.
[Chapter index](INDEX.md) / [Previous section](splitter-and-stereo-align.md) / [Stereo Align SA](splitter-and-stereo-align.md)
<a id="source-basic-node-setup-4"></a> <a id="source-common-controls-4"></a> <a id="source-example"></a> <a id="source-inputs-4"></a> <a id="source-outputs-4"></a> <a id="source-the-z-to-disparity-node"></a> <a id="source-z-to-disparity-node-introduction"></a> <a id="source-z-to-disparity-z2d"></a>

### Common Controls

Settings Tab On the remaining Stereo nodes this Inspector Settings tab is likewise present. Detailed write-ups of these common controls come at the chapter's end within the "The Common Controls" section.

### Example

Different settings for Eye Separation…

…and example settings for Convergence

### Z To Disparity [Z2D]

### The Z To Disparity node

NOTE: Fusion Studio and DaVinci Resolve Studio are the only places the Z To Disparity node appears.

### Z To Disparity Node Introduction

Handed a stereo camera plus an image carrying a Z channel, Z To Disparity returns that same image now holding disparity channels. It's handy for building a Disparity map out of CG renders, one that will beat the accuracy of the Disparity map the Disparity node makes.

### Inputs

You wire the left and right images plus a camera node into the three inputs on the Z To Disparity node. Left Input: Either the left eye image or the stack image hooks into the orange input. Right Input: The right eye image hooks into the green input. That input is on hand only while the Stack Mode menu is set to Separate. Stereo Camera: A stereo perspective camera connects through the magenta input; that can be a Camera 3D set with eye separation, or alternatively a tracked L/R Camera 3D.

### Outputs

Differing from most Fusion nodes, Z To Disparity carries two outputs, one per eye. Left Output: Out of this comes the left eye image now holding a fresh disparity channel, or else a Stacked Mode image equipped the same way. Right Output: Out of this comes the right eye image now holding a fresh disparity channel. That output is visible only if Stack Mode sits on Separate.

### Basic Node Setup

In the example below, a stereo camera together with an image carrying a Z channel feeds a Z To Disparity node. That same image comes out bearing disparity channels.

A Z To Disparity node that accepts a Z-channel image and builds a disparity channel from it Inspector
