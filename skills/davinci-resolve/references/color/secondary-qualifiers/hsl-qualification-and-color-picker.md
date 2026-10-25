# Basic qualification using the hsl qualifier and color picker button

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary qualifiers.
[Chapter index](INDEX.md) / [Previous section](color-3183-and-image-with-a-simple-primary-correction.md) / [Next section](draggable-qualifier-controls-and-hsl-qualification-controls.md)
<a id="source-add-and-subtract-color-buttons"></a> <a id="source-add-and-subtract-qualifier-softness"></a> <a id="source-altered-color-balance-of-the-ocean-and-sky"></a> <a id="source-basic-qualification-using-the-hsl-qualifier"></a> <a id="source-color-picker-button"></a> <a id="source-example-image-to-qualify"></a> <a id="source-high-contrast-bw-highlighting"></a> <a id="source-hsl-qualifier-presets"></a> <a id="source-oranges-qualified-and-highlighted"></a> <a id="source-qualifier-parameters"></a> <a id="source-secondary-qualifiers-part-2"></a> <a id="source-showing-picker-rgb-values"></a> <a id="source-the-color--presets-menu"></a> <a id="source-using-highlight-to-see-what-youre-isolating"></a> <a id="source-using-highlight-to-solo-nodes"></a>

### Basic Qualification Using the HSL Qualifier

The HSL qualifier ranks among the most flexible tools in DaVinci Resolve. Using any mix of sampled hue, saturation, and luma, you can carve out separate color and contrast ranges for targeted adjustment. As a general-purpose keyer, HSL lets you key any color at all; it's not held to blue or green. Sampling the image in the Viewer is the most direct way to drive any qualifier. Four controls let you sample image pixels in various ways. Sample one or more pixels and the Hue, Saturation, and Luma values are analyzed, then distinct ranges get set across each of the Hue, Saturation, and Luma qualifier controls. A number of different eyedropper controls stand ready to govern how you sample color in the image.

- Sample Eyedropper: The first control you reach for any time you sample the image. It sets the qualification's initial range; you have to use this tool ahead of any of the others. A single click of it picks one pixel value, whereas clicking and dragging picks a span of image values that combine.

### Color Picker button

- Add/Subtract Color Range: These two controls let you add image areas to, or take them away from, the currently selected inner range of values forming the key's core. As with the eyedropper, you can click single pixels or drag over a range of color.

### Add and Subtract color buttons

- Add/Subtract Softness: With this pair of controls you reshape the softness that eases out from the key's inner range, tapering toward its outer edge. As with the other controls, single-pixel clicks or a drag across a color range both work.

### Add and Subtract qualifier softness

NOTE: Once you select one of the sampling controls, it stays selected until you select another. If you select a different clip in the Timeline, then click the Viewer to sample a key and nothing happens, make sure you've selected the Eyedropper control in the Qualifier palette. When you're working with the DaVinci Resolve onscreen interface, the simplest way to qualify a subject is to use the pointer alongside the sampling controls.

### Example image to qualify

To single out a subject in the Viewer via the HSL Qualifier mode: 1 Open the Qualifier palette, set the mode drop-down to HSL, and click the eyedropper. 2 Either click one pixel of the part you want isolated, or click and drag over a span of pixels inside that subject.

Picking to qualify the ocean 3 To watch the key take shape as you go, click the Highlight button in the Viewer Options toolbar atop the Viewer. By default, the area you're isolating shows in color while the excluded area shows solid gray.

Viewer image with the highlight on; the isolated region shows in color and the omitted region shows gray Even with the highlight covering the rest of the image, you're still free to use the sampling tools to pick pixels you can't see. 4 To take away from the inner range of the key you're building, click the minus Color Range control, then click or drag over whatever portion of the keyed image you want excluded. 5 To put softness onto the key's outer range, click the plus Softness control, then click or drag over whatever portion of the image you want brought in as a soft edge. After you've worked the range and softness sampling controls to refine the key that isolates your subject, nearly every key you pull will gain from a little further "post-key" refinement. Here's what that comes down to: with the best procedural key built through image sampling, the resulting key itself, no more than a grayscale image, is now yours to adjust toward a better isolated result. That's the purpose of the Matte Finesse controls.

Matte Finesse controls

