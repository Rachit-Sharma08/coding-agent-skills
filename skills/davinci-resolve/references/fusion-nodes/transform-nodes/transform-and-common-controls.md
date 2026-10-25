# Transform and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Transform, Common controls.
[Chapter index](INDEX.md) / [Previous section](scale-and-transform.md) / [Next section](common-controls-settings-tab.md) / [Continue The Common Controls / Settings Tab](common-controls-settings-tab.md) / [Transform XF](scale-and-transform.md)
<a id="source-basic-node-setup-2"></a> <a id="source-controls-tab-2"></a> <a id="source-example-2"></a> <a id="source-inspector-2"></a> <a id="source-the-common-controls"></a> <a id="source-the-transform-controls-tab"></a>

### Basic Node Setup

The Transform node in the example below is dropped in between the MediaIn2 node and the foreground input of the Merge. In contrast to a Scale or Resize tool, transforming MediaIn2 leaves the clip's resolution untouched. That makes it the tool most often reached for to scale, move, and rotate a clip.

Via the Transform node, an image can be scaled while its resolution stays the same.

### Inspector

### The Transform Controls tab

### Controls Tab

A range of approaches to transform, flip (vertical), flop (horizontal), scale, and rotate an image sits on the Controls tab. Reference size controls ride along too, able to reinterpret the width and height coordinates — from relative values of 0-1 over into pixel values keyed to the image's resolution. Center X and Y Where the image sits on the screen is set here. Its default, 0.5, 0.5, drops the image dead center on the screen. Whatever value appears is always the real position multiplied by the reference size. A rundown of the reference size follows below. Pivot X and Y Where the axis of rotation and scaling lands is set here. Its default, 0.5, 0.5, falls on the image's center. Use Size and Aspect This checkbox settles whether the Transform node hands you independent Size controls for the X and Y scale, or whether Size and Aspect controls get used instead. Size This reshapes the image's scale. Values run from 0 to 5, though any value above zero can be typed into the edit box. With the Use Size and Aspect checkbox ticked, this control scales the image equally along both axes. With the Use Size and Aspect option off, separate control is supplied for X and Y. Aspect An image's aspect ratio gets altered by this control. Push the value above 1.0 and the image stretches along the X-axis. Keep it between 0.0 and 1.0 and the stretch falls along the Y-axis instead. Only while the Use Size and Aspect checkbox is enabled does this control stay on hand.

Angle This control spins the image around the axis. Raising the Angle spins the image counterclockwise. Lowering the Angle spins the image clockwise. Flip Horizontally and Vertically Toggle this control on and the image flips along either the X- or Y-axis. Edges How the image's edges get treated, once the raster's edge is exposed, is what this menu settles.

- Canvas: Whatever image edges get revealed are made to display the current Canvas Color. Its default is black carrying no Alpha, and the Set Canvas Color node is what sets it.
- Wrap: This wraps the image's edges around the borders of the image. It comes in handy for seamless images meant to be panned, building an endless moving background image.
- Duplicate: This makes the image's edges get duplicated as best as it can, carrying the image on past its original size.
- Mirror: To fill out to the frame's edge, the image's pixels are mirrored.

Filter Method When a pixel is being rescaled, the pixels around it often get drawn on to yield a more realistic result. A range of algorithms exists for combining these pixels, called filters. The more intricate filters can yield better results yet usually take longer to compute. Which filter suits the job best tends to hinge on how much scaling is involved and on the contents of the image itself.

- Box: A plain interpolation-based resize of the picture.
- Linear: Leans on a bare-bones filter that turns out fairly clean, fast results.
- Quadratic: Turns out a middling result from this filter. It strikes a fair balance

between speed and quality.

- Cubic: Turns out stronger results on continuous-tone pictures. Where the pictures hold fine detail,

the outcome can come out blurrier than you'd want.

- Catmull-Rom: Turns out solid results on continuous-tone pictures scaled down.

On finely detailed pictures it yields sharp results.

- Gaussian: Sits very close to Bi-Cubic in both speed and quality.
- Mitchell: Resembles Catmull-Rom yet turns out stronger results on finely detailed pictures. It is

slower than Catmull-Rom.

- Lanczos: Sits very close to Mitchell and Catmull-Rom, just a touch cleaner and a touch slower as well.
- Sinc: A high-end filter delivering exceptionally sharp, detailed results; that said, it can throw

visible "ringing" under certain conditions.

- Bessel: Resembles the Sinc filter though it may run a shade faster.

Window Method (Sinc and Bessel Only) Certain filters, Sinc and Bessel among them, would need an endless supply of pixels to compute precisely. To hasten this operation, a windowing function steps in to approximate the filter and cap the count of pixels needed. This control shows up once a filter calling for windowing is chosen.

- Hanning: A plain tapered window.
- Hamming: Hamming is a lightly adjusted take on Hanning that stops short of tapering all the way

down to zero.

- Blackman: A window whose falloff tapers more sharply.
- Kaiser: A more intricate window yielding results between Hamming and Blackman.

The bulk of these filters earn their keep only when you're enlarging an image. For shrinking images, the Bi-Linear filter is the common pick; the Catmull-Rom filter, though, lends a measure of sharpening to the results and can help hold onto detail while scaling an image down.

### Example

Various resize filters shown left to right: Nearest Neighbor, Box, Linear, Quadratic, Cubic, next Catmull-Rom, Gaussian, Mitchell, Lanczos, Sinc, and Bessel.

Invert Transform Pick this control to invert any position, rotation, or scaling transformation. This option earns its keep when you wire the Transform to a tracker's position so as to reintroduce motion back into a stabilized image. Flatten Transform What the Flatten Transform option does is stop this node from concatenating its transformation with neighboring nodes. The node may still concatenate transforms arriving from its input, yet it won't concatenate its own transformation with the node sitting at its output. Reference Size The controls beneath the Reference Size menu don't touch the image directly. Rather, they let you govern how Fusion depicts the position of the Transform node's center. Coordinates are normally depicted as values between 0 and 1, where 1 spans a distance equal to the image's full width or height. This affords resolution independence, since you can resize the image without having to change the center's value. One drawback to this approach is that it makes pixel-accurate adjustments to an image more complicated. To illustrate, picture an image measuring 100 x 100 pixels. To shift the image's center 5 pixels to the right, we'd change the transform center's X value from 0.5, 0.5 to 0.55, 0.5. We know the change has to be 0.05 because 5/100 = 0.05. The Reference Size controls let you state the image's dimensions. This alters the way the control values get displayed, so that the Center shows the actual pixel positions across the X and Y number fields of the Center control. Carrying our example on, if you set the Width and Height to 100 apiece, the Center would now read as 50, 50, and we'd shift it 5 pixels to the right by entering 55, 50. Under the hood, the Transform node still keeps this value as a number between 0 to 1, and were you to query the Center control's value through scripting, or publish the Center control for other nodes to use, you'd get back the original normalized value. The change shows up only in the value displayed for Transform Center within the node control. Reference Width and Height Sliders Match these to the image's width and height, and you change how the Center control's values get shown by Fusion for the Transform node. Auto Resolution Tick this checkbox so that the Reference Width and Reference Height values draw on whatever frame format settings Fusion Studio currently holds, or on the timeline resolution within DaVinci Resolve.

### The Common Controls

Several identical controls in the Inspector are shared by nodes that carry out Transform operations. The controls common across Transform nodes are described in this section.
