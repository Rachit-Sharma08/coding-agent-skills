# Bottom toolbar and photo viewer bottom toolbar

Version: DaVinci Resolve 21 New Features Guide. Context: Photo.
[Chapter index](INDEX.md) / [Previous section](photo-album-filtering-icons-and-photo-album-thumbnail-icons.md) / [Next section](quick-export-tab-in-the-photo-page-and-metadata.md)
<a id="source-adding-versions-in-a-photo-album"></a> <a id="source-bottom-toolbar"></a> <a id="source-crop-toolbar"></a> <a id="source-open-fx-and-fusion-overlays"></a> <a id="source-quick-export"></a> <a id="source-the-crop-toolbar"></a> <a id="source-the-new-version-dialog-box"></a> <a id="source-the-overlay-toolbar"></a> <a id="source-the-photo-viewer-bottom-toolbar"></a> <a id="source-the-transform-toolbar"></a> <a id="source-transform-toolbar"></a>

### Bottom Toolbar

### The Photo Viewer Bottom toolbar

- Tools: Brings up the Transform, Crop, and Effects Overlay interfaces.
- Exif Data: Displays the ISO, Shutter Speed, Aperture, and Lens metadata.
- Favorite: Marks the image a favorite with a tiny heart icon.
- Untag: Strips the favorite or reject tag off an image.
- Reject: Marks the image rejected with a tiny x icon.
- Version Selector: Pick a different saved version of the image.
- Rating: Lets you give the image a one-to-five star rating.
- Color: Lets you attach a color tag to the image. Color tags serve organizational

operations on DaVinci Resolve's other pages.

- Flag: Lets you attach a color flag to the image. Flags serve organizational operations on

DaVinci Resolve's other pages.

### Transform Toolbar

Choosing Transform brings up onscreen transform controls that let you work the image directly in the Viewer. Drag anywhere within the clip's bounding box to set pan and tilt, drag a diagonal corner to resize proportionally, drag a top, bottom, left, or right side to squeeze or stretch the width or height, or drag the center handle to rotate.

### The Transform Toolbar

NOTE: While the onscreen controls are active, the tool keeps the original photo size visible beneath the transform grid. The intent is to let you still see the regions beyond the frame as you make adjustments. Shutting the tool bar back down commits the transform operation and applies it to your image. These onscreen controls also map to the following editable parameters, themselves editable in the Video Inspector too.

- Toggle Button: Lets you switch an effect off or on without surrendering any custom adjustments you've put in.
- Zoom Width and Height: Lets you enlarge the image or scale it down. Link the X and Y parameters to lock the image's aspect ratio, or unlink them to stretch or squeeze the image along one direction alone.
- Zoom Link: Engage this lock to bind width and height zoom together so a zoom keeps the same proportions. Disengage it to zoom width and height on their own.
- Position X and Y: Shifts the image inside the frame so pan and scan adjustments are possible. X slides the image left or right; Y slides it up or down.
- Rotation Angle: Spins the image around the anchor point.
- Pitch: Tilts the image toward the camera or away from it about an axis crossing the

image's center from left to right. With positive values, the image's top swings away while the bottom comes forward. With negative values, the top comes forward while the bottom swings away. The larger the value, the more extreme the stretch.

- Yaw: Tilts the image toward the camera or away from it about an axis crossing the image's center from top to bottom. With positive values, the image's left comes forward while the right swings away. With negative values, the left swings away while the right comes forward. The larger the value, the more extreme the stretch.
- Flip Image: A pair of buttons flips the image along different dimensions. Flip Horizontal control: Mirrors the image along the X axis, left to right. Flip Vertical control: Mirrors the clip along the Y axis, flipping it upside down.
- Reset: Lets you return every parameter inside a given control category to its default settings.

### Crop Toolbar

A set of onscreen controls on the Photo page lets you crop the image straight in the Viewer. Every side of the image carries its own handle for cropping just that edge. These parameters are editable in the Video Inspector as well.

### The Crop Toolbar

NOTE: While the onscreen controls are active, the tool keeps the original photo size visible beneath the crop grid. The intent is to let you still see the regions beyond the frame as you make adjustments. Shutting the tool bar back down commits the crop operation and applies it to your image.

- Toggle Button: Lets you switch an effect off or on without surrendering any custom adjustments you've put in.
- Aspect Ratio: Lets you select common aspect ratios for still photo and video formats, or set a custom ratio of your own. Defaults to As Shot, your camera's native aspect ratio.
- Lock Aspect Ratio Engage this lock to fix the chosen aspect ratio across any crop operations. Release it to crop at a freeform aspect ratio.
- Crop Left, Right, Top, and Bottom: Lets you trim away, in pixels, each of the image's four sides.
- Reset: Lets you return every parameter inside a given control category to its

default settings.

### Open FX and Fusion Overlays

When you've applied an Open FX or Fusion Effect carrying onscreen viewer controls, those controls become reachable here by pressing the right icon.

### The Overlay Toolbar

### Adding Versions in a Photo Album

Among a Photo album's handier capabilities is its versioning feature. Make edits to a photo, save it as a version, then attempt something wildly different on that same image, secure in knowing the original version stays safely kept. Save as many versions of an image as you wish.

### The New Version dialog Box

Creating a version is straightforward: just make your edits, right-click a photo in the Photo Album, and pick New Version from the context menu. That brings up the New Version dialog box, where you can type a descriptive name for the version and then hit the OK button.

The Version Dropdown at the bottom of the Photo Viewer Switching versions is just as effortless. Any version you've saved becomes available in the very same right-click context menu you made it from. A simple dropdown selector also sits along the Photo Viewer's lower edge for the same purpose. IMPORTANT: At export time, only whichever version is selected goes out through Quick Export and the Deliver page; the rest are left out.

### Quick Export

A delivery window tailored specifically to still images is what Quick Export opens. You merely choose the image format you want from the left side, enter the file's parameters on the right, then click export.
