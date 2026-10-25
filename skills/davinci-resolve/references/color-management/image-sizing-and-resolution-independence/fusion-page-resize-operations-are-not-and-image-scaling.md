# Fusion page resize operations are not and image scaling

Version: DaVinci Resolve 20.3 Reference Manual. Context: Image sizing and resolution independence.
[Chapter index](INDEX.md) / [Previous section](about-resolution-independence-and-timeline-resolution.md) / [Next section](clip-scaling-and-cut-edit-sizing.md)
<a id="source-center-crop-with-no-resizing"></a> <a id="source-center-crop-with-no-resizing-1"></a> <a id="source-fusion-page-resize-operations-are-not"></a> <a id="source-image-scaling"></a> <a id="source-image-sizing-and-resolution-independence-part-2"></a> <a id="source-input-scaling-project-setting"></a> <a id="source-output-image-scaling-project-settings"></a> <a id="source-resize-filter-project-setting"></a> <a id="source-scale-entire-image-to-fit"></a> <a id="source-scale-entire-image-to-fit-1"></a> <a id="source-scale-full-frame-with-crop"></a> <a id="source-scale-full-frame-with-crop-1"></a> <a id="source-stretch-frame-to-all-corners"></a> <a id="source-stretch-frame-to-all-corners-1"></a>

### Fusion Page Resize Operations Are Not

Within Fusion there are two kinds of transform effect, the Transform node and the Resize node. Which one you reach for makes a dramatic difference to resolution independence.

- The Transform node always looks back to the clip's input resolution (as set by the Clip Attributes) so as to allow resolution-independent sizing, meaning several Transform nodes can scale the image down and up over and over on the Fusion page without needlessly losing image resolution.
- The Resize node genuinely lowers image resolution as you shrink an image, or raises it (with filtering) as you enlarge. That means the Resize node breaks resolution independence, locking the image's resolution to whatever you state from that spot in your composite's node tree onward.

In most cases you'll likely want the Transform node so resolution independence relative to the source media holds, unless you specifically aim to alter and maybe reduce image resolution for a particular special effect that deliberately degrades the image. If, for example, you want a clip forced to a standard definition resolution to mimic a low-resolution archival clip, the Resize node will do it. Enlarge the result with a Transform node afterward and it performs a filtered enlargement that looks like a genuine SD clip blown up. Transforms from the Fusion Page to the Edit Page So long as you avoid the Fusion page, every transform operation you apply on the Cut, Edit, and Color pages stays resolution independent, looking to the source media's original resolution. Say you shrink an image to 20% on the Edit page (using Edit sizing controls) and then bring it back to 100% on the Color page (using Input sizing controls); you finish with an image that retains every bit of the original media's resolution and sharpness, since the final resolution is drawn from the original source media.

The moment you use the Fusion page to touch a clip, though, whether adding a tiny effect or constructing an elaborate composition, the source-media resolution-independent link held by the Edit and Color pages is severed, and the resolution emerging from your Fusion composition turns into the clip's new effective resolution as shown on the Timeline. So if you shrink an image to 20% on the Fusion page (with a Transform node) and then enlarge it on the Color page by 150%, you end up with an image less sharp than the original, because the downconverted Fusion-page image is effectively that clip's new source resolution.

### Image Scaling

DaVinci Resolve carries a dedicated mechanism for handling automatically the sizing of clips whose resolutions don't match the timeline resolution, and it sits apart from the Zoom transform controls available for making creative clip adjustments. This is called Image Scaling, and you can customize it across a few different areas.

### Resize Filter Project Setting

The Resize Filter setting lets you pick the filter method used to interpolate image pixels as clips are resized:

- Smoother: Can give a more agreeable result on projects whose clips have to be scaled down to standard definition, since this filter shows fewer sharp edges at SD resolutions.
- Bicubic: Though the sharper and smoother options run slightly higher in quality, bicubic remains a remarkably good resizing filter and demands less of the processor than either of them.
- Blinear: A lower-quality, lighter-on-the-processor setting. Handy for previewing your work on an underpowered computer before you render, at which point you can shift to one of the higher-quality options.
- Sharper: Generally delivers the best quality across most projects, drawing on an optical-quality processing technique found only in DaVinci Resolve.
- Custom: With this setting you take charge of the precise algorithm every resizing operation uses. The custom Resize Filter options on offer include Bessel and Box; Catmul-Rom, Cubic, and Gaussian; Lanczos plus Mitchell; and Nearest Neighbor, Quadratic, and Sinc. Practically speaking, telling these methods apart can be fairly subjective. Still, when you must match a particular resizing method from another application, here's where you do it. For day-to-day work, the ordinary resizing filters in DaVinci Resolve ought to suffice.
- Override Input scaling: Tick this box to pick an Input Sizing preset for the project to use.
- Override Output scaling: Tick this box to pick an Output Sizing preset for the project to use.
- Anti-alias edges: A second batch of settings lets you decide how edge anti-aliasing is handled for source blanking.

Auto: Brings in anti-aliasing whenever any Sizing control transforms the image; otherwise anti-aliasing stays off. On: Keeps anti-aliasing on the whole time. Off: Turns anti-aliasing off. Switching anti-aliasing off may be needed if you spot black blurring along the edges of blanking applied to an image.

