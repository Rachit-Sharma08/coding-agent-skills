# Motion blur trails smear and stop motion

Version: DaVinci Resolve 20.3 Reference Manual. Context: Motion blur studio version only, Motion trails studio version only, Smear studio version only, Stop motion.
[Chapter index](INDEX.md)
<a id="source-advanced-options"></a> <a id="source-advanced-options-1"></a> <a id="source-general"></a> <a id="source-motion-blur-studio-version-only"></a> <a id="source-motion-trails-studio-version-only"></a> <a id="source-move-trail"></a> <a id="source-resolve-fx-temporal"></a> <a id="source-resolve-fx-temporal-1"></a> <a id="source-smear-studio-version-only"></a> <a id="source-stop-motion"></a>

### Resolve FX Temporal

Bundled with DaVinci Resolve are a handful of Resolve FX whose purpose is applying an effect across time.

### Motion Blur (Studio Version Only)

What this effect does is mirror the Motion Blur panel found in the Motion Effects palette on the Color page. Its Resolve FX form lets you bring those tools to bear on the program's other pages too. To manufacture artificial motion blur for clips that contain none, the Motion Blur settings lean on optical flow-based motion estimation. That comes in handy when footage was captured at a fast shutter speed and you afterward judge the video too strobed. The Motion Blur settings study the motion inside a clip and then blur the image selectively, keyed to how fast and in what direction each moving element travels through the scene. Three parameters govern how much motion blur is introduced and the quality at which it is rendered:

- Motion Est. Type: Picking Better yields more precise pixel mapping but demands more processing; Faster is cheaper on the processor though its result is rougher.
- Motion Range: Sets which motion speeds count when the regions to be blurred are worked out.
- Motion Blur: Push this parameter up for more motion blur and down for less. Its range runs 0–100, where 0 contributes no motion blur and 100 contributes the maximum.
- Blur Direction: Lets you decide which way the blur fans out, starting at the present frame. You can pick among: Both Directions, From Previous Frame, and Towards Next Frame.
- Granularity: Tunes the amount of detail introduced into the blur.

### Motion Trails (Studio Version Only)

What the Motion Trails effect does is duplicate the image so moving subjects leave ghostly trails behind them. You can lean on it to mimic clips captured at long shutter speeds as well as analog video feedback effects.

### General

The first pair of sliders set how many copied frames there are and how strong they are.

- Trail Length: Sets the count of copies enlisted to build the trails.
- Dropoff: Determines how much each copied frame fades. Note that the Dropoff value compounds.

As an example, a setting of .5 gives the first copy 50% opacity, hands the second 25%, drops the third to 12.5%, continuing that way.

### Advanced Options

What the advanced options govern is the way the overlapping copied frames get blended.

- Composite Gamma: A set of four options for managing how bright the overlapping frames are sits in the Composite Gamma menu. Timeline: Leans on the Timeline Color Space setting from the Project Settings to manage the overlapping brightness. By default that setting is Rec. 709, Gamma 2.4. Rec. 709: Manages the overlapping brightness with a Rec. 709 color space at Gamma 2.2. Linear: Leans on Linear Gamma, which tends to push much stronger highlights. Custom: Hands you a custom gamma slider whose default is Gamma of 2.4. Dialing this down to 1.0 matches what the menu's Linear option does.
- Input Alpha: How the Alpha channel feeds into blending the frames is decided by the choices in the Input Alpha menu. Each option presumes the clip carrying the Motion Trail already has an Alpha channel.

Ignore: As the default choice, this leaves the alpha channel out of the picture. Turning off the Use Alpha checkbox while Ignore is active makes the Alpha behave as a stencil effect on the trails. Use in Compositing: This pick employs the Alpha channel both for the trails and for compositing onto the video track below, on the assumption that the Use Alpha checkbox is switched on.

### Move Trail

This cluster of controls dictates the copies' offset, direction, size, and rotation. Whatever adjustment you set is applied cumulatively from one copy to the next. As an example, with rotation set to 5 degrees, the first trail copy turns 5 degrees, the second trail copy turns 10 degrees, the third copy turns 15 degrees, and onward.

- Pan: Adjusts the offset of the trail copies from the original image.
- Pan Angle: Alters the angle along which the trails get offset away from the source image. Those values appear

shown in degrees.

- Zoom: Adjust a scale adjustment, successively, to each copy.
- Rotate: Applies an angle of rotation, successively, to each copy.
- Reuse Current Frame: While this checkbox stays off (the default), every copy draws on the frame

following the one that preceded it. To illustrate, the first copy works out to the current frame -1, while the second copy lands on the current frame -2. Switch the checkbox on, however, and every copy draws from the very same frame the clip is currently parked on.

- Border Type: How the frame edges are dealt with once copies are scaled below the timeline resolution is set by this menu.

Black: Everything beyond the image goes black. Soften: This control feathers the edges of the rectangular frame borders so the images take on a more organic look. Replicate: Copies the outermost edge pixels of the image. Those pixels are stretched outward from each side until they hit the timeline resolution boundary. Reflect: The image gets flipped and flopped into a mirrored version reaching out to the timeline resolution frame boundary. Wrap-Around: Tiles the image into a video wall effect, filling the gap up to the timeline resolution frame boundary.

### Smear (Studio Version Only)

What the Smear effect does is fake motion blur within a clip by blending however many frames you specify.

- Frames Either Side: Sets the quantity of frames blended on each flank of the present frame. As an illustration, a value of 2 pulls in the two frames preceding and the two frames following the present frame to build the result.
- Luma Threshold: This control fixes the brightness a pixel needs before it can feed the smear effect. The lower the value, the more only darker pixels get smeared. Raise it and brighter pixels join the effect.
- Chroma Threshold: This control fixes the saturation a pixel needs before it can feed the smear effect. The lower the value, the more only low-saturated pixels get smeared. Raise it and more saturated pixels join the effect.

### Stop Motion

The point of this plugin is to recreate the stuttering motion look seen in stop motion animation. With classic stop motion, every frame of the shot is exposed on its own while the subject is nudged by hand in tiny steps between frames. Because the work was so laborious, individual frames were frequently held over within a shot to hurry production along, and that yielded a staccato motion cadence.

### Advanced Options

Set Reference Frame: Marks whatever frame is currently shown in the Viewer as the reference frame. Reference Frame: Holds the frame number of the reference frame that drives the skip pattern. That number is measured outward from where the whole original media clip begins (frame 0). Sampling Variation: As you raise this slider, the motion in the clip grows steadily more uneven. Frame Repeat: Chooses how many frames (from 1-10) get duplicated within the shot. A bigger number yields a more staggered cadence.
