# Pcustomforce and pdirectionalforce and pemitter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pcustomforce, Pdirectionalforce, Pemitter.
[Chapter index](INDEX.md) / [Previous section](pchangestyle-and-pcustom-and-pcustomforce.md) / [pCustomForce pCF](pchangestyle-and-pcustom-and-pcustomforce.md) / [Next section](pemitter-and-pflock-and-pfollow.md)
<a id="source-basic-node-setup-5"></a> <a id="source-basic-node-setup-6"></a> <a id="source-common-controls-4"></a> <a id="source-common-controls-5"></a> <a id="source-inputs-5"></a> <a id="source-inputs-6"></a> <a id="source-inspector-2"></a> <a id="source-inspector-3"></a> <a id="source-particle-nodes-part-2"></a> <a id="source-pdirectionalforce-pdf"></a> <a id="source-pemitter-pem"></a> <a id="source-the-pcustom-force-controls"></a> <a id="source-the-pdirectional-force-controls"></a> <a id="source-the-pemitter-controls"></a>

### Inspector

### The pCustom Force controls

The tabs and controls sitting in the Inspector resemble the controls found on the pCustom node. Turn to the pCustom node in this chapter for more information.

### Common Controls

Conditions, Style, Region, and Settings Tabs All Particle nodes carry these four tabs in common, so their explanation is gathered in the “The Common Controls” section toward the end of this chapter.

### pDirectionalForce [pDF]

The pDirectional Force node pDirectional Force Node Introduction This node brings a unidirectional force to bear that tugs the affected particles in a named direction. Its primary controls govern how strong the force is, plus the pull's angle along each of the X, Y, and Z axis. Because the everyday use of this node is faking gravity, by default the pull heads downward on the Y axis (-90 degrees), while the default behavior skips over regions and acts on every particle.

### Inputs

By default the pDirectional Force node carries a single orange input. As with most particle nodes, only fellow particle nodes feed this orange input. Set the Region tab's Region menu to Bitmap or Mesh and a green or magenta bitmap or mesh input then appears on the node.

Input: The output of other particle nodes is what the orange input draws in. Region: A 2D image or a 3D mesh is accepted at the green or magenta region input, decided by whether that Region menu reads Bitmap or Mesh. Which color the input wears comes down to whichever you pick first in the menu. The area where the directional force takes effect is set by the 3D mesh or a selectable channel out of the bitmap.

### Basic Node Setup

The pDirectional Force node slots in between the pEmitter and pRender and often serves to build gravity.

A pDirectional Force node placed between the pEmitter and pRender nodes Inspector

### The pDirectional Force controls

Randomize The Random Seed slider plus the Randomize button turn up any time a Fusion node leans on a random result. A pair of nodes sharing the same seed values will turn out the same random results. Press the Randomize button to settle a fresh seed value at random, or work the slider to settle a fresh seed value by hand. Strength Fixes the power of the force. Positive values drive the particles in the direction the controls set; negative values drive the particles the opposite way. Direction Fixes the direction in X/Y space. Direction Z Fixes the direction in Z space.

### Common Controls

Conditions, Style, Region, and Settings Tabs Held in common by every Particle node, these four tabs get their coverage in the “The Common Controls” section wrapping up this chapter.

### pEmitter [pEm]

The pEmitter node pEmitter Node Introduction The pEmitter node stands as the chief source of particles (pImage Emitter is another) and will as a rule be the first node put to work in any fresh particle system. This node holds controls for fixing the initial position, orientation, and motion of the particles, plus controls for the visual style of each particle. Like every other Particle node (the pRender node aside), the pEmitter turns out a particle set, not a visible image, and so cannot be shown straight in a viewer. To view the output of a particle system, drop a pRender node in after the pEmitter.

### Inputs

By default the pEmitter node holds no inputs whatsoever. You can switch an image input on by picking Bitmap off the Style menu in the Style tab. As well, set the Region tab's Region menu to Bitmap or Mesh and two region inputs then appear on the node, one for bitmap and one for mesh. These inputs' colors shift according to the order in which they get switched on. Style Bitmap Input: This image input takes a 2D image to serve as the particles’ image. Since this image multiplies into potentially thousands of particles, it's wise to keep these images small and square—say, 256 x 256 pixels. Region: The region inputs take a 2D image or a 3D mesh according to whether you set the Region menu to Bitmap or Mesh. Which color the input wears comes down to whichever you pick first in the menu. The area where the particles are emitted is set by the 3D mesh or a selectable channel out of the bitmap.

