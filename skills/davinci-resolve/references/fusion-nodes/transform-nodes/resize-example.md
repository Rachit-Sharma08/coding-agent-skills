# Resize example

Version: DaVinci Resolve 20.3 Reference Manual. Context: Resize.
[Chapter index](INDEX.md) / [Previous section](resize.md) / [Next section](scale-and-transform.md) / [Resize Rsz](resize.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-example"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-the-resize-controls-tab"></a>

### Inputs

A single input on the Resize node exists for hooking up a 2D image to resize. Input: The orange input takes the primary 2D image you intend to resize.

### Basic Node Setup

In the example below, the Resize node is dropped in between the MediaIn1 node and the background input of the Merge. In contrast to a Transform tool, resizing MediaIn1 alters the clip's resolution. With the resized MediaIn1 node wired into the orange background input, it also fixes the resolution of the Merge output.

With the Resize node, an image can be scaled and its resolution altered.

### Inspector

### The Resize Controls tab

### Controls Tab

Parameters for changing the image's resolution live on the Controls tab. It works in pixel values across the Width and Height controls. Width This governs the image's fresh resolution along the X-axis. Height This governs the image's fresh resolution along the Y-axis. TIP: The formatting contextual menu lets you grab a resolution off a list in a hurry. Rest the mouse pointer over the Width or Height controls, then right-click to bring up the contextual menu. Down at the foot of the menu sits a Select Frame Format submenu listing the available frame formats. Pick any of the entries from the menu to set the Height and Width controls on their own. Auto Resolution Switching this checkbox on sets the Width and Height sliders automatically to the Frame Format settings found within the Preferences window for Fusion Studio, or to the resolution in the DaVinci Resolve Timeline. Reset Size Returns the image dimensions to the image's original size. Keep Frame Aspect Switched on, the Resize node holds the original image's aspect, keeping the original ratio between width and height. Only Use Filter in HiQ For any non-HiQ renders, where speed counts for more than full accuracy, the Resize node will usually fall back on the fast Nearest Neighbor filter. Switch this checkbox off to force Resize to use the chosen filter across all renders. Change Pixel Aspect Switch this checkbox on to reveal a Pixel Aspect control that serves to alter the image's pixel aspect.

Filter Method When a pixel is being rescaled, the pixels around it often get drawn on to yield a more realistic result. A range of algorithms exists for combining these pixels, called filters. The more intricate filters can yield better results yet usually take longer to compute. Which filter suits the job best tends to hinge on how much scaling is involved and on the contents of the image itself.

- Box: A plain interpolation-based resize of the picture.
- Linear: Leans on a bare-bones filter that turns out fairly clean, fast results.
- Quadratic: Turns out a middling result from this filter. Between

speed and quality it strikes a fair balance.

- Cubic: Turns out stronger results on continuous-tone pictures. Where the pictures hold fine detail,

the outcome can come out blurrier than you'd want.

- Catmull-Rom: Turns out solid results on continuous-tone pictures scaled down.

On finely detailed pictures it yields sharp results.

- Gaussian: Sits very close to Bi-Cubic in both speed and quality.
- Mitchell: Resembles Catmull-Rom yet turns out stronger results on finely detailed pictures.

Compared to Catmull-Rom it runs slower.

- Lanczos: Sits very close to Mitchell and Catmull-Rom, just a touch cleaner and a touch slower as well.
- Sinc: A high-end filter delivering exceptionally sharp, detailed results; that said, it can throw

visible "ringing" under certain conditions.

- Bessel: Resembles the Sinc filter though it may run a shade faster.

Window Method (Sinc and Bessel Only) Certain filters, Sinc and Bessel among them, would need an endless supply of pixels to compute precisely. To hasten this operation, a windowing function steps in to approximate the filter and cap the count of pixels needed. This control shows up once a filter calling for windowing is chosen.

- Hanning: A plain tapered window.
- Hamming: Hamming is a lightly adjusted take on Hanning that stops short of tapering all the

way down to zero.

- Blackman: A window whose falloff tapers more sharply.
- Kaiser: A more intricate window yielding results between Hamming and Blackman.

The bulk of these filters earn their keep only when you're enlarging an image. For shrinking images, the Bi-Linear filter is the common pick; the Catmull-Rom filter, though, lends a measure of sharpening to the results and can help hold onto detail while scaling an image down.

### Example

Assorted resize filters, ordered left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic, then Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel.

### Common Controls

Settings Tab The Settings tab in the Inspector also has a duplicate across other Transform nodes. These shared controls get a full description toward the end of this chapter under the "The Common Controls" section.
