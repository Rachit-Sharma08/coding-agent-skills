# Sstar basic node setup

Version: DaVinci Resolve 20.3 Reference Manual. Context: Sstar.
[Chapter index](INDEX.md) / [Previous section](srectangle-and-srender-and-sstar.md) / [sStar](srectangle-and-srender-and-sstar.md) / [Next section](sstar-and-stext-and-stransform.md)
<a id="source-basic-node-setup-5"></a> <a id="source-external-inputs-3"></a> <a id="source-shape-nodes-part-3"></a>

### External Inputs

This node generates shapes and does not have any inputs.

### Basic Node Setup

Being a shape generator, the sStar node produces a shape and so carries no inputs. The sStar's output can feed a sRender for viewing and further compositing, or—more commonly—hook into another shape node such as sGrid or sDuplicate.


Inspector view of an sStar node wired into an sDuplicate node, with the result shown through an sRender node
