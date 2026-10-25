# Common controls region tab

Version: DaVinci Resolve 20.3 Reference Manual. Context: Common controls.
[Chapter index](INDEX.md) / [Previous section](pturbulence-and-pvortex-and-common-controls.md) / [The Common Controls](pturbulence-and-pvortex-and-common-controls.md) / [Next section](common-controls-style-options.md)
<a id="source-blur-controls"></a> <a id="source-fade-controls"></a> <a id="source-merge-controls"></a> <a id="source-mesh-regions"></a> <a id="source-particle-nodes-part-5"></a> <a id="source-particles-blur-controls"></a> <a id="source-particles-size-and-fade-controls"></a> <a id="source-region-tab"></a> <a id="source-size-controls"></a> <a id="source-style-tab-1"></a>

### Particles Size and Fade controls

### Size Controls

Most of the Size Controls explain themselves. The Size and Size Variance controls set the size and the spread of size variation for each particle. Worth flagging is that the Point style carries no size controls (each point measures a single pixel, with nothing more to adjust). Under a Bitmap Particle style, a value of 1.0 means each particle should match the input bitmap's size. A value of 2.0 grows the particle by 200%. For top-quality particles, always aim to keep the input bitmap as large as, or larger than, the biggest particle the system turns out. Under the Point Cluster style, the size control governs the cluster's density, that is, how tightly the particles pack. Further size controls exist for refining particle size against velocity and depth. Size to Velocity This grows each particle in proportion to its velocity or speed. The particle's velocity is folded into the size, scaled by this control's value. At 1.0 on this control, a particle moving at 0.1 picks up another 0.1 of size (velocity \* size to velocity + size = new size). It suits Line styles best, though the control will adjust the size of any style. Size Z Scale This control gauges how much each particle's size shifts with its Z position. The result is to overstate or dampen how strongly perspective reads. The default value is 1.0, which gives a fairly realistic perspective effect.

Anything on the focal plane (Z = 0.0) shows at its true size. Anything further out along Z shrinks. Anything nearer along Z grows. A value of 2.0 blows the effect up dramatically, whereas a value of 0.0 strips perspective out altogether. Size Over Life This spline control sets a particle's size over the course of its lifespan. The vertical axis stands for a percentage of the value the Size control defines, running 0 to 200%. The horizontal axis covers the particle's lifespan as a percentage, from 0 to 100%. Every feature a standard spline editor offers is supported on this graph. You reach those features by right-clicking the graph. You can equally view and edit the graph spline within the larger Spline Editor.

### Fade Controls

This plain range slider gives you a way to fade a particle in at the opening and out at the close of its lifetime. Raising the Fade In value fades the particle in as its life begins. Lowering the Fade Out value fades the particle out as its life ends. The control's values stand for a percentage of the particle's whole life, so putting the Fade In at 0.1 fades the particle in across the first 10% of its total lifespan. As an example, a particle that lives 100 frames would fade in from frame 0…10.

### Merge Controls

This batch of particle controls shapes how individual particles get merged. The Subtractive/ Additive slider behaves as the standard Merge node documents. The Burn-In control drives the particles to overexpose, or “blow out,” as they combine. Not one of the Merge controls does anything to a 3D particle system.

### Particles Blur controls

### Blur Controls

This batch of particle controls lets you lay a Blur onto the individual particles. The blurring can run globally, by age, or by Z depth position. Not one of the Blur controls does anything to a 3D particle system.

Blur (2D) and Blur Variance (2D) These controls blur each particle. In contrast to the Blur in the pRender node, this one hits each particle on its own before the particles get merged. The Blur Variance slider shifts how much blur lands on each particle. Blur Over Life This spline graph governs how much blur reaches the particle across its life. The vertical axis stands for a percentage of the value the Blur control defines. The horizontal axis stands for a percentage of the particle's lifespan. This graph supports every feature a standard Spline Editor offers. You reach those features by right-clicking the graph. Viewing and editing the spline inside the larger Spline editor is possible too. Z Blur (DoF) (2D) and DoF Focus This slider control blurs each particle according to where it sits along the Z axis. The DoF Focus range control marks out which part of the image stays sharp. Smaller values along Z lie nearer the camera; larger ones lie further off. Particles inside the range stay sharp. Particles beyond it pick up the blur the Z Blur control defines. Conditions

pVortex Conditions tab Conditions Tab The Conditions tab narrows which particles the node's behavior reaches. You can pare the particles down by probability or, more pointedly, by sets. Probability The Probability slider fixes the percentage chance that the node touches any one particle. At its default of 1.0 it touches every particle. A setting of 0.6 would give each particle a 60 percent chance of being touched by the control. The probability is worked out for each particle on each frame. So a particle left untouched by a force on one frame faces the same odds of being touched on the following frame.

Start/End Age This range control lets you confine the node's effect to a given percentage of the particle lifespan. As an example, to hold a node's effect to the final 20 percent of a particle's life, put the Start value at 0.8 and leave the End value at 1.0. Across frames 80 through 100 the node touches only a particle whose lifespan is 100 frames. Set Mode Menu The Set Mode menu steers how the particle node acts on the active particle sets. Three options come off this menu:

