# Uvolume controls

Version: DaVinci Resolve 20.3 Reference Manual. Context: Uvolume.
[Chapter index](INDEX.md) / [Previous section](utransform-and-uvariant-and-uvisibility-and-uvolume.md) / [uVolume uVo](utransform-and-uvariant-and-uvisibility-and-uvolume.md) / [Next section](usd-volume-and-light-nodes.md)
<a id="source-the-uvolume-controls-for-manipulating-vdb-files"></a> <a id="source-usage"></a> <a id="source-usd-nodes-part-3"></a>

### Usage

Adding uVolume to the Node Editor pops a File dialog open automatically so you can select a VDB file off your media drive. You may bring in either one VDB file or a VDB sequence (animated VDB). After a VDB is loaded with the uVolume node, the uVolume serves to trim, loop, and alter the speed of the imported asset.

### The uVolume controls for manipulating VDB files

Density is tunable through the Scale control, which opens the door to careful, fine-grained tweaks. Color controls for the VDB sit in the Emission section. The Mode selection pulldown is where you pick the method used to alter the VDB's color. The available emission modes are:

- Color: Lays a single ‘diffuse’ color across the imported VDB. Keep in mind that USD lights leave a VDB untouched once its color is set to white.
- Field: Spreads one overall color into a chosen Emission Field.
- Blackbody: Derives color and intensity from temperature, which makes it a good fit for rendering fire and

explosions.

- Gradient: Lets you lay a span of colors across a designated field. The Gradient choice hands

you several controls for aiming at a field and then painting it with the colors you nominate. Standard transformation controls — the kind seen on most nodes throughout Fusion's USD suite — come by way of the uVolume.
