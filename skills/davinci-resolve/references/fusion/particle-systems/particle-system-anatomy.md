# Introduction to particle systems and anatomy of a simple particle system

Version: DaVinci Resolve 20.3 Reference Manual. Context: Particle systems.
[Chapter index](INDEX.md) / [Next section](blowing-leaves-preset-from-the-templates-category.md)
<a id="source-anatomy-of-a-simple-particle-system"></a> <a id="source-compositing"></a> <a id="source-emitters"></a> <a id="source-forces"></a> <a id="source-introduction-to-particle-systems"></a> <a id="source-particle-nodes-explained-by-type"></a> <a id="source-particle-system-distribution"></a> <a id="source-particle-systems"></a> <a id="source-particle-systems-1"></a> <a id="source-rendering"></a>

### Particle Systems

The goal of this chapter is a short orientation toward building fully 3D particle systems, which rank among the strongest capabilities Fusion offers. After the fundamentals here make sense, you can dig into every individual particle system node by turning to Chapter 114, “Particle Nodes,” within the DaVinci Resolve Reference Manual, or alternatively Chapter 54 over in the Fusion Reference Manual.

### Introduction to Particle Systems

A particle system is a computer simulation driven by adjustable rules that spawn and animate huge quantities of elements on their own, mimicking smoke, dust, fire, leaves, sparks, or practically any other moving collection of shapes. Because Fusion functions as a complete 3D compositing environment, you can build these systems in either 2D or 3D, granting enormous flexibility and the ability to generate every sort of visual effect or abstract animated material destined for motion graphics.

A 3D particle system, also created entirely within Fusion You will find the three core nodes needed to assemble particle systems sitting on the toolbar. Like the 3D nodes positioned to their right, they sit in left-to-right sequence matching the order in which they have to be wired up, so should you ever forget how to assemble a basic particle system, just click those three particle system nodes one after another from left to right and a working particle system appears.

The pEmitter, pMerge, and pRender particle system nodes available from the toolbar That said, these three nodes barely scratch the surface. Expanding the Particle category within the Effects Library exposes a great many particle nodes built to operate jointly and produce ever more elaborate particle behavior.

A selection drawn from the nodes the Particles bin of the Effects Library offers

Every particle node's name starts with the letter “p,” and the whole family is engineered to cooperate, yielding refined results out of fairly basic operations and parameters. The section coming up demonstrates assorted ways these particle nodes can be wired to deliver distinct outcomes.

### Anatomy of a Simple Particle System

At its most basic, a particle system amounts to one pEmitter node feeding into a pRender node. The pEmitter node holds the essential controls that spawn assorted kinds of particles through different methods, whereas the pRender node has to be present to produce a 2D or 3D output suitable for compositing alongside the rest of the scenes in your composition.

The minimum node tree required to create a simple particle system Should your project demand something richer, you can join several pEmitter nodes through a pMerge node (essentially the particle-oriented counterpart of a Merge node) to build compound particle systems in which several particle types blend together into a single outcome.

Merging a pair of pEmitter nodes into a compound particle system that fuses two particle varieties When the goal is particle behavior that feels more lifelike, attach “forces” to each emitter. Such forces amount to physics-based or behavioral simulations that, on their own, drive the affected particles into varied patterns of movement or otherwise subject them to other objects present in the scene.

Tailoring how pEmitter nodes behave through assorted forces that enrich the particle animation

A pEmitter node can also have the node types below connected to it for deeper particle-system customization:

- Hook a 2D image up to a pEmitter node when you want fully custom particle shapes. Confirm the image carries a suitable alpha channel.
- Hook a Shape3D or another piece of 3D geometry to a pEmitter node to define a tighter emission region (by switching Region to Mesh inside the Region tab).

Tailoring pEmitter nodes via mesh geometry for regions and via 2D images for particle shape The cases above presume you intend to produce 2D renders for blending back into a larger 2D composition. Yet since particle systems are inherently 3D, you can alternatively emit your particle system in a form ready to live within other 3D scenes throughout your composition.

Wiring a particle system into a Merge3D node so that lighting and shadows in a 3D scene act on the particles

Sitting right at the top of the pRender node's Inspector controls, the Output Mode toggles between 2D and 3D according to whether you mean to merge the particle-system result with 2D layers or with elements inside a 3D scene.

Deciding via the pRender node’s Inspector controls whether a particle system emits 2D or 3D output Wiring a pRender node into a Merge3D node forces the Output Mode to 3D, so the pRender node emits 3D geometry meant for use inside the Merge3D node’s scene. As a result the particles become eligible for lighting, can throw shadows, and can engage with 3D objects living in that scene.

