# Curve window to isolate a car and converting linear circular and polygon windows into bezier curves

Version: DaVinci Resolve 20.3 Reference Manual. Context: Secondary windows.
[Chapter index](INDEX.md) / [Previous section](window-transform-and-viewer-position.md) / [Next section](windows-and-qualifiers-together.md)
<a id="source-combining-power-windows-with-the-mask-control"></a> <a id="source-converting-linear-circular-and-polygon-windows-into-bezier-curves"></a> <a id="source-copying-and-pasting-windows"></a> <a id="source-curve-window-to-isolate-a-car"></a> <a id="source-resetting-the-window-palette"></a> <a id="source-saving-window-presets"></a>

### Curve window to isolate a car

TIP: Switching the Viewer to full-screen mode can make drawing detailed shapes easier. As you draw, the Viewer can also be zoomed in and out — use a mouse scroll wheel, or press Command-Plus or Command-Minus. To draw a curve: 1 Switch on the Curve window style control. 2 Click somewhere in the Viewer to begin dropping control points and sketching the shape you want. 3 Click and drag to lay down and shape Bezier curves, or simply click and let go to place a sharp angle. 4 To wrap up the drawing and close the shape, click the first control point you placed for a corner, or click and drag on that first control point for a Bezier curve. With a curve drawn, there are many ways to work on it. Quick ways to modify a curve:

- To add points: Click anywhere on a curve to add control points.
- To reshape a curve: Drag any control point somewhere new. You can move control points even mid-draw on a fresh curve — picking earlier points to reposition them, tweak their spline handles, or delete previously added points — with no need to finish the window first.
- To move a curve: Drag anywhere inside or just outside a curve to shift it.
- To symmetrically change a Bezier curve: Drag any Bezier handle. Its opposite handle swings the other way on its own.
- To asymmetrically change a Bezier curve: Option-drag any Bezier handle. Its opposite handle holds still while you drag the current one. After you've built an asymmetric pair of Bezier handles, they travel together as a unit when you just drag a handle. Option-drag is needed to change the angle.
- To turn a curve into a corner: on any Bezier curve control point, Option-double-click to switch it to a sharp-angled corner point.
- To turn a corner into a curve: on any corner point, Option-click and drag to pull out a Bezier handle, switching it to a curve.
- To remove points: Middle-click the control point you want to remove.

NOTE: Should you delete a control point from a polygonal window that's been animated already by means of the Keyframe Editor, that point pops on and off sharply at the keyframes building the animation. You can likewise Shift-drag a bounding box to grab several control points on a curve and move, delete, or transform them all together.

A Shift-drag of a bounding box across several control points lets you handle them all in one go. To grab several control points on a curve: 1 Keep the Shift key held and drag a bounding box over whichever control points you'd like to adjust or remove. Every enclosed control point becomes highlighted. 2 Do one of the following:

- To move the control points: Drag anywhere within the bounding box.
- To transform the control points: Drag any outer corner to scale every control point

uniformly, drag the top, bottom, or side handles to squeeze or stretch the points against each other, or bring the pointer to a corner until the rotate cursor shows up, then drag to spin the control points.

- To delete the control points: Press the Backspace key.

3 Once you're done, press the Escape key to deselect the control points.

### Converting Linear, Circular, and Polygon Windows into Bezier Curves

Suppose you begin singling out a subject with one of the basic Linear, Circular, or Polygon shape windows and then realize the job needs a more involved shape; it's easy to upgrade them to a richer Bezier shape: from the Window palette Option menu, pick Convert to Bezier.

A before-and-after of a circular window turned into a Bezier curve, the result tweaked, prior to any edge softening being added After you've turned a simple shape into a Bezier window, you're free to add control points and mold the shape however you need so it hugs the subject better — exactly as you would with any curve.

### Resetting the Window Palette

The whole Window palette can be cleared via the Option menu's Reset command.

### Combining Power Windows with the Mask Control

Stacking several windows on one node is a simple route to composite keys. As windows combine, the Mask control decides whether one window adds to or subtracts from another. In the example below, both a Circular and a Curve window have been built, and each window's Mask control is on too (the default), so both masks sum together and the sunset look correction reaches both the sky and the woman's face.

The two images show the combination of the key mattes. Switching off the Mask control on the circular window subtracts that circular window from the curve.

Turning off the Mask control of the circular window At this point the woman's face is shielded from the heavy sky treatment.

The two images show the result of subtracting the circular window Because each window can be tracked and keyframed on its own, you can rapidly arrange elaborate window interactions to handle the everyday problems you run into. As an example, when tracking a window onto a moving subject that passes behind something in frame, a second window with Mask off can mask the object in front. Then, as the tracked window crosses the subtractive one, the correction drops away together with the subject. The Mask control likewise lets you build shapes more complex than a lone window allows.

Mattes and mask used together to make complex shapes On top of that, once you hit the ceiling of what the four windows can shape, you can join several nodes holding several shapes and qualifiers by way of the Key Mixer.

### Copying and Pasting Windows

When you've made a window you'd like to reuse within the current node or carry over to a different node, an individual window's shape can be copied and pasted from one Window list entry onto another. Ways to copy and paste windows:

- To copy a window: Click any active window in the Window list, then open the Window palette option menu and pick Copy Window.
- To duplicate a window: Once you've copied a window, build another window matching the type you copied, then open the Window palette option menu and pick Paste Window.
- To paste a window to another node: Double-click or otherwise pick a different node, open the Window palette, choose the same window type you copied within the Window list, then open the Window palette option menu and pick Paste Window.
- To paste a window to the same node: Click any active window in the Window list, open the Window palette option menu and pick Copy Window, then click Paste Append Window in the Window Option menu.

### Saving Window Presets

When there's a certain window shape or window combination you reach for often, you can store one or more windows as a preset and recall it any time. For instance, on a documentary where you wind up brightening a lot of faces, you might build preset face ovals for close-up, medium, and wide shots, so you're not customizing a stock circular window on every new shot. Groups of windows can also be saved together as one preset, letting you reuse complicated multi-window shapes. Window presets live in a cluster of Presets controls within the option menu at the upper right of the Window palette.

Controls for saving, applying, and deleting window presets

Ways to work with Power Window presets:

- To save a window preset: After building one or more windows you'd like to keep, click the Save as New Preset option within the Window palette’s option menu. Enter a name in the dialog that appears, and click OK. From then on that preset shows up in the Preset section of the option menu.
- To recall a window preset: Open the Window palette’s option menu, then pick a preset off the list. A loaded window preset replaces whatever windows had been arranged in that node.
- To update an already saved preset: Bring back a preset, edit its window(s), then open the Window palette’s option menu. Choose Update Preset, then choose the preset name. The selected preset is then overwritten with your revised window layout.
- To delete a window preset: Open the Window palette’s option menu, pick Delete Preset, then pick a preset off the list. Confirm you've picked the right preset name; no warning appears beforehand, and the deletion can't be undone afterward.

Once recalled, windows spawned by presets can be edited and tracked just like any other window.
