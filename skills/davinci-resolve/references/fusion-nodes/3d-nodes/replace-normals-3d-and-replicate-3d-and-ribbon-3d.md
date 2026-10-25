# Replace normals 3D and replicate 3D and ribbon 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Replace normals 3D, Replicate 3D, Ribbon 3D.
[Chapter index](INDEX.md) / [Previous section](renderer3d-and-replace-material-3d-and-replace-normals-3d.md) / [Next section](ribbon-3d-and-shape-3d-and-soft-clip.md) / [Replace Normals 3D 3RpN](renderer3d-and-replace-material-3d-and-replace-normals-3d.md)
<a id="source-basic-node-setup-2"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-controls-tab-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-jitter-tab"></a> <a id="source-replicate-3d-3rep"></a> <a id="source-replicate-3d-aligned-layout"></a> <a id="source-replicate-3d-aligned-tbn-layout"></a> <a id="source-replicate-3d-color-options"></a> <a id="source-replicate-3d-node-introduction"></a> <a id="source-replicate-3d-not-aligned-layout"></a> <a id="source-replicated-3d-jitter-controls"></a> <a id="source-replicated-3d-jitter-controls-1"></a> <a id="source-ribbon-3d-3ri"></a> <a id="source-ribbon-3d-node-introduction"></a> <a id="source-the-input-mode-loop-vs-random-order"></a> <a id="source-the-replicate-3d-node"></a> <a id="source-the-ribbon-3d-node"></a>

### Common Controls

Settings Tab The Settings tab is shared across many 3D nodes. You'll find the description of these controls in the “The Common Controls” section toward the end of this chapter.

### Replicate 3D [3Rep]

### The Replicate 3D node

### Replicate 3D Node Introduction

The Replicate 3D node duplicates input geometry at the positions of destination vertices. Those vertices may be mesh vertices as well as particle positions. To each copy of the duplicated input geometry, an assortment of transformations can be applied. The options within the Jitter tab permit non-uniform transformations, like random positioning or sizes.

### Inputs

