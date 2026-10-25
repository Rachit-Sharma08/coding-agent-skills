# Letterbox and planar transform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Letterbox, Planar transform.
[Chapter index](INDEX.md) / [Previous section](dve-and-letterbox.md) / [Next section](planar-transform-a-planar-transform-creating-a-match-move.md) / [Letterbox LBX](dve-and-letterbox.md)
<a id="source-basic-node-setup-4"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-3"></a> <a id="source-example-1"></a> <a id="source-inputs-4"></a> <a id="source-inspector-3"></a> <a id="source-planar-transform-pxf"></a> <a id="source-the-letterbox-controls-tab"></a> <a id="source-the-planar-transform-node"></a>

### Inspector

### The Letterbox Controls tab

### Controls Tab

The Controls tab supplies parameters for tuning the image's resolution and pixel aspect. It can also do either letterboxing or pan-and-scan formatting. Width and Height These control values fix the output image's size, expressed in pixels. TIP: The formatting contextual menu lets you grab a resolution from a list in a hurry. Hover the pointer over the Width or Height controls, then right-click to bring up the contextual menu. At the bottom you'll see a Select Frame Format submenu listing the available frame formats. Choose any entry from the menu and the Height, Width, and Aspect controls are set for you automatically. Auto Resolution Tick this checkbox and the Width and Height sliders are set automatically from the Frame Format settings in the Preferences window for Fusion Studio, or from the DaVinci Resolve Timeline's resolution. Pixel Aspect X and Y These controls fix the output image's pixel aspect ratio. Center X and Y This Center control shifts the image window when paired with Pan-and-Scan mode. While the node is set to Letterbox mode, it does nothing to the image. Mode This control selects the Letterbox node’s mode of operation.

- Letterbox/Envelope: Fixes the input image's aspect and rescales it so it fits the width you specify.
- Pan-and-Scan: Fixes the input image's aspect and rescales it so it fits the height you specify. Where the rescaled input image ends up wider than the specified width, you can lean on the Center control to animate which slice of the rescaled input stays visible.

Filter Method While rescaling a pixel, nearby pixels are frequently consulted to yield a more believable outcome. The various methods of blending those pixels together are known as filters. The more elaborate filters tend to deliver better quality at the cost of slower computation. Which filter suits a given task usually comes down to how much scaling is involved and what the image itself contains.

- Box: A plain interpolation resize applied to the image.
- Linear: Relies on a basic filter that turns out fairly tidy, quick results.
- Quadratic: Delivers a middling outcome, striking a reasonable balance between

speed and quality.

- Cubic: Yields stronger results on continuous-tone images. Where an image holds fine detail,

the outcome can come out blurrier than you'd want.

- Catmull-Rom: Performs well on continuous-tone images that are scaled down.

On finely detailed images it returns sharp results.

- Gaussian: Roughly matches Bi-Cubic in both speed and quality.
- Mitchell: Resembles Catmull-Rom but handles finely detailed images more effectively. It runs

slower than Catmull-Rom.

- Lanczos: Closely tracks Mitchell and Catmull-Rom, though it is a touch cleaner and slower too.
- Sinc: A sophisticated filter delivering exceptionally sharp, detailed output; in certain cases, though, it can introduce

visible “ringing.”

- Bessel: Behaves much like the Sinc filter while running a little quicker.

Window Method (Sinc and Bessel Only) A handful of filters, Sinc and Bessel among them, would in theory need an unlimited count of pixels to compute precisely. A windowing function speeds this up by approximating the filter and capping how many pixels it has to touch. Whenever you pick a filter that needs windowing, this control becomes visible.

- Hanning: A plain tapered window.
- Hamming: A lightly adjusted variant of Hanning that stops short of tapering completely

down to zero.

- Blackman: A window whose falloff tapers more steeply.
- Kaiser: A more involved window landing somewhere between Hamming and Blackman.

For the most part these filters earn their keep only when you are enlarging an image. To downsize, the Bi-Linear filter is the usual pick; that said, the Catmull-Rom filter adds a touch of sharpening and can help hold onto detail as you scale an image down.

### Example

A range of resize filters. Reading across, the samples run Nearest Neighbor, then Box, Linear, Quadratic, and Cubic, followed by Catmull-Rom and Gaussian, then Mitchell, Lanczos, Sinc, plus Bessel.

### Common Controls

Settings Tab Other Transform nodes carry a copy of the same Settings tab found here in the Inspector. You will find a full account of these shared controls under the “The Common Controls” section at this chapter's close.

### Planar Transform [PXF]

### The Planar Transform node

The Planar Transform node takes the perspective distortions a Planar Tracker node produces and lays them onto any input mask or masked image. You can lean on the Planar Transform node to cut down the hours sunk into rotoscoping objects. The idea behind this workflow rests on the fact that the Planar Tracker node is able to track objects that are only loosely planar. Once an object has been tracked, a Planar Transform node can warp a rotospline so that it roughly trails the object across time. After that, the rotospline still needs detailed cleanup by hand. How much tedious rotoscoping time you save hinges on how faithfully the Planar Tracker followed the object, and the savings can be considerable. The trick to this technique is spotting the cases where the Planar Tracker does a strong job on an object that has to be rotoscoped. Here is a rough sketch of the steps involved: 1 Track: With a Planar Tracker node, choose a pattern that stands in for the object you want to rotoscope. Track the shot (consult the tracking workflow in the Track section covering the Planar Tracker node). 2 Create a Planar Transform node: Click the Create Planar Transform button on the Planar Tracker node to make one. That brand-new Planar Transform node can be cut and pasted into a different composition however you like. 3 Rotoscope the object: Jump to any frame the Planar Tracker tracked. If you are unsure whether a frame got tracked, check the Spline Editor for a tracking keyframe on the Planar Transform node. Wire a Polygon node into the Planar Transform node, and while viewing the Planar Transform node, rotoscope the object. 4 Refine: Scrub along the timeline to gauge how closely the polygon trails the object, and tweak the polyline on any frames where it drifts. You can also drop in new points to sharpen the polygon further.

### Inputs

There are just two inputs on the Planar Transform: Image Input: A 2D image that the transform will act on plugs into the orange image input. Effect Mask: A mask shape—drawn from polylines, simple primitive shapes, paint strokes, or bitmaps from other tools—feeds the blue input. Wiring a mask here confines the Planar Transform's output to particular regions.

### Basic Node Setup

In the example below, a Planar Transform node is placed so it sits between a masked MediaIn2 node and a Merge node's foreground input. The background MediaIn1 node runs into the Planar Tracker that was used to produce the Planar Transform. After the Planar Transform exists, you no longer need the Planar Tracker in the node tree.
