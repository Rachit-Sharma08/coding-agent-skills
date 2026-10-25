# Resetting color and zone adjustments

Version: DaVinci Resolve 20.3 Reference Manual. Context: HDR palette.
[Chapter index](INDEX.md) / [Previous section](zone-controls-and-customizing-zones-using-the-zone-panel.md)
<a id="source-hdr-palette-part-3"></a> <a id="source-resetting-color-and-zone-adjustments"></a>

### Resetting Color and Zone Adjustments


Within the HDR palette’s Option menu you’ll find a Reset submenu holding three fairly obvious commands: Reset All, Reset Color Adjustments, and Reset Zone Definitions. They matter because, as you build out a grade, you’ll frequently need to clear your color adjustments while keeping your customized Zone graph intact, or the reverse. Beyond that, every reset button shown in the GUI responds to keyboard modifiers, letting you pinpoint exactly what gets cleared. Clicking the master reset button in the HDR palette’s title bar wipes the whole palette (much like the Reset All command). Holding keyboard modifiers as you click it, though, alters the scope of the reset.

- Click the master reset button while holding Command+Shift to clear only the Zone graph’s Range and Falloff controls, leaving your color adjustments untouched.
- Click the master reset button while holding Command+Option to clear only the color adjustments, leaving the zones as they are.

These same modifiers apply to the zone-specific reset controls in the Wheels panel as well, so you can reset just the Zone controls or just the Color controls for any individual zone.
