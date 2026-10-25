# Viewer and subview types and magnifier

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using viewers.
[Chapter index](INDEX.md) / [Previous section](viewer-subview-selection.md) / [Next section](display-red-channel-and-display-green-channel.md)
<a id="source-color-inspector"></a> <a id="source-full-rgb-color-display"></a> <a id="source-magnifier"></a> <a id="source-vectorscope"></a> <a id="source-viewer-and-subview-types"></a> <a id="source-viewing-color-channels"></a> <a id="source-viewing-selective-channels"></a> <a id="source-waveform"></a>

### Viewer and Subview Types

A viewer can present many kinds of information about the image, yet not every view type is on hand at any given moment. The 3D Viewer, for example, isn’t offered for a 2D node, and several of the measurement viewers exist only as subviews. What follows is detailed coverage of the various view types. Navigator The Navigator is a subview-only view. It gives a compact overview of the whole image, with a rectangle marking the slice of the image presently visible in the main viewer. That comes in handy when you’ve zoomed into an image in the main view.

The Navigator subview for panning the image while zoomed in

### Magnifier

The Magnifier works in a subview only. It presents an enlarged view of the pixels sitting beneath the cursor over in the main viewer.

The Magnifier subview, showing an enlarged rendering of the image

The subview serving as a second viewer A 3D Image Viewer placed in a subview

2D Viewer The default view type for displaying images is the 2D Viewer. As a subview, it can show a different node than the one in the main viewer, which you set by dragging that node into the subview. It is the only subview type that isn’t merely an alternate view of the main viewer’s node. 3D Image Viewer You get the 3D Image Viewer whenever a node from the 3D category is being viewed. Image Info The Image Info view exists only as a subview. Its tab places a horizontal bar along the top of the image carrying details about the viewed image’s frame size, pixel aspect, and color depth.

The Image Info subview, used to read size, pixel aspect, and color depth details The Color Inspector subview, used to assess the colors in an image

### Color Inspector

The Color Inspector works in a subview only. It reports on the color channels of whichever pixel sits beneath the cursor. Every channel present is shown, including auxiliary ones such as Z buffer, XYZ normals, and UV mapping channels.

The 3D Histogram Viewer type, used to assess out-of-range colors The Histogram Viewer type, used to assess an image’s contrast and color cast The Metadata subview, used to read embedded metadata

3D Histogram The more sophisticated 3D Histogram Viewer plots an image’s color distribution inside a 3D cube. A benefit of a 3D Histogram is its faithful depiction of the out-of-range colors that frequently turn up in floating-point and high-dynamic-range images. It can likewise be used to inspect vector images such as position, normal, velocity, and the like. To rotate within a 3D Histogram, do one of the following:

- With the Option key held, drag to the left or right while using the middle mouse button.
- Keep both the middle and right mouse buttons pressed as you drag.

Histogram The Histogram Viewer is an analysis node useful for spotting trouble with an image’s contrast and dynamic range. Its graph plots the frequency distribution of the image’s colors, out-of-range colors in floating-point images included. Colors run along the horizontal axis from shadows toward highlights, while the vertical axis counts how many of the image’s pixels land at each level. The Histogram Viewer can also show gradient information. Gradients can be produced with the From Image and Perturb modifiers; to view one represented within a histogram, drag that modifier’s title bar onto the viewer. Metadata Exactly how much this subview shows hinges entirely on how much metadata your image carries. Most Loaders supply the image’s color space and file path, and far more can appear when the image holds it.

### Vectorscope

The Vectorscope Viewer mimics the behavior of a particular kind of video test instrument, showing a circular graph that aids in visualizing the strength of chrominance signals.

The Vectorscope Viewer type for evaluating chrominance in an image

### Waveform

The Waveform Viewer mimics the behavior of a particular kind of video test instrument, showing a line or bar graph that aids in visualizing a broadcast signal’s voltage or luminance.

The Waveform Viewer type for evaluating luminance in an image

### Viewing Selective Channels

In compositing you work just as often with an image’s individual color components or channels as you do with the whole image’s full RGB color. Both the viewers and the subviews can isolate and display the color, alpha, depth channels, and even the auxiliary channels that comprise the image.

### Viewing Color Channels

The full RGB color channel appears by default, but the channel on display can be changed three ways: through the Channel toolbar button, through the viewer’s contextual menu, or via keyboard shortcuts. To switch between the RGB and alpha channels in whichever viewer is active:

- In the viewer toolbar, click the Color button to flip between full RGB color and that image’s alpha channel.

The Channel toolbar button for switching between color, alpha, and depth channels

To toggle the channel that’s displayed in the active viewer:

- Click the arrow just right of the Color button to pick one specific channel to view from the current image’s list of available channels.
- Click the viewer you intend to toggle, then hit one of these keyboard shortcuts;

C

### Full RGB color display

R
