# Pchangestyle and pcustom and pcustomforce

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pchangestyle, Pcustom, Pcustomforce.
[Chapter index](INDEX.md) / [Previous section](pavoid-and-pbounce-and-pchangestyle.md) / [Next section](pcustomforce-and-pdirectionalforce-and-pemitter.md) / [pChangeStyle pCS](pavoid-and-pbounce-and-pchangestyle.md)
<a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-basic-node-setup-4"></a> <a id="source-common-controls-2"></a> <a id="source-common-controls-3"></a> <a id="source-inputs-3"></a> <a id="source-inputs-4"></a> <a id="source-inspector-1"></a> <a id="source-inter-1-8"></a> <a id="source-pcustom-pcu"></a> <a id="source-pcustomforce-pcf"></a> <a id="source-position-1-8"></a> <a id="source-the-pchange-style-controls"></a> <a id="source-the-pcustom-controls"></a>

### Basic Node Setup

Counter to what you might expect, to bring about a style change that looks like the work of some physical event, the pChange Style node ought to sit ahead of the node that brings about the event. Take the case below, where the particles spawned by the Emitter node shift style after bouncing off a pBounce. The pChange Style and pBounce both lean on the same Shape 3D node as the region. The pChange Style has to sit ahead of the pBounce. Place the pChange Style node after the pBounce and the particles bounce off the region before the pChange Style works out its effect. The particle never gets the chance to cross into the pChange Style node’s region, so the style never shifts.

A pChange Style node placed before the pBounce node Inspector

### The pChange Style controls

Randomize The Random Seed slider plus the Randomize button turn up any time a Fusion node leans on a random result. A pair of nodes sharing the same seed values will turn out the same random results. Press the Randomize button to draw a fresh seed value at random, or work the slider to settle a fresh seed value by hand. Change Sets Through this option the user can shift the particle’s Set so it falls under the sway of forces apart from the original particle. Turn to “The Common Controls” in this chapter to read more about Sets. Style Through this option the user can shift the particle’s Style and thereby the look. Turn to “The Common Controls” in this chapter to read more about Styles.

### Common Controls

Conditions, Style, Region, and Settings Tabs Every Particle node shares this same set of four tabs, so you’ll find them detailed within the “The Common Controls” section that closes the chapter.

### pCustom [pCu]

The pCustom node pCustom Node Introduction You reach for the pCustom node to write custom expressions that bear on the properties of particles. This node parallels the Custom node, except that the calculations bear on particles rather than pixels.

### Inputs

The pCustom node carries three inputs. As with most particle nodes, only fellow particle nodes feed this orange input. For custom image calculations there are the green and magenta inputs, both of them 2D image inputs. Optionally, teal or white bitmap or mesh inputs appear on the node the moment the Region tab's Region menu gets set to Bitmap or Mesh. Input: Arriving at the orange input is the output of other particle nodes. Image 1 and 2: 2D images come in through the green and magenta image inputs, where they drive per pixel calculations and compositing functions. Region: A 2D image or a 3D mesh reaches the teal or white region input, hinging on whether that Region menu reads Bitmap or Mesh. Which color the input wears comes down to whichever you pick first in the menu. The area where the custom particle node takes effect is set by the 3D mesh or a selectable channel out of the bitmap.

### Basic Node Setup

The pCustom node slots in between the pEmitter and pRender. A Shape 3D node serves to carve out the region where the Custom particle event occurs.

A pCustom node leaning on a Shape 3D node to mark the region where the custom event plays out

### Inspector

Every one of the operators, functions, and conditional statements laid out for the Custom node carries over to the pCustom node as well, Pixel-read functions for the two image inputs included (getr1w(x,y), getz2b(x,y), and the rest).

### The pCustom controls

Number 1-8 Numbers are variables fitted with a dial control that can be animated or wired to modifiers exactly as any other control could. Within particle equations the numbers can stand in either for the current moment as n1, n2, n3, n4, … or for an arbitrary moment as n1_at(float t), n2_at(float t), n3_at(float t), n4_at(float t), with t standing for whichever time you mean. These controls' values lie open to expressions in the Setup and Intermediate tabs.

pCustom Position tab

### Position 1-8

