# Perturb

Version: DaVinci Resolve 20.3 Reference Manual. Context: Perturb.
[Chapter index](INDEX.md) / [Previous section](offset-angle-distance-position-and-path.md) / [Next section](perturb-and-probe-and-publish-and-resolve-parameter-and-shake.md)
<a id="source-modifiers-part-3"></a> <a id="source-perturb"></a>

### Perturb


The Perturb modifier produces smoothly shifting random values for a chosen parameter, driven by Perlin noise. You can lean on it to introduce jitter, shake, or wobble into any animatable parameter, even one that's already animated. The outcome resembles what the Shake modifier delivers, though Perturb relies on a different, perhaps more intuitive, set of controls. Setting it apart from the other random modifiers, the Perturb modifier applies to polylines, shapes, grid meshes, and even color gradients. As an example, to layer camera shake onto an existing path, right-click the crosshair, pick Insert > Perturb, then trim the Strength down to taste. As another route, right-clicking the path's “Right-click here for shape animation” label down at the foot of the Inspector lets you put perturb on the path's polyline. That works best with a polyline holding plenty of points—say one that's been tracked or hand-drawn using the Draw Append pencil tool. A third option uses the Insert contextual menu to drop the modifier onto the Displacement control. The motion along the path then jitters to and fro without ever straying off the path.

NOTE: Perturb is only able to introduce jitter; smoothing out existing animation curves is beyond it.
