# Stereo materials and disparity

Version: DaVinci Resolve 20.3 Reference Manual. Context: Optical flow and stereoscopic nodes.
[Chapter index](INDEX.md) / [Previous section](aux-deep-channels-and-optical-flow-workflows.md) / [Next section](vector-and-disparity-channels.md)
<a id="source-about-the-disparity-channel"></a> <a id="source-cropping-the-source"></a> <a id="source-depth-of-field"></a> <a id="source-disparity"></a> <a id="source-disparitytoz-ztodisparity"></a> <a id="source-motion-blur"></a> <a id="source-neweye-stereoalign"></a> <a id="source-nodes-with-multiple-outputs"></a> <a id="source-picking-from-aux-channels"></a> <a id="source-semi-transparent-objects"></a> <a id="source-separate-vs-stack"></a> <a id="source-setting-up-stereo-in-the-node-editor"></a> <a id="source-stereo-and-optical-flow-best-practices"></a> <a id="source-stereo-materials"></a> <a id="source-viewing-of-disparity-and-vector-channels"></a> <a id="source-where-to-calculate-disparity-and-optical-flow"></a>

### Stereo Materials

The Stereo Mix material node makes it possible to hand each eye a different texture.

Material viewer showing stereoscopic material.

### Disparity

The bulk of the work in producing disparity maps falls to the Disparity node. It creates the Disparity channel and tucks it away inside the hidden aux channels of the output image.

### NewEye, StereoAlign

Both NewEye and StereoAlign consume and discard the Disparity channel as they interpolate the color channel. The hidden channels get destroyed along the way because, once the nodes have run, the original Disparity channels would be meaningless. These nodes require either an upstream Disparity node producing the hidden channels or an OpenEXR Loader feeding those channels in.

### DisparityToZ, ZToDisparity

The nodes here pass through, alter, or create new aux channels without destroying any. TIP: Should the colors vary from one shot to another, run a global alignment first with Color Corrector or Color Curves before you compute the Disparity map. Route the image you intend to alter into the orange input and the reference into the green input. Under the Histogram section of the Color Corrector, pick Match and also pick Snapshot Match Time. Within the Color Curves’ Reference section, pick Match Reference.

### Separate vs. Stack

Stereo nodes operate in either Separate or Stack modes. Under Stack mode the left/right eyes sit stacked either horizontally or vertically, yielding a single image of double width or double height respectively. What makes Stack mode appealing is that you avoid keeping duplicate branches of the Node Editor for the left and right eyes. Because of this, Stereo nodes appear with two inputs and two outputs marked “Left” and “Right.” While in Stack mode, wire the stack into the left eye input and rely on the Left output to feed downstream nodes. Under Stack mode the corresponding Right eye inputs and outputs stay hidden.

### Setting Up Stereo in the Node Editor

Generating the disparity comes first. You can arrange this inside the Node Editor in two distinct ways.

Two stereoscopic workflows.

Within the example above, the right-hand workflow takes the left and right eye, builds the disparity, and immediately calls on NewEye to produce a new eye for the image. The left-hand example renders the disparity-bearing frames out to intermediate EXR images. Those images then get pulled back into Stereo nodes and used to build the NewEye images. Computing the disparity first via Render nodes lets the later creative steps run far more quickly and interactively. While the diagram above doesn't depict it, it's generally wise to color correct the right eye toward the left eye prior to disparity generation, since that aids the disparitytracking algorithm. Perfect color matching isn't required — for instance, the “Match” option in a Color Corrector’s histogram options can handle it.

### About the Disparity Channel

Inside the Disparity channel are the displacement vectors that pair pixels from one eye with the matching pixels in the other. Vectors held in the left image’s Disparity channel map left>right; vectors held in the right image’s Disparity channel map right>left. To illustrate the left-to-right case: (xleft, yleft) + (Dleft. x, Dleft. y) -> (xright, yright). The right-to-left case follows the same pattern: (xright, yright) + (Dright. x, Dright. y) -> (xleft, yleft). For pixels that aren't occluded you'd anticipate Dleft = -Dright, though the disparity generation algorithm makes that equality only roughly true. NOTE: Disparity holds X as well as Y values because left/right images are seldom lined up perfectly in Y, even when captured through a meticulously arranged camera rig. Values for both Disparity and Optical Flow are kept as un-normalized pixel shifts. Notably, that departs from Fusion’s resolution-independent convention. The choice was made deliberately so that you needn't fuss over rescaling the Disparity/Flow values while cropping an image, nor over scale factors when importing/exporting these channels into other applications. Since the Flow and Disparity channels record values in pixel shifts, friction can arise with Proxy and AutoProxy. Fusion's rule is that, for proxied images, these channels keep unscaled pixel shifts that hold for the full-sized image. Therefore, to read the Disparity values from a script or through a probe, always remember to scale them by (image. Width/image. OriginalWidth, image. Height/ image. OriginalHeight).

### Viewing of Disparity and Vector Channels

