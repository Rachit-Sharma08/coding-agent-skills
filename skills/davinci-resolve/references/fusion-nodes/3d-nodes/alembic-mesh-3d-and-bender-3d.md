# Alembic mesh 3D and bender 3D

Version: DaVinci Resolve 20.3 Reference Manual. Context: Alembic mesh 3D, Bender 3D.
[Chapter index](INDEX.md) / [Next section](bender-3d-and-camera-3d.md)
<a id="source-3d-nodes"></a> <a id="source-3d-nodes-part-1"></a> <a id="source-alembic-import-dialog"></a> <a id="source-alembic-import-options"></a> <a id="source-alembic-mesh-3d-abc"></a> <a id="source-alembic-mesh-3d-controls"></a> <a id="source-alembic-mesh-node-introduction"></a> <a id="source-alembic-node-structure"></a> <a id="source-animation"></a> <a id="source-basic-node-setup"></a> <a id="source-bender-3d-3bn"></a> <a id="source-bender-3d-introduction"></a> <a id="source-common-controls"></a> <a id="source-controls-tab"></a> <a id="source-inputs"></a> <a id="source-inspector"></a> <a id="source-the-alembic-mesh-3d-node"></a> <a id="source-the-bender-3d-node"></a>

### 3D Nodes

Across this chapter we work through, at length, the nodes that go into building 3D composites.

Each node name carries an abbreviation beside it that serves in the Select Tool dialog while you hunt for tools and within scripting references. Throughout this document, treat node trees that show MediaIn nodes in DaVinci Resolve as equivalent to Loader nodes in Fusion Studio, except where a note says otherwise.

### Alembic Mesh 3D [Abc]

### The Alembic Mesh 3D node

### Alembic Mesh Node Introduction

There will be moments when you have to pull in 3D geometry out of programs such as Blender, Cinema4D, or Maya. Among the formats available for bringing in 3D geometry is the Alembic file format. That file type acts as a 3D scene interchange format carrying baked animation alongside its geometry. Put another way, it removes the animation calculation times by tucking fixed, uneditable animation in with 3D geometry. Such animation usually rides along inside a point cache, which preserves the dynamic data — velocity, for instance — once it has been worked out. An Alembic object may hold mesh geometry, cameras, points, UVs, normals, and baked animation. There are two routes to bring Alembic files (.abc) into Fusion:

- Within Fusion pick File > Import > Alembic Scene; over on DaVinci Resolve’s Fusion page the route is Fusion > Import > Alembic Scene instead.
- Add an AlembicMesh3D node to the Node Editor.

That first route is the one to favor; on their own, both Alembic and FBX nodes pull in the whole model as a single object. The Import menu, by contrast, splits the model, lights, camera, and animation apart into a chain of separate nodes. Doing so makes editing, tweaking, and reusing portions of the imported Alembic mesh straightforward. On top of that, transforms held in the file land in Fusion splines and in the Transform 3D nodes, which then save with the comp. Afterward, when the comp is reopened, those transforms come back from the comp rather than from the Alembic file. Meshes get treated another way by Fusion, which always pulls them anew out of the Alembic file. Whatever arbitrary user data exists shifts according to the software that authored the Alembic file, so this category of metadata is largely disregarded.

### Alembic Import Dialog

Picking the file to import brings up an Alembic Import dialog

### Alembic Import options

Up in the top half of the Import dialog you'll see details about the chosen file: the name of the plugin/application that authored the Alembic file, which version of the Alembic software developer kit handled the export, how long the animation runs in seconds where that figure exists, and the frame rate(s) carried in the file. You can pull in assorted objects and attributes by ticking the checkboxes within the Import section.

- Hierarchy: With this on, the entire parenting hierarchy gets rebuilt in Fusion through multiple Transform 3D nodes. With it off, the transforms held in the Alembic file collapse down into the cameras and meshes. That flattening leaves several meshes/cameras wired to one Merge node in Fusion. Keeping it off works best whenever the file carries animation. Turned on, the numerous rigs that drive objects through a scene spawn an equally hefty count of nodes in Fusion, so flattening trims how many nodes land in your node tree.
- Orphaned Transforms: Once the hierarchy option is on, an Orphaned Transforms setting shows up. Switching this Orphan Transforms setting on brings in transforms that parent a mesh or camera. Say you've got a skeleton plus its matching mesh model: the model arrives as an Alembic mesh while the skeleton arrives as a node tree of Merge3Ds. Leave it off and those Merge3Ds never get built.
- Cameras: With this on, bringing in a file pulls cameras along too, complete with Aperture, Angles of View, Plane of Focus, plus the Near and Far clipping plane settings. Whether the resolution Gate Fit comes across hinges on whether the application that exported the file tagged the resolution Gate Fit metadata correctly. Should your camera fail to import properly, look at the setting for the Camera3D Resolution Gate Fit. Bear in mind that 3D Stereoscopic information does not come across.
- InverseTransform: Imports the Inverse Transform (World to Model) for cameras.
- Points: A Points type is among what Alembic files can carry. It amounts to a set of 3D points, each holding position

