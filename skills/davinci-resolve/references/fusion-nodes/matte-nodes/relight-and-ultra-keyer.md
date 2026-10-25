# Relight and ultra keyer

Version: DaVinci Resolve 20.3 Reference Manual. Context: Relight, Ultra keyer.
[Chapter index](INDEX.md) / [Previous section](primatte-and-relight.md) / [Next section](ultra-keyer-inputs.md) / [Continue Ultra Keyer UKY / Inputs](ultra-keyer-inputs.md) / [Relight RLT](primatte-and-relight.md)
<a id="source-external-map"></a> <a id="source-the-ultra-keyer-node"></a> <a id="source-ultra-keyer-node-introduction"></a> <a id="source-ultra-keyer-uky"></a>

### External Map

- Rescale Oversaturated: Different software scales the Surface Map differently. One widespread format resembles the Relight plugin’s own internal maps but with the colors heavily saturated, sometimes turning dark or black in places. Should your imported surface map look like this, tick this box to re-interpret it.
- Reinterpret Left/Right: Tick this box to flip the orientation of your external surface map when its surfaces read as concave rather than convex.
- Reinterpret Up/Down: Tick this box to flip the orientation of your external surface map when its surfaces look lit from beneath even though the light sits above them.

### Ultra Keyer [UKY]

### The Ultra Keyer node

### Ultra Keyer Node Introduction

As with the newer Delta Keyer, the Ultra Keyer node packs two keyers inside it: a pre-matte keyer that works as a garbage matte creator and a color difference keyer that pulls out fine detail and transparency. As a rule, you’d open with the Delta Keyer as your first pick. Should that fall short, give Primatte a go if you’re on Fusion Studio. The Ultra Keyer makes a solid third option.
