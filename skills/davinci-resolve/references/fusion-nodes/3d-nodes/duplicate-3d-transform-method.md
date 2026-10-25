# Duplicate 3D transform method

Version: DaVinci Resolve 20.3 Reference Manual. Context: Duplicate 3D.
[Chapter index](INDEX.md) / [Previous section](duplicate-3d-a-cube-3d-is-duplicated.md) / [Next section](duplicate-3d-and-extrude-3d.md) / [Duplicate 3D 3Dp](custom-vertex-3d-and-displace-3d-and-duplicate-3d.md)
<a id="source-3d-nodes-part-3"></a> <a id="source-transform-method"></a>

### Transform Method


- Linear: With this option, transforms get multiplied by the copy's number, and the cumulative scale, rotation, and translation are each applied one after another, independent of the other copies.
- Accumulated: With this option, every object copy begins where the previous object ended and is transformed onward from that point. That result is then transformed again to produce the next copy.

Transform Order This menu lets you choose the sequence in which the transforms get calculated. Its default is ScaleRotation-Transform (SRT). Different orders yield different placements of your final objects. Translation The X, Y, and Z Offset sliders define the offset position given to each copy. An X offset of 1 shifts each copy 1 unit along the X-axis away from the previous copy. Rotation The buttons running across the top of this rotation control group set the sequence in which rotations get applied to the geometry. A rotation order of XYZ would rotate first on the X-axis, next on the Y-axis, then on the Z-axis. The three Rotation sliders define how much rotation each copy receives.

Pivot The pivot controls fix where the pivot point sits when each copy is rotated. Scale

- Lock: While the Lock XYZ checkbox is on, any change to the duplicate scale carries across all three axes at once. Switching this checkbox off swaps the Scale slider for separate sliders covering the X, Y, and Z scales.
- Scale: The Scale controls tell Duplicate the amount of scaling to give each copy.
