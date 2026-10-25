# Loader and saver nodes in the Fusion page and loader node parameters

Version: DaVinci Resolve 20.3 Reference Manual. Context: Getting clips into Fusion.
[Chapter index](INDEX.md) / [Previous section](mediain-timeline-clips-and-source-color-space.md) / [Next section](setting-up-a-composition-and-reading-clips-into-fusion-studio.md)
<a id="source-auto-save"></a> <a id="source-loader-node-parameters"></a> <a id="source-manual-disk-caching-using-loader-and-saver-nodes"></a> <a id="source-opening-closing-and-saving-compositions"></a> <a id="source-outputting-images-using-saver-nodes"></a> <a id="source-preparing-compositions-in-fusion-studio"></a> <a id="source-the-composition-file-format"></a> <a id="source-using-loader-and-saver-nodes-in-the-fusion-page"></a>

### Using Loader and Saver Nodes in the Fusion Page

Within the Fusion Page, the Loader and Saver nodes serve workflows built around multi-channel EXR files in particular. OpenEXR media is able to carry high-quality floating-point image data, several matte channels, and auxiliary channels output by 3D software. With the Loader node you pull OpenEXR files into a composition straight off the file system while keeping every channel stored inside that file. Saver nodes let you write all or some of a composition out to disk as EXR files, skipping past the DaVinci Resolve Deliver page. Here is how to bring a multi-channel EXR image sequence into the Fusion page: 1 Go to the Fusion page. 2 Bring up the Effects Library, pick the Tools > I/O category, and click the Loader node. 3 Within the OS navigation window that appears, choose the EXR image sequence for import, then click Open. 4 A Loader node tied to that EXR file turns up on the Fusion page, yet no clip arrives in the Media Pool.

### Loader Node Parameters

A Loader node’s image tab carries the same parameters that MediaIn nodes do, as covered earlier here. When a Loader node points at EXR files, though, the Format tab lets you turn specific auxiliary channels held in the file on or off.

Within a Loader node Inspector, the Format tab shows the Aux channels carried by EXR files.

### Outputting Images Using Saver Nodes

Straight from the Fusion page, Saver nodes write OpenEXR image sequences to disk. Because a Saver node attaches to any branch of a node tree, you can export one or several subsets of nodes within a composition. Drop as many Saver nodes as needed onto whatever branches of your composition’s node tree you want to send out, exporting several pieces of a composition. Say a given composition has one branch of nodes building an elaborate background and a second branch making a transparent foreground character: you could write the background and foreground branches to separate OpenEXR files through two Saver nodes. For that, just place a Saver node downstream of whichever nodes you wish to output, then open the Inspector and click Browse to pick a name and destination for the render.

As you name the file, you have to append the .exr file extension; Fusion then sets the output format to match. The software inserts a four-digit frame number ahead of the filename extension automatically. You may, however, dictate the frame padding by tacking on extra zeroes to signal how many digits you want. As an example, 000 stands for 001. With the Saver node configured, output one or more Saver nodes by choosing Fusion > Render All Savers.

The Inspector parameters for a Saver node.

### Manual Disk Caching Using Loader and Saver Nodes

On the Fusion page, the Loader and Saver nodes also help streamline compositions that are deeply complex and heavy on the processor. As an instance, you might use a Saver node to write out branches of a node tree that rarely need tweaking anymore to OpenEXR, then pull that result back in to stand in for the original branch and so lift your composition’s performance. Employed in this fashion, Loader and Saver nodes give you a rock-solid manual caching workflow whose media files are never purged on their own unless you delete them yourself. Provided you keep the original branch of nodes around, you can revisit and re-render these hand-cached portions of a composition whenever the need arises.

### Preparing Compositions in Fusion Studio

Coming up, the next handful of sections walk through getting a project ready and dropping clips into a composition while working in Fusion Studio. We call the Fusion project file a composition, or comp for short. Launching the Fusion Studio application spawns a fresh empty composition by default. Inside a composition you may hold single frames, image sequences, or movie files across various resolutions and bit depths. The opening moves of compositing are learning which files you can bring in, configuring a composition to accept them, and at last reading those files in.

### Opening, Closing, and Saving Compositions

