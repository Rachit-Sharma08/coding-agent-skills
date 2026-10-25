# Quick export tab in the photo page and metadata

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Previous section](bottom-toolbar-and-photo-viewer-bottom-toolbar.md) / [Next section](setting-up-camera-tethering-capture-live-view.md) / [Continue Setting up Camera Tethering / Capture Live View](setting-up-camera-tethering-capture-live-view.md)
<a id="source-capture"></a> <a id="source-metadata"></a> <a id="source-quick-export-tab-in-the-photo-page"></a> <a id="source-setting-up-camera-tethering"></a>

### Quick Export tab in the Photo Page

Exactly which file parameters appear hinges on the image format you choose, but the usual ones are:

- Export: Choose whether to export the whole Album of photos or only the selected ones.
- File Name: Lets you supply text that serves as a file name prefix.
- Scale: Pick either original resolution or a percentage-reduced resolution to shrink file sizes.
- Include Metadata: Tick this box to bake the photo's metadata into the final image.

TIP: When you need finer control over your photo export, the Deliver page tools are an alternative.

### Metadata

On the Photo page, the Metadata Editor appears in the same spot as the Inspector. Select a photo in the Media Pool or Album and its metadata shows up inside the Metadata Editor. Select several clips and only the first clip's information is displayed. Up in the Metadata Editor's header sit uneditable details about the chosen clip, among them the file name, directory, duration, frame rate, resolution, and codec.

Given how very many metadata fields exist, a pair of drop-down menus at the top let you switch which set of metadata the Metadata Editor displays. Metadata Presets (on the left): If you built your own custom metadata sets through the Metadata panel of the User Preferences, this drop-down picks which one to surface. Rather amusingly, this sits at "Default" by default. Metadata Groups (on the right): This drop-down menu lets you jump between the assorted metadata groups available, sorted for particular tasks or workflows. At the heart of the Metadata Editor lies a run of editable fields below the header that let you review and revise the various metadata criteria on offer.

### Capture

This tab opens up the Capture Live View interface for tethered shooting straight from your camera into DaVinci Resolve. It lets you immediately move your shots into the Media Pool or a Photo Album for editing, client review, or simply to view your image at higher resolution on a bigger screen.

### Setting up Camera Tethering

To begin, you'll have to set up Camera Tethering on the camera itself. Every camera make and model handles this differently, so do consult your camera's manual for the specifics. After that, connect the camera to your DaVinci Resolve Workstation with a USB cable. Lastly, a little additional configuration may be required on your local computer: BETA NOTES For this Beta release, tethered live capture works at present with Canon and Sony cameras alone.

- macOS: Both Canon and Sony cameras are supported natively.
- Windows: Canon cameras are supported natively. Sony cameras are supported,

but require additional software to be installed: https://creatorscloud.sony.net/catalog/en-us/ ie-desktop/index.html

- Linux: Tethering is not supported.
- iPad: Tethering is not supported.

Should your camera give you trouble connecting to DaVinci Resolve, here are a few troubleshooting pointers:

- Confirm that no other software, such as photo editing applications, is open and

grabbing the camera connection on its own.

- On occasion, restarting DaVinci Resolve may be needed before it will connect to your camera.

Once your camera and computer system are configured, hitting the Capture tab links to your camera on its own, and hitting the Capture Live View icon atop the viewer brings you into the Capture Live View interface.
