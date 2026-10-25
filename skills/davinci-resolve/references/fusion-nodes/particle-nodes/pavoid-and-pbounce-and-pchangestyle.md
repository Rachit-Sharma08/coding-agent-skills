# Pavoid and pbounce and pchangestyle

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pavoid, Pbounce, Pchangestyle.
[Chapter index](INDEX.md) / [Next section](pchangestyle-and-pcustom-and-pcustomforce.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-particle-nodes"></a> <a id="source-particle-nodes-part-1"></a> <a id="source-pavoid-pav"></a> <a id="source-pbounce-pbn"></a> <a id="source-pchangestyle-pcs"></a> <a id="source-the-pavoid-controls"></a> <a id="source-the-pbounce-controls"></a>

### Particle Nodes

This chapter walks through the Particle nodes on offer in Fusion.

Each node name carries an abbreviation beside it that serves in the Select Tool dialog while you hunt for tools and within scripting references. Throughout this document, treat node trees that show MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a note says otherwise.

You reach for the Particle nodes to spawn a great many duplicated objects that animate on their own. They serve to build elements such as falling rain, fireworks, smoke, pixie dust, and a whole lot besides. The possibilities run on without end. In Fusion, particles amount to a set of nodes chained together for spawning, reshaping, and rendering particles within a 2D or 3D scene. As a starting point, each particle system you build has to hold two fundamental nodes:

- pEmitter: Spawns the particles and governs their basic look, motion. and behavior.
- pRender: Turns the pEmitter's output into a rendered 2D or 3D scene. When creating

particles, you only ever view the pRender node.

Whatever particle nodes are left reshape the pEmitter results to mimic natural phenomena such as gravity, flocking, and bounce. Every particle node's name opens with a lowercase p, setting them apart from non-particle nodes. You'll find them in the particles category within the Effects Library.

### pAvoid [pAv]

The pAvoid node pAvoid Node Introduction You reach for the pAvoid node to carve out a region or area inside the image that affected particles try to keep from entering and crossing. Two primary controls govern it. The first fixes how far from the region a particle ought to be before it starts drifting away from the region. The second fixes how firmly the particle drifts away from the region. What a pAvoid node plants in a particle is a “desire” to drift away from a specific region. Where the velocity of the particle outweighs the combined distance and strength of the pAvoid region, the particle’s urge to steer clear of the region fails to beat its momentum, and the particle crosses that region all the same.

### Inputs

By default the pAvoid node carries a single orange input. As with most particle nodes, only other particle nodes feed this orange input. Set the Region tab's Region menu to Bitmap or Mesh and a green bitmap or mesh input then surfaces on the node. Input: Fed by the output of other particle nodes is the orange input. Region: A 2D image or a 3D mesh is what the green or magenta region input takes, hinging on whether the Region menu reads Bitmap or Mesh. Which color the input wears comes down to whichever you pick first in the menu. The area particles avoid is set by the 3D mesh or a selectable channel out of the bitmap.

### Basic Node Setup

The pAvoid node slots in between the pEmitter and pRender. A Shape 3D node serves to carve out the region the particles will avoid.

A pAvoid node leaning on a Shape 3D node to mark out the region to steer clear of Inspector

### The pAvoid controls

Randomize The Random Seed slider plus the Randomize button turn up any time a Fusion node leans on a random result. A pair of nodes sharing the same seed values will turn out the same random results. Press the Randomize button to draw a fresh seed value at random, or work the slider to settle a fresh seed value by hand. Distance Fixes how far from the region a particle ought to be before it starts drifting away from the region. Strength Fixes how firmly the particle drifts away from the region. Negative values drive the particles toward the region instead.

### Common Controls

Conditions, Style, Region, and Settings Tabs These four tabs turn up on every Particle node alike, so a full account of them waits in the “The Common Controls” section at this chapter’s close.

### pBounce [pBn]

The pBounce node pBounce Node Introduction You reach for the pBounce tool to carve out a region off which affected particles will bounce the moment they touch it.

### Inputs

By default the pBounce node carries a single orange input. As with most particle nodes, nothing but other particle nodes feeds this orange input. Dial the Region tab's Region menu over to Bitmap or Mesh and a green or magenta bitmap or mesh input then appears on the node. Input: What the orange input draws in is the output of other particle nodes. Region: Depending on whether that Region menu reads Bitmap or Mesh, the green or magenta region input accepts a 2D image or a 3D mesh. Which color the input wears comes down to whichever you pick first in the menu. The area particles bounce off is set by the 3D mesh or a selectable channel out of the bitmap.

### Basic Node Setup

The pBounce node slots in between the pEmitter and pRender. A Shape 3D node serves to carve out the region the particles bounce off.

A pBounce node leaning on a Shape 3D node to set the region off which particles rebound

### Inspector

### The pBounce controls

Randomize The Random Seed slider plus the Randomize button turn up any time a Fusion node leans on a random result. A pair of nodes sharing the same seed values will turn out the same random results. Press the Randomize button to draw a fresh seed value at random, or work the slider to settle a fresh seed value by hand. Elasticity Elasticity bears on the strength of a bounce, that is, how much velocity the particle keeps after striking the Bounce region. A value of 1.0 leaves the particle carrying the same velocity after the bounce as it brought entering the bounce. A value of 0.1 strips the particle of 90% of its velocity as it bounces off the region. This control runs from 0.0 to 1.0 by default, yet larger values can be typed in by hand. That makes the particles pick up momentum after an impact rather than shed it. Negative values get accepted but yield no useful result. Variance By default, particles that hit the Bounce region reflect evenly off the edge of the Bounce region, going by the vector or angle of the region. Pushing the Variance past 0.0 brings a measure of variation into that angle of reflection. You can lean on this to fake the effect of a rougher surface. Spin By default, particles that hit the region come away with their angle or orientation untouched. Raising or lowering the Spin value makes the Bounce region hand the particle a spin keyed to the angle of collision, or alters whatever spin the particle already carries. Positive values hand over a forward spin, while negative values hand over a backward spin. The bigger the value, the quicker the spin laid on the particle. Roughness This slider varies the bounce off the surface to nudge particle direction a touch at random. Surface Motion This slider makes the bounce surface act as though it carried motion, thereby bearing on the particles. Surface Motion Direction This thumbwheel control fixes the angle relative to the bounce surface.

### Common Controls

Conditions, Style, Region, and Settings Tabs Each of these four tabs is common to all the Particle nodes, which is why their write-up lives in the “The Common Controls” section ending this chapter.

### pChangeStyle [pCS]

The pChange Style node pChange Style Node Introduction The pChange Style node hands you a means of shifting the appearance or style of particles that meet a defined region. Its primary controls echo those sitting in the Style tab of the pEmitter node. Particles that cross into or enter the defined region shift according to the parameters of this node. Save for the pCustom node, this stands as the only node that reworks the particles’ appearance rather than its motion. It often serves to set off a shift in appearance in answer to some event, such as hitting a barrier.

### Inputs

By default the pChange Style node carries a single orange input. As with most particle nodes, only fellow particle nodes feed this orange input. Once the Region tab's Region menu gets set to Bitmap or Mesh, a green or magenta bitmap or mesh input then turns up on the node. Input: The output of other particle nodes is what arrives at the orange input. Region: Whether that Region menu is set to Bitmap or Mesh decides if the green or magenta region input accepts a 2D image or a 3D mesh. Which color the input wears comes down to whichever you pick first in the menu. The area where the custom particle node takes effect is set by the 3D mesh or a selectable channel out of the bitmap.
