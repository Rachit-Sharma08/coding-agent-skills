# Soft clip basic node setup

Version: DaVinci Resolve 20.3 Reference Manual. Context: Soft clip.
[Chapter index](INDEX.md) / [Previous section](ribbon-3d-and-shape-3d-and-soft-clip.md) / [Next section](soft-clip-and-spherical-camera-and-text-3d.md) / [Soft Clip 3SC](ribbon-3d-and-shape-3d-and-soft-clip.md)
<a id="source-3d-nodes-part-7"></a> <a id="source-basic-node-setup-5"></a>

### Basic Node Setup

The Soft Clip node usually sits just ahead of the Renderer 3D node so that downstream tweaks to lighting and textures leave the result untouched. It can sit anywhere within the 3D portion of the node tree whenever the soft clipping effect is called for over only a portion of the scene.


Soft Clip sitting in the chain between a Merge 3D and a Renderer 3D node
