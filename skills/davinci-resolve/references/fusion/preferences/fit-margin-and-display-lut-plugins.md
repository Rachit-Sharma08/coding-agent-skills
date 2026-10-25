# Fit margin and display LUT plugins

Version: DaVinci Resolve 20.3 Reference Manual. Context: Preferences.
[Chapter index](INDEX.md) / [Previous section](user-interface-and-user-interface-preferences.md) / [Next section](vr-headsets-3d.md) / [Continue VR Headsets / 3D](vr-headsets-3d.md)
<a id="source-api"></a> <a id="source-display-lut-plugins"></a> <a id="source-fit-margin"></a> <a id="source-headset-options"></a> <a id="source-mode"></a> <a id="source-stereo"></a> <a id="source-vr-headsets"></a>

### Fit Margin

The Fit Margin setting fixes how much padding stays around the frame once the Fit button is pressed or Fit is picked from the viewer’s contextual menu.

### Display LUT Plugins

This list shows the display LUTs on hand and switches the picked one on as the default.

### VR Headsets

The VR Headsets preferences let you set up any connected Virtual Reality headsets, including how stereo and 3D scenes get viewed.

### Headset Options

The Headset options serve to pick the type of VR headset you’re using to view the composite, along with the video layout of the 360° view.

### API

- Disabled: Disabled switches off and hides every use of headsets.
- Auto: Auto will detect which headset is plugged in.
- Oculus: Oculus will point the VR output at the Oculus headset.
- OpenVR: OpenVR will back a number of VR headsets like the HTC Vive.

The VR Headsets preferences 360° Video Format

- Auto: Auto reads the incoming image layout off the metadata together with the image frame aspect.
- VCross and HCross: With VCross and HCross, a cube’s six square faces sit in a cross — vertical or horizontal — the forward view holding the cross’s center, within a 3:4 or 4:3 image.
- VStrip and HStrip: With VStrip and HStrip, a cube’s six square faces run vertically or horizontally along a line, in the order Left, Right, Up, Down, Back, Front (+X, -X, +Y, -Y, +Z, -Z), within a 1:6 or 6:1 image.
- LatLong: LatLong amounts to one 2:1 image in equirectangular mapping.
- Enable Mirror Window: Enable Mirror Window brings up a window that mirrors the headset user’s live view.

### Stereo

Much like the normal viewer options for stereo 3D comps, these preferences steer how a stereo 3D comp shows in a VR headset.

### Mode

- Mono: Mono puts out one non stereo eye.
- Auto: Auto works out the way the stereo images have been stacked.
- Vstack: With Vstack, the stereo images stack one above the other — left up top, right beneath.
- Hstack: With Hstack, the stereo images stack side by side — left and right.
- Swap Eyes: Swap eyes flips the eyes whenever stereo comes through reversed.
