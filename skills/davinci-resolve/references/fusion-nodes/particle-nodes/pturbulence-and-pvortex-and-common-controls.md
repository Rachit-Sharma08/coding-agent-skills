# Pturbulence and pvortex and common controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pturbulence, Pvortex, Common controls.
[Chapter index](INDEX.md) / [Previous section](pturbulence-inspector.md) / [Next section](common-controls-region-tab.md) / [Continue The Common Controls / Style Tab](common-controls-region-tab.md) / [pTurbulence pTr](pspawn-and-ptangent-force-and-pturbulence.md)
<a id="source-basic-node-setup"></a> <a id="source-color-controls"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-particles-color-over-life-controls"></a> <a id="source-pvortex-pvt"></a> <a id="source-style"></a> <a id="source-style-tab"></a> <a id="source-the-common-controls"></a> <a id="source-the-pemitter-style-tab"></a> <a id="source-the-pvortex-controls"></a>

### Common Controls

Conditions, Style, Region, and Settings Tabs Because the Conditions, Style, Region, and Settings tabs are shared across every Particle node, you will find what they do described in “The Common Controls” section at this chapter's close.

### pVortex [pVt]

The pVortex node pVortex Node Introduction The pVortex node lays a rotational force on every particle, pulling them in toward the Vortex's source. On top of the Common Particle Controls, the pVortex node carries these controls as well.

### Inputs

Out of the box the pVortex node shows one orange input. As with most particle nodes, that orange input will accept nothing but other particle nodes. A green bitmap or mesh input materializes on the node once you switch the Region tab's Region menu to either Bitmap or Mesh. Input: The orange input receives the output coming from other particle nodes. Region: The green or magenta region input receives a 2D image or a 3D mesh, depending on whether the Region menu reads Bitmap or Mesh. Which color the input takes follows whichever you picked first in the menu. The 3D mesh, or a channel you select from the bitmap, marks out the vortex's area.

### Basic Node Setup

You drop the pVortex node between the pEmitter and pRender nodes. A pVortex node sets up a spiraling motion for whichever particles land inside its pull.

### Inspector

### The pVortex controls

Randomize Whenever a Fusion node depends on a random outcome, both the Random Seed slider and the Randomize button appear. Hand two nodes identical seed values and the random results they yield will match. Press the Randomize button for a randomly drawn seed value, or drag the slider to set a seed value by hand. Strength This control fixes the Strength of the Vortex Force that lands on each particle. Power This control fixes how steeply the Strength of the Vortex Force tapers off with distance. X, Y, and Z Offset Work these sliders to dial in how far the vortex Offsets the particles it affects. Size This sets the Size of the Vortex Force. Angle X and Y These sliders govern how much rotational force the Vortex exerts along the X and Y axes.

### Common Controls

Conditions, Style, Region, and Settings Tabs Since the Conditions, Region, and Settings tabs are shared by all Particle nodes, descriptions of them live in the “The Common Controls” section that follows.

### The Common Controls

A whole set of identical controls turns up in the inspector across the particle nodes. This section walks through the Style, Conditions, Region, and Settings tabs that those nodes hold in common.

### Inspector

### The pEmitter Style tab

### Style Tab

The Style Tab is shared by the pEmitter, pSpawn, pChangeStyle, and pImage Emitter. Through broad controls such as type, size, and color, it dictates how the particles look.

### Style

The Style menu opens up the assorted particle types the Particle Suite supports. Every style carries controls of its own plus controls it holds in common with other styles.

- Point: This choice yields particles exactly one pixel across. Two controls belong to Point Style alone: Apply Mode plus Sub Pixel Rendered. Apply Mode: This menu bears only on 2D particles; 3D particle systems go untouched. It offers Apply modes for Add and Merge. Add fuses overlapping particles by summing each one's color values. Merge fuses overlapping particles with a plain over operation. Sub Pixel Rendered: This checkbox sets whether the point particles render at Sub Pixel precision, which yields smoother-looking motion at the cost of blurrier particles that take a touch longer to render.
- Bitmap: This style builds particle cells off an image file or another node in the Node editor. Selecting it makes an orange image input show up on the node in the node editor. A handful of controls govern the look and animation. Beyond the Style section's controls, picking Bitmap as the Style brings a Merge section to the foot of the inspector. That Merge section holds controls for additive or subtractive merges wherever the particle cells overlap.

