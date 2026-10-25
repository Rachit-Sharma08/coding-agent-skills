# Pkill and pmerge and ppoint force and prender

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pkill, Pmerge, Ppoint force, Prender.
[Chapter index](INDEX.md) / [Previous section](pkill-inputs.md) / [Next section](prender-and-pspawn.md) / [pKill pKI](pimage-emitter-and-pkill.md)
<a id="source-basic-node-setup"></a> <a id="source-basic-node-setup-1"></a> <a id="source-basic-node-setup-2"></a> <a id="source-basic-node-setup-3"></a> <a id="source-common-controls"></a> <a id="source-common-controls-1"></a> <a id="source-inputs"></a> <a id="source-inputs-1"></a> <a id="source-inputs-2"></a> <a id="source-inspector"></a> <a id="source-inspector-1"></a> <a id="source-pmerge-pmg"></a> <a id="source-ppoint-force-ppf"></a> <a id="source-prender-prn"></a> <a id="source-the-prender-controls"></a>

### Basic Node Setup

You slot the pKill node between the pEmitter and pRender nodes. To build the region in which particles die, a Shape 3D node serves the purpose.

A pKill node that leans on a Shape 3D node to mark out where particles perish Inspector Only the common controls in the Conditions and Regions tabs live on this node. With the Conditions and Regions controls you spell out the location, the age, and the set of particles getting killed.

### Common Controls

Conditions, Style, Region, and Settings Tabs Since every Particle node shares the Conditions, Style, Region, and Settings tabs, you'll find them written up under "The Common Controls" toward the close of this chapter.

### pMerge [pMg]

The pMerge node pMerge Node Introduction Not a single control sits on this node. Its job is to fuse particles arriving from two streams. Downstream of the pMerge node, any node regards those two streams as a single one. Whatever sets were attached to the combined particles at creation time stay intact, which lets nodes after the pMerge pick out particular particles whenever that's needed.

### Inputs

A matched pair of inputs, one orange and one green, sits on the pMerge node. Both of these inputs will take nothing but other particle nodes. Particle 1 and 2 Input: Two particle streams arrive through the two inputs and get merged.

### Basic Node Setup

Two pEmitter nodes are wired together by the pMerge node. From the pMerge, the output can carry on to feed further particle nodes or head into a pRender.

A pMerge node combining two pEmitter nodes.

### pPoint Force [pPF]

The pPoint Force node pPoint Force Node Introduction A force radiating out from one point in 3D space gets applied to the particles by this node. Particles caught inside its sphere of influence can be pulled in or pushed away by the pPoint Force. Four controls belong specifically to the pPoint Force node.

### Inputs

By default a lone orange input sits on the pPoint Force node. Like the majority of particle nodes, that orange input accepts only other particle nodes. Setting the Region menu in the Region tab to Bitmap or Mesh makes a green bitmap or mesh input show up on the node. Input: Output from other particle nodes flows into the orange input. Region: Depending on whether the Region menu points at Bitmap or Mesh, the green or magenta region input receives a 2D image or a 3D mesh. The first option chosen in the menu dictates the input's color. The area in which the point force acts on the particles is set by the 3D mesh or by a channel selected from the bitmap.

### Basic Node Setup

You drop the pPoint Force node in between a pEmitter and a pRender node.

The pPoint Force node sets down a tangent force that pulls particles toward it or drives them away.

### Inspector

Randomize Anytime a Fusion node depends on a random outcome, the Random Seed slider and Randomize button appear. Identical seed values across two nodes yield identical random results. Hit the Randomize button to pick a fresh seed value at random, or move the slider to dial one in by hand. Strength The force the node throws out has its Strength set by this parameter. Attractive forces come from positive values, while negative values give repellent forces. Power This sets how steeply the force's Strength tapers off across distance. With a value of zero, strength never tapers. The bigger the value, the steeper the drop in the force's strength as distance grows. Limit Force The Limit Force control exists to offset possible trouble from temporal sub-sampling. Since a particle's position gets sampled just once per frame (barring increased sub-sampling in the pRender node), a particle could shoot past the Point Force's position and wind up flung off the other way. Raising this control's value cuts the chance of that occurring. X, Y, Z Center Position Within 3D space, these controls stand in for the point force's coordinates along X, Y, and Z.