The result of using a particle system within a 3D scene NOTE: After you choose 2D or 3D for the pRender node and then alter any of the nodes in the Inspector, switching the output mode afterward is no longer possible.

### Particle System Distribution

To tune how emitted particles are spread out, click the pEmitter node so its controls appear in the Inspector, expand the Velocity controls under the Controls tab, and work the Angle, Angle Variance, Angle Z, and Angle Z Variance controls to shape both the direction and the spread across which particles leave the emitter. Every one of these controls supports animation.

The Velocity Angle and Angle Variance controls on a pEmitter node govern both the direction and the spread of particle distribution You can place and orient particle systems by loading the pEmitter nodes that produce the particles into a viewer and then using the onscreen 3D position and Rotation controls supplied there to reposition the whole system.

A pEmitter node that has been loaded into the viewer while its onscreen rotation controls are switched on As another option, turn to the Inspector controls on the pEmitter’s Region tab to set Translation, Rotation, and Pivot. Each of these controls can likewise be animated.

A pEmitter node’s Region controls open in the Inspector

### Particle Nodes Explained by Type

Here we walk through the four categories of particle system nodes found in the Effects Library.

### Emitters

Every particle traces back to a pEmitter node as its origin. Any given pEmitter node can be tuned to emit one type of particle, with so much customization that you'll essentially never produce two identical particle types. Together with the pRender node, it is the sole other node that a particle system absolutely cannot do without. A pEmitter node carries four parameter tabs: Controls: The chief controls dictating the particle count (Number), how long particles persist (Lifespan), their speed (Velocity), how broadly they spread (Angle and Angle Variance), their orientation (Rotation Mode together with X, Y, and Z controls), and any spin present (Spin X, Y, and Z controls). Alongside each particle-generation parameter sits a matching Variance control, which lets you make that parameter less uniform and more lifelike by adding random variation. Sets: This tab gathers settings governing the physics of the particles the node emits. They leave the particles' look untouched. Rather, they alter behaviors like velocity, spin, quantity, and lifespan. Style: Where the Controls tab offers only a basic option for picking a particle color, the Style tab supplies fuller controls such as color variance and Color Over Life controls. On top of that, size controls including Size Over Life, fade controls, and blur controls allow elaborate particle animations from very few adjustments, while Merge controls hand you extra say over how overlapping particles blend on screen. A cluster of controls along the bottom governs the timing of animated effects.

Region: The Region tab is where you pick the kind of geometric region used to scatter particles through space and decide whether particles emerge from that region's volume or its surface. The Winding Rule and Winding Ray Direction controls govern how the mesh region copes with creating particles across geometric meshes that aren't fully sealed, a frequent situation with meshes brought in from outside applications. Adjusting these final parameters comes up often whenever imported mesh geometry serves as an emission region, because even seemingly sealed geometry tends to “leak” particles due to vertices that were never properly welded.

### Forces

A large share of the particle nodes housed in the Particles bin of the Effects Library are “forces,” which strengthen a particle simulation by mimicking how assorted forces press on the particles an emitter produces. Certain forces—pDirectionalForce, pFlock, pFriction, pTurbulence, and pVortex among them—operate on particles without requiring any additional input. They function as plain “acts of nature” that nudge particles into different behaviors. Different forces, including pAvoid, pBounce, pFollow, and pKill, team up with 3D geometry in a scene like shapes or planes so that events trigger whenever a particle touches or approaches that geometry. Keep in mind that several of the particles covered earlier are also able to use geometry to steer their behavior, so this split between the two force categories isn't always sharp.

### Compositing

A straightforward route to merging several emitters, so that varied particle types act in concert toward a polished result, is the pMerge node. The pMerge node exposes no parameters at all; you merely wire emitters into it and they merge automatically.

### Rendering

You need the pRender node regardless of whether a particle system's output feeds a 2D Merge node or a Merge3D node bound for a 3D scene. Together with the pEmitter node, it is the only other node a particle system truly requires. Controls: The principal controls letting you decide between 2D and 3D image output, choose whether to layer blur or glow onto the particle systems, plus numerous further settings that shape how particles get rendered. Scene: These controls let you reposition the whole particle scene in one move. Grid: The grid serves as a useful, non-rendering reference for situating 2D particles within 3D space. It never appears in any render. You can set the width, depth, line count, and grid color through the controls held in this tab. Image: Governs the pRender node's output, with say over the process mode, resolution, and color space settings applied to that output.
