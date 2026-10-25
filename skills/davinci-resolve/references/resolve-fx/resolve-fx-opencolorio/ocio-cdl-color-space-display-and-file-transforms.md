# Ocio cdl transform and ocio color space and ocio display and ocio file transform

Version: DaVinci Resolve 20.3 Reference Manual. Context: Ocio cdl transform, Ocio color space, Ocio display, Ocio file transform.
[Chapter index](INDEX.md)
<a id="source-cdl-controls"></a> <a id="source-ocio-cdl-transform"></a> <a id="source-ocio-color-space"></a> <a id="source-ocio-display"></a> <a id="source-ocio-file-transform"></a> <a id="source-resolve-fx-opencolorio"></a> <a id="source-resolve-fx-opencolorio-1"></a>

### Resolve FX OpenColorIO

OpenColorIO (OCIO) is a freely available color management framework developed under the Academy Software Foundation. A wide range of professional editing and vfx applications rely on it (DaVinci Resolve and Fusion among them) so that color stays consistent across every stage of the production pipeline.

The effects below are the technical tools that bring OpenColorIO data into how you work inside DaVinci Resolve.

### OCIO CDL Transform

With the OCIO CDL Transform FX you can build, store, and apply standard Color Decision List (CDL) grades either onto or off of the node. A CDL is what hands basic primary color values from one program over to another.

- CDL File: Pressing Load lets you bring a Color Decision List (.cc or .ccc) file into the controls. A CC holds one CDL, while a CCC bundles several CDL looks together. When you open a CCC file, an extra CCID field shows up so you can pick the index by name or number. Enter the name or number, then press Reload to bring in the new version.
- Reload: Refreshes a CDL once you have picked a different name or number out of a CCC file's index.
- Export: Saves whatever is currently set in Controls as a fresh .cc file.

### CDL Controls

With these controls you can change the node's basic color values, which can then be written out as a CDL file that other programs are able to read. The four of them, Slope, Offset, Power and Saturation, represent the way the American Society of Cinematographers stores color values. What each color control does is fairly obvious, but skipping past the underlying math, they give you a way to shift color in a manner that is either film-oriented or video-oriented, as shown here:

- Slope is essentially Gain
- Offset is essentially Exposure
- Power is Essentially Gamma
- Contrast is a combination of Slope and Offset
- Lift is a combination of Slope and Offset

Forward: Puts the CDL adjustments onto the node. Reverse: Tries to strip the CDL adjustments back off the node. As an example, if footage arrives with a color grade already baked in, reversing the CDL that was used peels those adjustments away to recover the original ungraded source. That said, certain color corrections simply cannot be reversed. Export: Saves whatever is currently set in Controls as a fresh .cc file.

### OCIO Color Space

With this effect you can perform color space transforms by way of an OCIO config file (.ocio).

- OCIO Config File: Press Browse to bring in a .ocio config file for the color space transform.
- Source Space: The source color spaces that are available come from the config file and are listed here. The

contents shown depend entirely on the profile you loaded, so they can differ enormously.

- Output Space: The output color spaces that are available come from the config file and are listed here. The

contents shown depend entirely on the profile you loaded, so they can differ enormously.

- Look: Any OCIO Color Transform Looks you have installed show up in this menu. When nothing is installed, the

menu lists only None as a choice.

- Forward: Puts the Color Space adjustments onto the node.
- Reverse: Tries to strip the Color Space adjustments off the node.

### OCIO Display

With this effect you can preview display transforms by way of an OCIO config file (.ocio).

- OCIO Config File: Press Browse to bring in a .ocio config file for the display transform.
- Source Space: Pick the color space your source material uses from the list.
- Display: Pick which monitor and which type your viewer is set to.
- View: Pick which color space you want shown on your monitor.

### OCIO File Transform

With this effect you can bring in and apply Look Up Tables (LUTs) onto the node.

- LUT File: Press Browse to bring in a LUT through the file browser.
- CCC ID: This is the ID key that pinpoints the particular file transform sitting inside the ASC CDL color correction XML file.
- Forward: Puts the LUT onto the node.
- Reverse: Tries to strip the LUT off the node.
- Interpolation: Lets you pick the color interpolation that gives the best balance between quality and render time.
