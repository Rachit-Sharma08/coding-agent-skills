# Adjusting printer points in the bars mode and adjusting printer points via keyboard shortcuts

Version: DaVinci Resolve 20.3 Reference Manual. Context: Primaries palette.
[Chapter index](INDEX.md) / [Previous section](log-wheels-for-log-encoded-media.md)
<a id="source-adjusting-printer-points-in-the-bars-mode"></a> <a id="source-adjusting-printer-points-via-keyboard-shortcuts"></a> <a id="source-printer-light-step-project-settings"></a>

### Adjusting Printer Points in the Bars Mode

Every Offset slider carries a pair of arrow buttons too, one up top and one at the bottom. These buttons deliver “Printer Point” adjustment of those values, letting you shift each Offset channel in discrete steps. Printer Points come in handy for projects tightly bound to a film lab, and are built to mimic color adjustments made on optical printers.

The “plus” and “minus” red, green, and blue buttons that make printer point adjustments Sitting under the Offset sliders, the Offset wheel control shifts all three sliders at once, performing a master or setup adjustment. Keyboard shortcuts can drive the Offset sliders, the Printer Point buttons, and the Offset wheel alike. NOTE: Printer point adjustment is supported on both the DaVinci Resolve Advanced and Mini color grading panels, each through rotary controls covering the Red, Green, and Blue channels, plus All channels together.

### Adjusting Printer Points Via Keyboard Shortcuts

Should you lack a color control panel that handles printer points, one of the finest ways to use them is to switch the numeric keypad over to dedicated keyboard shortcuts meant just for printer points.

To use the Printer Lights Hotkeys: Pick Color > Printer Light Hotkeys, or press Option-Command-Grave Accent (`) Once Printer Light Hotkeys are on, two sets of shortcuts let you work the printer points. The first set is for when you'd like to drive RGB directly in whole steps.

Red 7 - Plus Red 4 - Minus Red

Green 8 - Plus Green 5 - Minus Green

Blue 9 - Plus Blue 6 - Minus Blue

If instead you'd rather work the classic way, driving cyan, magenta, and yellow in whole steps, a second set of shortcuts covers that, drawing on the rest of the keys on the numeric keypad.

Cyan 1 - Plus Cyan Minus (–) - Minus Cyan

Magenta 2 - Plus Magenta 0 - Minus Magenta

Yellow 3 - Plus Yellow Period (.) - Minus Yellow

There's also a pair of keyboard modifiers that hand you finer command over printer points tweaks made with these special keyboard shortcuts, while keeping the coarser default tweaks that let you swing bigger changes faster:

- Hold Command as you use these key shortcuts to shift printer points in quarter‑increments.
- Half-increments are available as well, though you'll have to assign their keyboard shortcuts by hand.

### Printer Light Step Project Settings

Whatever steps the Printer Point buttons take get defined by the Printer Light Step Calibration parameters, which live in the Color panel of the User Preferences. Their defaults are built to mimic traditional film printer adjustments, yet you can customize them so DaVinci Resolve's printer points adjustments match those of a particular film lab's gear. Still, when no lab is in the picture, altering the Step and Density settings changes how big an adjustment each printer point delivers, however your own taste runs. For more information, see Chapter 4, “System and User Preferences.” The Color panel of the User Preferences holds controls for tuning Printer Point functionality TIP: Should you feel left out because everybody else relies on printer points while they remain new to you, surfacing the Parade scope makes a great way to learn how these adjustments behave as you watch their exact effect on the red, green, and blue channels of the video signal.
