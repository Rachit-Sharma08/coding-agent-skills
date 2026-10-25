# Pemitter and pflock and pfollow

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pemitter, Pflock, Pfollow.
[Chapter index](INDEX.md) / [Previous section](pcustomforce-and-pdirectionalforce-and-pemitter.md) / [Next section](pfollow-and-pfriction-and-pgradientforce-and-pimage-emitter.md) / [pEmitter pEm](pcustomforce-and-pdirectionalforce-and-pemitter.md)
<a id="source-basic-node-setup"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-inputs"></a> <a id="source-pflock-pfl"></a> <a id="source-pfollow-pfo"></a> <a id="source-region-tab"></a> <a id="source-rotation"></a> <a id="source-sets-tab"></a> <a id="source-spin"></a> <a id="source-style-tab"></a> <a id="source-the-pemitter-sets-tab"></a> <a id="source-the-pemitter-style-tab"></a> <a id="source-the-pflock-controls"></a> <a id="source-velocity"></a>

### Velocity

The controls under the Velocity section govern the speed and heading of the particle cells as they spill from the emitter region. Velocity and Velocity Variance These fix the starting speed, or velocity, of fresh particles. By default a particle carries no velocity and stays put at its origin until some outside force acts on it. Set velocity to 10.0 and the particle clears the whole width of the image in a single step, so a velocity of 1.0 would have the particle traverse the image's width across 10 frames.

Velocity Variance shifts each particle's velocity at birth, the same way laid out for Lifespan Variance and Number Variance above. Inherit Inherit Velocity hands the emitter region's velocity down to the particles. This slider spans a broad range covering both negative and positive values. A negative value sends the particles off in the opposite direction, a value of 1 has the particles travel at a velocity equal to the emitter region's velocity, and a value of 2 pushes the particles out ahead of the emitter region. Angle and Angle Variance This fixes the angle that velocity-bearing particles head off at upon birth. Angle Z and Angle Z Variance Same as above, save that this control fixes the particles' angle along the Z space axis (toward or away from the camera).

### Rotation

Rotation controls serve to set the orientation of particle cells and to animate that orientation across time. Rotation Mode Through this menu control sit two options that help settle the orientation of the emitted particles. With spherical particles, this control's effect goes unseen.

- Absolute Rotation: The particles take whatever orientation the Rotation controls dictate, no matter their velocity and heading.
- Rotation Relative To Motion: The particles face the way the particle travels. From there the Rotation controls can turn the particle's orientation off of its heading.

Rotation XYZ and Rotation XYZ Variance These controls open up Rotation of the individual particles. That comes in especially handy with a bitmap particle type, since the incoming bitmap might not face the direction you want. Through Rotation XYZ Variance you can randomly nudge the rotation by a set amount around the center of the Rotation XYZ value, sparing you a batch where every particle faces the exact same way.

### Spin

Spin controls are auto-animated controls that shift the orientation of particle cells across time. Spin XYZ and Spin Variance These hand a spin to each particle at birth. A particle turns 'x' degrees per frame, as fixed by the Spin XYZ value. The Spin XYZ variances shift how much rotation lands on each frame, in the manner spelled out by Number Variance and Lifespan Variance covered above.

### Sets Tab

The settings on this tab bear on the physics of the particles the node emits. They have no direct say over how the particles look. What they shape instead is behavior such as velocity, spin, quantity, and lifespan.

### The pEmitter Sets tab

Set 1-32 To file the particles a pEmitter makes into a given set, just tick the checkbox of the set number you'd like to assign. One pEmitter node may belong to a single set or to several. Once they're assigned within the pEmitter, you can switch sets on in other particle nodes so those nodes touch only particles from particular pEmitters.

### Style Tab

How the particles look is governed by the controls on the Style tab. For a thorough rundown of the Style tab, turn to the "The Common Controls" section closing out this chapter.

### The pEmitter Style tab

### Region Tab

The Region tab steers the shape, size, and placement of the zone that emits the particle cells. People often call this the Emitter. A single pEmitter node admits only one emitter region. With the pRender set to 2D, the emitter region spills particles across a flat plane in Z Space. A 3D emitter region carries depth and can spill particles throughout a user-defined, three-dimensional zone. For fuller detail on the Region tab, turn to the "The Common Controls" section closing out this chapter.

### Common Controls

Conditions, Style, Region, and Settings Tabs Every Particle node shares the Conditions, Style, Region, and Settings tabs, so you'll find them described in the "The Common Controls" section that closes this chapter.

### pFlock [pFl]

The pFlock node pFlock Node Introduction You can call on the pFlock node to mimic how organic systems behave, like a flock of birds or a colony of ants. Putting it to work can lend an otherwise mindless particle system the look of something motivated, as though it acts under some guiding intelligence. Two basic principles drive the pFlock node. Every particle tries to hug the other particles, and every particle tries to keep a minimum gap from the others. How strongly these "desires" pull yields the seemingly purposeful behavior the viewer reads.

### Inputs

By default the pFlock node carries one orange input. As with most particle nodes, this orange input takes only other particle nodes. A green or magenta bitmap or mesh input shows up on the node once you switch the Region menu on the Region tab to either Bitmap or Mesh. Input: Output from other particle nodes feeds the orange background input. Region: Into the green or magenta region input goes a 2D image or a 3D mesh, hinging on whether the Region menu reads Bitmap or Mesh. Whichever option you pick first in the menu decides the input's color. Where the flocking takes hold is set by the 3D mesh or by a selectable channel off the bitmap.

### Basic Node Setup

Paired with pFollow, the pFlock node can generate natural swarming behaviors that shift direction.

A pFlock node lending more herd-type mentality to particles Inspector

### The pFlock controls

Randomize Any time a Fusion node leans on a random result, you'll see the Random Seed slider and Randomize button. A pair of nodes carrying matching seed values turns out matching random results. Hit the Randomize button to draw a new seed value at random, or work the slider to set one by hand. Flock Number This control's value stands for how many other particles the affected particle will try to trail. The larger the value, the more obvious the "clumping" across the particle system and the bigger the particle groups grow. Follow Strength This value stands for how strongly each particle wants to trail the others. Larger values make the particle look like it spends more energy and effort chasing the others. Smaller values raise the odds that a given particle peels off from the pack. Attract Strength This value stands for the pull between particles. Once a particle drifts farther from the others than the Maximum Space set in the pFlock node, it will try to close back in. Larger values have the particle guard its spacing energetically, settling spacing conflicts faster.

Repel Strength This value stands for the force put on particles that crowd nearer than the gap set by the pFlock node's Minimum Space control. Larger values drive particles away from their neighbors faster, firing them off from the pack. Minimum/Maximum Space This range control stands for the gap each particle tries to hold between itself and the others. Particles will try to sit no nearer and no farther than the gap set by this range control's Minimum/Maximum values. Tighter ranges read as more orderly motion. Wider ranges come across as disorderly and chaotic.

### Common Controls

Conditions, Style, Region, and Settings Tabs Since every Particle node holds the Conditions, Style, Region, and Settings tabs in common, their write-ups live in the "The Common Controls" section that closes this chapter.

### pFollow [pFo]

The pFollow node pFollow Node Introduction Dropping the pFollow node into a particle branch sets the particles springing back and forth toward a follow object. You can place that follow object in 3D or animate it to carve a fresh motion path for the particles.
