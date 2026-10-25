# Underlay and fuses

Version: DaVinci Resolve 20.3 Reference Manual. Context: Underlay, Fuses.
[Chapter index](INDEX.md) / [Previous section](underlay-flow-organizational-nodes.md) / [Underlay UND](sticky-note-and-underlay.md)
<a id="source-a-fuse-node"></a> <a id="source-an-example-comment-in-a-router-node"></a> <a id="source-fuses"></a> <a id="source-fuses-1"></a> <a id="source-fuses-fus"></a> <a id="source-fuses-introduction"></a> <a id="source-installing-fuses"></a> <a id="source-working-with-fuses-in-a-composition"></a>

### An example comment in a Router node

## Fuses

### Fuses

This chapter presents Fuses — scriptable plugins you can run inside Fusion.

### Fuses [Fus]

### A Fuse node

### Fuses Introduction

A Fuse is a plugin. What sets a Fuse apart from an Open FX plugin is that you build a Fuse from a Lua script. You can edit Fuses right inside Fusion or DaVinci Resolve, and your edits compile on the spot. Because they rely on a Lua script, even people who aren't programmers find it straightforward to prototype and build custom nodes. You can drop a new Fuse into a composition, edit it, and reload it without ever closing the composition you're in. Fuses also work as modifiers to drive parameters, curves, and text in a hurry. ViewShader Fuses are able to tap the GPU to run faster. All of this makes Fuses far handier than an Open FX plugin built on Fusion's OFX SDK. That flexibility, though, isn't free. A Fuse compiles on the spot, so it can run markedly slower than the same node produced with the Open FX SDK. To illustrate, a Fuse might build a mask out of the blown-out regions of an image, or set up starting particle positions from the XYZ position kept inside a text file. To obtain the SDK (Software Developer Kit) documentation, get in touch with Blackmagic Design.

### Installing Fuses

Fuses live in the Fusion:\Fuses path map. Out of the box, that folder sits at Users/ User_Name/Library Application Support/Blackmagic Design/Fusion (or DaVinci Resolve)/Fuses under macOS, or at C:\Users\User_Name\AppData\Roaming\Blackmagic Design\Fusion (or DaVinci Resolve)\ Fuses under Windows. A file has to carry the extension .fuse, otherwise Fusion passes over it.

### Working with Fuses in a Composition

You can set a Fuse up to show under whichever category you like in the Effects Library. After installation, you place one into a composition the same way you would any built-in or third-party plugin node. But because a Fuse is nothing more than a text document, you can edit it by clicking the Edit button that shows at the top of the Inspector while the Fuse node is selected. That action opens the Fuse in whatever default script editor you've named in the Global Preferences/Scripting panel. NOTE: Edits you make to one Fuse's script won't right away carry over to other copies of that same Fuse node already placed in a composition. To push the revised Fuse script onto every matching Fuse in the composition, either shut and reopen the composition or hit the Reload button inside each Fuse's Inspector. Opening a composition that holds a Fuse node loads whatever version of the Fuse script was most recently saved. The simplest way to be certain a composition runs the latest Fuse is to close it and open it again.
