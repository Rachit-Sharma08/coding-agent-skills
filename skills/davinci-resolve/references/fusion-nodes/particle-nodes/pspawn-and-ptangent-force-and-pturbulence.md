# Pspawn and ptangent force and pturbulence

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pspawn, Ptangent force, Pturbulence.
[Chapter index](INDEX.md) / [Previous section](prender-and-pspawn.md) / [Next section](pturbulence-inspector.md) / [Continue pTurbulence pTr / Inspector](pturbulence-inspector.md) / [pSpawn pSp](prender-and-pspawn.md)
<a id="source-basic-node-setup-5"></a> <a id="source-basic-node-setup-6"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-inputs-4"></a> <a id="source-inputs-5"></a> <a id="source-inspector-2"></a> <a id="source-ptangent-force-ptf"></a> <a id="source-pturbulence-ptr"></a> <a id="source-the-ptangent-force-controls"></a>

### Common Controls

Conditions, Style, Region, and Settings Tabs Every Particle node carries the Conditions, Style, Region, and Settings tabs in common, so their write-ups appear in "The Common Controls" section at this chapter's end.

### pTangent Force [pTF]

The pTangent Force node pTangent Force Node Introduction This node serves to apply a tangential force to the particles—one that acts at right angles to the vector running between the pTangent Force's region and whichever particle it touches.

### Inputs

A lone orange input sits on the pTangent Force node by default. Like the bulk of particle nodes, this one will only take, through that orange input, the output of fellow particle nodes. Set the Region tab's Region menu to either Bitmap or Mesh and the node gains a green bitmap or mesh input. Input: Output from other particle nodes feeds the orange input. Region: When the Region menu sits on Bitmap, or alternatively Mesh, the green or magenta region input ends up receiving either a 2D image or else a 3D mesh. The first option chosen in the menu fixes the input's color. The area where the tangent force acts on the particles is defined by the 3D mesh or by a channel selected from the bitmap.

### Basic Node Setup

You drop the pTangent Force node in between a pEmitter and a pRender node.

The pTangent Force node sets a tangent force that particles steer around.

### Inspector

### The pTangent Force controls

This node's controls let you place the offset in 3D space and set the tangential force's strength along each axis on its own. Randomize The Random Seed slider and Randomize button turn up whenever a Fusion node leans on a random outcome. Two nodes sharing the same seed values turn out the same random results. Click the Randomize button to draw a fresh seed value at random, or shift the slider to choose one by hand. X, Y, Z Center Position Within 3D space, these controls stand for the Tangent force's coordinates across X, Y, and Z. X, Y, Z Center Strength Within 3D space, these controls fix the Tangent force's Strength.

### Common Controls

Conditions, Style, Region, and Settings Tabs These four tabs—Settings, Region, Style, and Conditions—are shared across all Particle nodes, so their descriptions appear in "The Common Controls" section at the close of this chapter.

### pTurbulence [pTr]

The pTurbulence node pTurbulence Node Introduction The pTurbulence node lays a frequency-driven chaos onto each particle's position, making the motion turn erratic and uneven. This node's controls govern the Turbulence's strength and density along each axis.

### Inputs

By default the pTurbulence node carries a single orange input. Like most particle nodes, this one accepts, by way of that orange input, nothing but the output of other particle nodes. Set the Region tab's Region menu to either Bitmap or Mesh and a green bitmap or mesh input shows up on the node. Input: Output from other particle nodes feeds the orange input. Region: When the Region menu rests on Bitmap, or instead on Mesh, the green or magenta region input correspondingly receives a 2D image or else a 3D mesh. The first option chosen in the menu sets the input's color. The region of turbulence is defined by the 3D mesh or by a channel picked from the bitmap.

### Basic Node Setup

You drop the pTurbulence node in between a pEmitter and a pRender node.

The pTurbulence node breaks up the stiff flow of particles to give a more natural motion.