- Deinterlace quality: (only available in Studio version) A fourth batch of settings lets you weigh quality against processing time when deinterlacing Media Pool clips via the Enable Deinterlacing checkbox in the Clip Attributes window. Two settings exist:

Normal: A high-quality deinterlacing method fit for most clips. On many clips, Normal can't be told apart from High. During playback in DaVinci Resolve, Normal is always the one used automatically.

High: A more processor-hungry method that can occasionally turn out better results, depending on the footage, at the cost of slower rendering. DaVinci Neural Engine: This option taps the DaVinci Neural Engine's advanced machine learning algorithms to study motion between the fields of interlaced material and rebuild them into one frame. Hugely demanding to compute, this option should ideally yield a result even more pleasing to the eye than the "high" setting.

### Input Scaling Project Setting

When an imported clip's native resolution doesn't match the timeline resolution, the Input Scaling Preset currently chosen in the Image Scaling panel of the Project Settings governs how mismatched clips get handled project-wide. By default it's "Scale entire image to fit," which shrinks or grows the image to match the frame's present dimensions while cropping none of it, laying in letterboxing or pillarboxing as required to cover the frame's remaining area, according to whether the image's horizontal or vertical dimension hits the frame edge first. The Mismatched resolution files option lets you decide how clips that don't match the current project resolution are dealt with. The illustrated examples below show an SD clip fit into an HD project using each of the different options.

### Center crop with no resizing

Clips of differing resolution aren't scaled at all. Clips smaller than the current frame size get surrounded by blanking, while clips larger than it get cropped. Bear in mind this is a good setting to use when importing a timeline from another NLE where clip resolution adjustments come in as scaling adjustments. Choosing "Center Crop with no resizing" keeps DaVinci Resolve from "double scaling" clips in imported timelines.

### Center crop with no resizing

### Scale full frame with crop

Clips of differing resolution get scaled so the clip fills the frame with no blanking. The surplus pixels are cropped. Reach for this setting when clips that fall outside the project resolution should fill the frame on their own, leaving no letterboxing or pillarboxing.

### Scale full frame with crop

### Stretch frame to all corners

Useful for projects relying on anamorphic media. Clips of differing resolution get squished or stretched to match the frame size across every dimension. That way anamorphic media can be stretched to fill full raster, or full raster media squished to fit an anamorphic frame. A bonus of this setting is that it makes blending anamorphic and non-anamorphic clips in one project easy.

### Stretch frame to all corners

### Scale entire image to fit

The default setting. Clips of differing resolution get scaled so each one fills the frame without cropping. The dimension that comes up short receives blanking (letterboxing or pillarboxing). Reach for this setting when clips that fall outside the project resolution should fit the frame automatically without any cropping, and the letterboxing or pillarboxing that follows is fine by you. If, though, you've brought a timeline in from another NLE and certain clips run twice the size they ought to, that's because this setting is on by default and your imported timeline holds imported scaling settings that were used to resize clips not matching the timeline resolution. When that happens, swap to "Center crop with no resizing" instead, and the trouble clears up.

### Scale entire image to fit

### Output Image Scaling Project Settings

Another batch of settings, also sitting in the Image Scaling panel of the Project Settings, optionally lets you choose a different output resolution, whether through the Deliver page or through your video output interface for monitoring or tape output. In particular, within the Render Settings panel of the Deliver page, set the "Resolution" to anything but the timeline resolution and these settings carry out the change. That helps when you're mastering a high resolution 4K project yet want to monitor on an HD display, and you intend eventually to output HD resolution deliverables alongside the 4K ones for which you want different Scaling and/or Resize Filter settings that suit the lower resolution better.

- Match timeline settings: Enabled by default, this checkbox keeps these values in sync with the Image Scaling and Input Scaling settings covered earlier. Clearing the checkbox frees you to pick separate values for monitoring, tape output, or rendering by way of the remaining controls listed below.
- Output resolution: Picks a substitute resolution for both monitoring and delivery. The same value is available through the “Resolution” drop-down menu within the Video panel under the Render Settings on the Deliver page.
- For “X x Y” processing: Lets you enter a separate custom alternate resolution of your own.
- Pixel aspect ratio: Lets you set a substitute pixel aspect ratio that fits the alternate

timeline format.

- Mismatched resolution files: Lets you select a different approach to handling mismatched resolution files, one better suited to whichever alternate resolution you picked. The behavior here parallels what the “Input Scaling” group offers. As an illustration, on an HD or UHD resolution project your Image Input Scaling might sit at “Scale Full Frame With Crop” so that every Standard Definition resolution file gets center-cut to drop blanking. Yet when Output Image Scaling is producing a Standard Definition deliverable, you might prefer the Output Image Scaling > Mismatched resolution files setting at “Scale entire image to fit,” letterboxing each HD or UHD resolution clip while the SD clips keep their original aspect ratio.
- Super Scale: Engages a high-quality upscaling algorithm, heavy on the processor, that genuinely synthesizes fresh pixels for the resized image. Allowed values are None, 2-3-4x, 2-3‑4x Enhanced, and Auto.