These eight point controls carry 3D X,Y,Z position controls. They behave as ordinary positional controls and can be animated or wired to modifiers as any other node could. They lie open to expressions typed in the Setup, Intermediate, and Channels tabs.

pCustom Setup tab Setup 1-8 As many as eight separate expressions can be worked out in the Setup tab of the pCustom node. The Setup expressions get evaluated once per frame, ahead of any other calculations. Their results then become reachable, as the variables s1, s2, s3, and s4, by the node's remaining expressions. Picture them as global setup scripts that the intermediate and channel scripts can call on.

pCustom Intermediate tab

### Inter 1-8

A further eight expressions can be worked out in the Intermediate tab. The Intermediate expressions get evaluated once per frame, after the Setup expressions get evaluated. Results lie open as variables i1, i2, i3, i4, i5, i6, i7, i8, which channel scripts can call on.

Particle Particle position, velocity, rotation, and the rest of the controls live in the Particle tab. The particle properties below are laid open to the pCustom control:

px, py, pz vx, vy, vz rx, ry, rz sx, sy, sz pxi1, pyi1 pxi2, pyi2 mass size id r, g, b, a rgnhit rgndist condscale rgnix, rgniy, rgniz rgnnx, rgnny, rgnnz w1, h1 w2 h2 i1, i2, i3, i4 s1, s2, s3, s4 n1..n8 p1x, p1y, p1z .. p4x, p4y, p4z time age lifespan

a particle's position along the x, y, and z axis a particle's velocity along the x, y and z axis a particle's rotation along the x, y, and z axis a particle's spin along the x, y, and z axis a particle's 2d position, adjusted for image 1’s aspect a particle's 2d position, adjusted for image 2’s aspect nothing makes use of this right now a particle's present size the identifier of the particle the red, green, blue and alpha color values of the particles this value reads 1 where the particle struck the pCustom node’s defined region this variable holds how far the particle lies from the region how strong the region is at the particle’s position values marking where on the region the particle struck the region's surface normal at the spot the particle struck it the width and height of image 1 the width and height of image 2 the outcome of the intermediate calculations 1 through 4 the outcome of the setup calculations 1 through 4 whatever numeric inputs 1 through 8 hold whatever position inputs 1 through 4 hold the composition's frame or time as it stands now how old the particle is right now the lifespan of the current particle

### Common Controls

Conditions, Style, Region, and Settings Tabs This quartet of tabs recurs across all Particle nodes, and a description of each sits in the “The Common Controls” section near the chapter’s end.

### pCustomForce [pCF]

The pCustom Force node pCustom Force Node Introduction Through the pCustom Force node you can alter the forces brought to bear on a particle system or subset. This node ranks among the most intricate and the most potent node in Fusion. Anyone at home with scripting or C++ programming ought to find the structure and terminology the Custom Force node uses familiar. A particle's forces within a system can see their positions and rotations swayed by forces. The position in XYZ along with the Torque, which is the spin of the particle, fall under independent custom equations. You reach for the Custom Force node to write custom expressions and filters that rework the behavior. On top of supplying three image inputs, this node opens the door to wiring up as many as eight numeric inputs plus as many as four XY position values out of other controls and parameters in the node tree.

### Inputs

The pCustom Force node carries three inputs. As with most particle nodes, nothing other than fellow particle nodes feeds this orange input. Serving custom image calculations, a green and magenta stand as 2D image inputs. Optionally, teal or white bitmap or mesh inputs surface on the node the instant the Region tab's Region menu is set to Bitmap or Mesh. Input: Reaching the orange input is the output of other particle nodes. Image 1 and 2: Through the green and magenta image inputs come 2D images, which then power per-pixel calculations and compositing functions. Region: A 2D image or a 3D mesh lands at the teal or white region input, hinging on whether that Region menu reads Bitmap or Mesh. Which color the input wears comes down to whichever you pick first in the menu. The area where the pCustom Force takes effect is set by the 3D mesh or a selectable channel out of the bitmap.

### Basic Node Setup

The pCustom Force node drops in between a pEmitter and pRender node to act as a catalyst for particles by way of advanced C++ and scripting.

A pCustom Force is applied to the particles generated by the pEmitter.