- Ignore Sets: The particle node pays no mind to the Set checkboxes' state and applies to all nodes.
- Affect Specified Sets: The particle node directs its behavior at the active Set checkboxes alone.
- Ignore Specified Sets: The particle node directs its behavior at the inactive Set checkboxes alone.

Set # A Set # checkbox's state decides whether the Particle node's effect reaches the particles in that set. It lets you hold some nodes' effects to a slice of the particles. Sets get handed out by the nodes that create particles, namely the pEmitter, pImage Emitter, pChangeStyle, and the pSpawn nodes.

### Region Tab

The Region tab serves to pen the node's effect into a geometric region or plane and to fix the area where particles spawn on a pEmitter node, or where a node's behavior carries weight.

pEmitter Regions tab set to mesh The Region tab is shared by nearly all particle nodes. On the pEmitter node, Emitter Regions fix where particles spawn. On most other tools, it pens the tool's effect into a geometric region or plane. Seven region types exist, each with controls of its own. A single pEmitter node admits just one emitter region. With the pRender set to 2D, the emitter region spawns particles along a flat plane in Z Space. 3D emitter regions carry depth and can spawn particles inside a user-defined, three-dimensional region.

Region Mode Menu The Region Mode menu holds seven region types for defining the area, each with its controls.

- All: In 2D, particles spawn anywhere inside the image's bounds. In 3D, the region is a cube measuring 1.0 x 1.0 x 1.0 units.
- Bézier: Bézier mode leans on a user-drawn polyline to set where particles spawn. The mode functions in both 2D and 3D, yet the Bézier polyline region itself can be drawn only in 2D. To animate the polyline's shape over time or wire it to another polyline, right-click the Shape animation label at the foot of the inspector and pick the fitting option from the drop-down.
- Bitmap: A Bitmap source drawn from one of the composition's other nodes serves as the region where particles are born.
- Cube: A full 3D Cube sets the region inside which particles spawn. Its height, width, depth, and XYZ positions are all yours to set and to animate over time.
- Line: A plain line control sets where particles spawn. The line runs between two end-points, which you can wire to Paths or Trackers as the need arises. This emitter region type brings X, Y, and Z position controls for both the line's start and its end
- Mesh: Any 3D Mesh will serve as a region. Under Mesh mode, you can also pare the region down by Object ID through the ObjectID slider. A fuller account of how mesh regions work appears below.
- Rectangle: The Rectangle region type works like the Cube type, except this one carries no depth in Z space. Setting it apart from other 2D emitter regions, it can be positioned and rotated in Z space.
- Sphere: This is a spherical 3D emitter region carrying Size and Center Z controls. Sphere (3D) stands as the default region type for a fresh pEmitter node.

### Mesh Regions

Region Type The Region Type drop-down lets you decide whether the region takes in the inner volume or only the surface. On a pEmitter mesh region, for instance, this settles whether particles emit off the surface or out of the full volume. Winding Rule and Winding Ray Direction Together, these two parameters set how the mesh region copes with particle creation on meshes that are not closed, a frequent state of affairs in many meshes brought in from outside applications. It crops up often with imported mesh geometry, and even geometry that looks closed will routinely seem to “leak” owing to vertices that were welded improperly. To judge whether a particle sits inside an object, a ray is fired from infinity through that particle and onward to -infinity. The Winding Ray Direction sets the direction in which this ray is fired. Every time the ray pierces a surface, that is logged and tallied into a running winding number. Crossing against a surface's normal scores +1, and crossing with the normal scores -1. The Winding Rule then settles what counts as inside versus outside. Set the Winding Rule to Odd, for instance, and only particles whose winding number is odd are kept as the particles are created. That very same method makes sure self-intersecting polylines close up correctly.

As an example, the node tree and image below show a pair of image planes pressed into service as a mesh region for particle creation.

Switch the region's Winding Ray Direction to the Z (blue) axis and this mesh can then stand in as a closed volume for the sake of particle creation, as the picture below shows.

Limit By ObjectID Ticking this checkbox frees the Object ID slider to choose the ObjectID brought into the region.

### Style Tab

The Style tab is present on the pEmitter, pSpawn, pChangeStyle, and pImage Emitter. It dictates how the particles look, letting their appearance be designed and animated over time. Style The Style menu opens up the assorted particle types the Particle Suite supports. Every style holds controls of its own along with controls it shares with other styles.

- Point Style: Particles drawn by this option measure exactly a single pixel across. The controls unique to the Point style are Apply Mode and Sub Pixel Rendered.
- Bitmap Style and Brush Style: Each of the Bitmap and Brush styles draws its particles from an image file. Whereas the Bitmap style pulls its image from a different node within the node tree, the Brush style draws on image files kept in the Brushes directory. Both expose a wide array of controls governing how they look and move, which are covered below.
- Blob Style: Choosing this gives you sizable, soft, sphere-shaped particles, offering controls for Color, Size, Fade timing, Merge method, and Noise.
- Line Style: Here the particles take the form of straight lines that can have optional "falloff." Often handy with this Line type is the Size to Velocity control (covered below under Size Controls). How much falloff runs along the line's length is governed by the Fade control.
- Point Cluster Style: This produces tight clusters made of single-pixel particles. While Point Clusters resemble the Point style, they handle large particle counts far more efficiently. The style borrows its parameters from the Point style. The extra controls unique to Point Cluster style are Number of Points and Number Variance.
