# Pkill inputs

Version: DaVinci Resolve 20.3 Reference Manual. Context: Pkill.
[Chapter index](INDEX.md) / [Previous section](pimage-emitter-and-pkill.md) / [Next section](pkill-and-pmerge-and-ppoint-force-and-prender.md) / [pKill pKI](pimage-emitter-and-pkill.md)
<a id="source-inputs-5"></a> <a id="source-particle-nodes-part-3"></a>

### Inputs


Out of the box, the pKill node carries one orange input. As with the bulk of particle nodes, that orange input will take nothing but other particle nodes. Switch the Region menu over in the Region tab to either Bitmap or Mesh and a green bitmap or mesh input shows up on the node. Input: Output from other particle nodes flows into the orange input. Region: Whether you point the Region menu at Bitmap or Mesh decides whether the green or magenta region input receives a 2D image or a 3D mesh. Which input color you see depends on whichever option you choose first from the menu. Where particles get killed is set by the 3D mesh or by a channel you pick from the bitmap.
