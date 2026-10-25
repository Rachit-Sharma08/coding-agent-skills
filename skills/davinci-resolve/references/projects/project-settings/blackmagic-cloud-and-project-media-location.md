# Blackmagic cloud and project media location

Version: DaVinci Resolve 20.3 Reference Manual. Context: Project settings.
[Chapter index](INDEX.md) / [Previous section](video-monitoring-and-optimized-media-and-render-cache.md) / [Next section](output-scaling-and-color-management.md)
<a id="source-blackmagic-cloud"></a> <a id="source-blackmagic-cloud-1"></a> <a id="source-blackmagic-cloud-storage-syncing"></a> <a id="source-image-scaling"></a> <a id="source-image-scaling-1"></a> <a id="source-input-scaling"></a> <a id="source-multi-user-collaboration"></a> <a id="source-project-media-location"></a> <a id="source-remote-cameras"></a>

### Blackmagic Cloud

Settings that govern how a project connects to the Blackmagic Cloud service live inside the Blackmagic Cloud panel.

### Project Media Location

Sets the destination where media tied to Blackmagic Cloud projects is kept.

- Folder Location: Displays the path on your machine that holds the Blackmagic Cloud media. To point it elsewhere, click the Change location button and pick a fresh destination through the file browser.

### Multi User Collaboration

Determines whether more than one person is permitted to edit this particular project.

- Allow multiple users to simultaneously access and work on this project: Tick this option to switch on the collaboration tools for the cloud project. Leave it clear when you alone are handling a cloud project.

### Blackmagic Cloud Storage Syncing

Use these controls to govern how Blackmagic Cloud Storage handles synchronization.

- For Media Files: Decide here which media gets pushed up and synchronized to your Blackmagic Cloud Storage account so collaborators can reach it. Don’t Sync media: Sends nothing at all to Blackmagic Cloud Storage. Sync proxies only: Pushes just the proxy media up to Blackmagic Cloud Storage. Sync proxies and originals: Sends the proxies together with the source media to Blackmagic Cloud Storage, which may consume a very large quantity of storage based on how much original media there is and how big it runs. Generate proxies automatically: Enable this option so DaVinci Resolve builds proxy media for your master clips on its own.
- Proxies are created as: Pick from these entries which codec the generated proxy files adopt.
- Display synced media in: Defines the timeframe used when showing synced media.

### Remote Cameras

Establishes access rights for people using the Blackmagic Cameras and the Camera app.

- Allow remote cameras to view this project and load media straight into the media pool: Lets project members on the Blackmagic Camera and Camera app push camera footage to the Blackmagic Storage account, which then lands straight in the project’s Media Pool.

### Blackmagic Cloud

Hit the Blackmagic Cloud Website button to reach the Blackmagic Cloud web interface, the place where you arrange, reach, and purchase the assorted Blackmagic Cloud services.

### Image Scaling

The conditions and methods by which clips get resized for assorted purposes are governed inside the Image Scaling panel.

### Image Scaling

The way clips are resized under different conditions is shaped by these settings.

- Resize Filter: This opening cluster of options picks which filtering approach interpolates pixels as clips are resized: Smoother: Can deliver better results for projects whose clips have to shrink down to an SD resolution frame size. Bicubic: Although Sharper and Smoother edge it out slightly in quality, Bicubic remains a remarkably capable resizing filter and demands less of the processor than either alternative. Bilinear: A reduced-quality option that taxes the processor less. Handy for checking your work on a slower machine ahead of rendering, after which you can move up to a finer-quality choice. Sharper: Generally yields the finest output for projects whose clips need enlarging to a bigger frame or shrinking to HD resolutions. Custom: Hands you direct command over the precise algorithm governing every resize. For the custom Resize Filter, your menu lists these algorithms: Bessel, Box, Catmul-Rom, Cubic, and Gaussian, plus Lanczos, Mitchell, Nearest Neighbor, Quadratic, and Sinc. Realistically, telling these approaches apart can be fairly subjective. Even so, when you must replicate a particular resize technique from a different program, this is where you do it. For routine work, the standard resizing filters within DaVinci Resolve will serve fine.
- Override input scaling: Ticking this box lets you select an Input Sizing preset for the project.
- Override output scaling: Ticking this box lets you select an Output Sizing preset for the project.
- Deinterlace quality: (only available in Studio version) A fourth cluster lets you balance quality against processing time when deinterlacing Media Pool clips via the Enable Deinterlacing checkbox of the Clip Attributes window. Three choices exist: Normal: A high-quality deinterlacing approach fit for the bulk of clips. With many clips, Normal can’t be told apart from High. During playback in Resolve, Normal always runs automatically. High: A heavier method on the processor that, with certain footage, may produce nicer results at the cost of longer render times.

DaVinci Neural Engine: Drawing on the sophisticated machine-learning algorithms of the DaVinci Neural Engine, this choice studies the motion between an interlaced frame’s fields and rebuilds them as one combined frame. Though extremely demanding to compute, it should ideally hand you an even more visually pleasing outcome than the “high” option.

### Input Scaling

Holds a single control, Mismatched resolution files, which governs the treatment of clips whose resolution differs from the project’s current resolution. Four choices exist:

- Center crop with no resizing: Clips at a different resolution receive no scaling whatsoever. Anything smaller than the present frame size gets framed by blanking, while anything larger than that frame is cropped.
- Scale full frame with crop: Clips at a different resolution are scaled until the clip’s narrowest side aligns with the frame. The leftover pixels get cropped.
- Scale entire image to fit: The default setting. Clips at a different resolution are scaled until the clip’s widest side aligns with the frame. Blanking fills the narrower side (either letterboxing or pillarboxing).
- Stretch frame to all corners: Handy for projects built on anamorphic media. Clips of varying resolution get compressed or pulled to meet the frame size across every dimension. Through this, anamorphic footage can be expanded to fill full raster, while full raster footage can be compressed into an anamorphic frame. A nice side effect is how readily it lets you blend anamorphic and non-anamorphic clips within one project.
