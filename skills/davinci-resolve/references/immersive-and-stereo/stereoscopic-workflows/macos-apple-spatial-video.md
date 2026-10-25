# Apple spatial video macos only using apple spatial video in DaVinci resolve

Version: DaVinci Resolve 20.3 Reference Manual. Context: Stereoscopic workflows.
[Chapter index](INDEX.md) / [Previous section](floating-window-controls-and-animating-floating-windows.md) / [Apple Spatial Video (MacOS Only)](floating-window-controls-and-animating-floating-windows.md)
<a id="source-spatial-video-export-settings"></a> <a id="source-stereoscopic-workflows-part-3"></a> <a id="source-using-apple-spatial-video-in-davinci-resolve"></a>

### Using Apple Spatial Video in DaVinci Resolve


Moving Spatial Video footage shot on an iPhone into DaVinci Resolve is straightforward, though the MacOS version is the only one that supports it. Follow these steps to bring iPhone Spatial Video footage into DaVinci Resolve: 1 Before recording, switch your iPhone’s camera mode over to Spatial Video (not photo). 2 After you’ve finished shooting, open the Photos app, locate the clip, and tap the Share icon. 3 Send the spatial video to your computer using AirDrop or whatever method you prefer. 4 Launch DaVinci Resolve and bring the spatial video clips into the Media Pool the usual way. 5 When spatial video clips import correctly, a 3D icon shows up automatically on their thumbnails. After import, the full DaVinci Resolve toolset is available for editing, color, audio mixing, and visual effects, exactly as you’d treat ordinary 3D footage.

Spatial Video clips that import correctly should display a 3D icon on their thumbnails.

Tips for using Apple Spatial Video in DaVinci Resolve:

- At present Apple Spatial Video has to be 1080p at 30fps. Confirm your project settings

match this.

- Within the 3D tools on the Color page, verify that the Left/Right eyes and

Convergence are linked. To export a Spatial Video meant for playback across different VR headsets, set the Deliver page Video Settings to:

- Format: QuickTime
- Codec: H.265
- Render Stereoscopic 3D: Both eyes as: MV-HEVC

### Spatial Video export settings