The moment Fusion Studio opens, a fresh empty composition appears. Should you need them, you can also make or open several compositions together. Every extra composition opens as its own tab on the main Fusion Studio window.

Three compositions opened as tabs in Fusion Studio.

To create a second new composition:

- Choose File > New.

To open an existing composition, do one of the following:

- Choose File > Open.
- Choose File > Open Recent, then pick from the roster of comps opened lately.
- Drag a composition file out of an OS file browser onto the tabbed composition strip at the top of the Fusion Studio window.
- Double-click a composition file within the OS file browser.

Any of these approaches will close the composition you have open:

- Choose File > Close from the menu running along the top of the Fusion window.
- Click the Close X icon at the right end of the composition’s tab. Should the composition hold unsaved edits, a dialog box pops up offering to save before it closes.

TIP: Any composition holding unsaved edits shows an asterisk (\*) beside its name both in the Fusion Studio title bar and on the composition’s tab. These are the ways to save the composition you currently have open:

- Choose File > Save and supply a name when the comp has not been named yet.
- Choose File > Save As to store it under a different name.
- Choose File > Save Version to write out the open composition with a three-digit version number appended to its name. With every version you save, that number steps up on its own and the comp file lands in the same folder as the original version.

### Auto Save

At fixed intervals, auto save writes the composition out to a temporary file on its own. This guards your work against power outages, software trouble, or an accidental close. Turn it on for new compositions by choosing Fusion Studio > Preferences, then finding Global > General > Auto Save inside the Preferences dialog. The auto-save file leaves the current composition on disk untouched. It puts a same-named file in the composition’s folder but gives it the extension .autosave rather than .comp. For compositions never saved, the autosave file goes to the default folder named by the Comp: path under the Paths panel of the Global Preferences. When Fusion Studio loads a composition and an auto-save file exists, a dialog asks whether to bring in the auto-saved or the original version.

### The Composition File Format

A composition file is stored as a human-readable plain text file. Describing a composition in plain text makes it simpler to fold Fusion into organized visual effects pipelines and asset management systems. You can open and edit a composition file in any ordinary text editor. That said, never open one in a word processor like Microsoft Word or Apple Pages, since those tend to embed extra formatting data that leaves the composition unreadable to Fusion.

Importing and Exporting a Composition from DaVinci Resolve Even though compositions built on DaVinci Resolve’s Fusion page live inside the DaVinci Resolve project library as .drp project files, you are free to import and export Fusion composition files while on the Fusion page. That makes passing Fusion compositions between the two applications quite simple. Here is how to export a Fusion composition out of DaVinci Resolve: 1 Inside DaVinci Resolve, move to the Fusion page holding the composition you wish to export. 2 Choose File > Export Fusion Composition. 3 A Save dialog opens where you supply a name and place for the exported Fusion composition. The filename gets a .comp extension appended. What exports is solely the node tree built on the Fusion page. Any clips left out of the Node Editor will not show up in the Fusion Studio bins. Likewise, ResolveFX placed in the comp do not carry over from the Fusion page to Fusion Studio. DaVinci Resolve’s MediaIn nodes convert to Loader nodes automatically, and when the file path stays the same the media relinks on its own. MediaOut nodes turn into Saver nodes. You can run the trip in reverse too, writing a composition file out of Fusion Studio and bringing it into the Fusion page inside DaVinci Resolve. Here is how to import a composition from Fusion Studio onto the Fusion page within DaVinci Resolve: 1 Inside Fusion Studio, open the composition you intend to bring over to the Fusion page. 2 Inside DaVinci Resolve, move to the Fusion page that holds an empty composition. Whatever you import will entirely supplant the composition already sitting in that page’s Node Editor. 3 Choose File > Import Fusion Composition. 4 From the Open dialog, browse to the Fusion comp and click Open. That new comp loads into the Node Editor and takes the place of the one that was there. TIP: To preserve an existing comp on the Fusion page while folding in a new comp from Fusion Studio, open Fusion Studio, select every node in the Node Editor, and press Command-C to copy them. Next, open DaVinci Resolve, switch the Fusion page to the composition you want, click an empty spot in the Node Editor, and press Command-V to paste in the Fusion Studio nodes. Then wire the pasted node tree into the existing one through a Merge or Merge 3D node.
