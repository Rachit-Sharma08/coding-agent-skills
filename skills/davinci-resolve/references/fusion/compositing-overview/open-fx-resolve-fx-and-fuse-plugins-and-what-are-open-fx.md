# Open FX resolve FX and fuse plugins and what are open FX

Version: DaVinci Resolve 20.3 Reference Manual. Context: Compositing overview.
[Chapter index](INDEX.md) / [Previous section](planar-tracking-and-introduction-to-tracking.md)
<a id="source-applying-open-fx-and-resolve-fx-plugins"></a> <a id="source-davinci-resolve-ofx-renderer-for-fusion-studio"></a> <a id="source-introduction-to-fuse-plugins"></a> <a id="source-using-open-fx-resolve-fx-and-fuse-plugins"></a> <a id="source-using-open-fx-resolve-fx-and-fuse-plugins-1"></a> <a id="source-what-are-open-fx"></a> <a id="source-what-are-resolve-fx"></a>

## Using Open FX, Resolve FX, and Fuse Plugins

### Using Open FX, Resolve FX, and Fuse Plugins

You can stretch what Fusion does through several flavors of plugin. Every composition across Fusion Studio and the Fusion page of DaVinci Resolve accepts third-party Open FX plugins. On top of that, the Fusion page of DaVinci Resolve opens up the whole set of Resolve FX bundled with DaVinci Resolve. Finally, you can roll your own plugins without any computer development environment by scripting Fusion's built-in Fuse plugins.

### What Are Open FX?

Fusion can run compatible Open FX (OFX) plugins that sit installed on your machine. Open FX is an open standard covering visual effects plugins. Plugins authored to that standard run on both DaVinci Resolve and Fusion Studio, plus any other application backing the standard. You can buy and download OFX plugins from outside vendors like BorisFX, Red Giant, and RE:Vision Effects. Every OFX shows up under the Open FX category of the Effects Library, sitting beside all the other effects Fusion makes available.

### What Are Resolve FX?

The Fusion page in DaVinci Resolve can also reach Resolve FX. Resolve FX are filter effects living inside DaVinci Resolve. While the bulk of Resolve FX behave identically across every DaVinci Resolve page, a few belong solely to the Color page and lean on the Color page tracker for their full feature set. Each Resolve FX turns up in the Fusion page Effects Library under the Open FX category, right alongside third-party OFX plugins. Resolve FX aren't offered in Fusion Studio. To learn more about Resolve FX, turn to Chapter 154, “Resolve FX.”

### Applying Open FX and Resolve FX Plugins

You drop Resolve FX and OFX plugins into the Node Editor exactly the way you'd add native Fusion nodes. They're handy for whipping up quick, eye-catching looks and effects on the Color page, or inventive transitions and effects on your clips over on the Edit page. Resolve FX ship alongside DaVinci Resolve, Once you've installed a batch of OFX plugins, you reach them or the Resolve FX plugins inside Fusion by opening the Open FX category in the Effects Library. Getting a plugin into the Node Editor takes one of two routes: click its Open FX or Resolve FX name listed in the Effects Library, or drag the plugin and drop it over a connection line so that it slots into the node tree. When the plugin carries editable settings, you tune them in the Inspector.

### DaVinci Resolve OFX Renderer for Fusion Studio

The OFX DaVinci Resolve Renderer plugin is available to you within Fusion Studio. This plugin gives Fusion Studio the ability to open and apply DaVinci Resolve's color changes through exported DRX stills. In effect, it converts a DaVinci Resolve Studio install into a single huge OFX plugin. That proves handy when round tripping between DaVinci Resolve Studio and Fusion Studio, in cases where you want to hang onto the exact look built in DaVinci Resolve. A DRX still you export carries far richer grade information than a plain LUT. DRX files can hold things like every native color and sizing palette plus other items you tucked into a Gallery still. That way, whatever grade the colorist crafted carries across with full precision into the VFX software. At the time of writing, these attributes WILL carry over through the DaVinci Resolve OFX Renderer Plugin:

- All native color palettes (Primaries, HDR, Curves, etc.).
- All native sizing palettes (Input, Output, Node, etc.).
- Most Resolve FX.
- Most third-party Open FX.

At the time of writing, these attributes WILL NOT carry over through the DaVinci Resolve OFX Renderer Plugin:

- Resolve FX and Open FX that are temporal based.
- Magic Mask.

To set up the DaVinci Resolve OFX Renderer Plugin: 1 While installing DaVinci Resolve Studio, choose Custom Install and then tick the plugin option inside the program installer.

Choosing Custom Install and ticking DaVinci Resolve Open FX Renderer to get the plugin installed 2 Build your grade for a clip on the Color page, then stash a still in the Gallery. Out of the Gallery, export a .DRX file.

3 Over in Fusion Studio, drop the DaVinci Resolve Renderer plugin wherever it fits your composition.

Slotting the DaVinci Resolve Renderer OFX in among a Fusion Studio node tree 4 Within the DaVinci Resolve Renderer Inspector in Fusion Studio, pick the .DRX file you exported using the file browser.

Select the .DRX file you exported from DaVinci Resolve in the plugin

### Introduction to Fuse Plugins

Fuses are plugins built for Fusion through the Lua built-in scripting language. Because they're script-driven, Fuses compile on-the-fly inside Fusion with no computer programming environment required. Even where a Fuse lags behind a matching Open FX plugin built on Fusion's C++ SDK, it still taps into the nodes Fusion already provides plus GPU acceleration. Installing a Fuse goes like this: 1 Append the .fuse extension to the document name. 2 Under DaVinci Resolve, drop it into whichever of these spots fits your platform. On macOS, the path is `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ DaVinci Resolve/Fusion/Fuses` while a Windows machine uses `C:\Users\username\AppData\Roaming\Blackmagic Design\DaVinci Resolve\ Support\Fusion\Fuses` and the Linux equivalent is `home/username/.local/share/DaVinciResolve/Fusion/Fuses` Under Fusion Studio, the choices follow the same per-OS pattern. On macOS, head to `Macintosh HD/Users/username/Library/Application Support/Blackmagic Design/ Fusion/Fuses/` whereas under Windows it sits at `C:\Users\username\AppData\Roaming\Blackmagic Design\Fusion\Fuses` and on a Linux box it lives at `home/username/.fusion/BlackmagicDesign/Fusion/Fuses` To open and edit Fuses, select the Fuse node in the Node Editor and press the Edit button up top in the Inspector. The Fuse loads inside the text editor named in the Global Preferences/Scripting panel. TIP: Edits you make to a Fuse in a text editor don't instantly ripple out to the other copies of that Fuse across the composition. Reopening a composition refreshes every Fuse in it against the version currently saved. As an alternative, press the Reload button in the Inspector to refresh the chosen node without shutting and reopening the composition.
