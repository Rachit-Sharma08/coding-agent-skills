# Pfollow and pfriction and pgradientforce and pimage emitter

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pfollow, Pfriction, Pgradientforce, Pimage emitter.
[Chapter index](INDEX.md) / [Previous section](pemitter-and-pflock-and-pfollow.md) / [Next section](pimage-emitter-and-pkill.md) / [pFollow pFo](pemitter-and-pflock-and-pfollow.md)
<a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-common-controls-4"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-pfriction-pfr"></a> <a id="source-pgradientforce-pgf"></a> <a id="source-pimage-emitter-pie"></a> <a id="source-the-pfollow-controls-tab"></a> <a id="source-the-pfriction-controls"></a> <a id="source-the-pgradient-force-controls"></a>

### Inputs

By default the pFollow node carries one orange input. As with most particle nodes, this orange background input takes only other particle nodes. A green bitmap or mesh input shows up on the node once you switch the Region menu on the Region tab to either Bitmap or Mesh. Input: Output from other particle nodes feeds the orange input. Region: Into the green or magenta region input goes a 2D image or a 3D mesh, hinging on whether the Region menu reads Bitmap or Mesh. Whichever option you pick first in the menu decides the input's color. Where the particles trail the position point is set by the 3D mesh or by a selectable channel off the bitmap.

### Basic Node Setup

Paired with pFlock, the pFollow node can generate natural swarming behaviors that shift direction.

A pFollow node brings in a follow object that sways the particles' motion.

### Inspector

### The pFollow Controls tab

Random Seed Any time a Fusion node leans on a random result, you'll see the Random Seed slider and Randomize button. A pair of nodes carrying matching seed values turns out matching random results. Hit the Randomize button to draw a new seed value at random, or work the slider to set one by hand. Position XYZ The position controls serve to carve the new path by placing the follow object. Shifting the XYZ parameters reveals the onscreen position of the follow object. Animating those parameters carves the new path that will sway the particles. Spring The Spring setting sets the particles moving back and forth along the path. The reach of that spring motion widens over the particles' life according to the gap between the particles and the follow object. Larger spring settings boost the elasticity, while smaller ones cut it back. Dampen This value tames the spring action. A smaller setting puts up less resistance to the back-and-forth spring action. A larger setting puts up more.

### Common Controls

Conditions, Style, Region, and Settings Tabs Because all Particle nodes carry the Conditions, Style, Region, and Settings tabs alike, you'll find their descriptions in the "The Common Controls" section wrapping up this chapter.

### pFriction [pFr]

The pFriction node pFriction Node Introduction The pFriction node lays resistance on a particle's motion, dragging the particle's movement as it passes through a defined region. The node turns out two kinds of Friction. One kind cuts the velocity of any particle that intersects/crosses the defined region, and the other cuts or wipes out spin and rotation.

### Inputs

By default the pFriction node carries one orange input. As with most particle nodes, this orange input takes only other particle nodes. A green or magenta bitmap or mesh input shows up on the node once you switch the Region menu on the Region tab to either Bitmap or Mesh. Input: Output from other particle nodes feeds the orange input. Region: Into the green or magenta region input goes a 2D image or a 3D mesh, hinging on whether the Region menu reads Bitmap or Mesh. Whichever option you pick first in the menu decides the input's color. Where the friction happens is set by the 3D mesh or by a selectable channel off the bitmap.

### Basic Node Setup

The pFriction node sits between the pEmitter and pRender. A Shape 3D node serves to build the region the particles rebound from.

A pFriction node leaning on a Shape 3D node as the region where friction meets the particles.

### Inspector

### The pFriction controls

Random Seed Any time a Fusion node leans on a random result, you'll see the Random Seed slider and Randomize button. A pair of nodes carrying matching seed values turns out matching random results. Hit the Randomize button to draw a new seed value at random, or work the slider to set one by hand. Velocity Friction This value stands for the Friction force laid on the particle's Velocity. The bigger the value, the heavier the friction, and so the more the particle slows. Spin Friction This value stands for the Friction force laid on the particle's Rotation or Spin. The bigger the value, the heavier the friction, and so the more the particle's rotation slows.

