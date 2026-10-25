# Importing and exporting polylines and native format

Version: DaVinci Resolve 20.3 Reference Manual. Context: Animating with motion paths.
[Chapter index](INDEX.md) / [Previous section](recording-motion-paths.md)
<a id="source-importing-and-exporting-polylines"></a> <a id="source-native-format"></a>

### Importing and Exporting Polylines

Polyline shapes can move in and out of either a widely supported editable ASCII text file or the program’s own native format. Workflows like these let you stash an especially handy or all-purpose mask or path so you can reuse it later or pull it into a different application, such as Maya or LightWave. Bringing in FXF, SSF, or Nuke shape files is supported as well.

### Native Format

To store a polyline shape using Fusion’s native ASCII format, right-click the header of the Mask node over in the Inspector, then choose Settings > Save As off the contextual menu. Give the file a name and location, then click OK to write out a file carrying the .setting extension. What gets stored is the mask or path geometry together with whatever animation splines drive its points or controls. Bringing that saved setting back into Fusion means first spinning up a fresh polyline of the matching type, then picking Settings > Load from the mask’s context menu, or simply dropping the .setting file straight onto the Node Editor. Should you need to relocate a polyline across compositions, another route is to copy the node onto the clipboard, switch over to your other composition, and paste it in there from the clipboard.
