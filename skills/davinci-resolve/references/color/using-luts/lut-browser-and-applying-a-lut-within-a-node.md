# LUT browser and applying a LUT within a node

Version: DaVinci Resolve 20.3 Reference Manual. Context: Using luts.
[Chapter index](INDEX.md) / [Previous section](what-is-a-lut-and-supported-lut-formats.md)
<a id="source-applying-a-lut-within-a-node"></a> <a id="source-exporting-luts"></a> <a id="source-favorite-luts-submenu-in-node-editor"></a> <a id="source-luts-are-the-last-operation-within-a-node"></a> <a id="source-missing-luts"></a> <a id="source-the-lut-browser"></a>

### The LUT Browser

To open the LUT Browser:

- Up in the UI Toolbar running along the top of the Color page, click the LUT Browser button.

Methods of working with the LUT Browser:

- To view the LUTs within a category: In the sidebar, click a LUT category so it is selected, and the browser area fills with its LUTs.
- To flag a LUT as a favorite: Rest the mouse on a LUT and click the star badge surfacing at its upper right-hand corner, or else right-click any LUT and pick Add to Favorites. From then on, that LUT shows up under the Favorites category within the node contextual menu of the Node Editor.
- To hunt down or filter particular LUTs: Open whichever bin holds the LUT you are after, click the magnifying glass icon so the search field opens, and key in text that pins down the LUTs you are after.
- To switch LUTs between Column and Thumbnail view: At the LUT Browser's top right, click the Column or Thumbnail buttons to set how the browser area presents LUTs.
- To order LUTs in Thumbnail view: Open the Thumbnail Sort pop-up menu and select the criteria by which LUTs should sort. Available are filename, type, relative path, file path, usage, date modified. Ascending and descending sort modes are offered as well.
- To order LUTs in Column view: Click a column header so sorting follows that column. Clicking a header again and again flips between ascending and descending modes.
- To swap a LUT's thumbnail for an image drawn from a clip: Settle on the clip and frame you would like as that particular LUT's fresh thumbnail, then right-click the LUT and pick Update Thumbnail With Timeline Frame.
- To restore a LUT's thumbnail back to the standard one: Right-click the LUT and pick Reset Thumbnail, which returns it to the standard test image.
- To bring a LUT category up to date with newly installed LUTs: Pick a LUT category, then right-click somewhere inside the browser area and pick Refresh, pulling that category's contents fresh off disk.

Enabling and Disabling the LUT Viewer live preview: 1 Bring up the LUT Viewer's option menu and pick Live Preview.

For the LUT browser, the Live Preview option lets you hover a LUT to preview it against the current clip in the Viewer 2 In the Node Editor, click whichever node you want to preview applying a LUT to. What the live preview shows is how the current clip will look once the LUT you choose is laid on the currently selected node of the active grade, which shapes the result. 3 Drag the pointer over whichever LUT you want to preview. The Viewer image refreshes to reveal how that clip would appear with that LUT laid on the currently selected node.

To push a LUT out of the LUT Browser onto a particular node, take one of these routes:

- Right-click a LUT and choose Apply LUT to current node.
- Pull a LUT out of the LUT Browser and let it fall onto whichever node should receive it. Dropping a LUT onto a node that already holds one replaces the earlier LUT with the new arrival.

### Applying a LUT Within a Node

DaVinci Resolve lets you bring a LUT into a grade by hooking it onto a specific node in the Node Editor. That gives you the most command over where in your image processing pipeline the LUT lands, and it also opens the door to making image adjustments both ahead of the LUT and after the LUT, as you need. To apply a LUT within a node, do one of the following:

- Right-click whatever node you want, then inside the LUT submenu pull a LUT from any of its submenus: the 1D Input LUT, the 1D Output LUT, plus the 3D LUT, along with DCTL, and also CLF (common LUT format). Whichever LUTs sit installed on your workstation are the ones these LUT submenus enumerate.