### Common Controls

Conditions, Style, Region, and Settings Tabs Every Particle node, without exception, carries these four tabs in common, so look for their descriptions in the "The Common Controls" section at this chapter's end.

### pGradientForce [pGF]

The pGradient Force node pGradient Force Node Introduction A force born of the gradients in the input image's alpha values acts on the particles. Particles pick up speed along the gradient, traveling from white toward black (high values toward low values). You can lean on this node to give particles the look of rolling downhill or tracing the contour of a supplied shape.

### Inputs

The pGradient Force node takes two inputs: the default orange input off a particle node, plus one off a bitmap image bearing an alpha channel gradient. A magenta or teal bitmap or mesh input shows up on the node once you switch the Region menu on the Region tab to either Bitmap or Mesh. Input: Output from other particle nodes feeds the orange input. Input: Into the green input goes the 2D image holding the alpha channel gradient. Region: Into the magenta or teal region input goes a 2D image or a 3D mesh, hinging on whether the Region menu reads Bitmap or Mesh. Whichever option you pick first in the menu decides the input's color. Where the gradient force happens is set by the 3D mesh or by a selectable channel off the bitmap.

### Basic Node Setup

The pGradient Force node sits between the pEmitter and pRender nodes. A Fast Noise node serves to build the alpha gradient that shifts the particles' velocity. A pGradient Force node leaning on a Fast Noise node as the gradient that reshapes the particles' motion Inspector

### The pGradient Force controls

Randomize Any time a Fusion node leans on a random result, you'll see the Random Seed slider and Randomize button. A pair of nodes carrying matching seed values turns out matching random results. Hit the Randomize button to draw a new seed value at random, or work the slider to set one by hand. Strength Gradient Force carries just one control of its own, which governs how strong the force and acceleration laid on the particles are. Negative values here flip the Gradient Force so it runs from black toward white (low values toward high values).

### Common Controls

Conditions, Style, Region, and Settings Tabs Every Particle node shares the Conditions, Style, Region, and Settings tabs, so their write-ups can be found in the "The Common Controls" section closing this chapter.

### pImage Emitter [pIE]

The pImage Emitter node pImage Emitter Node Introduction Feeding an input image to the pImage Emitter node, it handles each of that image's pixels as though it were a particle. What chiefly sets the pImage Emitter apart from the ordinary pEmitter is that, rather than scattering particles at random inside a given region, this node lays pixels out on a regular 2D grid, coloring them off the input image.

### Inputs

The pImage Emitter node carries three inputs. As with most particle nodes, the orange input takes only other particle nodes. For custom image calculations, the green and magenta inputs serve as 2D image inputs. There may also be teal or white bitmap or mesh inputs, surfacing on the node once the Region menu on the Region tab is set to Bitmap or Mesh. Input: In a departure from most other particle nodes, the pImage Emitter's orange input accepts a 2D image that acts as the emitter of the particles. Where a region is defined for the emitter, this input sets the particles' color. Style Bitmap Input: This image input takes a 2D image to serve as the particles' image. Because that image can multiply into thousands of particles, holding these images small and square works best—say, around 256 x 256 pixels. Region: Into the teal or white region input goes a 2D image or a 3D mesh, hinging on whether the Region menu reads Bitmap or Mesh. Whichever option you pick first in the menu decides the input's color. Where the particles are emitted is set by the 3D mesh or by a selectable channel off the bitmap.

### Basic Node Setup

The pImage Emitter node sits at the head of a particle branch, taking the place a pEmitter node would hold. Below, a MediaIn node serves to emit particles using the clip's colors.

A pImage Emitter node emits particles off an image wired into the orange input.
