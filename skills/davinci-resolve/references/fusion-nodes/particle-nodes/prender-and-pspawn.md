# Prender and pspawn

Version: DaVinci Resolve 20.3 Reference Manual. Context: Prender, Pspawn.
[Chapter index](INDEX.md) / [Previous section](pkill-and-pmerge-and-ppoint-force-and-prender.md) / [Next section](pspawn-and-ptangent-force-and-pturbulence.md) / [pRender pRn](pkill-and-pmerge-and-ppoint-force-and-prender.md)
<a id="source-about-pre-roll"></a> <a id="source-basic-node-setup-4"></a> <a id="source-conditions"></a> <a id="source-grid-tab"></a> <a id="source-image-tab"></a> <a id="source-inputs-3"></a> <a id="source-only-render-in-hi-q"></a> <a id="source-pspawn-psp"></a> <a id="source-scene-tab"></a> <a id="source-the-prender-grid-tab"></a> <a id="source-the-prender-image-tab"></a> <a id="source-the-prender-scene-tab"></a> <a id="source-the-pspawn-controls"></a> <a id="source-view"></a>

### About Pre-Roll

Pre-Roll matters because a particle system's state hinges entirely on the last known position of the particles. Should current time jump to a frame where the prior frame's particle state isn't known, the particle's display is worked out from the last known position, giving inaccurate results. To see it in action: 1 Drop a pEmitter plus a pRender node into the composition. 2 Show the pRender inside one of the viewers. 3 Dial the particles' Velocity to 0.1. 4 Park the pEmitter along the screen's left edge. 5 Bring the Current Frame to 0.

6 Define a Render Range that runs from 0–100 and click the Play button. 7 Watch the way the particle system behaves. 8 Pause playback and roll the current time back to frame 0. 9 Within the pRender node, switch off the Automatic Pre-Roll option. 10 With the current time number field, leap to frame 10, then on to frames 60 and 90. See how the particle system merely adds onto the particles it already made and won't try to produce the particles that should have emitted across the in-between frames. Now try clicking the Pre-Roll button in the pRender node. The particle system state now reads correctly. With simple, fast-rendering particle systems, leaving the Automatic Pre-Roll option on is advised. With slower particle systems spanning long time ranges, you may prefer to PreRoll only by hand, when needed.

### Only Render in Hi-Q

Tick this checkbox and the particles' style is overridden whenever the Hi-Q checkbox is off, yielding only fast-rendering Point-style particles. That comes in handy while you deal with a big batch of sluggish Image-based or Blob-style particles. To view the particles the way they'd look in a final render, just switch the Hi-Q checkbox on.

### View

This drop-down list offers options that set where the camera view sits within a 3D particle system. Its default, Scene (Perspective), renders the particle system from a virtual camera's viewpoint, whose position you can change through the Scene tab's controls. The remaining options deliver orthographic views of the particle system's front, top, and side. Bear in mind this control leaves the position of the onscreen controls for Particle nodes untouched. While in 2D mode, the onscreen controls always draw as though the viewer were displaying the front orthographic view. (In 3D mode the control positions stay correct throughout.) The View setting gets ignored when a Camera 3D node is wired to the pRender node's Camera input on the node tree, or when the pRender sits in 3D mode.

### Conditions

Blur, Glow, and Blur Blend During 2D particle generation, these sliders lay a Gaussian blur, glows, and blur blending over the image as it renders, handy for softening the particles and blending them. The result matches what you'd get by dropping a Blur downstream of the pRender node within the node tree. Sub-Frame Calculation Accuracy This sets how many sub-samples get taken between frames while the particle system is computed. Raising the value sharpens the calculation's accuracy yet also lengthens how long the particle system takes to render. Pre-Generate Frames This control makes the particle system pre-generate a chosen number of frames ahead of its first valid frame. It's there to hand the particle system a starting state to launch from.

A handy case for this is a shot where particles build the smoke drifting up from a chimney. Dial Pre-Generate Frames high enough that the smoke is already in the scene as the render starts, instead of having it merely begin to creep from the emitter over the opening few frames. Kill Particles That Leave the View Tick this checkbox control and any particles wandering past the image's visible edges get destroyed automatically. That can trim render times. Particles wiped out this way never come back, no matter what external forces push on them.Generate Z Buffer Tick this checkbox and the pRender node turns out a Z Buffer channel in the image. Each particle's depth is captured in the Z Buffer. That channel then feeds further depth operations such as Depth Blur, Depth Fog, and Downstream Z Merging. Switching this option on tends to push the particle system's render times up sharply. Depth Merge Particles Switch this option on and the particles get combined through Depth Merge techniques in place of layer-based ones.

### Scene Tab

Z Clip With the Z Clip control you place a clipping plane out in front of the camera. Particles passing through that plane get clipped, which keeps them from striking the camera's virtual lens and overrunning the scene.

### The pRender Scene tab

### Grid Tab

None of these controls touch 3D particles. The grid is a useful, non-rendering display aid for orienting the 2D particles in 3D space. It never turns up in renders, much as a center crosshair never appears in a render. You set the width, depth, line count, and grid color through the controls in this tab. Animating these controls isn't possible.

### The pRender Grid tab

### Image Tab

This tab's controls let you dial in the rendered image's resolution, its color depth, and its pixel aspect as produced by the node.

### The pRender Image tab

