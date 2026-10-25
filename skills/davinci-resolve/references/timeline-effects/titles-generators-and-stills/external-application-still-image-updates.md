# Stills and viewer updates to still images by other applications

Version: DaVinci Resolve 20.3 Reference Manual. Context: Titles generators and stills.
[Chapter index](INDEX.md) / [Previous section](fusion-generators.md)
<a id="source-photoshop-file-support"></a> <a id="source-the-results-of-splitting-a-psd-file"></a> <a id="source-using-stills"></a> <a id="source-viewer-updates-to-still-images-by-other-applications"></a>

### Using Stills

Still images can be brought into the Media Pool and cut into the Timeline as clips whose durations you set yourself. Imported stills default to 10 seconds, yet you can stretch a still image's Out point all the way to 17 hours and 40 minutes, which should be plenty for nearly any project you have in mind, unless of course you happen to be Andy Warhol. In the same vein, DaVinci Resolve can pull in still image clips that XML or AAF project files point to, provided they sit in a supported format. The still formats DaVinci Resolve works with are:

File Format .tif .png .jpg .dpx .exr .dng .psd .tga .heif .NEF .CR2

Alpha Channel Support (by format, in order): Yes Yes No No Yes No No Yes No No No

After a still image clip is edited into the Timeline, it carries the very same Composite, Transform, Cropping, Retime, and Scaling attributes that any other clip has.

### Viewer Updates to Still Images by other Applications

When a still image is open in a Viewer inside DaVinci Resolve, you are now able to edit that exact image in a separate image editing application, save the change, and watch the Viewer refresh on its own to show the updated version.

Editing the image inside a separate app, here sketching a red circle within Pixelmator Pro, and then saving

Once the still image is saved in that separate app, DaVinci Resolve refreshes it on its own

### Photoshop File Support

At first a Photoshop (.psd) file shows up as one clip presenting only the bitmapped layers across the Edit page and Color page of DaVinci Resolve. That said, while you are on the Edit page, you can right-click an Adobe Photoshop Document (.psd) sitting in a timeline and pick Split PSD Layers in Place to break out each of the file's layers onto its own track. However many layers the file holds is how many new tracks you end up with.

Right-click Photoshop PSD layers and pick Split PSD Layers in Place to break them out onto separate tracks

### The results of splitting a PSD file

Because DaVinci Resolve interprets and divides rasterized flattened layers, you have to do a bit of prep on the source PSD asset ahead of importing it. Flattening layers in Photoshop to produce flattened layers is usually done by hand. The goal is to keep the image structure simple, bake in Photoshop-specific effects, and rasterize fonts so the file plays nicely with DaVinci Resolve. Here is how the process breaks down: Rasterize transparency and effects When your layers or fonts carry effects such as shadows or gradients, merging them may occasionally shift how they look. It is worth rasterizing first. To do that, pick one or more layers, right-click, and choose Rasterize Layer Style. Doing the same with text layers is advised too. Merge and flatten similar layers Group related layers next to each other and pick the ones you intend to merge. Right-click the chosen layers and choose Merge Layers (Cmd/Control+E) to fuse them into a single ‘flat’ layer. Where the Photoshop document is more involved, you might reach for the option: File > Scripts > Flatten All Layer Effects. Name layers Give the layers names that reflect the image, effect, or element beneath them. Labeling the flattened layers now lets DaVinci Resolve carry those names into the split clips.