6 With the Matte Finesse controls, the three go-to refinement moves are bumping up Clean Black to plug "holes" in the parts you're discarding (the background), bumping up Clean White to seal holes in the part you're isolating (the foreground), and then turning to the Blur Radius and In/Out Ratio controls to feather the key's edge and shift it inward or outward. Such controls let you dramatically better nearly any key with no endless return to the Qualifier controls. Further detail on the Matte Finesse controls comes later in this chapter. 7 Once finished, click the Highlight control so the highlight turns off, then apply whatever adjustment is called for. Here, saturation has been raised and the color balance shifted to make the adjustment plain.

### Altered color balance of the ocean and sky

### HSL Qualifier Presets

A collection of HSL Qualifier presets, also known as Six Vector presets, is available for automatically singling out a predefined color wedge (green, blue, red, magenta, yellow, or cyan) or a chroma intensity (chroma light, chroma dark, or both). You reach these presets either through the Color > Presets menu or through the DaVinci Resolve Advanced control panel. Picking one of these presets automatically sets the HSL Qualifier to the matching range of color or lightness. Afterward you can keep modifying the HSL Qualifier to suit your purpose.

### The Color > Presets menu

### Using Highlight to See What You're Isolating

Sitting atop the Viewer, the Highlight control (which appears once Viewer Options is switched on from the Viewer's Option menu) draws a representation of the key under construction over the current image in the Viewer. Overlays are mirrored to your video output too, so they'll appear on an external display as well, in case you're hiding the onscreen Viewer. There are two kinds of highlight for evaluating a qualification you're building. Each suits different tasks. Flat-Gray: The default highlight DaVinci Resolve uses shows the selected portion of the image in its original colors and the unselected portion in a flat gray. It's handy for seeing the subject you're isolating even while you adjust the Qualifier controls, which lets you also watch the color or contrast adjustments you're applying at the same time.

### Oranges qualified and highlighted

High-Contrast: Hitting Option-Shift-H gives you what's termed a "high-contrast" highlight, one you'll recognize if other color correction applications and plugins are part of your past; this more conventional display paints the selected portion of the image white and the unselected portion black. The high-contrast highlight is useful when you need to eliminate holes in a key, or gauge how "chattery" a key is, since irregularities stand out more once they're divorced from the original image.

### High-Contrast B&W highlighting

To enable or disable a highlight, do one of the following:

- Up in the Viewer Options toolbar atop the Viewer, click the Highlight control, then pick the highlight type you're after from the buttons that turn up on the right.
- Pick an option out of the Highlight submenu within the Viewer's option menu; Shift-H gives a regular Highlight.

To switch a high-contrast highlight on or off, take one of these routes:

- From the Viewer's option menu, choose Highlight > Highlight BW (Option-Shift-H).

To set high-contrast black and white as the default highlight: 1 Open the Preferences > User > Color window. 2 Tick "Mattes display high contrast black and white." 3 Click Save. The next click of the Highlight control in the Qualifier palette brings up the high-contrast highlight.

### Using Highlight to Solo Nodes

There's one more job the Highlight control does: it solos single nodes in the Viewer and video out instead of sending the sum of the entire node tree. Suppose you're adjusting a stack of nodes wired into a Parallel or Layer Mixer node; tuning one node of that stack is hard to see, since only the final result goes out. Switch Highlight on while a keyless node is selected, however, and only that selected node is sent, so viewing a lone node as you tune it becomes easy. Be sure, though, to turn Highlight off before you carry on, or you risk confusing yourself.

### Showing Picker RGB Values

As you drag the pointer across the Viewer in search of a feature to sample, a tooltip displaying the RGB Value of the pixel under the pointer can be enabled: right-click the Viewer and pick Show Picker RGB Value to flip the feature on and off. Once it's on, the Show RGB Picker Values In submenu, found in the Viewer's option menu, offers choices for showing either 8- or 10-bit tristimulus values.

The Color Picker tooltip that shows up once you switch on show RGB Picker Values

### Qualifier Parameters

Each Qualifier mode, the 3D qualifier aside, carries parameters matching the relevant color components for that mode, with which you can pin down a range and softness, much as you would with the sample tools. You can edit these parameters precisely with virtual sliders using the pointer, or with the knobs of a supported grading control panel. Mouse and tablet users, however, can lean on each qualifier's draggable white overlays for more direct adjustment.

- Pull the left or right edge of a qualifier control overlay to set the Low and High values (or, on the Hue control, its Width value).
- Pull on the middle of any qualifier control to shift the center, or to move the Low and High parameters in tandem.
- Hold Option while dragging an overlay's left or right edge to set softness. This drag behavior applies to the HSL, RGB, and LUMA qualifier controls (the 3D qualifier behaves in its own way).