### Common Controls

Conditions, Style, Region, and Settings Tabs Every Particle node alike carries these four tabs—Settings, Region, Style, and Conditions—so look for their descriptions in "The Common Controls" portion at the end of this chapter.

### pRender [pRn]

The pRender node pRender Node Introduction Turning the particle system into either an image or geometry is the pRender node's role. By default it produces a 3D particle system, which has to be hooked up to a Renderer 3D before it yields an image. That lets the particles blend with other pieces of a 3D scene ahead of rendering.

### Inputs

There's one orange input on the pRender node, plus a green camera input and a blue effects mask input. As with most particle nodes, the orange input accepts only other particle nodes. Set the Region menu in the Region tab to Bitmap or Mesh and a green bitmap or mesh input appears on the node. Input: Output from other particle nodes flows into the orange input. Camera Input: A camera node connected directly, or a 3D scene carrying a connected camera, can feed the optional green camera input, which frames the particles as they render. Effect Mask: A mask shape built from polylines, simple primitive shapes, paint strokes, or bitmaps coming from other tools is what the optional blue input wants. Hooking a mask to this input on 2D particles trims the particle output so the particles show up only inside the mask.

### Basic Node Setup

A particle branch always finishes with the pRender node sitting at its end. With the pRender set to 2D, its output ties into other 2D nodes such as a Merge node. With the pRender set to 3D, its output ties into a 3D node such as a Merge 3D.

All particle branches end with a pRender node.

### Inspector

### The pRender controls

Output Mode (2D/3D) The pRender defaults to 3D output, yet you can make it render a 2D image instead. The 3D and 2D buttons on the Output Mode control handle that. When the pRender isn't tied to a 3D-only or 2D-only node, you can also flip it by picking View > 2D Viewer from the viewer's pop-up menu.

In 3D mode, just a handful of the pRender node's controls do anything at all: Pre-Generate frames, Sub-Frame Calculation Accuracy, Restart, plus Pre-Roll and Automatic Pre-Roll. Every other control touches 2D particle renders alone. On the node tree, the pRender node additionally carries a Camera input that lets a Camera 3D node be connected. Across both 2D and 3D modes, this governs the viewpoint from which an output image renders. Render and the Viewers Select the pRender node within a node tree and the viewers present every onscreen control belonging to the Particle nodes wired into it. That gives a quick, easily tweaked picture of the forces acting on the particle system overall. Pre-Roll Options Before they can work out how the applied forces affect them on the current frame, particle nodes usually need to know each particle's position on the previous frame. That makes shifting current time by hand in anything other than single-frame steps prone to yielding an inaccurate image. The controls here help with this by offering ways to compute the frames in between. Restart This control functions in 3D as well. Click the Restart button and the particle system restarts at the current frame, clearing out any particles made up to that point and beginning the particle system anew at the current frame. Pre-Roll This control functions in 3D as well. Click this button and the particle system recomputes, running from the render range's start through to the current frame. The image produced isn't rendered. Only each particle's position gets calculated. That offers a fairly fast way to confirm the particles shown in the views sit correctly. When the pRender node is on display as the Pre-Roll button gets clicked, the pre-roll's progress appears in the viewer with each particle drawn in point style alone. Automatic Pre-Roll Tick the Automatic Pre-Roll checkbox and the particle system auto-pre-rolls the particles to the current frame each time the current frame changes. That spares you from manually clicking the Pre-Roll button every time you skip through time by more than one frame. So you aren't distracted by visual disruptions, the particle system's progress during an Automatic Pre-Roll isn't shown in the viewers.
