# Apple immersive motion data and select the axis to view

Version: DaVinci Resolve 20.3 Reference Manual. Context: Apple immersive workflow.
[Chapter index](INDEX.md) / [Previous section](image-output-scaling-settings-and-color-management.md) / [Next section](final-node-graph-and-color-grading.md)
<a id="source-apple-immersive-motion-data"></a> <a id="source-apple-immersive-workflow-part-2"></a> <a id="source-compositing-with-the-immersive-patcher"></a> <a id="source-creative-considerations"></a> <a id="source-mediaout-nodes"></a> <a id="source-renderer3d"></a> <a id="source-select-the-axis-to-view"></a> <a id="source-the-stereo-eye-parameter"></a> <a id="source-titles"></a> <a id="source-vfx-compositing"></a>

### Apple Immersive Motion Data

With immersive content, fast or abrupt camera moves can throw the viewer off. For the sake of viewer comfort, steer clear of takes that have snappy pans/tilts, rotating motion, or crooked horizons. The Apple Immersive Motion Data feature plots the x, y, and z acceleration along with gyroscope position values, giving an objective picture of where the camera’s motion may be too forceful. Editors lean on that readout to steer away from disorienting stretches of footage. 1 Right-click an immersive clip out on the timeline. 2 Pick Apple Immersive Motion Data.

Pick the Apple Immersive Motion Data feature as an aid for steering clear of disorienting stretches of footage

A graph turns up in the video track charting the x, y, z acceleration rates In this case, the camera kept rolling while the operator was still rigging it. Those spikes in the graph mark abrupt movement as the camera got lifted, turned, and set on his shoulder. The better choice is the back half of the video, where the readouts flatten out once the camera has settled. Up at the graph’s top left, click the displacement arrow.

### Select the Axis to view

Readouts can be switched on or off depending on what the shot contains and how the camera was moving.

### Titles

On the edit page, text can be laid into an immersive scene with any of the Effects panel’s title tools – Text, Text+, MultiText, Scroll, and the various lower third options. Set above an immersive clip, the title generator draws on that clip’s ILPD (Immersive Lens Profile Data) to bend the text precisely to the scene’s lens warp. Where no ILPD exists (say, when you put text over a black backdrop or an immersive CGI scene), default lens distortion steps in so the text still looks suitably warped through the Apple Vision Pro. 1 Within the Effects panel, head to Toolbox > Titles. 2 Drag the Text generator onto the timeline. Drop it on a video track above an immersive clip to fold it into the scene. Like backdrops, Text generators can’t straddle clip boundaries. Since every clip renders with its own lens space, any title spilling across shots risks getting warped between them. 3 Trim the title back to the video edit point(s). 4 Turn to the Inspector to compose and style the title text. 5 Open the Settings tab and work the Convergence slider to place the text within 3D space. Slide it left to push the title deeper, or right to pull it nearer.

Convergence reads most clearly while you monitor on the Apple Vision Pro. Relying on other monitoring methods, you can alter how text convergence shows in the viewer by switching the Vision mode of the video layer beneath it on the color page. 6 Head to the color page. 7 Open the 3D palette. Mid-palette, the Vision column lets you swap the stereoscopic standard that projects the immersive media. 8 Pick the Stereo tab. 9 Set the Out mode to Anaglyph (Color).

Adjusting the text generator’s Convergence parameter back in the edit page’s Inspector panel becomes far more intuitive once you view it through anaglyph (or anachrome) glasses.

### Creative Considerations

So early in the life of the Blackmagic URSA Cine Immersive camera, with Apple Vision Pro production just beginning, the encouragement to filmmakers is to play with the format, surfacing best practices, setting fresh rules, and uncovering workflows that conventional filmmaking never pictured before.

Keeping that in view, several facets of immersive production have already been singled out for extra care, all toward keeping audiences fully absorbed and visually at ease.

- The edit should be in mind from pre-production onward. Given the particular demands of shot length and audience motion comfort, filmmakers have to shoot scenes already thinking of the final cut.
- Keep clips with fast camera moves to a minimum or skip them, since they can disorient the viewer. Favor locked-off shots or gentle pans and dollies instead.
- Tilted or extreme camera angles can disorient too – go with takes that sit level to the subject and at an easy distance (not crowded in close).
- Fresh environments take more time to take in within immersive media than they do in a 2D scene. Slow your cuts down so the viewer can adjust to each new setting.
- As you cut from clip to clip, keep track of where the viewer was likely looking during the earlier shots. Don’t stage key action on the left of the frame if the audience’s gaze was just drawn toward the right.
- Spatial Audio carries a great deal of the storytelling – think of it as one more character in immersive productions.

### VFX Compositing

Switch ‘Apple Immersive workflow’ on in the Project Settings and purpose-built Fusion parameters open up smooth stereoscopic workflows and immersive-compliant compositing. MediaOut nodes offer left and right eye output choices, while the Immersive Patcher tool handles equirectangular projection and composition.

### MediaOut nodes

The first time you step onto the Fusion page with an immersive clip loaded, the Nodes graph holds a pair of MediaIn nodes wired to their two matching MediaOut nodes.

The nodes graph carries two MediaIn nodes wired to two MediaOut nodes Inside the MediaOut Inspector, the Stereo Eye parameter serves to route the eye signal output.

### The Stereo Eye parameter

Out of the box, MediaOut1 maps to the Left eye and MediaOut2 to the Right. With that arrangement you can dive straight into building stereo-compliant composites and graphic overlays. Those twin MediaOut nodes also push two signal variants into the color page’s node editor for additional image refinement. Reach the MediaOut2 signal on the color page by right-clicking in the node editor and picking ‘Add Source’.

Adding the MediaOut2 source into the node editor. Set the Stereo Eye parameter to Auto and the MediaOut node merges the signals, handing them to the correct eyes on the timeline. That lets you run Fusion’s multilayer workflow to feed both left and right signals into one MediaOut node.

### Renderer3D

For 3D graphics or CGI on an immersive timeline, the Renderer3D node provides several eye setups along with the capacity to process both left and right layers.

That opens the door to building elaborate 3D titles or whole CGI scenes and feeding them straight onto a stereoscopic timeline in immersive projects With this setup in play, the drop-down menu at the top right of the Fusion viewers lets you toggle between the left and right eye of your composition.

The Fusion viewers’ drop-down menu lets you toggle between the left and right eye

### Compositing with the Immersive Patcher

The Immersive Patcher tool lets you briefly ‘undistort’ a stretch of an immersive clip so tracking, painting, and compositing become easier on a flat plane. When you’re done, a second Immersive Patcher re-distorts the immersive signal and folds the freshly composited elements back into the scene. 1 Drop Immersive Patcher into the node pipeline. The immersive patcher 2 Within the Inspector, click Undistort.

The Undistort tab 3 Lean on the X, Y, and Z rotation parameters to pick out a portion of the immersive image you want flattened. 4 Carry on compositing just as you would with an ordinary 2D video signal. That covers (though isn’t limited to) standard paint techniques for erasing stray objects, sampling frame regions with transforms and polygons to extend a set, or laying in mattes, text, and outside image/video layers to swap out signs or screens. With that done, the flat image has to be re-distorted so it lines up with the original immersive warp. 5 Copy the Immersive Patcher so the original rotation and angle-of-view information is kept. 6 Paste the Immersive Patcher beyond the composite nodes and wire it to the tail of the composition pipeline.

The second Immersive Patcher, pasted out of that first copy.

7 Within the Inspector, click Distort. 8 Merge the composited patch onto the original clip so the effect folds into the immersive scene.