information. Certain 3D programs push out particles as points. Keep in mind, though, that even though position carries over, the particles' direction and orientation drop away.

- Meshes: This setting governs whether the import takes in 3D models out of the Alembic file. Switch it on and options to bring along UVs and normals appear.

### Animation

A single option lives in this section, the Resampling rate. As an Alembic animation is exported, it gets written to disk using frames per second (fps). On bringing Alembic data into Fusion, the fps get picked up and dropped into the Resample Rate field, unless you already altered it earlier in the current comp. The smart move is to hold the exported frame rate as the resample rate, keeping your samples aligned with the original. Up at the top of the dialog the Detected Sampling Rates information can hint at a good pick if you're uncertain. Even so, by way of this field you can shift the frame rate to produce effects such as slow motion. Within the Alembic file format, not every object and property in a 3D scene enjoys an agreed-upon universal convention. Given that, Lights, Materials, Curves, Multiple UVs, and Velocities currently go unsupported as you bring in Alembic files. Because the FBX file format does carry materials and lights, our advice is to reach for FBX where lights, cameras, and materials are concerned. Reserve Alembic for meshes alone.

### Inputs

Within the Node Editor the AlembicMesh3D node carries two inputs. Each one is optional, since the node is meant to run off the imported mesh. SceneInput: That orange input lets you wire in another 3D scene or model. The imported Alembic objects then join with the other 3D geometry. MaterialInput: The optional green input serves to put a material onto the geometry by wiring up a 2D bitmap image. It lays the connected image across the surface of the geometry in the scene.

### Basic Node Setup

The AlembicMesh3D node is built to sit within a bigger 3D scene. As a rule, once imported, a single node stands in for a 3D geometry model while any transforms live in a separate node. Those nodes brought in as part of the Alembic file feed into a Merge 3D node together with a camera, lights, and whatever else the scene happens to call for.

### Alembic node structure

### Inspector

### Alembic mesh 3D controls

### Controls Tab

Heading the Inspector is the Controls tab. Within it sits a run of distinct controls tied to the Alembic Mesh 3D node along with six clusters of controls shared by most 3D nodes. Over at the close of this chapter, the Common Controls section spells out the shared controls in full. What follows describes the controls specific to the Alembic Mesh 3D. Filename The full file path of the imported Alembic file shows up here. By way of this field you can swap or refresh the file tied to this node.

Object Name This text field lists the name of the imported Alembic mesh, the same name applied when renaming the Alembic Mesh 3D node in the Node Editor. As you import by way of the Alembic Mesh 3D node, leaving this text field empty causes the whole of the Alembic geometry to come in as one mesh. Where geometry is imported via File > Import > Alembic Scene, Fusion fills in this field for you. Wireframe Turning this option on makes the mesh show nothing but the wireframe for the object inside the viewer. Once on, a second option for wireframe anti-aliasing appears. These wireframes can even be rendered out to a file provided the Renderer 3D node has the OpenGL render type chosen.

### Common Controls

Controls, Materials, Transform, and Settings Tabs Within the Controls tab, several controls recur across many 3D nodes: Visibility, Lighting, Matte, Blend Mode, Normals/Tangents, and Object ID. Likewise, the Inspector's Materials tab, Transforms tab and Settings tab show up again on other 3D nodes. Full coverage of these shared controls waits at the close of this chapter inside the “The Common Controls” section.

### Bender 3D [3Bn]

### The Bender 3D node

### Bender 3D Introduction

You reach for the Bender 3D node to bend, taper, twist, or shear 3D geometry off the back of the geometry’s bounding box. It runs by wiring any 3D scene or object into the orange input on the Bender 3D node, then tuning the controls over in the Inspector. Only the geometry within the scene gets reshaped. Whatever lights, cameras, or materials pass straight through untouched. No fresh vertices come out of the Bender node; it merely shifts the vertices already in the geometry. So, when you apply the Bender 3D node to primitives such as the Shape 3D, or Text 3D nodes, raise the Subdivision setting over in the primitive’s node to land a finer result.
