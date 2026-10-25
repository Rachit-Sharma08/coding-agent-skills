# Photoshop psd and quicktime

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md) / [Previous section](setting-up-a-composition-and-reading-clips-into-fusion-studio.md)
<a id="source-photoshop-psd"></a> <a id="source-quicktime"></a>

### Photoshop PSD

Photoshop PSD files come in by way of two approaches. You may bring in the PSD file so it shows as one single node in the Node Editor, or bring in the PSD so each layer shows as its own node in the Node Editor. When you have no need for separate control of each layer, or no blend modes went into building the PSD, importing the PSD as a single node keeps things tidier. When you do need per-layer control, or the Blend modes inside the PSD are essential, then import the file so every layer turns into a node in the Node Editor. Below, each approach is laid out for the Fusion page and for Fusion Studio.

Using the Media Pool in DaVinci Resolve’s Fusion page: Whatever PSD file you add to the Media Pool in DaVinci Resolve becomes reachable from the Fusion page. Once you drag that PSD file out of the Media Pool onto the Node Editor, the image shows up as a MediaIn node. From there the Inspector’s Layer drop-down menu lets you choose which layer of the PSD file to use. Using a Loader node in Fusion Studio: This route reads in Photoshop PSD files and lets you pick which layer of the PSD file the comp uses. Fusion can pull in any single layer held in the PSD file, or the finished image with all of its layers. It does not support transformation and adjustment layers.

Within the Inspector, the Format tab presents controls particular to a Photoshop PSD file. To pull in every layer separately from a PSD file with the right blend modes, take one of these routes:

- Inside DaVinci Resolve, move to the Fusion page and choose Fusion > Import > PSD.
- In Fusion Studio, choose File > Import > PSD. Either route above builds a node tree in which a node stands for each PSD layer and one or more Merge nodes join the layers together. Those Merge nodes adopt the Apply mode found in the PSD file and get named automatically from that Apply mode setting.

Here a Photoshop PSD file’s two layers come in and wire into a Merge node whose Apply mode is set to Screen.

### QuickTime

A QuickTime file may hold several tracks. The Inspector’s Format tab lets you pick which one of those tracks to use.
