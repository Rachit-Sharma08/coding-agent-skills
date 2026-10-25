# Navigating the 3D view and transforming cameras and lights using the viewers

Version: DaVinci Resolve 20.3 Reference Manual. Context: 3D compositing basics.
[Chapter index](INDEX.md) / [Previous section](merge3d-lighting-and-scene-transforms.md) / [Next section](transformations-and-transform-tab-of-a-merge3d-node.md)
<a id="source-3d-compositing-basics-part-2"></a> <a id="source-material-viewer"></a> <a id="source-navigating-the-3d-view"></a> <a id="source-the-material-viewer-mode-of-the-viewer"></a> <a id="source-transforming-cameras-and-lights-using-the-viewers"></a> <a id="source-transparency-sorting"></a> <a id="source-transparency-sorting-in-the-viewer-contextual-menu"></a>

### Navigating the 3D View

By and large, panning and scaling the 3D Viewer relies on the same controls the 2D Viewer uses. For fuller detail on the choices the 3D Viewer provides, turn to "Using Viewers." — that's Chapter 69 of the DaVinci Resolve Reference Manual, or Chapter 7 within the Fusion Reference Manual. Panning in a 3D Viewer goes like this:

- Hold the middle mouse button and drag in the viewer.

To dolly (zoom) in the 3D Viewer, do one of the following:

- Press and hold both the middle and left mouse buttons, then drag sideways inside the viewer.
- Keep the Command key held while you work the scroll control on your pointing device.

To rotate around the 3D Viewer, do the following:

- With the Option key held, middle-button-drag from side to side within the viewer.

To frame particular objects within the viewer: 1 Pick the viewer where you intend to work. 2 Do one of the following:

- Press Shift-F to Fit all objects in the viewer.
- Hit F for Fit to selection (or, with nothing selected, Fit All).
- Hit D to Rotate the viewer so it faces the middle of whichever object is selected without

shifting where the viewer sits. On top of that, picking a 3D node in the Node Editor likewise picks its matching object in the 3D Viewer.

### Transforming Cameras and Lights Using the Viewers

When the viewer looks through a 3D object in the scene — a camera or spotlight, say — the ordinary panning and rotating controls for the viewer now act straight on the position of whatever camera or spotlight you're peering through. Here's an example. To reposition a camera while you're viewing through it: 1 Right-click the viewpoint label and pick a camera off the contextual menu. (Optional) In dual-viewer mode, you can drop the camera you chose in one viewer into the second viewer so you can watch its position as you go. 2 Bring the pointer over into whichever viewer is showing that camera's viewpoint. 3 Drag with the middle and left mouse buttons held to zoom that viewer, middle-clickdrag to pan it, or option-middle-click-drag to spin it — and in every case the camera moves right along with you.

Once a viewer is showing what a camera or light sees, panning, zooming, or rotating that viewer (at right) really moves the very camera or light you're looking through (at left) The scene can even be observed from a Merge3D or Transform3D node's vantage point by choosing that object from the Camera > Others menu. The very same transform techniques will then reposition the object. That comes in handy when you're attempting to point an object a particular direction.

### Transparency Sorting

Although a 3D scene's geometry order normally follows the Z-position of every object, sorting each face of each object across a big scene can eat up a tremendous amount of time. For the best achievable performance, the OpenGL renderer and viewers fall back on a Fast Sorting mode. You set it by right-clicking in the viewer and picking Transparency > Z-buffer. That route is far quicker than a complete sort, yet it can also give wrong results once scene objects turn partly transparent. The Sorted (Accurate) mode is there to carry out a more precise sort, trading away some performance to do it. You choose that mode from the Transparency menu in the viewer's contextual menu. A Transparency menu also appears on the Renderer3D whenever its Renderer Type is set to OpenGL. Sorted mode won't support shadows under OpenGL. The software renderer relies on the Sorted (Accurate) method at all times.

### Transparency Sorting in the viewer contextual menu

The simple guideline: reach for the Full/Quick Sort modes whenever a scene holds overlapping transparency, and otherwise stick with Z-buffer (Fast). Should the Full Sort method prove too sluggish, fall back to Z-buffer (Fast).

### Material Viewer

Viewing a node drawn from the 3D > Material category of nodes in the Effects Library makes the viewer flip over to a Material Viewer automatically. That Material Viewer lets you preview the material as it sits on a lit 3D sphere, rendered with OpenGL by default.

### The Material Viewer mode of the viewer

Right-clicking the viewer and picking options from the contextual menu lets you set the kind of geometry, the renderer, and the lighting state alike. Every viewer carries A and B buffers to help you compare several materials. Ways to work with the Material Viewer:

- To swap the shape of the previewed geometry, right-click the viewer and pick an option from the contextual menu's Shape submenu. Whatever geometry the material covers is pinned to the viewer's center and scaled to fit. Neither panning nor scaling the Material Viewer is possible.
- For a different angle on the material, rotate the Material Viewer by holding Option, pressing the middle mouse button, and dragging side to side.
- The light previewing the material can be repositioned by dragging with the middle mouse button. As an alternative, right-click the viewer and pick an option from the contextual menu's Lighting > Light Position submenu.
- Lighting can also be switched on and off by right-clicking the viewer and selecting Lighting > Enable Lighting from the contextual menu.
- To set which renderer previews the material, right-click the viewer and pick an option from the contextual menu's Renderer submenu.
