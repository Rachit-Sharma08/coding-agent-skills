# Converting layer mixers to parallel mixers overview

Version: DaVinci Resolve 20.3 Reference Manual. Context: Grading overview.
[Chapter index](INDEX.md) / [Previous section](serial-parallel-and-layer-node-structures.md)
<a id="source-converting-layer-mixers-to-parallel-mixers"></a>

### Converting Layer Mixers to Parallel Mixers

Turning a Layer Mixer back into a Parallel Mixer is simple if you realize you'd rather blend your overlapping corrections evenly instead of stacking them by priority. Just remember that doing so forfeits your access to Composite modes. To turn a Layer Mixer node into a Parallel Mixer node:

- Right-click a Parallel Mixer node and choose Morph Into Parallel Node.