Animate Over Time: This menu carries three options that set how movie files play once pressed into service as particle cell bitmaps. The Over Time setting runs the movie file in order. So when the comps sits on frame 2, frame 2 of the movie file shows; when the comp sits on frame 3, frame 3 of the movie files shows; and onward. Should a particle cell not come into being until frame 50, it opens on frame 50 of the movie file. What follows is that, on any give frame of the comp, all the particle cells draw the identical image. The Particle Age setting has each particle cell open on the movie file's first frame, no matter when that cell was born. The Particle Birth Time setting has each particle open on the frame that lines up with its own particle cell birth time. So if the particle comes into being on frame 25, it sticks with frame 25 of the movie file across the whole comp. Setting it apart from the other two, the Particle Birth Time setting holds one frame for the length of the comp Time Offset: This dial slides or offsets which starting frame is taken from the movie file. As an example, putting it at 10 makes the movie file open on frame 10 rather than frame 1. Time Scale: This slider acts as a multiplier on the frame. Rather than offsetting, it shifts the starting frame by multiplying the frame by the value you pick with the slider. As an example, with a value of 2 chosen, the moment the playhead hits frame 2, the movie files shows frame 4 (2x2=4), and the moment the playhead hits frame 8, the movie file shows frame 16 (8x2=16). Gain: The gain slider acts as a multiplier on the pixel value. Its job is to correct the overall Gain of the Bitmap. Suppose you have a bitmap particle cell carrying a pixel value of R0.5 G0.5 B0.4 and you apply a Gain of 1.2; you wind up with a pixel value of R0.6 G0.6, B0.48 (i.e., 0.4 \* 1.2 = 0.48) while black pixels stay put. Bigger numbers brighten the image, while smaller ones cut both its brightness and its transparency. Style Bitmap: This control surfaces when the Bitmap style is chosen, and an orange Style Bitmap input joins the node's icon over in the Node view. Wire a 2D node into this input to feed the images the particles will use. You can do that within the Node view; alternatively, drop the image source node onto the Style Bitmap control out of the Node Editor or Timeline, or right-click the control and pick the source you want from the Connect To menu.

- Blob: This choice yields big, soft, spherical particles and comes with controls for Color, Size, Fade timing, Merge method, and Noise.

Noise: This slider bears only on 2D Blob particles. Its purpose is to inject a computer-generated Perlin noise pattern into the blob particles so the blobs gain more texture. At a setting of 0 no noise reaches the Blob particles, and at a setting of 1 the noise is at its maximum.

- Brush: This style builds particle cells off whatever image file sits in the brushes directory. Plenty of controls govern the look and animation.

Gain: The gain slider acts as a multiplier on the pixel value. Its role is to correct the overall Gain of the image serving as the Brush. Suppose you have a brush particle cell carrying a pixel value of R0.5 G0.5 B0.4 and you apply a Gain of 1.2; you wind up with a pixel value of R0.6 G0.6, B0.48 (i.e., 0.4 \* 1.2 = 0.48) while black pixels stay put. Bigger numbers brighten the image, while smaller ones cut both its brightness and its transparency. Brush: This menu lists the names of whatever image files reside in the Brushes directory. Where the Brushes directory lives is set in the Preferences dialog, under Path Maps. By default that is the Brushes subdirectory inside Fusion's install folder. Use Aspect From: The Use Aspect From menu carries three settings for the brush image's aspect ratio. Pick image format to keep the brush image's native aspect ration. Pick Frame Format to adopt the aspect ratio set in the Frame Format Setting within the Fusion Preferences, or pick Custom to type in your own Pixel X and Y dimensions.

- Line: This style yields straight, line-shaped particles with optional “falloff.” The Size to Velocity control covered further down (under Size Controls) often pairs well with this Line type. The Fade control sets how much falloff runs along the line's length.
- Point Cluster: This style yields small clusters made of single-pixel particles. Point Clusters resemble the Point style, but they prove more efficient when a great many particles are needed. The style borrows parameters from the Point style. Two controls belong specifically to Point Cluster style: Number of Points along with Number Variance. Sub Pixel Rendered: This checkbox sets whether the point particles render at Sub Pixel precision, which yields smoother-looking motion at the cost of blurrier particles that take a touch longer to render. Number of Points and Variance: This control's value sets how many points each Point Cluster holds.

### Color Controls

The Color Controls pick the color and Alpha values for the particles the emitter spawns. Color Variance These range controls give you a way to broaden the colors the pEmitter turns out. Putting the Red variance range at -0.2 to +0.2 yields colors that swing 20% to either side of the red channel, a total variance of 40%. With the pEmitter set to turn out R0.5, G0.5, B0.5 (pure gray), the variance just described yields points spanning a color range from R0.3, G0.5, B0.5, to R0.7, G0.5, B0.5. To picture color space as values from 0-256 or from 0-65535, swap the values Fusion uses through the Show Color As option in the General tab of the Preferences dialog. Lock Color Variance Ticking this checkbox locks the particles' color variance. Unlock it and the color variance can be applied unevenly per color channel, opening up a wider range of colors.

### Particles Color Over Life controls

Color Over Life This ordinary gradient control lets you pick a span of color values the particle will follow across its lifetime. The gradient's left point stands for the particle color at birth. Its right point gives the particle color at the close of its lifespan. Drop extra points onto the gradient control and the particle color shifts as its life runs on.

A control of this sort comes in handy for fire-type effects (for instance, the flame might open blue, move to orange, and finish on a darker red). You can animate the gradient itself over time by right-clicking the control and picking Animate from the contextual menu. Every point on the gradient is driven by one Color Over Life spline, which sets how fast the gradient itself shifts. There is also the From Image modifier, which builds a gradient out of the spread of colors in an image taken along a line drawn between two points.
