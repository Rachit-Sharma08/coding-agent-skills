# Looks and adjustments

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Previous section](overlay-and-scopes.md) / [Next section](deliver-page-in-photo-album-mode-and-render-settings.md)
<a id="source-adding-luts-to-your-photos"></a> <a id="source-adjustments"></a> <a id="source-effects"></a> <a id="source-exporting-from-the-deliver-page"></a> <a id="source-file"></a> <a id="source-file-data"></a> <a id="source-inspector-option-menu"></a> <a id="source-looks"></a> <a id="source-metadata"></a>

### Looks

- Type: Lets you place preset look filters onto the photo. Pick one from the dropdown menu, or leave it on Default (Original) to skip the look filters.
- Intensity: Controls the strength at which the look filter blends into the picture.

### Adjustments

- Auto Balance: A single-button option that sets the parameters below automatically by way of machine learning.
- Temp: Lets you slide the image along a warm/orange to cool/blue axis matching the natural span of color temperatures used in lighting. Raising this control shifts the color balance toward orange, while pushing it negative shifts the color balance toward a blue/cyan.
- Tint: Lets you slide the image along a magenta-to-green axis matching the unnatural span of color temperatures from artificial lighting sources such as fluorescent and sodium vapor fixtures. Raising this control shifts the color balance toward magenta (often called “minus green” to fix fluorescent lighting), while pushing it negative shifts the color balance toward green (“plus green” to fix other kinds of lighting).
- Lift: Lets you change the perceived shadow density by moving the image’s black point. Dragging the Lift slider left darkens the darkest values, widening the gap between the image’s black and white points and stretching all the midtones in between. Dragging the Lift slider right lightens the darkest values, cutting contrast and squeezing all the midtones between the black and white points.
- Gamma: Lets you change the overall perceived brightness by reshuffling those midtones lying in between where the Lift and Gain master wheels are set. Push the Gamma master wheel toward the left and the whole image darkens; push it right and the image brightens.
- Gain: Lets you change the brightness of the highlights by moving the image’s white point. Dragging the Gain slider left darkens the lightest values, squeezing the midtones between the image’s white and black points. Dragging Gain right brightens the lightest values further, eventually clipping at maximum white.
- Contrast: The Contrast parameters let you swiftly narrow or widen image contrast about a userdefinable pivot point. This single parameter raises or lowers the gap between an image’s darkest and lightest values, increasing or decreasing image contrast.
- Pivot: Moves the tonal center about which the dark and bright parts of the image are stretched or pinched during a contrast adjustment. Darker images may need a lower Pivot value to avoid crushing the shadows too hard when contrast is stretched, while lighter images may gain from a higher Pivot value to build adequate shadow density.
- Midtone Details: Raising this control lifts the contrast in image regions rich in edge detail to heighten the sense of sharpness, an effect sometimes called definition. Pushing it to a negative value softens regions that hold little detail while leaving high-detail areas alone.
- Shadows: Lets you selectively brighten or darken shadow detail. Raising this value recovers shadow detail captured below 0 percent while leaving the midtones untouched.
- Highlights: Makes it simple to win back blown-out highlight detail in high-dynamic-range media by lowering this control, blending the recovered highlights smoothly into the untouched midtones for a natural look.
- Saturation: A consistent saturation move that, when set above 50 boosts — or below 50 cuts — the color intensity of each color value across the picture. At 50 it is unity and saturation stays as it was. Its span goes from 0 (completely desaturated) up through +100 (saturation is doubled).
- Hue: Spins every hue of the image right around the full circumference of the color wheel. With 50 as the default, the original spread of hues is kept. Nudging this value up or down sends all the hues forward or back along that hue spread as it would appear on a color wheel.

### Effects

When you have applied an effect from the Effects tab to your photo, its parameters can be tuned here. With no effect applied, this tab appears grayed out. NOTE: You will find full coverage of every effect within the Resolve FX portion of the DaVinci Resolve Reference Manual

### File

These settings present data about your file format and let you edit commonly used metadata fields.

### File Data

- File Name: The file name of the photo.
- Star Rating: Lets you grade the photo anywhere from one star up to five.
- ISO: Shows the ISO setting that the photo was shot with.
- Shutter Speed: Shows the shutter speed that the photo was shot with.
- Aperture: Shows the lens aperture that the photo was shot with.
- White Balance: Shows the current white balance setting from the RAW controls.
- Image Format: Shows the image file format.
- Resolution: Shows the source resolution of the image.
- Color Space: Shows the current Color Space setting from the RAW controls.

### Metadata

- Date Created: Adjust the date that the photo was taken.
- Camera: For sorting and organization, lets you record a camera name, letter, or number.
- Tag: For sorting and organization, lets you mark a photo Good, Untagged, or Rejected.
- Keywords: For sorting and organization, lets you attach keywords to the photo.
- Color: For sorting and organization, lets you give the photo a color code.
- Name: Lets you change the photo’s name as it appears in the media pool. Altering this name does

not change the original file name.

- Comments: Lets you add comments that are attached to the photo.
- Flags: For sorting and organization, lets you attach a color flag to the photo.
- Auto Select Next Photo: With this box ticked, hitting the return button after you finish a metadata field automatically selects the next photo in the Media Pool

and drops the cursor into that same field. This lets you race through metadata one photo after another without clicking to load each photo manually in the Media Pool.

- Next Photo: This button selects the next photo in the Media Pool no matter how the Auto Select Next Photo checkbox is set.

### Inspector Option Menu

- Reset Photo: (Command-R) Resets any adjustments made in the Photo tab.
- Remove All Photo Effects: (Shift-R) Strips off whatever effects you had placed onto the picture.
- Reset Camera Raw: Returns each RAW adjustment you made on the RAW tab to its default state.
- Remove and Reset All: (Shift-Command-R) Clears every applied effect and returns the image

to it’s original state.

### Adding LUTs to your Photos

Once you have installed a custom or ready-made look up table (LUT) into DaVinci Resolve, a LUT can be applied to any photo in the Media Pool or the Photo Album. Just right-click the photo’s thumbnail and pick the LUT from the LUT context menu.

### Exporting from the Deliver Page

You get finer control over exporting still photos from the Deliver page. Clicking Deliver while an Album is active opens a dedicated export view built for stills.
