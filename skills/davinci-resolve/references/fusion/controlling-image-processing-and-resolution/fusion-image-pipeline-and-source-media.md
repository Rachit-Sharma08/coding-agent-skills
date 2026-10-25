# Fusions place in the DaVinci resolve image processing pipeline and source media into the Fusion page

Version: DaVinci Resolve 20.3 Reference Manual. Context: Controlling image processing and resolution.
[Chapter index](INDEX.md) / [Next section](clip-resolution-changes-and-mixed-resolution-compositing.md)
<a id="source-clip-attributes"></a> <a id="source-color-effects"></a> <a id="source-color-effects-1"></a> <a id="source-controlling-image-processing-and-resolution"></a> <a id="source-controlling-image-processing-and-resolution-1"></a> <a id="source-edit-page-plugins"></a> <a id="source-editcut-page-inspector-adjustments"></a> <a id="source-editcut-page-inspector-adjustments-1"></a> <a id="source-editcut-plug-ins-resolve-fx"></a> <a id="source-forcing-effects-into-the-fusion-page"></a> <a id="source-fusion-effects"></a> <a id="source-fusion-effects-1"></a> <a id="source-fusion-page-uhd"></a> <a id="source-fusion-timeline-sizing-for-the-fusion-page"></a> <a id="source-fusions-place-in-the-davinci-resolve-image-processing-pipeline"></a> <a id="source-hd-res"></a> <a id="source-hd-timeline"></a> <a id="source-managing-resolution-in-fusion"></a> <a id="source-output-from-the-fusion-page-to-the-color-page"></a> <a id="source-raw-debayering"></a> <a id="source-resize-scale-crop-letterbox"></a> <a id="source-source-media"></a> <a id="source-source-media-into-the-fusion-page"></a> <a id="source-uhd-source-media"></a> <a id="source-what-viewers-show-in-different-davinci-resolve-pages"></a>

### Controlling Image Processing and Resolution

The image-processing pipeline as a whole is the subject of this chapter, which takes up color bit-depth alongside the means of steering output resolution within a resolution‑independent setting.

### Fusion’s Place in the DaVinci Resolve Image-Processing Pipeline

Inside one unified setting such as DaVinci Resolve, grasping the sequence in which the pages operate matters a great deal. DaVinci Resolve reveals part of that sequence through how the page buttons line up along the bottom of the screen — the Media, Cut, and Edit page opening the chain, with the Color, Fairlight, and Deliver page closing it. That ordering tells only part of the tale, though, particularly where the Fusion page is concerned. Below, the sections lay out exactly where the Fusion page sits within DaVinci Resolve's image-processing chain.

### Source Media into the Fusion Page

For plain single clips arriving from the Edit or Cut page, the source media is stood in for by the Fusion page's MediaIn node, shaped by whatever the Clip Attributes window specifies. You may pick the clip over on the Edit or Cut page Timeline, yet within the Fusion page it's reached through the Media Pool. TIP: Decoding or debayering of RAW files runs ahead of everything else, so any RAW tweaks render accurately on the Fusion page. What this gives you is the whole source clip on the Fusion page, though the render range gets set to the clip's Timeline duration. The source clip's full resolution is likewise at your disposal, even should the Timeline be configured for something lower. None of the Edit or Cut page Inspector tweaks travel into the Fusion page, however, save for the Lens Correction adjustment. Make Zoom, Position, Crop, or Stabilization changes on the Edit or Cut page and they stay invisible in the Fusion page. The same holds for any Resolve FX or Open FX third-party plugins: apply such items to a clip on the Edit or Cut page, then open the Fusion page, and you won't watch them take hold. Every Edit and Cut page timeline effect and Inspector tweak, the lone exception being the Lens Correction adjustment, is calculated after the Fusion page but ahead of the Color page. Open the Color page and you'll find the Edit and Cut page transforms and plugins laid onto that clip, in effect as a step preceding the grading tweaks and effects you set in the Color page Node Editor. Bearing that in mind, the way effects get processed across the various DaVinci Resolve pages runs like this:

### Source Media

### RAW Debayering

### Clip Attributes

### Fusion Effects

### Edit/Cut Page Inspector Adjustments

### Edit/Cut Plug-ins Resolve FX

### Color Effects

TIP: Retiming you've placed on a clip in the Edit page Timeline likewise fails to follow it into the Fusion page.

### Forcing Effects into the Fusion Page

You can in fact push a clip that carries Edit page Inspector adjustments, alongside plugins, retiming, and grades from the Color page, on into the Fusion page — the trick is converting that clip into a compound clip or a Fusion clip. With Edit page effects and Color page grading baked into compound or Fusion clips, the MediaIn nodes that stand for compound clips feed the affected clip onward into the Fusion page. Pulling a compound clip or Fusion clip into the Fusion page does, however, reset the source clip's resolution so it lines up with the Timeline resolution. Further detail lives in this chapter's “Sizing Between DaVinci Resolve Pages” section.

### Output from the Fusion Page to the Color Page

Whatever composition emerges from the Fusion page's MediaOut node travels onward through the Color page's source input — the one exception being that, if you've attached plugins to that clip on the Edit or Cut page, the pass from the Fusion page to the Color page proceeds like this:

### Fusion Effects

### Edit/Cut Page Inspector Adjustments

### Edit Page Plugins

### Color Effects

### What Viewers Show in Different DaVinci Resolve Pages

Because compositing artists, editors, and colorists each need something different, the viewers present the clip in differing states. The Edit page source viewer: It shows the source media at all times, the one exception being when you open a compound clip stored in the Media Pool. Turn on Resolve Color Management and the Edit page source viewer then renders the source media using the Timeline's gamma and color space. The Edit page Timeline viewer: Here clips appear with every Edit page effect, Color page grade, and Fusion page effect in place, letting editors view the program amid the full set of effects and grading. The Fusion page viewer: This presents Media Pool source clips at the Timeline color space and gamma, Resolve Color Management adjustments included, yet without any Edit page Inspector adjustments or Resolve FX effects and without Color page grades. The Color page viewer: This shows clips carrying every Edit page effect, Color page grade, and Fusion page effect.

### Managing Resolution In Fusion

A comp in Fusion carries no formal resolution of its own.

- On the Fusion page, the Timeline resolution dictates the default resolution of Fusion-generated images such as the Background tool, Fast Noise, Text+, and the like.
- Within Fusion Studio, generator resolution is configured under Preferences > Frame Format, where a standard resolution can be chosen from the drop-down menu or the Width and Height entered by hand.
- A Fusion page composition's resolution is, to begin with, governed by the source resolution of the input image.

Say your Timeline runs at HD resolution (1920 x 1080) while a clip sitting on that timeline has a source resolution of UHD (3840 x 2160); opening the clip in the Fusion page pushes the composition's resolution up to UHD (3840 x 2160). From then on, every Fusion-generated image in the composition comes out at UHD resolution.

### UHD Source Media

### HD Timeline

### Fusion timeline sizing for the Fusion page

### Fusion Page UHD

### Resize Scale Crop Letterbox

### HD res

TIP: Whatever the Fusion page produces returns into the Edit page Timeline according to DaVinci Resolve's Image Sizing setting. Out of the box, DaVinci Resolve relies on an image sizing setting named Scale to Fit. The result is that, even when the Fusion page turns out a 4K composition, it conforms to 1920 x 1080 should that be the project's or a given Timeline's setting. Altering the image sizing setting in DaVinci Resolve's Project Settings changes how Fusion compositions fold into the Edit page Timeline.
