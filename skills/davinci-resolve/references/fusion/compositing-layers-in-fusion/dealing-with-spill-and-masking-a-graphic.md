# Dealing with spill and masking a graphic

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing layers in Fusion.
[Chapter index](INDEX.md) / [Previous section](transform-controls-in-the-merge-node-and-final-composite.md)
<a id="source-dealing-with-spill"></a> <a id="source-masking-a-graphic"></a> <a id="source-selecting-the-crop-tool-in-the-viewer-toolbar"></a>

### Dealing with Spill

Whatever screen color bounces off the background and falls onto your subject, the DeltaKeyer is able to deal with it. That reflected screen light goes by the name spill. Still, rather than letting a single node take care of both building the matte and fixing the spill, think about switching this off inside the DeltaKeyer and stripping the spill out with a dedicated color correction node instead. Switch off spill suppression in the DeltaKeyer like so.

- Select the matte tab in the Inspector.
- In the Replace Mode drop-down menu, pick Source. Doing that draws on the color taken from the original

source image, effectively disabling any spill correction in the DeltaKeyer.

Within the DeltaKeyer, the Replace Mode menu is what governs the way spill suppression behaves

You can now take care of spill with a color correction node dropped straight after the DeltaKeyer, or split off from the original MediaIn or Loader node and joined back together through a MatteControl.

Splitting the original image into two paths, one feeding the DeltaKeyer and the other feeding color correction

### Masking a Graphic

It is now time to deal with the top video track: the news graphic meant to sit to the newscaster's left. Since the graphic we are using is really one sheet holding several logos, we have to isolate a single logo with a mask and drop it into position.

A single graphic carrying several logos, which has to be trimmed down so only one remains. The simplest route to cropping a MediaIn or Loader node is attaching one of the toolbar's mask shapes straight onto it. With the MediaIn or Loader node selected, clicking the Rectangle mask in the toolbar will crop, or mask off, the graphic.

Masking off the logo with a Rectangle mask wired straight into a Merge node

From here, the only remaining task is to drive the Rectangle mask's onscreen controls to trim down to the region we want, sliding the mask around with the center handle and scaling it by pulling the top/bottom and left/right handles along the outer border. On top of that, you can deal with rounded corners while masking a graphic by reaching for the Corner Radius slider in the Rectangle mask's Inspector controls to apply that same rounding.

Shifting and scaling the mask so it frames our logo, then softening the corners by way of the Corner Radius Inspector control. On a basic over-the-shoulder graphic, masking the image might be the whole job, yet masking an image leaves the graphic's real dimensions untouched. All it alters is the portion you can see. As a result, placing the graphic precisely relative to the composite's center grows trickier, and any sort of match move would come out wrong since the graphic's resolution differs from the background's. You can correct this resolution mismatch by adding a Crop node after the MediaIn so the graphic layer's actual dimensions change.

Placing a Crop node downstream of the masked MediaIn so the trimmed logo sits centered over the background. Once the Crop node is selected, a Crop tool appears in the viewer toolbar.

### Selecting the crop tool in the viewer toolbar

Crop the image by dragging a bounding box around it. Whereas a mask just opens a small window you peer through, a crop genuinely resets the graphic's resolution to match the size of the crop bounding box.

At left, a bounding box being dragged with the Crop tool; at right, the trimmed logo sitting centered in the frame. NOTE: An image's resolution is likewise altered by the Resize, Letterbox, and Scale nodes. We are now ready to move the logo into position. Since the logo feeds the foreground input of a Merge, you can pick the Merge2 node, load it into the viewer, and rely on the built-in Center X and Y controls or the onscreen controls to drop the logo wherever you like and size it appropriately.

Positioning the logo by way of the Merge2 node's foreground input transform controls