### Basic Node Setup

The pEmitter node opens the branch of a particle system that always closes with a pRender node. The pEmitter can run straight into a pRender node to feed other particle nodes.

Wiring a pEmitter node into a pRender node makes for the usual arrangement behind most particle systems.

### Inspector

The pEmitter inspector splits into four main tabs plus a common settings tab. The controls tab is the first one shown, and it holds settings touching the general setup of the particle cells the node emits. These settings bear no direct effect on the appearance of the cells or shape of the emitter region. They rework fundamental behaviors such as quantity, duration, speed, and rotation of the particle cells.

### The pEmitter controls

Randomize and Random Seed The Random Seed slider serves to seed every variance and random number generator the node draws on while building the particle system. Two pEmitter nodes carrying exactly the same settings across all controls and the same random seed will spawn exactly the same particle system. Shifting the random seed brings variation between the nodes. Press the Randomize button to set a randomly chosen value for the Random Seed on its own. Number This control serves to fix the count of new particles spawned on each frame. A value of 1 would spawn one new particle each frame. Come frame 10, a total of 10 particles would be in existence (unless Particle Lifespan sat at fewer than 10 frames). Animate this parameter to name the count of particles spawned in total. Say only 25 particles in total are wanted; animate the control to put out five particles on frame 0–4, then drop a key on frame five to spawn zero particles across the rest of the project. Number Variance This reworks the count of particles spawned for each frame as named by the Number control. Say Number sits at 10.0 and Number Variance sits at 2.0; the emitter will then put out anywhere from 9-11 particles per frame. Where the value of Number Variance runs more than twice as large as the value of Number, it's possible no particles get spawned for a given frame.

Lifespan This control sets how many frames a particle lasts before it vanishes or 'dies.' Its default sits at 100 frames, though you may dial in any value. Plenty of other particle controls time themselves against the particle's Lifespan. As an example, you can have a particle's size grow across the final 80% of its life, by way of the Size Over Life graph on the pEmitter's Style tab. Lifespan Variance Much like Number Variance, the Lifespan Variance control lets you tweak the Lifespan of the particles being produced. Set Particle Lifespan to 100 frames and the Lifespan Variance to 20 frames, and the emitter's particles would run a lifespan of 90–110 frames. Color This lets you state where each particle pulls its color from. By default it sits at Use Style Color, which colors each particle per the settings on the pEmitter node's Style tab. The other choice, Use Color From Region, overrides the Style tab's color settings and instead takes its color from the underlying bitmap region. Use Color From Region only holds meaning when the pEmitter region is set to draw on a bitmap built by another node in the composition. Particles born in any region that isn't a bitmap region come out white once Use Color From Region is picked. Position Variance This control decides whether particles may be 'born' beyond the edges of the pEmitter region. Its value defaults to zero, which pens the birth area for new particles to the exact edges of the defined region. Push this control above 0.0 and a particle can be born a little past that region's edges. The larger the value, the 'softer' the region's edge grows. Temporal Distribution Ordinarily an effect gets processed once per frame, off the comp frame rate. Yet handling certain particles only at the precise frame boundaries can bring on pulsing. For subtly more lifelike behavior, particles can instead be birthed in subframe steps. The default At The Same Time setting renders on frame boundaries, whereas the remaining two settings lean on sub frame rendering. Randomly Distributed jitters birth times by +/- about the frame number — for example, birthing 10 particles one at a time at random sub times like 24.1 24.85, 24.21, 24.37 etc. As for Evenly Distributed, it births particles at uniform sub times — say, 10 particles, one apiece, at 24.0, 24.1, 24.2, 24.3, 24.4, 24.5 ... 24.8, 24.9. The Sub Frame Accuracy setting on the pRender node shapes these settings. How many in-between frames get computed between each frame is governed by the Sub Frame Accuracy slider. A larger value sharpens the particle calculation but stretches the render times.
