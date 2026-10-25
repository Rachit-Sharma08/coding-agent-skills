# Importing an fbx scene fbx scene import dialog

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](3d-geometry-visibility-parameters.md) / [Next section](fbx-exporter-and-text3d.md) / [Importing an FBX Scene](3d-geometry-visibility-parameters.md)
<a id="source-3d-compositing-basics-part-4"></a> <a id="source-an-imported-model-via-the-fbxmesh3d-node"></a> <a id="source-fbx-scene-import-dialog"></a>

### An imported model, via the FBXMesh3D node

### FBX Scene Import Dialog


You bring mesh geometry in from an FBX file by way of the FBX Mesh node. Where one is present, the first texture mapped to a mesh comes along too. Because various 3D applications gauge their 3D scenes in different units, the imported geometry can come in gigantic next to everything else, since Fusion regards its measurement scale as matching its own system. As an example, when your 3D application is set to millimeters by default, a 100-millimeter object lands as a colossal 100 units. The Size slider among the FBX Mesh Inspector parameters lets you shrink such files down to a scale that fits Fusion’s 3D scene.
