# Pimage emitter and pkill

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pimage emitter, Pkill.
[Chapter index](INDEX.md) / [Previous section](pfollow-and-pfriction-and-pgradientforce-and-pimage-emitter.md) / [Next section](pkill-inputs.md) / [Continue pKill pKI / Inputs](pkill-inputs.md) / [pImage Emitter pIE](pfollow-and-pfriction-and-pgradientforce-and-pimage-emitter.md)
<a id="source-common-controls-5"></a> <a id="source-inspector-2"></a> <a id="source-pkill-pki"></a> <a id="source-sets-tab-1"></a> <a id="source-the-pimage-emitter-controls"></a> <a id="source-the-pimage-emitter-sets-tab"></a>

### Inspector

### The pImage Emitter controls

The overwhelming bulk of this node's controls match those on the pEmitter, and you'll find them documented back in that earlier section. Below you'll find write-ups for the controls that belong to the pImage Emitter node alone. X and Y Density Through the X and Y Density sliders you set how particles map onto pixels along each axis. They govern how dense the sampling grid is. A value of 1.0 on either slider means 1 sample for every pixel. Smaller values yield a looser, more pointillistic spread of particles, while values past 1.0 spawn several particles per pixel across the image. Alpha Threshold The Alpha Threshold serves to rein in particle generation so that pixels carrying semitransparent alpha values won't spawn particles. You can lean on it to firm up the edges of an otherwise soft alpha channel. The larger the threshold value, the more opaque a pixel has to be before it spawns a particle. Note that the default threshold of 0.0 spawns particles for every pixel no matter its alpha, though many may sit transparent and unseen. Lock Particle Color to Initial Frame Tick this checkbox to make the particles hold the color they were born with across the particle's whole life. Leave it off, and as the input image shifts over successive frames, the particles will recolor to track the image. That permits video playback across a grid of particles. Create Particles Every Frame Switch this on and a whole fresh set of particles spawns every frame, rather than just one set on the frame. That can balloon into very large particle systems but opens the door to some intriguing effects—for instance, when the particles get some starting velocity or when emitting off an animated source. Try a small velocity, an

Angle Z of -90, and a seething Fast Noise as the source to land smoothly shifting clouds of particles you could fly through. Note that with this checkbox left off, only a single set of particles ever spawns, so animating any of the emitter's other controls does nothing. X/Y/Z Pivot These controls let you place the grid of emitted particles. Use Z Channel for Particle Z Where the input image driving the particles carries a Z depth channel, that channel can set the particle's starting position in Z space. That can yield an intriguing hollow shell effect when paired with camera rotation on the pRender node.

### Sets Tab

### The pImage Emitter Sets tab

NOTE: A pixel with a black (transparent) alpha channel still spawns invisible particles, unless you push the Alpha Threshold past 0.0. Doing so can drag rendering down badly. An Alpha Threshold value of 1/255 = 0.004 works well for clearing out every fully transparent pixel. The pixels go out on a fixed-size 2D grid across the XY plane, centered on the Pivot position. Switching the Region off its All default lets you pen particle creation to tighter areas. Should you need to resize this grid, drop a Transform 3D node after the pRender. Bear in mind that the various emitter controls touch particles only as they're emitted. That is, they fix the particle's starting state and leave it untouched for the rest of its lifespan. Since pImageEmitter, by default, lets particles out on the first frame alone, nothing comes of animating these controls. Turn the Create Particles Every Frame checkbox on, though, and fresh particles get emitted each frame, taking the stated starting settings for that frame.

### Common Controls

Conditions, Style, Region, and Settings Tabs All Particle nodes share these four tabs alike, so their descriptions sit in the "The Common Controls" section that ends this chapter.

### pKill [pKI]

The pKill node pKill Node Introduction The Kill node exists to destroy (kill) any particle that crosses or intersects its region. It carries no controls of its own, since it has just one possible effect on a particle. The controls on the Region tab usually serve to rein this node in by holding its effect to particles inside a certain region, age, or set, or by lowering the odds of the node acting on a given particle.