Process Mode This menu control lets you pick the Fields Processing mode Fusion applies when rendering image changes. The Has Fields checkbox control in the Frame Format preferences decides the default option. Use Frame Format Settings Tick this checkbox and the width, height, and pixel aspect of the images the node renders get pinned to the values laid out in the composition's Frame Format preferences. Should those Frame Format preferences change, the resolution of the node's output image shifts to keep pace. Turning this option off can help when you want to build a composition at a resolution different from the eventual target resolution for the final render. Width/Height You set the rendered image's Width and Height dimensions with this pair of controls. Pixel Aspect This control sets the Pixel Aspect ratio of the rendered particles. A 1:1 aspect ratio yields a square pixel measuring the same on every side (like a computer display monitor), whereas a 0.9:1 aspect yields a slightly rectangular pixel (like an NTSC monitor). NOTE: Right-click the Width, Height, or Pixel Aspect controls to bring up a menu listing the file formats set in the preferences Frame Format tab. Picking any listed option sets the width, height, and pixel aspect to that format's values accordingly. Depth The Depth menu sets the particles' pixel color depth. A 32-bit pixel eats 4X the memory of an 8-bit pixel but carries far better color accuracy. Float pixels permit high dynamic range values past the usual 0…1 range, for depicting colors brighter than white or darker than black. Source Color Space The Source Color Space menu lets you set the footage's Color Space to support a linear workflow. Unlike the Gamut tool, this performs no real color space conversion; instead it writes the source space data into the metadata when that metadata is absent. A downstream Gamut tool using the From Image option, or a Saver where explicit output spaces are defined, can then draw on that metadata. Two options are on offer:

- Auto: On its own, reads whatever metadata the image holds and carries it forward.
- Space: Brings up a Color Space Type menu from which you pick the image's right color

space. Source Gamma Space Through the Curve type menu you assign the footage's Gamma Space, and the Remove Curve checkbox lets you take it off while in a linear workflow. Three options live in the Curve type menu:

- Auto: On its own, reads whatever metadata the image holds and carries it forward.
- Space: Brings up a Gamma Space Type menu from which you pick the image's right

gamma curve.

- Log: Brings up the Log/Lin settings, similar to the Cineon tool.

For deeper detail, turn to Chapter 99, "Film Nodes," within the DaVinci Resolve Reference Manual, or to Chapter 39 over in the Fusion Reference Manual. Remove Curve Based on the Gamma Space you picked, or the one detected under Auto mode, the Gamma Curve is either pulled off the material or run through a log-lin conversion, which effectively recasts it as a linear output space. Motion Blur As with Fusion's remaining 2D nodes, you turn Motion Blur on from within the Settings tab. Quality, Shutter Angle, Sample Center, and Bias are all yours to set, and Blur then applies to each moving particle. NOTE: When Motion Blur runs on 3D mode particles (those rendered via a Renderer 3D), the identical motion blur settings must likewise be set on the Renderer 3D node.

### pSpawn [pSp]

The pSpawn node pSpawn Node Introduction The pSpawn node turns each affected particle into an emitter in its own right, capable of spawning one or more particles. The source particle carries on to the close of its lifespan, while every particle it throws off turns fully independent, holding a lifespan and properties all its own. For as long as a particle stays under the pSpawn node's effect, it keeps producing particles. Reining in the node's reach matters: use limiters such as Start and End Age, Probability, Sets and Regions, and animate the emitter's parameters so the node only kicks in when it should.

### Inputs

The pSpawn node ships with a single orange input by default. As with most particle nodes, that orange input accepts only other particle nodes. An image input becomes available once you pick Bitmap from the Style menu in the Style tab. On top of that, switching the Region tab's Region menu to Bitmap or Mesh makes a pair of region inputs—one for bitmap, one for mesh—appear on the node. Which colors these inputs take depends on the order in which they're switched on. Input: Output from other particle nodes feeds the orange input. Style Bitmap Input: A 2D image meant to serve as the particles' image goes into this image input. Because that image gets duplicated into potentially thousands of particles, keeping these images small and square is wise—say, 256 x 256 pixels.

Region: Whether the Region menu is set to Bitmap or Mesh decides whether the region inputs take a 2D image or a 3D mesh. The first option picked in the menu sets the input's color. Where particles get emitted is defined by the 3D mesh or by a channel chosen from the bitmap.

### Basic Node Setup

You position the pSpawn node between the pEmitter and pRender nodes. With the Age parameter inside the pSpawn's Conditions tab, fresh particles can spawn as the older ones expire. That's one route to sending a trail of particles rocketing skyward and bursting into glittering fireworks.

A pSpawn node set up to spawn fresh particles at chosen moments across the lifespan of the older ones Inspector A great many controls sit on the pSpawn node, the bulk of them precise duplicates of those in the pEmitter node. A handful are unique to the pSpawn node, and what they do is laid out below.

### The pSpawn controls

Affect Spawned Particles Tick this checkbox and particles born from spawning fall under the pSpawn node's effect too on later frames. That can balloon the system's particle count exponentially, shoving render times to an unreasonable level. Treat this checkbox with care.

Velocity Transfer This control sets how much of the source particle's velocity carries over to the particles it spawns. At its default of 1.0, each new particle inherits 100 percent of the source particle's velocity and direction. Lower the value and less of the original motion passes to the new particle.