To learn more about getting LUTs installed, consult Chapter 4, "System and User Preferences."

- Right-click whatever node you want, then grab a LUT out of the LUT > Favorites submenu.
- Lean on the LUT Browser to locate the LUT you are after, then drag it and drop it onto the

node it should apply to TIP: Holding the Option key as you scroll the submenu of LUTs inside a Corrector node's contextual menu gives you a live Viewer update showing how each LUT shapes the image. To reveal a selected node's LUT: Where a node in the Node Editor carries a LUT, right-clicking that node and choosing Reveal Selected LUT auto-opens the LUT viewer with that LUT selected.

### LUTs Are the Last Operation Within a Node

Each node in the Node Editor can run several operations, and those operations happen in a set order. Whatever LUTs you add to a node impose their transformation as the final operation within that node, once every other Color page adjustment that node applies has run. In practice, this means you can put a node's Color and Contrast controls to work trimming the image data that gets fed into a LUT applied on that same node. For instance, if a LUT's contrast adjustment clips the image's highlights too hard, you can use that node's Contrast controls to bring the image's highlights down ahead of the LUT, restoring detail to the image.

### Favorite LUTs Submenu in Node Editor

After you "star" a LUT as a favorite over in the LUT Browser, each of those favored LUTs appears in a submenu of the contextual menu that pops up when a node gets right-clicked in the Node Editor. That makes building a short roster of your go-to LUTs for assorted situations easy, ready for fast use straight in the Node Editor.

The Node Editor contextual menu's Favorite LUTs submenu hands you a short list

### Missing LUTs

Clips whose LUTs are missing show an overlay at the bottom right of the screen naming the LUT when a single LUT is missing, or flagging that multiple LUTs are missing. That allows quick previews of missing LUTs without interruption. You can view and manage multiple missing LUTs from the Missing LUTs tab in the LUT Browser, which surfaces only when one or more LUTs are missing.

### Exporting LUTs

Whenever image adjustments have to move across to other grading applications, compositing applications, or NLEs, the simplest inter-app answer is often to export a LUT. Whether your grade runs to a single node or many, this works provided they carry nothing beyond Primaries palette adjustments, Custom Curves palette adjustments, plus compatible ResolveFX plugins — namely those handling Color Space Transform, ACES Transform, and Gamut Mapping. Each node holding compatible functions is folded together mathematically and rendered down into one LUT. Bear in mind, though, that any node leaning on Qualifiers, Windows, filtering operations that are not compatible (sharpening or blurring, say), or Resolve FX or Open FX that are not compatible gets skipped wholesale — and so does every other correction operation carried out inside those nodes. To export a LUT: 1 In the Color page's Timeline, right-click a clip thumbnail, then pick an entry off the Generate LUT submenu. Generate 3D LUT (17 Point Cube): a format developed at DaVinci. Generate 3D LUT (33 Point Cube): likewise a DaVinci-developed format. Generate 3D LUT (65 Point Cube): again, a DaVinci-developed format. Generate 3D LUT (Panasonic VLUT): a LUT format tied to Panasonic VariCam cameras.

2 In the file dialog, pick where the resulting LUT file should go. Which default file path applies hinges on your operating system; storing it here keeps it on hand for DaVinci Resolve down the road. The per-platform defaults are listed here. On OS X: Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/ — that is the macOS spot. On Windows: C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT — that is the Windows spot. On Linux: /home/resolve/LUT — that is the Linux spot. Should you prefer, spin up a new folder for your custom LUTs to live in. 3 Type a name into the Save As field, then click Save. With that, a LUT file gets written. From then on, an exported LUT is usable inside DaVinci Resolve — laid directly on a clip or node, or laid across the entire project by way of the settings under the Color Management panel of the Project Settings. You could also drop the LUT onto a memory stick and pass it to someone for monitoring or previewing during an onset workflow, or to someone working in another grading application able to read this LUT format.