The Replicate 3D node carries a pair of inputs: one taking the destination geometry that holds the vertices, plus one for the 3D geometry you wish to duplicate. Destination: The orange destination input takes a 3D scene or geometry carrying vertex positions, whether from the mesh or from 3D particle animations. Input[#]: The input takes the 3D scene or geometry for duplicating. As soon as this input is wired up, a fresh input for alternating 3D geometry gets made. A minimum of one wired input is needed.

### Basic Node Setup

In the example below, a Replicate 3D node drops in right after the pRender node. A spaceship FBX node is wired to the green input standing for the object that will be duplicated based on the particles. Each particle cell adopts the shape of the 3D geometry wired to the input.

Replicate 3D used to create an armada of swarming spaceships

### Inspector

### Replicated 3D Jitter controls

### Controls Tab

Step Sets how many positions get skipped over. As an example, a step of 3 means only every third vertice of the destination mesh gets used, whereas a step of 1 means all positions get used. The Step setting helps hold performance reasonable for large destination meshes. On parametric geometry such as a torus, it can serve to single out particular parts of the mesh. Point clouds are represented internally by six points once the Make Renderable option has been switched on. To land a single point, apply a step of 6 and assign an X offset of –0.5 so you reach the center of the point cloud. Use –0.125 for Locator 3Ds. After these have been scaled, the offset may shift. Input Mode This menu sets the order in which several input scenes get duplicated at the destination. Whichever setting you pick, supplying just one input scene leaves this setting with no effect.

- Set to Loop, the inputs get used one after another. The first input lands at the first position, the second input at the second position, and onward. Should the destination hold more positions than there are inputs, the sequence loops back around.
- Set to Random, a fixed yet random input gets used per position based on the seed within the Jitter tab. This input mode can serve to feign variety out of only a few input scenes.
- The Death of Particles setting makes the input geometries' IDs shift; as a result, their copy order may shift too.

### The Input Mode Loop vs. Random order

Time Offset Reach for the Time Offset slider to shift any animations applied to the input geometry by a fixed amount per copy. As an example, dial the value to –1.0 while taking, as your source, a cube configured to spin on the Y-axis. The first copy displays the animation from a frame earlier; the second copy displays animation from a frame ahead of that, etc. This can be put to powerful effect on textured planes—for instance, where consecutive frames of a video clip can be shown. Alignment Alignment lays out how the copies get aligned relative to the destination mesh normal or particle rotation. Not Aligned: Leaves the copy unaligned. It stays spun in the same direction as its input mesh.

### Replicate 3D Not Aligned layout

Aligned: This mode draws on the point's normal and attempts to rebuild an upvector. It performs best with organic meshes carrying unwelded vertices, like imported FBX meshes, since it gives the same rotations to vertices at the same positions. On flat geometric meshes, a gradual drift in rotation becomes visible. For the best outcome, the advice is to apply this method at the origin ahead of any transformations.

### Replicate 3D Aligned layout

Aligned TBN: This mode yields a more accurate, steadier alignment grounded in the tangent, binormal, and normal of the destination point. It performs best for particles and geometric shapes. On unwelded meshes, two copies of several unwelded points at the same position may end up with different alignments owing to their individual normals.

### Replicate 3D Aligned TBN layout

Color Shapes the diffuse color or shader of each copy according to the input's particle color. Use Object Color: Leaves the destination particle's color unused. Combine Particle Color: Draws on the shader of whatever input mesh and tweaks the diffuse color so it lines up with the color from the destination particle. Use Particle Color: Swaps out the whole shader of whatever input mesh for a default shader. Its diffuse color is drawn from the destination particle.

### Replicate 3D Color options

Translation These three sliders inform the node how much offset to lay on each copy. An X Offset of 1 would shove each copy one unit, one unit along the X-axis away from the prior copy. Rotation Order These buttons serve to set the sequence in which rotations get applied to the geometry. Setting the rotation order to XYZ would lay the rotation on the X-axis first, then carry out the Y-axis spin, and finish with the Z-axis spin. XYZ Rotation These three rotation sliders inform the node how much rotation to lay on each copy. XYZ Pivot The pivot controls fix where the pivot point used while rotating each copy sits. Lock XYZ With the Lock XYZ checkbox ticked, whatever adjustment you make to the scale lands on all three axes at once. With this checkbox switched off, the Scale slider splits into separate sliders covering the X, Y, and Z scales each on their own. Scale The Scale control fixes how much scaling lands on each copy.

### Jitter Tab

The Jitter tab serves to bring randomness into an assortment of parameters.

### Replicated 3D Jitter controls

Random Seed/Randomize The Random Seed serves to generate the jitter laid on the replicated objects. Two Replicate nodes carrying identical settings but different random seeds will turn out two wholly different results. Click the Randomize button to hand over a Random Seed value.

Time Offset Reach for the Time Offset slider to shift any animations applied to the source geometry. Unlike Time Offset over on the Controls tab, Jitter Time Offset is random, grounded in the Random Seed setting. Translation XYZ Jitter Reach for these three controls to tune the variation in the translation of the replicated objects. Rotation XYZ Jitter Reach for these three controls to tune the variation in the rotation of the replicated objects. Pivot XYZ Jitter Reach for these three controls to tune the variation in the rotational pivot center of the replicated objects. This touches only the extra jitter rotation, not the rotation yielded by the rotation settings over on the Controls tab. Scale XYZ Jitter Reach for this control to tune the variation in the scale of the replicated objects. Untick the Lock XYZ checkbox to tune the scale variation on its own across all three axes.

### Common Controls

Settings Tab The Settings tab is shared across many 3D nodes. You'll find the description of these controls in the “The Common Controls” section toward the end of this chapter.

### Ribbon 3D [3Ri]

### The Ribbon 3D node

### Ribbon 3D Node Introduction

Ribbon 3D builds an array of subdivided line segments or a single line running between two points. It comes in quite handy for motion graphics, particularly alongside Replicate 3D to fasten other geometry onto the lines, and alongside Displace3D for crafting lightning bolt-like structures. By default, the array of lines comes assigned texture coordinates, so they're usable with a 2D texture. As is customary, UVMap 3D can serve to change the texture coordinates. This node leans heavily on certain OpenGL features and yields no visible result once the Renderer 3D node has been set to use the software renderer. What's more, how the lines get drawn rests entirely on the graphics card capabilities, so the ribbon's look may differ depending on your computer's graphics card.