You can show aux channels right in the viewers via the Channel viewer button’s menu. The CopyAux node serves to copy those channels straight into the RGB channels for display or downstream processing. What's nice about the CopyAux node is its static normalization, which cuts much of the flicker stemming from the viewer’s time-variant normalization. For long runs of aux channels, the CopyAux node offers an option to drop the aux channels and retain just the current RGB channels, which frees precious memory and lets you cache additional frames.

TIP: While the Channel Booleans can also copy any aux channel into RGBA, doing so takes a few extra clicks versus CopyAux. Keep in mind that aux channels are memory-hungry. A float-32 1080p image holding only RGBA occupies roughly 32 MB of memory, yet with every aux channel switched on it climbs to about 200 MB of memory.

### Stereo and Optical Flow Best Practices

Several factors — the way you assemble your composition, the images in play, and the kind of shot at hand — all influence whether Disparity generation and Optical Flow analysis succeed. Below we'll examine some scenarios worth watching for and how to sidestep common traps when working with optical flow.

### Semi-Transparent Objects

The Optical Flow and Disparity generation algorithms in Fusion presume a single layer per pixel as they track pixels from one frame to the next. Transparent objects and motion blur are especially troublesome. Take a shot soaring through clouds, with semi-transparent clouds up front and a far-off landscape behind: this baffles the Optical Flow/Stereo algorithms, which can't tell apart overlapping objects moving differently. Typically the optical flow winds up following patches of one object or the other. It stops being an issue when the transparent object and the background sit at nearly the same depth and therefore share the same disparity.

### Motion Blur

Motion blur poses a serious challenge as well, for the same reason just described. The Disparity and Optical Flow algorithms can't decide whether a pixel inside the motion blur belongs to the moving object or to the background pixel. Because these algorithms are global by nature, the vectors over the motion blur come out wrong and the algorithm also gets confused in areas neighboring the motion blur.

### Depth of Field

Depth of field is yet another difficulty tied to the previous two. Trouble shows up when a defocused foreground object sits over a background object that is in motion (the Optical Flow case) or that shifts between L/R (the Stereo Disparity case). The softened edges throw off the tracking, since it can't recognize that those edges are really two distinct objects.

### Where to Calculate Disparity and Optical Flow?

The point in your composition at which you produce optical flow or disparity can sharply alter the outcome.

For example, when you've composited a lens flare in, it's wiser to compute OpticalFlow/ Disparity ahead of it, because the semi-transparent lens flare misleads the tracking algorithms. When you're color correcting the left/right eyes to match or to deflicker, applying the OpticalFlow/Disparity afterward works better, since matching colors between frames makes it easier for the tracking algorithm to find correspondences. When you're stripping out lens distortion, weigh carefully whether to do so before or after Disparity computation. Doing it afterward turns your Disparity map into a lens distortion map too, fusing the two effects into one. The broad rule of thumb is to apply OpticalFlow/Disparity ahead of any compositing steps apart from an initial color-matching correction and a lens distortion removal.

### Cropping the Source

A general pointer: whenever you crop your input images for whatever reason, you're usually better off computing the optical flow or disparity prior to the crop and then cropping the flow/disparity alongside the color afterward. This is because flow/disparity matching thrives when shared pixel data exists in both frames; once pixels appear in only one frame (or one eye), the Disparity/ OpticalFlow nodes have to guess and fill in the gaps. The largest occlusions traveling L <–> R are normally pixels along the L/R edges of the images that shift outside the frame. The same holds for optical flow with a moving camera. Watch out, too, for black borders ringing the edges of your frames, which you ought to crop off.

### Nodes with Multiple Outputs

Plenty of the stereo nodes in the Fusion toolset carry multiple outputs, which can puzzle newcomers. A notably confusing detail is that dragging a Stereo node into the view always shows the left output. Seeing the right output is impossible unless you attach another node such as BC (BrightnessContrast) to the right output and view that instead.

### Picking from Aux Channels

Certain nodes — StereoAlign among them — let you drag-pick from the Z or Disparity auxiliary channels. You have to pick from a node upstream of the StereoAlign rather than from the StereoAlign's output. Attempting to pick a disparity from a StereoAlign node's output returns nothing, because StereoAlign consumes/destroys the Disparity aux channel (and even were the Disparity channel left intact, you'd grab the wrong value, since you'd be picking from the aligned result). A typical picking sequence goes like this: 1 Display StereoAlign within the left view. 2 Put whatever node feeds into StereoAlign on the right view. 3 Grab the Disparity value off the left eye, working in that right view.

Even though this picking behaves no differently from ordinary picking of color channels, the situation can still trip people up. As an analogy, the equivalent color-node blunder would be a user attempting to pick a gradient color for a Background node from a view that's showing that very Background node (picking a color for a node out of its own output). One more thing to mind is which eye you're picking from. The safe habit is to always pick from the left eye. That's because the Disparity channels differ between the left and right eyes, and when you pick from a horizontal/vertical stereo stack, Fusion can't tell whether your Disparity value came from the left or right eye. None of the above are strict rules — they're guidelines meant to keep you from shooting your own foot. Grasp the reasoning fully and you'll spot exceptions where everything still works — for instance, taking disparity off the left output of DisparityToZ, or pulling Z off either the left or right output of ZToDisparity.
