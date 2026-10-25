# Photo editing example and original camera phone image

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Previous section](deliver-page-in-photo-album-mode-and-render-settings.md)
<a id="source-global-reduced-resolution-control"></a> <a id="source-gpu-accelerated-batch-exports-and-conversions"></a> <a id="source-keyboard-shortcut"></a> <a id="source-keyboard-shortcuts"></a> <a id="source-native-raw-support-for-major-camera-formats"></a> <a id="source-photo-editing-example"></a> <a id="source-photo-multiuser-collaboration-and-blackmagic-cloud-syncing"></a> <a id="source-photos-support-for-davinci-resolves-native-ai-toolset"></a> <a id="source-support-for-davinci-color-control-toolset-and-grading-panels"></a> <a id="source-the-original-camera-phone-image"></a>

### Photo Editing Example

Pairing a still image editor with the broad film-and-video editing toolkit inside DaVinci Resolve opens the door to an entirely fresh assortment of artistic and down-to-earth photo effects. Say we grab an ordinary phone camera snapshot and aim to pass it off as 35mm motion picture film footage instead. Our first move is to reach for the Photo Inspector and dial in the usual exposure and color balance corrections on the image.

### The original camera phone image

In this phone camera shot, the statues that form the subject barely stand out from what’s behind them. Because a minuscule phone camera lens captured it, the whole scene — backdrop included — stays crisply in focus, and that crispness tends to merge everything and bury the statue subject. The remedy is to drop DaVinci Resolve’s new CineFocus effect onto the image within the album, spinning up a fresh virtual lens to look at the picture through. The lens we build sports a wider aperture, more shallow depth of field behavior, and prettier bokeh. As a first step CineFocus studies the photo and builds a fresh Depth Map charting how far away things seem within the 2D image.

The CineFocus Depth Map working out which regions of the picture sit in the foreground (shown brighter) and which sit in the backgroud. From there, the Focus mode lets us pin down precisely the aperture and depth of field we’re after, singling out the foreground statues while shoving the whole backdrop out of focus.

With the CineFocus Focus mode you dial in a fresh focus distance and depth of field (color images) against the out-of-focus regions (white). After that, the precise lens parameters are ours to fine-tune to whatever degree we please — anything from a plain virtual lens up to an 11 bladed, anamorphic lens carrying a touch of chromatic aberration and a faintly off-center lens curvature. For this walkthrough, though, we’ll simply leave the lens parameters at their default.

In the CineFocus image, see how the backdrop now sits convincingly blurred behind the statues. That blur deepens by degrees as distance grows, which reads as more lifelike than just masking off a region and blurring it. With the picture now looking as though a far more cinematic lens captured it, we’ll round out the effect by making it seem shot on 35mm motion picture film rather than a tiny CMOS sensor. For that, we drop the Film Look Creator effect onto the image inside the Photo Album as well. Two effects are now operating on the one image side by side. The Film Look Creator is yet another deep effect, opening up film parameters such as halation, grain, bloom, vignetting, and so on. For this run-through, however, we’ll merely lay on the Default 35mm film preset to bring a film-style color profile and a grain pattern of the right size.

The completed image, once the Film Look Creator has been applied

In the end result, the statues stand out plainly from their backdrop and a pleasing filmic character settles across the whole frame.

### Keyboard Shortcuts

As with every other page in DaVinci Resolve, the Photo Page carries its own collection of keyboard shortcuts that speed up your work.

Function Image Capture requires either the Capture Panel or Capture Live View to be running Star Rating functions across the Photo Album as well as the Media Pool Tag Clip Rotate and Flip Reset and Clear depend on the Inspector holding focus

### Keyboard Shortcut

C The keys Numbers 1-5 set a star rating, and 0 wipes every star away S = Good Take X = Rejected Take Hit S or X a second time to strip the tag off. For rotation and flipping, the bindings are Rotate Left: Command - [ and Rotate Right: Command - ] alongside Flip Horizontal: Shift - [ plus Flip Vertical: Shift - ]. The resetting shortcuts are Reset Photo: Command-R together with Remove All Photo Effects: Shift-R and Remove and Reset All: Command-Shift-R

### Native RAW Support for Major Camera Formats

At this beta stage, the RAW camera formats DaVinci Resolve handles are:

- Canon CR3
- Fujifilm RAF
- Apple ProRAW
- Nikon NEF
- Sony ARW

### Photo Multiuser Collaboration and Blackmagic Cloud Syncing

The Photo page is equally able to tap into the wide-ranging Multiuser collaboration and Blackmagic Cloud tooling in DaVinci Resolve. As an instance, running Capture Live View inside a collaboration project hands a second user a remote window onto the video feed from somewhere else. Photos can likewise be synced and kept in a Blackmagic Cloud Folder, opening your photo edits to collaborators across the globe and letting them make changes together.

### Support for DaVinci Color Control Toolset and Grading Panels

DaVinci Resolve color control panels work with the Photo Page, giving you purpose-built hands-on control over the image editing settings you use most. Beyond that, Photo Albums open straight inside the Color Page, putting DaVinci Resolve’s top-tier color grading toolset within reach.

### Photos Support for DaVinci Resolve’s Native AI Toolset

A number of DaVinci Resolve’s AI tools — IntelliSearch and Motion Deblur among them — work on pictures within the Photo page.

### GPU Accelerated Batch Exports and Conversions

Whether they come from Quick Export or the Deliver Page, photo exports get GPU acceleration.

### Global Reduced Resolution Control

Photo works at the native resolution of your shots, and certain cameras’ photo formats run staggeringly high in both megapixels and resolution. Because of that, processing at native size can occasionally bog the computer down to an unworkable degree. To keep things responsive, the Photo page drops to a reduced preview resolution in the viewer. You govern this behavior under Playback > Photo Album Preview Resolution, where the choices are:

- Auto (default): Takes any photo above 4k in resolution and scales it down to 4k

for the preview.

- Full: Compels Photo to render the image preview at full-sized resolution, no matter the

hit to performance.

- Half: Halves the photo’s resolution for the image preview.
- Quarter: Cuts the photo’s resolution down to a quarter for the image preview.

NOTE: This control affects only how the working image previews; you can count on DaVinci Resolve drawing on the original full-sized image when it renders the final output on export.
